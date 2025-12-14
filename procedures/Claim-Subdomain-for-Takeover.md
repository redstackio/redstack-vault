---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - subdomain-takeover
  - phishing
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-http-access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.425Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Subdomain-for-Takeover

## Summary

This procedure demonstrates claiming an unclaimed subdomain on a service like statuspage.io to gain control, allowing deployment of phishing pages or scripts that leverage the parent domain's trust for attacks like cookie theft.

## Description

Once an unclaimed subdomain is identified (e.g., status.vimeo.com pointing to hosted.statuspage.io), an attacker registers on the service and claims the subdomain during setup. This grants full administrative control, enabling custom HTML/JS for fake login forms that exploit same-origin policy to steal Vimeo session cookies, leading to account compromises.

## Requirements

1. Free account on the target service (e.g., statuspage.io)
2. Knowledge of the vulnerable subdomain's CNAME
3. Web browser for registration and customization

## Defense

Defensive measures and detection strategies:

- Proactively claim all subdomains on third-party services
- Use monitoring tools to alert on DNS changes or unclaimed pages
- Implement certificate pinning or HSTS to limit subdomain trust abuse

## Objectives

1. Secure control over the subdomain for malicious content hosting
2. Exploit domain trust for phishing or session hijacking
3. Validate impact through proof-of-concept deployment

## Instructions

### Step 1: Register on External Service

**Context**: Create an account to access the claiming interface.

**Command** (N/A - manual browser step):
Navigate to https://www.statuspage.io/register and sign up with an email.

> Upon registration, proceed to create a new status page and enter the subdomain (e.g., status.vimeo.com) when prompted for custom domain.

### Step 2: Claim and Verify Control

**Context**: Confirm the claim and test access to deploy content.

**Command** ([[commands/curl-http-access]]):
```bash
curl http://status.vimeo.com
```

> After claiming, customize the page (e.g., add phishing form). Expected output now shows your custom content instead of the unclaimed prompt, confirming takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-http-access]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[Phishing]]
- [[initial-access]]
