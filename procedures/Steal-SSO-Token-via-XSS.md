---
tags:
  - xss
  - token-theft
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-access-with-token]]'
platforms:
  - Web
  - GCP
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5ee2653e-2e92-4ba6-ab70-24cba0f8dffc
created_at: '2025-12-13T09:01:26.657Z'
updated_at: '2025-12-13T09:01:26.657Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Steal SSO Token via XSS

## Summary

This procedure uses XSS in an uploaded SVG to extract and steal the SSO token from the URL hash fragment.

## Description

The JS in the SVG accesses location.hash and can log or exfiltrate it. This completes the theft after redirect.

## Requirements

1. Redirected URL with token in hash
2. Browser or simulator to load SVG
3. Exfiltration server if needed

## Defense

Defensive measures and detection strategies:

- Block JS in SVGs
- Monitor console logs for anomalies

## Objectives

1. Extract token from hash
2. Log or send to attacker
3. Enable account access

## Instructions

### Step 1: Load SVG with Token

**Context**: Access the GCS URL with hash.

**Command** ([[commands/curl-access-with-token]]):
```bash
curl 'https://storage.googleapis.com/creativesuite-prod-media/*#<token>'
```

> Loads the SVG, executing JS.

### Step 2: Capture Output

**Context**: Check console for stolen token.

**Command** ([[commands/curl-access-with-token]]):
```bash
curl -v 'https://storage.googleapis.com/creativesuite-prod-media/*#<token>'
```

> In browser, JS alerts or logs the token.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/curl-access-with-token]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[token-theft]]
