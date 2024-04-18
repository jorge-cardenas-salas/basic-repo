Feature: Basic endpoints testing
  Try hitting the endpoints and getting the expected data

  Scenario: API is alive
    When Endpoint "docs" is called with the following params using "GET"
    Then api should succeed

  Scenario: Non-existing endpoint is hit
    When Endpoint "non-existing" is called with the following params using "GET"
    Then api should fail

  Scenario: Timeout
    When Endpoint "get-data" is called with the following params using "PUT"
    """
    Many records
    """
    Then api should fail

  Scenario: Something
    Given Clean tables
    And Item table with data
    | Name | Event | Address |
    | --- | --- | --- |
    | Name | Event | Address |
    | Name | Event | Address |
    When Endpoint "get-data" is called with the following params using "PUT"
    """
    [JSON]
    """
    Then response should be
    """[1,2,3,4]"""

