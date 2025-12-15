---
tags:
  - reconnaissance
  - subdomain-enumeration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.149Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 9f203a2c-8e2e-4698-a3aa-53f61f9eab3b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Subdomain-Redirect

## Summary

This procedure verifies the existence and redirect behavior of a protected subdomain, confirming it as a potential entry point to internal tools without direct access.

## Description

In the context of Yelp's proze.yelp.com, this step accesses the base subdomain to observe its redirect to the main site, indicating restricted access for external users. This reconnaissance confirms the subdomain's activity and sets up for direct path probing. Expected outcome: Identification of redirect patterns that can be bypassed.

## Requirements

1. Internet access to the target subdomain
2. Web browser or curl tool
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Implement strict subdomain isolation and redirect policies
- Monitor access logs for anomalous direct path requests
- Use WAF rules to block unauthorized endpoint probing

## Objectives

1. Confirm subdomain responsiveness
2. Identify redirect to main site
3. Prepare for internal endpoint discovery

## Instructions

### Step 1: Access Base Subdomain

**Context**: Send a request to the root of the subdomain to check for redirects.

**Command** ([[commands/curl-access-url]]):
```bash
curl -i https://proze.yelp.com/
```

> This command performs a HEAD request equivalent with -i to show headers. Expected output includes HTTP 302 status and Location header pointing to www.yelp.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[Reconnaissance]]
- [[subdomain-enumeration]]
