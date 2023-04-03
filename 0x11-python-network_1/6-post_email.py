#!/usr/bin/python3
"""A script that:
    takes in a URL,
    - sends a request to the URL and displays the value
    - of the X-Request-Id variable found in the header of the response.
    """
import sys
import urlib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urlib.request.Request(url)
    with urlib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request_Id"))