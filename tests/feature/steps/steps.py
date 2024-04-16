"""
Feature test steps (Cucumber) will be defined here
"""
import json
import traceback
# import urllib.parse # To parse filenames correctly
from typing import Optional, List

from behave import given, when, then
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.endpoints import app
from common.constants import PROJECT_NAME
from common.database.database import Base, get_session
from common.database.row_models.row_models import ItemRow
from common.utilities import DefaultLogger

# Mock elements:
TEST_DB_NAME = f"{PROJECT_NAME}_test.db"
engine = create_engine(f"sqlite:////app/resources/{TEST_DB_NAME}.db")
logger = DefaultLogger(logger_name="FeatureTestLogger").get_logger()
TestSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class FeatureTestClient:
    """
    Little helper class to generate a FastAPI test client
    """

    def __init__(self, existing_rows: Optional[List[ItemRow]] = None):
        """
        Initialize the helper
        Args:
            existing_rows: Optional data to pre-populate our table
        """
        self.existing_rows = existing_rows

    def get_empty_session(self) -> TestSessionLocal:
        """
        Super important, FastAPI uses this override to avoid doing permanent changes in our DB
        
        Returns
            TestSessionLocal: DB Session just for testing
        """
        logger.info("Overriding get_session with empty session")
        session = TestSessionLocal()
        yield session
        session.rollback()
        session.close()

    def get_populated_session(self) -> TestSessionLocal:
        """
        A variation on the previous one, some duplicated code but necessary for the override (see below) 
        
        Returns
            TestSessionLocal: DB Session just for testing
        """
        logger.info("Overriding get_session with populated session")
        session = TestSessionLocal()
        # Here we pre-populate our tables
        session.add_all(self.existing_rows)
        session.commit()
        yield session
        session.close()

    def get_test_client(self) -> TestClient:
        client = TestClient(app)

        # Use the proper override depending on weather we need to pre-populate data
        if self.existing_rows:
            client.app.dependency_overrides[get_session] = self.get_populated_session
        else:
            client.app.dependency_overrides[get_session] = self.get_empty_session
        return client


@given('Clean tables')
def step_impl(context):
    """
    Wipes the test database, for testing from scratch
    """
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


@given("Item table with data")
def step_impl(context):
    """
    Add pre-populate data to the context

    Args:
        context: Behave context, table expected here
    """
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    temp_rows = []
    for row in context.table.rows[1:]:
        # ignore first row (it's expected to be a |---| divider)
        item_row = ItemRow(key=int(str(row.cells[0]).strip()), name=str(row.cells[1]).strip())
        temp_rows.append(item_row)
    context.existing_rows = temp_rows


@then("response should be")
def step_impl(context):
    """
    Assert the response from the context
    
    Args:
        context: Behave context, contains test-related data
    """
    assert context.success is True
    response_dict = json.loads(context.response.text)
    expected = json.loads(context.text)
    assert response_dict == expected


@then("api should fail")
def step_impl(context):
    """
    Assert that the API failed
    
    Args:
        context: Behave context, contains test-related data
    """
    assert context.success is False


@then("api should succeed")
def step_impl(context):
    """
    Assert that the API succeeded

    Args:
        context: Behave context, contains test-related data
    """
    assert context.success is True


@when('Endpoint "{endpoint}" is called with the following params using "{method}"')
def step_impl(context, endpoint: str, method: str):
    """
    Call an endpoint with specific ids and HTTP method
    Args:
        context: Behave context, contains test-related data
        endpoint: The endpoint to call. POST is assumed
        ids: The list of ids to pull
        method: HTTP method to be used (restricted to POST and DELETE)
    """
    try:
        existing_rows = context.existing_rows if hasattr(context, "existing_rows") else None
        params = context.text
        client = FeatureTestClient(existing_rows).get_test_client()
        if params:
            response = client.request(url=f"/{endpoint}", method=method, json=json.loads(params))
        else:
            response = client.request(url=f"/{endpoint}", method=method)

        if response.status_code == 200:
            context.response = response
            context.success = True
        else:
            context.success = False
    except Exception as ex:
        print(traceback.format_exc())
        context.success = False
