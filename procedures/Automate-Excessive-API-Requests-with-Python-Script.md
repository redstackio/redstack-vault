---
tags:
  - dos-automation
  - api-flooding
  - python-script
type: procedure
tools:
  - '[[tools/dos.py-Python-Script]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/run-dos-python-script]]'
platforms:
  - Web
techniques:
  - '[[Python]]'
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 25a612d8-5c7d-4af0-b23f-53566ae682e3
created_at: '2025-12-14T17:32:01.648Z'
updated_at: '2025-12-14T17:32:01.648Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
  - '[[Endpoint Denial of Service]]'
---
# Automate-Excessive-API-Requests-with-Python-Script

## Summary

This procedure deploys a custom Python script (dos.py) to send unlimited authenticated requests to Semmle's internal API endpoints, exploiting the absence of rate limiting to cause server overload and DoS.

## Description

Using captured session cookies and nonces, the script automates GET and POST calls to endpoints like /internal_api/v0.2/getSuggestedProjects and /internal_api/v0.2/setUsername. Without restrictions, this floods the server, leading to heavy load, potential buffer overflows, and denial of service for legitimate users.

## Requirements

1. Captured cookie and nonce from previous interception
2. Python environment with requests library installed
3. Network access to lgtm-com.pentesting.semmle.net

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on all API endpoints (e.g., using nginx or application-level throttling)
- Monitor for anomalous request volumes from single sessions
- Use WAF rules to detect scripted API abuse patterns

## Objectives

1. Overwhelm server resources with excessive calls
2. Induce DoS on the platform
3. Demonstrate vulnerability impact

## Instructions

### Step 1: Prepare the Script

**Context**: Insert authentication details into dos.py.

Edit the dos.py file to include the captured cookie in headers and nonce in request bodies. Target endpoints such as getLanguages, getLoggedInUser, etc.

> The script uses Python's requests module to loop indefinitely.

### Step 2: Execute the Script

**Context**: Run the script to begin flooding the APIs.

Execute [[commands/run-dos-python-script]] from the terminal in the script's directory.

```bash
python dos.py
```

> Expected output: Console logs showing successful requests per second; monitor for server errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]
- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/run-dos-python-script]]

## Tools Used

- [[tools/dos.py-Python-Script]]

## Tags

- [[api-automation]]
- [[dos-script]]
