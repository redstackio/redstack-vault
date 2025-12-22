---
tags:
  - verification
  - takeover
  - poc
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-http-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.715Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 87645592-62ba-4fed-a692-d929e7ae4fb4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Subdomain Takeover

## Summary

This procedure confirms successful subdomain takeover by serving and accessing arbitrary content on the controlled subdomain.

## Description

Post-claim, upload custom content to the resource and test resolution via the subdomain. This validates control for phishing or malware hosting. Targets are the hijacked subdomain; requires prior claim.

## Requirements

1. Control of the third-party resource
2. Content to upload (e.g., HTML file)
3. Time for DNS propagation (5-15 minutes)

## Defense

Defensive measures and detection strategies:

- Monitor subdomains for unexpected content changes
- Use content security policies and certificate pinning
- Alert on DNS changes via external services

## Objectives

1. Serve custom content
2. Confirm DNS resolution
3. Provide proof (screenshot/URL)

## Instructions

### Step 1: Upload Arbitrary Content

**Context**: Place a test file on the resource.

No command; web-based: Upload index.html with "Takeover Verified" to the resource.

### Step 2: Test Access via Subdomain

**Context**: Fetch the subdomain to verify content.

**Command** ([[commands/curl-http-request]]):
```bash
curl -v https://███████.target.com
```

> Output should return the uploaded HTML, confirming takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-http-request]]

## Tools Used


## Tags

- [[verification]]
- [[takeover]]
- [[poc]]
