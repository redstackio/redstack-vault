---
tags:
  - information-disclosure
  - access-control
  - valve
  - srcds
  - api-keys
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-fetch-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:39.204Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 1e24334f-2645-45e7-991d-3863b2afd3cb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Leaked-Valve-Server-Configurations

## Summary

This procedure exploits insufficient access controls on the https://srcds.valve.net/find/ endpoint to unauthenticated retrieve sensitive configuration information, including server configs and API keys for Valve's Source Dedicated Servers (srcds). It demonstrates a straightforward information disclosure vulnerability discovered through public service exploration.

## Description

The /find/ endpoint on srcds.valve.net lacks proper authentication, allowing any unauthenticated user to access internal server configurations and API keys. This can lead to exposure of credentials that could be used for further unauthorized access to game server infrastructure. The attack requires no special privileges or tools beyond basic HTTP requests, making it highly accessible. Expected outcomes include direct leakage of JSON-formatted data containing keys and configs, with high impact on confidentiality.

## Requirements

1. Public internet access to https://srcds.valve.net
2. Basic HTTP client (e.g., curl or browser)
3. No credentials or prior access needed

## Defense

Defensive measures and detection strategies:

- Implement authentication and authorization checks on all public endpoints handling sensitive data
- Use web application firewalls (WAF) to monitor and block anomalous access to admin-like endpoints
- Regularly audit public-facing APIs for over-exposure using tools like OWASP ZAP or Burp Suite
- Log all requests to sensitive endpoints and alert on unauthenticated access patterns

## Objectives

1. Retrieve leaked server configurations and API keys without authentication
2. Identify exploitable credentials for potential follow-on attacks
3. Validate the presence of information disclosure vulnerability

## Instructions

### Step 1: Query the Vulnerable Endpoint

**Context**: Directly access the /find/ endpoint to fetch sensitive data, exploiting the lack of access controls.

**Command** ([[commands/curl-fetch-endpoint]]):
```bash
curl https://srcds.valve.net/find/
```

> This command sends a GET request to the endpoint and outputs the response. Successful execution will display raw data including server configs and API keys. If the vulnerability persists, expect JSON or structured text with sensitive fields; otherwise, an error or empty response may indicate patching.

### Step 2: Analyze Response for Sensitive Data

**Context**: Parse the output to extract and evaluate leaked information for usability in further attacks.

**Command** (Manual inspection or pipe to jq if JSON):
```bash
curl https://srcds.valve.net/find/ | jq '.'
```

> Inspect for API keys, server IPs, or configs. Look for patterns like 'api_key': 'value' or server endpoints. Document findings for reporting or exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-endpoint]]

## Tools Used


## Tags

- information-disclosure
- access-control
- valve
- srcds
- api-keys
