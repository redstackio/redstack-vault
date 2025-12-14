---
id: uuid-1
tags:
  - idor
  - endpoint-discovery
  - recon
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-identify-post-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:33:24.289Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Vulnerable-POST-Endpoint-for-IDOR

## Summary

This procedure involves discovering a POST endpoint susceptible to IDOR by inspecting application traffic and testing the member_id parameter, enabling subsequent exploitation for unauthorized access.

## Description

In web applications handling user data, POST endpoints often process parameters like member_id without robust authorization. This procedure uses network inspection to locate such endpoints, typically in account management features. The target environment is a web app with API access, and outcomes include confirming the endpoint's vulnerability to parameter tampering, leading to potential account takeover.

## Requirements

1. Authenticated access to the web application (e.g., valid session token)
2. Proxy tool like Burp Suite for traffic interception
3. Knowledge of common API patterns or access to app documentation

## Defense

Defensive measures and detection strategies:

- Implement proper server-side authorization checks for all object references
- Use indirect references (e.g., UUIDs with mapping) instead of direct IDs
- Monitor for anomalous parameter values in logs and alert on ID mismatches

## Objectives

1. Locate the POST endpoint processing member_id
2. Verify it accepts requests without authorization validation
3. Prepare for parameter manipulation in follow-on steps

## Instructions

### Step 1: Intercept Application Traffic

**Context**: Use a proxy to capture requests during normal user interactions, such as viewing or editing account details, to identify relevant POST endpoints.

**Command** ([[commands/curl-identify-post-endpoint]]):
```bash
curl -X POST 'https://target.com/█████████' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"member_id": "YOUR_ID"}'
```

> This sends a legitimate request to probe the endpoint. Expected output: JSON response confirming successful processing (e.g., {"status": "success"}). If the endpoint is found via proxy, note its path and parameters.

### Step 2: Test Endpoint Response

**Context**: Confirm the endpoint's functionality and parameter usage by sending a test request and observing if it directly references the provided member_id.

**Command** ([[commands/curl-identify-post-endpoint]]):
```bash
curl -v -X POST 'https://target.com/█████████' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"member_id": "YOUR_ID"}'
```

> Verbose output (-v) shows headers and response codes. Success: 200 OK without errors, indicating no immediate validation on member_id.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-identify-post-endpoint]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[recon]]
