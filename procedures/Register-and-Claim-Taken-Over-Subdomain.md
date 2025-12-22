---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - subdomain-takeover
  - dns-hijacking
  - cloud-misconfig
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-subdomain]]'
verified: false
platforms:
  - Web
  - Cloud
  - DNS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.620Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-and-Claim-Taken-Over-Subdomain

## Summary

This procedure claims control of a dangling subdomain by registering the unused service it points to, such as creating a new app on Heroku or bucket on AWS S3 matching the DNS record.

## Description

After identifying a dangling DNS record, the attacker registers on the third-party service and creates a resource with the exact name referenced in the DNS. This redirects the subdomain traffic to the attacker's controlled service. No direct access to the target's DNS is needed, making it stealthy. Expected outcome: Full control over the subdomain for further exploitation.

## Requirements

1. Account on the target service (e.g., Heroku, AWS)
2. Confirmed dangling record from prior recon
3. Basic knowledge of the service's registration process

## Defense

Defensive measures and detection strategies:

- Remove or update dangling DNS records during resource decommissioning
- Monitor third-party services for unauthorized registrations matching domain subdomains
- Use subdomain validation tools to alert on takeovers

## Objectives

1. Gain ownership of the subdomain
2. Verify resolution to controlled service
3. Enable content hosting

## Instructions

### Step 1: Register on Service

**Context**: Create an account and resource matching the dangling record's target.

**Command** (No CLI; manual via web):

> Log into the service (e.g., heroku.com), create a new app named 'subdomain' to match the CNAME.

### Step 2: Verify Control

**Context**: Confirm the subdomain now points to your service.

**Command** ([[commands/curl-check-subdomain]]):
```bash
curl -I https://subdomain.mozaws.net
```

> This checks the HTTP headers; expected output: 200 OK from your service, not 404 or error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-check-subdomain]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[initial-access]]
