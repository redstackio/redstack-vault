---
tags:
  - redirect
  - token-leak
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-sso-request]]'
platforms:
  - Web
  - GCP
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: e6a669d7-f486-403e-a42b-cbef9e60c0fe
created_at: '2025-12-13T09:01:26.664Z'
updated_at: '2025-12-13T09:01:26.664Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Redirect to Malicious SVG

## Summary

This procedure triggers a redirect from Snapchat to Google Cloud Storage, carrying the SSO token in the hash fragment.

## Description

The 307 redirect preserves the hash, allowing the token to reach the malicious SVG. This bridges the referrer manipulation to XSS.

## Requirements

1. Manipulated referrer set up
2. Hosted malicious SVG
3. Access to media endpoint

## Defense

Defensive measures and detection strategies:

- Prevent hash preservation in redirects
- Validate redirect targets

## Objectives

1. Carry token to XSS vector
2. Enable execution context
3. Facilitate theft

## Instructions

### Step 1: Initiate Redirect

**Context**: Request the media file URL.

**Command** ([[commands/curl-sso-request]]):
```bash
curl -L 'https://snappublisher.snapchat.com/api/v1/media/████/file/somthine.svg?%23pranav'
```

> Follows the redirect chain.

### Step 2: Confirm Token in Hash

**Context**: Verify hash in final URL.

**Command** ([[commands/curl-sso-request]]):
```bash
curl -v 'https://snappublisher.snapchat.com/api/v1/media/████/file/somthine.svg?%23pranav'
```

> Shows redirect details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-sso-request]]

## Tools Used

- [[tools/Curl]]

## Tags

- [[redirect]]
- [[token-leak]]
