import http.client, urllib.request, urllib.parse, urllib.error, os

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': os.getenv('RESOURCE_KEY'),
}

params = urllib.parse.urlencode({
    # Request parameters
    'skip': '0',
    'top': '10',
})

try:
    conn = http.client.HTTPSConnection('scenera-computervision-rnd-resource.cognitiveservices.azure.com')
    conn.request("GET", "/computervision/models?api-version=2023-02-01-preview&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################