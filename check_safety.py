#!/usr/bin/python

'''
Simple command-line example for The Google Safe browsing v4 API.

Command-line application that check if a website is safe for browsing.
Usage:
  $ python check_safety.py <URL1> [<URL2> ...]
'''
from __future__ import print_function

__author__ = 'ziro.alberto@gmail.com (Alberto Zirondelli)'

from apiclient.discovery import build
import os
import sys
import json

def do_analysis(urls):
    api_name = "safebrowsing"
    api_version = "v4"
    api_key = os.environ.get("SAFE_BROWSING_API_KEY")
    if not api_key:
        print("Error: Google safe browsing API key missing")
        sys.exit(1)

    service = build(api_name, api_version, developerKey=api_key)

    tm = service.threatMatches()
    req_body = {
        "threatInfo": {
          "threat_types": ["MALWARE", "THREAT_TYPE_UNSPECIFIED", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
	      "platform_types": ["ANY_PLATFORM"],
          "threatEntryTypes": ["URL"],
          "threatEntries": [
            map(lambda x: {"url": x}, urls)
          ]
        }
    }
    #create request
    request = tm.find(body=req_body)
    #execution
    response = request.execute()
    #return response
    return response


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage Error: python check_safety.py <URL1> [<URL2> ...]")
        sys.exit(1)

    response = do_analysis(args)
    print("%s\n\n" % json.dumps(response, sort_keys=True, indent=4))
