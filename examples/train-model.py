import http.client, urllib.request, urllib.parse, urllib.error, requests

headers = {
    # Request headers
    'Content-Type': 'application/json-patch+json',
    'Ocp-Apim-Subscription-Key': '2c1491d2155e44d795c502005873182b',
}

params = urllib.parse.urlencode({})
data = {
  "name": "apiModel",
  "createdDateTime": "2023-10-11T06:01:57.192Z",
  "updatedDateTime": "2023-10-11T06:01:57.192Z",
  "status": "notStarted",
  "trainingParameters": {
    "trainingDatasetName": "testcocodataset",
    "timeBudgetInHours": 1,
    "modelKind": "Generic-Detector"
  },
  "trainingCostInMinutes": 0,
  "error": {
    "code": "string",
    "message": "string",
    "target": "string",
    "details": [
      "string"
    ],
    "innererror": {
      "code": "string",
      "message": "string",
      "innererror": "string"
    }
  },
  "modelPerformance": {
    "accuracyTop1": 0,
    "accuracyTop5": 0,
    "averagePrecision": 0,
    "calibrationECE": 0,
    "meanAveragePrecision30": 0,
    "meanAveragePrecision50": 0,
    "meanAveragePrecision75": 0,
    "tagPerformance": {
      "additionalProp1": {
        "accuracy": 0,
        "averagePrecision50": 0
      },
      "additionalProp2": {
        "accuracy": 0,
        "averagePrecision50": 0
      },
      "additionalProp3": {
        "accuracy": 0,
        "averagePrecision50": 0
      }
    }
  }
}

endpoint = "https://scenera-computervision-rnd-resource.cognitiveservices.azure.com"
model_name = "scenera-custom-model-v1"

try:
    # conn = http.client.HTTPSConnection('scenera-computervision-rnd-resource.cognitiveservices.azure.com')
    # conn.request("PUT", "/computervision/models/scenera-custom-model-v1?api-version=2023-02-01-preview&%s" % params, "{}", headers)
    # response = conn.getresponse()
    # data = response.read()
    # print(data)
    # conn.close()
    response = requests.put(f"{endpoint}/computervision/models/{model_name}?api-version=2023-02-01-preview", data=data, headers=headers)
    print(response.status_code)
    print(response.content)
    
except Exception as e:
    print("[Errno {0}] {1}".format(e, e))

####################################