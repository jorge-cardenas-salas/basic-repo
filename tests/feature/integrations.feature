Feature: Basic endpoints testing
  Try hitting the endpoints and getting the expected data

  Scenario: API is alive
    When Endpoint "docs" is called with the following params using "GET"
    Then api should succeed

  Scenario: Non-existing endpoint is hit
    When Endpoint "non-existing" is called with the following params using "GET"
    Then api should fail

