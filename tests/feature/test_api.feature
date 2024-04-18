Feature: Test API endpoints
  # Enter feature description here

  Scenario: Valid add records
    When The following is posted to the "add-records" endpoint using PUT
    """
     [
      {
        "model": "Tiguan",
        "make": "VW",
        "plate": "123-123",
        "year": "2024-01-01",
        "color": "bLUE"
      }
    ]
    """
    Then response should be
    """
    [
      1
    ]
    """
    Scenario: File updoad
      When The string "validData.csv" posted to the "upload-file" endpoint using PUT
    Then response should be
    """
    [2,3,4,5,6,7,8]
    """
