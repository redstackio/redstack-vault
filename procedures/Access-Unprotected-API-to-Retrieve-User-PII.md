---
tags:
  - information-disclosure
  - api
  - pii
  - unauthenticated-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-api-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.913Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: e5e8d415-b4c5-4ec2-91c7-61f73e565ab2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Unprotected-API-to-Retrieve-User-PII

## Summary

This procedure exploits an information disclosure vulnerability in an unauthenticated API endpoint on Uber's campus-vtc.com site, allowing retrieval of personal identifiable information (PII) such as full names, emails, and phone numbers for contest participants. It demonstrates how lack of authentication enables unauthorized data access during bug bounty exploration.

## Description

The vulnerability stems from an API endpoint handling contest entry data without proper authentication or authorization checks. An attacker, likely during reconnaissance or bug bounty hunting, discovers the endpoint through API exploration (e.g., inspecting network requests or guessing paths). Issuing a simple HTTP request returns sensitive PII for 83 Uber France users who uploaded contest entries. This can lead to privacy violations, phishing, or identity theft. The target environment is a web-based API, accessible publicly without credentials.

## Requirements

1. Internet access to campus-vtc.com
2. Basic HTTP client (e.g., curl, browser dev tools)
3. Knowledge of API endpoint paths (discovered via exploration)

## Defense

Defensive measures and detection strategies:

- Implement authentication (e.g., API keys, JWT) on all endpoints handling sensitive data
- Use rate limiting and IP whitelisting to prevent unauthorized access
- Monitor API logs for anomalous requests without auth tokens
- Conduct regular API security audits and input validation

## Objectives

1. Retrieve unauthorized PII from the contest database
2. Validate the absence of access controls
3. Assess impact on user privacy

## Instructions

### Step 1: Identify the Vulnerable API Endpoint

**Context**: During site exploration, inspect JavaScript files, network traffic, or guess common API paths related to contests (e.g., /api/contest-entries).

No specific command; use browser dev tools or manual testing to confirm the endpoint responds without auth.

### Step 2: Send Request to Retrieve Data

**Context**: Use an HTTP client to access the endpoint and exfiltrate PII. This step confirms the disclosure.

**Command** ([[commands/curl-api-request]]):
```bash
curl -X GET "https://campus-vtc.com/api/contest-entries" -H "User-Agent: Mozilla/5.0 (compatible; Bug Bounty Bot/1.0)" -o user_pii.json
```

> This command sends a GET request to the endpoint, mimicking a browser, and saves the response to a file. Expected output is a JSON object listing user details without errors.

### Step 3: Parse and Validate Retrieved Data

**Context**: Review the output to confirm PII exposure.

Use jq or manual inspection:
```bash
cat user_pii.json | jq '.users[] | {name, email, phone}'
```

> Expected output: Structured list of 83+ entries with names, emails, and phones.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-api-request]]

## Tools Used


## Tags

- information-disclosure
- api
- pii
- unauthenticated-access
