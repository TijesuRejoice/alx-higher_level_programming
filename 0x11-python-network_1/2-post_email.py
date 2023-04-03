#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import sys
import urlib.parse
import urlib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urlib.parse.urlencode(value).encode("ascii")

    request = urlib.request.Request(url, data)
    with urlib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
