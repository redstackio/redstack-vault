---
id: d03aaf14-49b5-4f1f-968e-39de6c4a14a8
name: Python Pickle Deserialization
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.489923+00:00'
updated_at: '2023-04-06T03:55:59.504077+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Scheduled Transfer|T1029 - Scheduled Transfer]]'
tags:
- '[[Pickle]]'
- '[[Python Deserialization]]'
commands:
- '[[Load Auth Token]]'
- '[[Print Welcome Message]]'
---

# Python Pickle Deserialization

## Summary

Python Pickle Deserialization is a vulnerability that allows attackers to execute arbitrary code on the server. The vulnerability is introduced when a token is loaded from user input. An attacker can take advantage of this vulnerability by creating a malicious pickle object that will execute arbitr

## Description

# Description

Python Pickle Deserialization is a vulnerability that allows attackers to execute arbitrary code on the server. The vulnerability is introduced when a token is loaded from user input. An attacker can take advantage of this vulnerability by creating a malicious pickle object that will execute arbitrary code on the server. This technique is commonly used in combination with other attacks to gain persistence on the system. 

This vulnerability can be mitigated by not using pickle module with untrusted sources, and by properly validating user input. 

## Requirements

1. Python environment

## Defense

1. Implement input validation to ensure that user input is properly sanitized and free of malicious code.

1. Avoid using pickle module with untrusted sources.

1. Use the latest version of Python to ensure that known vulnerabilities are patched.

## Objectives

1. Execute arbitrary code on the server

1. Gain persistence on the system

# Instructions

1. Run the following code in a Python environment:

**Code**: [[cPickle]]

> This command generates an auth_token which is a serialized User object using the cPickle module.

2. Run the following code in a Python environment:

**Code**: [[import cPickle
from base64 import b64decode

def l]]

> This command loads the auth_token from user input and deserializes it using the cPickle module. It then prints the username of the deserialized object.

**Command** ([[Load Auth Token]]):

```bash
import cPickle
from base64 import b64decode

def load_token(token):
    return cPickle.loads(b64decode(token))

auth_token = raw_input("Enter Auth Token : ")
user = load_token(auth_token)
```

**Command** ([[Print Welcome Message]]):

```bash
print "Welcome {}".format(user.username)
```

3. Run the following code in a Python environment:

**Code**: [[import cPickle, os
from base64 import b64encode

c]]

> This command generates a malicious pickle object that will execute the 'whoami' command on the server when deserialized using the cPickle module. The output of the 'whoami' command will be printed as the evil token.

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Scheduled Transfer|T1029 - Scheduled Transfer]]

## Commands Used

- [[Load Auth Token]]
- [[Print Welcome Message]]

## Tags

- [[Pickle]]
- [[Python Deserialization]]
