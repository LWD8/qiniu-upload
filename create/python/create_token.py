#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hmac
import hashlib
import base64
import time

access_key = '-aVSsKYfAgHKPbWEEgWeCbgVV7gcTAOcGjxKBXlw'
secret_key = 'T6b_Omsly45YoHnag7so-prfIsANPvs0g87bnzUG'
scope = 'blog'
deadline = '3344156400'

def put_policy_encode():
    json_text = '{"scope":"%s","deadline":%s}' % (scope, deadline)
    return json_text


def urlsafe_base64_encode(text):
    urlsafe_base64_text = base64.urlsafe_b64encode(text)
    return urlsafe_base64_text


def HMAC_SHA1_encode(text):
    HMAC_SHA1_text = base64.urlsafe_b64encode(hmac.new(secret_key,text,hashlib.sha1).digest())
    return HMAC_SHA1_text


def create_token():
    json_text = put_policy_encode()
    urlsafe_base64_text = urlsafe_base64_encode(json_text)
    HMAC_SHA1_text = HMAC_SHA1_encode(urlsafe_base64_text)
    token = '%s:%s:%s' % (access_key, HMAC_SHA1_text, urlsafe_base64_text)
    deadtime = time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(int(deadline)))
    print 'token : %s' % token
    print 'dead time : %s' % deadtime


if __name__ == '__main__':
    create_token()