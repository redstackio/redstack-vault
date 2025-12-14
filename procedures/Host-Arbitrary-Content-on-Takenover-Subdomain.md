---
id: proc-uuid-3
tags:
  - content-hosting
  - phishing
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-http-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T04:51:26.879Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host Arbitrary Content on Takenover Subdomain

## Summary

This procedure uploads and serves custom content on the taken-over subdomain to demonstrate control, enabling attacks like phishing or brand impersonation.

## Description

With control of the subdomain (e.g., example-sub.mozaws.net), attackers deploy malicious or proof-of-concept files via the service's upload mechanisms. This can host phishing pages mimicking Mozilla services, leading to reputation damage. The content is served over HTTPS if the service supports it, amplifying trust.

## Requirements

1. Control of the registered service resource
2. Content files (e.g., HTML for PoC)
3. Access to upload/deploy tools for the service

## Defense

Defensive measures and detection strategies:

- Monitor traffic to subdomains for anomalous content
- Use domain shadowing detection tools
- Implement web application firewalls to block suspicious uploads

## Objectives

1. Serve custom content under the trusted domain
2. Enable phishing or malware distribution
3. Prove takeover impact

## Instructions

### Step 1: Upload Content to Service

**Context**: Deploy files to the controlled resource (e.g., git push to Heroku).

No command; manual: Create index.html with "Taken Over by Attacker", then `git add . && git commit -m 'poc' && git push heroku main`.

> Expected: Content deployed to the service.

### Step 2: Test Content Serving

**Context**: Verify the subdomain serves the uploaded content.

**Command** ([[commands/curl-http-test]]):
```bash
curl https://example-sub.mozaws.net
```

> Fetches the page. Expected output: HTML content from your upload, confirming control.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-http-test]]

## Tools Used

- None specific

## Tags

- [[Phishing]]
- [[web]]
