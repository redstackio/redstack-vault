---
id: proc-cname-propagate-001
tags:
  - dns-propagation
  - domain-claim
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/AWS-CloudFront-Console]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:39.692Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Wait for CNAME Propagation and Claim Domain

## Summary

This procedure monitors and verifies the propagation of the added CNAME in CloudFront, confirming the subdomain takeover once traffic routes to the attacker's distribution.

## Description

DNS and CloudFront propagation takes time globally; this step ensures the claim is active by testing resolution and access, targeting AWS and DNS systems for hijacking confirmation.

## Requirements

1. Recently created CloudFront distribution with CNAME
2. DNS query tools
3. Browser or curl for verification

## Defense

Defensive measures and detection strategies:

- Implement short TTL on DNS records and monitor changes
- Use services like SecurityTrails for DNS change alerts
- Scan for takeovers with tools like Subjack or dnsrecon

## Objectives

1. Confirm global propagation
2. Validate traffic redirection
3. Secure the hijacked domain

## Instructions

### Step 1: Monitor Distribution Status

**Context**: Check CloudFront console for deployment completion.

Refresh [[tools/AWS-CloudFront-Console]]; wait for status to change from 'In Progress' to 'Deployed' (about 15 minutes).

### Step 2: Test DNS and Access

**Context**: Verify the subdomain now resolves to your distribution.

Run:

```bash
dig partners.ubnt.com
```

Then access http://partners.ubnt.com in browser.

> Expect resolution to your CloudFront and content loading.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AWS-CloudFront-Console]]

## Tags

- [[dns-propagation]]
- [[subdomain-takeover]]
