---
id: proc-uuid-3
tags:
  - exfiltration
  - idor
  - web
  - api
  - data-leak
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-send-api-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:25:23.376Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
---
# Send-Modified-Request-and-Exfil-Data

## Summary

This procedure submits the tampered Veris API request and captures the response containing unauthorized venue data, confirming the IDOR and enabling data exfiltration.

## Description

With the venue_id modified, the attacker sends the request to the Veris endpoint. Due to the IDOR, the server returns the full venue data for the targeted organization without checking permissions. The response typically includes sensitive details like venue configurations, addresses, and metadata. Attackers can repeat this for multiple IDs to map and exfiltrate data. Detection may occur via anomalous API calls, but the simplicity makes it stealthy.

## Requirements

1. Modified request from previous procedure
2. Ability to forward via proxy or command-line tool like curl
3. Target API endpoint URL and auth details

## Defense

Defensive measures and detection strategies:

- Rate-limit API requests per user and monitor for ID enumeration patterns
- Use role-based access control (RBAC) to validate object ownership
- Encrypt sensitive data in responses and audit access logs for anomalies

## Objectives

1. Retrieve unauthorized venue data via the exploited endpoint
2. Validate IDOR success through response analysis
3. Exfiltrate data for further use or reporting

## Instructions

### Step 1: Forward Request via Proxy

**Context**: Use Burp Suite to send the modified request and inspect the response.

In Burp Repeater, click 'Send' on the edited request.

> Expected output: HTTP 200 response with JSON payload containing target venue data, e.g., {"venue_id": 456, "name": "Target Org Venue", "details": {...}}.

### Step 2: Alternative Direct Send with Curl

**Context**: For automation or non-proxy use, replicate the request using curl.

Execute [[commands/curl-send-api-request]] to mimic the API call:

```bash
curl -X GET "https://veris.example.com/api/venues/456" -H "Authorization: Bearer your_token" -H "Content-Type: application/json"
```

> Expected output: JSON response with unauthorized data; save to file for analysis, e.g., curl ... > exfil_data.json.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Local System]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-api-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[Exfiltration]]
- [[idor]]
- [[data-leak]]
