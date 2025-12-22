---
tags:
  - service-verification
  - uservoice
  - http-probe
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:51:10.584Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 27f49bbb-088f-48b6-a0df-0439e59d5996
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify Inactivity of UserVoice Service

## Summary

This procedure checks if a third-party service instance, such as a UserVoice subdomain, is active by probing its HTTP endpoint, confirming vulnerability to takeover.

## Description

For screenhero.uservoice.com, the attacker verifies deactivation by sending an HTTP request. Inactive instances return errors like 404 or 503, indicating no verification process blocks claiming the namespace. This step ensures the CNAME is exploitable.

## Requirements

1. Internet access to the target URL
2. HTTP client like curl or browser
3. Knowledge of the CNAME target from prior DNS query

## Defense

Defensive measures and detection strategies:

- Monitor third-party service status and promptly remove DNS records upon deactivation
- Use certificate transparency logs or external scanners to detect dangling records
- Implement subdomain validation in service providers

## Objectives

1. Confirm service inactivity to proceed with takeover
2. Assess exploitability without alerting defenders
3. Identify potential for unverified account creation

## Instructions

### Step 1: Probe HTTP Endpoint

**Context**: Send a HEAD request to the UserVoice instance to check for active responses.

**Command** ([[commands/curl-check-url]]):
```bash
curl -I https://screenhero.uservoice.com
```

> Expected output: HTTP/1.1 404 Not Found or similar, indicating the instance is not active and claimable.

### Step 2: Inspect Response

**Context**: Analyze headers and body for signs of deactivation, such as UserVoice error pages.

Use browser if needed to view full page; look for messages like "This site is not active."

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-url]]

## Tools Used


## Tags

- [[http-probe]]
- [[service-verification]]
