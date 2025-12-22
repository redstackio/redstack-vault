---
id: proc-secret-extract-ssrf
tags:
  - secret-disclosure
  - ssrf
  - ibm
  - turbonomic
  - cloud
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-secret-fetch]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T03:46:09.189Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Extract-Secret-Keys-via-SSRF

## Summary

This procedure uses an established SSRF vector in IBM Turbonomic to access and extract secret keys from internal configuration endpoints or files, exposing credentials for further unauthorized actions.

## Description

Building on SSRF exploitation, this targets improper handling of sensitive data in Turbonomic's backend, where config files or API responses may leak keys like database passwords or API tokens. The attack scenario involves chaining SSRF requests to localhost paths containing secrets, leading to high-severity impacts like account compromise. Expected outcomes include obtaining usable credentials without direct authentication.

## Requirements

1. Confirmed SSRF vulnerability in the target endpoint.
2. Identification of internal paths holding secrets (e.g., /config/secrets.json).
3. Ability to parse and validate extracted credentials.

## Defense

Defensive measures and detection strategies:

- Encrypt and restrict access to configuration files; avoid exposure via web paths.
- Implement secret scanning in logs and responses.
- Use runtime application self-protection (RASP) to block anomalous internal requests.

## Objectives

1. Retrieve secret keys through SSRF-mediated access.
2. Validate keys for usability in external systems.
3. Enable escalation to data access or lateral movement.

## Instructions

### Step 1: Target Config Endpoint via SSRF

**Context**: Use SSRF to request an internal config file that may contain secrets.

**Command** ([[commands/curl-secret-fetch]]):
```bash
curl -X POST 'https://target.turbonomic.example.com/vulnerable-endpoint' -d '{"url":"http://localhost:8080/config/secrets"}' -H 'Content-Type: application/json'
```

> This fetches the secrets endpoint. Success shows raw config data; failures may reveal partial leaks or errors confirming access.

### Step 2: Parse and Test Extracted Key

**Context**: Extract the key from the response and test it against a protected resource.

**Command** ([[commands/curl-key-test]]):
```bash
curl -H 'Authorization: Bearer extracted_key_here' 'https://internal.api.example.com/test'
```

> Replace 'extracted_key_here' with the leaked token. A 200 OK response confirms validity.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Credentials In Files]]

## Commands Used

- [[commands/curl-secret-fetch]]
- [[commands/curl-key-test]]

## Tools Used


## Tags

- secret-leak
- credential-access
- ssrf
