Feature: Test API

  Scenario: Add new data
    When The following is posted to the "create-models" endpoint using PUT
    """
    [
      {
      "ssn":"555-555-55",
      "height":107.0,
      "weight":80,
      "name":"Jorge Cardenas",
      "admitted":"2024-04-11",
      "birthday":"1977-02-21",
      "phone":"555-555-5555",
      "email":"jorge@me.com",
      "gender":"Male",
      "occupation":"SW Engineer"
      }
    ]
    """
    Then response should be
    """
    [1]
    """