import urllib.request
import json

body = {
    "origins": [{
        "latitude": 47.6044,
        "longitude": -122.3345
    },
    {
        "latitude": 47.6731,
        "longitude": -122.1185
    },
    {
        "latitude": 47.6149,
        "longitude": -122.1936
    }],
    "destinations": [{
        "latitude": 45.5347,
        "longitude": -122.6231
    },
    {
        "latitude": 47.4747,
        "longitude": -122.2057
    }],
    "travelMode": "driving",
    "distanceUnit": "kilometer",
    "timeUnit": "minute"
}

def processBingAPI(jsonBody):
    bingKey = "{Bing Maps Key here}"
    serviceUrl = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?key="+bingKey

    req = urllib.request.Request(serviceUrl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(jsonBody)
    jsondataasbytes = jsondata.encode('utf-8')
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)

    data = response.read().decode()

    print("retrieving ",serviceUrl)
    print("Retrieved",len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None
        return js
    json_result = js['resourceSets'][0]['resources'][0]['results']
    print(json.dumps(json_result, indent=4))
    return json_result

processBingAPI(body)
