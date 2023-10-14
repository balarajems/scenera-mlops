import http.client, urllib.request, urllib.parse, urllib.error, requests, os

headers = {
    # Request headers
    'Content-Type': 'application/json-patch+json',
    'Ocp-Apim-Subscription-Key': os.getenv('RESOURCE_KEY'),
}

params = urllib.parse.urlencode({})
data = {
    "name": "scenera-custom-model-v1",
    "trainingParameters": {
        "trainingDatasetName": "scenera-dataset-v1",
        "modelKind": "Generic-Detector",
        "timeBudgetInHours": 1,
    }
}

try:
    # conn = http.client.HTTPSConnection('scenera-computervision-rnd-resource.cognitiveservices.azure.com')
    # conn.request("PUT", "/computervision/models/scenera-custom-model-v1?api-version=2023-02-01-preview&%s" % params, "{}", headers)
    # response = conn.getresponse()
    # data = response.read()
    # print(data)
    # conn.close()
    response = requests.get('https://httpbin.org/put', data=data, headers=headers)
    print(response.status_code)
    print(response)
    
except Exception as e:
    print("[Errno {0}] {1}".format(e, e))

####################################