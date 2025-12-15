---
id: proc-002
tags:
  - intercept
  - json-conversion
  - burp-suite
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Content-Type-Converter]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:34.524Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Convert-Reset-Request-to-JSON

## Summary

This procedure uses Burp Suite to intercept the GitLab password reset request and converts its form-encoded body to JSON format, enabling easier modification and exploitation of the backend's JSON parsing without validation.

## Description

Targeting the HTTP POST to the password reset endpoint, this step captures the request during submission. The original request uses application/x-www-form-urlencoded, but conversion to JSON exploits the server's acceptance of JSON payloads. Prerequisites include Burp Suite setup as a proxy. Outcome: A modifiable JSON structure for email injection.

## Requirements

1. Burp Suite running and browser proxied to it (e.g., 127.0.0.1:8080)
2. Content-Type Converter extension installed in Burp
3. Active interception enabled in Proxy tab

## Defense

Defensive measures and detection strategies:

- Enforce strict Content-Type validation on endpoints (reject JSON if not expected)
- Log and alert on proxy-like User-Agent strings or unusual request modifications
- Use WAF rules to detect format changes in reset requests

## Objectives

1. Capture the reset submission for tampering
2. Convert payload to exploit JSON processing
3. Maintain request integrity for forwarding

## Instructions

### Step 1: Intercept the Request

**Context**: Proxy the submission to hold the request for inspection.

Configure Burp Proxy to intercept POST requests to /users/password.

> Submit the form from Step 1; request appears in Intercept tab with body like user[email]=victim@gmail.com.

### Step 2: Convert to JSON

**Context**: Transform the body to JSON using the extension.

In the Raw tab of the request editor, right-click the body and select Extensions > Content-Type Converter > Convert to JSON.

> Expected: Body becomes {"user":{"email":"victim@gmail.com"}}, Content-Type: application/json.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

None

## Commands Used

None

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Content-Type-Converter]]

## Tags

- [[intercept]]
- [[json-conversion]]
- [[tools/Burp-Suite]]
- [[web]]
