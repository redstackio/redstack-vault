---
id: proc-waf-bypass-defaults
tags:
  - waf-bypass
  - authenticated-access
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:36.743Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-WAF-via-Authenticated-Access-with-Default-Credentials

## Summary

This procedure exploits the fact that WAF rules often allow legitimate authenticated traffic, using default credentials to create a valid session that evades security filters.

## Description

Web Application Firewalls (WAFs) typically inspect and block suspicious unauthenticated requests but permit traffic from authenticated users. In the Starbucks case, default credentials on the POC site provided a clean path to authentication, bypassing WAF scrutiny and exposing the application to further attacks like command injection.

## Requirements

1. Successful login from prior procedure
2. Valid session cookie or token
3. Knowledge of protected endpoints

## Defense

Defensive measures and detection strategies:

- Configure WAF to inspect authenticated traffic for anomalies
- Implement rate limiting and behavioral analysis on all sessions
- Regularly audit WAF rules for bypass paths
- Monitor for default credential usage in logs

## Objectives

1. Access protected application features
2. Evade WAF detection
3. Prepare for vulnerability exploitation

## Instructions

### Step 1: Maintain Authenticated Session

**Context**: Use the session established with default credentials to send requests.

Include the session cookie in subsequent HTTP requests, e.g., via browser or curl:

```bash
curl -X GET 'https://alipoc.stg.starbucks.com.cn/protected' -H 'Cookie: session=valid_token'
```

> The request succeeds without WAF intervention, returning application data.

### Step 2: Test WAF Evasion

**Context**: Attempt a benign but potentially flagged request to confirm bypass.

Submit a request that might trigger WAF if unauthenticated, such as a parameter with special characters.

### Step 3: Explore Application

**Context**: Navigate to features that could be vulnerable.

Use the authenticated access to locate input fields or forms for further testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[waf-bypass]]
- [[default-credentials]]
