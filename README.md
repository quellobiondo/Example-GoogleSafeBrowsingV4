# Google safe browsing usage example
This is an example usage of [Google Safe Browsing API](https://developers.google.com/safe-browsing/v4/), using python 2.7.

[Here](https://console.cloud.google.com/apis/library/safebrowsing.googleapis.com/?q=safe&project=safe-engine-demo) there is the possibility to test its functions online

The code has been developed using the Google API Python Client

### Obtaining permissions
For accounting purposes the requests are authenticated with an API key.

Get an API Key as indicated [here](https://support.google.com/cloud/answer/6158862) for Google Safe Browsing v4

1. Create a project
2. Activate Google Safe Browsing Api [here](https://console.cloud.google.com/launcher/details/google/safebrowsing.googleapis.com?project=safe-engine-demo)
3. Create credential
4. Get API Key

NB: For the Lookup API the amount of daily requests is capped to 10 000.


### How to run

Python
```
SAFE_BROWSING_API_KEY="XXXX"
python check_safety.py url1 [url2 ...]
```

Docker
```
docker build -t safebrowsingsample .
docker run -e SAFE_BROWSING_API_KEY="XXXX" safebrowsingsample url1 [url2 ...]
```

Sample result
```bash
$ docker run -e SAFE_BROWSING_API_KEY=$API_KEY safebrowsingsample "d99q.cn" "google.com"

{
    "matches": [
        {
            "cacheDuration": "300s",
            "platformType": "ANY_PLATFORM",
            "threat": {
                "url": "d99q.cn"
            },
            "threatEntryType": "URL",
            "threatType": "MALWARE"
        }
    ]
}
```
