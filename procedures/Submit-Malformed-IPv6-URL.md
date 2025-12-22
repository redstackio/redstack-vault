---
id: proc-ipv6-url-submit-001
tags:
  - ssrf
  - ipv6
  - url-injection
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.538Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Malformed-IPv6-URL

## Summary

This procedure involves submitting a specially crafted IPv6 URL with a percent-encoded zone identifier to a libcurl-based application, setting up the conditions for parsing inconsistencies and potential SSRF.

## Description

Attackers target applications that accept user-supplied URLs for fetching, providing an IPv6 link-local address like http://[fe80::1%25eth0]/ where %25eth0 encodes the zone ID 'eth0'. The application, relying on libcurl, is expected to parse the full literal per RFC 6874 for interface routing, but stripping occurs. This step assumes access to an input endpoint (e.g., API or form) and focuses on URL construction without triggering immediate validation failures.

## Requirements

1. Access to a web application endpoint accepting URLs.
2. Knowledge of target network interfaces (e.g., eth0 for link-local routing).
3. No special tools beyond standard HTTP clients.

## Defense

Defensive measures and detection strategies:

- Implement strict URL schema validation to reject malformed IPv6 literals.
- Log and sanitize user-supplied URLs before parsing.
- Use allowlists for permitted host formats.

## Objectives

1. Inject a malformed URL to exploit parsing deviation.
2. Ensure the URL is processed by libcurl without rejection.
3. Prepare for observation of routing bypass.

## Instructions

### Step 1: Construct and Submit URL

**Context**: Craft the URL using percent-encoding for the zone ID to bypass basic filters.

**Command** (using curl for submission if API):
```bash
curl -X POST http://target-app.com/fetch -d 'url=http://[fe80::1%25eth0]/'
```

> Submits the URL to the application's fetch endpoint. Expected: 200 OK or processing acknowledgment.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- ipv6
- url-injection
