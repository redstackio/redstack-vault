---
tags:
  - intercept
  - proxy
  - http-manipulation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:24:48.291Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c0ceedb1-04aa-4c61-90cc-741a53be97f3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
---
# Intercept-Login-POST-Request-with-Burp-Suite

## Summary

Use Burp Suite to capture the POST request to Grammarly's login endpoint during the MFA submission, allowing inspection of the JSON payload and headers.

## Description

Configure Burp Suite as a browser proxy to intercept traffic to auth.grammarly.com. When submitting the invalid MFA code, the tool captures the request containing the MFA mode, secureLogin flag, and cookies like 'tdi'. This step is crucial for the subsequent modification in the bypass attack.

## Requirements

1. Burp Suite installed and running
2. Browser proxy set to 127.0.0.1:8080
3. Victim's session active

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and certificate pinning to hinder proxy interception
- Detect proxy usage via timing anomalies or header inconsistencies

## Objectives

1. Capture the exact request structure
2. Verify presence of exploitable fields
3. Preserve cookies for reuse

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception for the target endpoint.

In Burp, enable Intercept in Proxy tab; scope to auth.grammarly.com.

> Expected: Traffic routed through Burp.

### Step 2: Trigger and Capture

**Context**: Submit MFA to intercept.

Perform login/MFA submission; request pauses in Burp.

> Expected: POST /v3/api/login visible with JSON body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[proxy]]
- [[http-manipulation]]
