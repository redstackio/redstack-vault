---
id: 8d01eb2b-3771-40f4-a232-82c0a9a8d440
name: vulnerable-python-pickle-load-and-print
type: code
language: python
verified: true
created_at: '2023-04-06T03:55:59.484467+00:00'
updated_at: '2024-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - pickle
  - deserialization
  - vulnerable
validated: true
---

# Vulnerable Python Pickle Load and Print

## Code

```python
import cPickle
from base64 import b64decode

def load_token(token):
    return cPickle.loads(b64decode(token))

auth_token = raw_input("Enter Auth Token : ")
user = load_token(auth_token)
print "Welcome {}".format(user.username)
```

## Description

This code snippet represents vulnerable server-side Python logic that deserializes a base64-encoded user-supplied token using cPickle without validation. It prompts for input, decodes and unpickles it to retrieve a User object, then prints a welcome message. When exploited with a malicious token, it triggers arbitrary code execution during deserialization instead of loading the object.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| auth_token | User-supplied base64-encoded token (attacker provides malicious one) | gASV... (malicious base64) |

## Usage

Embed this in a web app or service handling auth tokens (e.g., Flask route). Attacker submits malicious token via POST/GET. Used in red teaming to demonstrate deserialization risks; run locally to test with benign/malicious input.

## Detection

- Static code analysis for cPickle.loads or pickle.loads on untrusted input.
- Runtime monitoring for unexpected os.system or subprocess calls from Python processes.
- Input logging: Alert on base64 strings with suspicious patterns (e.g., containing 'reduce').
- Python sandboxing or WAF rules blocking pickle gadgets.

## Related

- [[procedures/Exploit-Python-Pickle-Deserialization-for-RCE]]
- [[commands/python-generate-malicious-pickle-token]]
