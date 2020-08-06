from flask import Flask, jsonify
from flask import render_template
from flask import request
from datetime import datetime
import json
import logging
logging.basicConfig(filename='error.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
import os

#Documentation located at: https://garyhostt.github.io/OIC_start-stop/
import requests
import oci
import datetime
from datetime import date, time, datetime
import time
import sys

# declare constants for flask app
HOST = '0.0.0.0'
PORT = 5000

# initialize flask application
app = Flask(__name__)
print("Welcome to the 'OIC start/stop scheduler' API, Bienvenue a la planificatrice de l'CIO")
today = datetime.now() 
print(today)

# what you need to set
# lines: 39, 53, 67, 79, 84, 86, 88; if outside of ashburn region, change lines 42, 56, 69

# endpoints
@app.route('/api/test', methods=['GET'])
def version():
    return jsonify(status='success')

@app.route('/api/OIC/start',methods=['GET'])
def start_input():
    oicOCID = ""
    auth = SignedRequestAuth(api_key, private_key)
    print ("Instance with OCID: " + oicOCID + " is now starting.")
    url = "https://integration.us-ashburn-1.ocp.oraclecloud.com/20190131/integrationInstances/" + oicOCID + "/actions/start"
    payload  = {}
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, auth = auth, headers=headers, data = payload)
    print("The response code from the OCI API is below:")
    print(response.status_code)

@app.route('/api/OIC/stop',methods=['GET'])
def stop_input():
    oicOCID = ""
    auth = SignedRequestAuth(api_key, private_key)
    print ("Instance with OCID: " + oicOCID + " is now stopping.")
    url = "https://integration.us-ashburn-1.ocp.oraclecloud.com/20190131/integrationInstances/" + oicOCID + "/actions/stop"
    payload  = {}
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, auth=auth, headers=headers, data = payload)
    print("The response code from the OCI API is below:")
    print(response.status_code)

@app.route('/api/OCI/announcements')
def announcements():
    tenancyOCID = ""
    auth = SignedRequestAuth(api_key, private_key)
    url = "https://announcements.us-ashburn-1.oraclecloud.com/20180904/announcements?compartmentId=" + tenancyOCID
    payload  = {}
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, auth = auth, headers=headers, data = payload)
    print(response.text.encode('utf8'))

# Custom Signed header request work
#Verify the file location below is where you placed your API key
with open("/.oci/oci_api_key.pem") as f:
    private_key = f.read().strip()

api_key = "/".join([
    #in the parenthesis below, input yoru tenancy's root compartment's OCID
    "",
    #in the quotes below, input the OCID for the user
    "",
    #in these quotes below, paste your API key fingerprint
    ""
])

# Universal signed header request work, leave stuff between here and line 172
import base64
import email.utils
import hashlib
import httpsig_cffi.sign
import requests
import six

class SignedRequestAuth(requests.auth.AuthBase):
    """A requests auth instance that can be reused across requests"""
    generic_headers = [
        "date",
        "(request-target)",
        "host"
    ]
    body_headers = [
        "content-length",
        "content-type",
        "x-content-sha256",
    ]
    required_headers = {
        "get": generic_headers,
        "head": generic_headers,
        "delete": generic_headers,
        "put": generic_headers + body_headers,
        "post": generic_headers + body_headers
    }

    def __init__(self, key_id, private_key):
        # Build a httpsig_cffi.requests_auth.HTTPSignatureAuth for each
        # HTTP method's required headers
        self.signers = {}
        for method, headers in six.iteritems(self.required_headers):
            signer = httpsig_cffi.sign.HeaderSigner(
                key_id=key_id, secret=private_key,
                algorithm="rsa-sha256", headers=headers[:])
            use_host = "host" in headers
            self.signers[method] = (signer, use_host)

    def inject_missing_headers(self, request, sign_body):
        # Inject date, content-type, and host if missing
        request.headers.setdefault(
            "date", email.utils.formatdate(usegmt=True))
        request.headers.setdefault("content-type", "application/json")
        request.headers.setdefault(
            "host", six.moves.urllib.parse.urlparse(request.url).netloc)

        # Requests with a body need to send content-type,
        # content-length, and x-content-sha256
        if sign_body:
            body = request.body or ""
            if "x-content-sha256" not in request.headers:
                m = hashlib.sha256(body.encode("utf-8"))
                base64digest = base64.b64encode(m.digest())
                base64string = base64digest.decode("utf-8")
                request.headers["x-content-sha256"] = base64string
            request.headers.setdefault("content-length", len(body))

    def __call__(self, request):
        verb = request.method.lower()
        # nothing to sign for options
        if verb == "options":
            return request
        signer, use_host = self.signers.get(verb, (None, None))
        if signer is None:
            raise ValueError(
                "Don't know how to sign request verb {}".format(verb))

        # Inject body headers for put/post requests, date for all requests
        sign_body = verb in ["put", "post"]
        self.inject_missing_headers(request, sign_body=sign_body)

        if use_host:
            host = six.moves.urllib.parse.urlparse(request.url).netloc
        else:
            host = None

        signed_headers = signer.sign(
            request.headers, host=host,
            method=request.method, path=request.path_url)
        request.headers.update(signed_headers)
        return request


if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
