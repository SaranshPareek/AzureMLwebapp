import urllib.request
import json
import os
import ssl


def req_model(dat):
    # bypass the server certificate verification on client side
    #if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        #ssl._create_default_https_context = ssl._create_unverified_context

    #allowSelfSignedHttps(True)
    try:
        #rslt = dict()
        url = 'http://066d5e19-1b56-4e12-8a5a-18780cb5384b.eastus2.azurecontainer.io/score'
        headers = {'Content-Type':'application/json'}

        data = {"data": dat}

        body = str.encode(json.dumps(data))

        req = urllib.request.Request(url, body, headers)
        response = urllib.request.urlopen(req)

        result = response.read()
        
        msg = "Success"
        rs = str(result)
    
        return msg,rs
    
    except urllib.error.HTTPError as error:
        #msg = dict()
        msg = "Failed"
        rs = str(error.read().decode("utf8", 'ignore'))
        return msg,rs