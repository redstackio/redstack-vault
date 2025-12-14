---
tags:
  - subdomain-takeover
  - verification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-verify-subdomain]]'
platforms:
  - Web
  - AWS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 21db98f2-4d61-44a5-a4cc-aa6ed9704d88
created_at: '2025-12-14T05:32:24.288Z'
updated_at: '2025-12-14T05:32:24.288Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Subdomain-Takeover-Success

## Summary

This procedure confirms the subdomain takeover by accessing the original subdomain URL and verifying it serves the uploaded attacker content.

## Description

Post-upload, the DNS CNAME routes traffic to the new S3 bucket. Accessing http://gameday.websummit.net should display the POC, proving full control and potential for phishing or other exploits.

## Requirements

1. Successful bucket creation and upload
2. Public DNS propagation (minimal delay)
3. HTTP client for testing

## Defense

Defensive measures and detection strategies:

- Implement subdomain monitoring with tools like certificate transparency logs
- Use web application firewalls to detect anomalous content on subdomains
- Conduct regular subdomain takeover scans with tools like subjack

## Objectives

1. Validate content serving from subdomain
2. Demonstrate impact to stakeholders
3. Confirm exploit completion

## Instructions

### Step 1: Access Subdomain

**Context**: Fetch the root page of the hijacked subdomain.

**Command** ([[commands/curl-verify-subdomain]]):
```bash
curl http://gameday.websummit.net
```

> Response should match the uploaded POC HTML, not an error.

### Step 2: Browser Validation

**Context**: Manually browse to confirm visual takeover.

**Command** ([[commands/curl-verify-subdomain]]):
```bash
curl -L http://gameday.websummit.net
```

> Use -L for any redirects; expect attacker content in browser too.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-verify-subdomain]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[verification]]
