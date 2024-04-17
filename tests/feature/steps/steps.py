import json

from behave import when, then
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.endpoints import app, get_session
from common.database.database import Base

test_client = TestClient(app)

engine = create_engine("sqlite:///./test.db")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
TestSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def override_get_session() -> TestSessionLocal:
    session = TestSessionLocal()
    yield session
    session.rollback()
    session.close()


app.dependency_overrides[get_session] = override_get_session


@when('The following is posted to the "{endpoint_name}" endpoint using PUT')
def step_impl(context, endpoint_name):
    try:
        response = test_client.put(url=f"/{endpoint_name}", json=json.loads(context.text))
        if response.status_code == 200:
            context.response = response
            context.success = True
        else:
            context.success = False
    except Exception as ex:
        context.success = False


@then("response should be")
def step_impl(context):
    assert context.success is True
    response_dict = json.loads(context.response.text)
    expected = json.loads(context.text)
    assert response_dict == expected
