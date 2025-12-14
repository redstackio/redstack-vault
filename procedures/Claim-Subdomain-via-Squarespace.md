---
tags:
  - subdomain-takeover
  - dns-hijacking
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-dns-lookup-for-subdomain-resolution]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.490Z'
sub_techniques: []
id: 128007e8-1767-41f4-93b6-55a3b26b21bc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim Subdomain via Squarespace

## Summary

This procedure claims a dangling subdomain by entering it into Squarespace's domain settings, leveraging the existing verification CNAME to gain control and redirect DNS to the attacker's site.

## Description

With an active Squarespace account, the attacker navigates to domain settings and claims the subdomain '8ybhy85kld9zp9xf84x6.imgur.com'. The process verifies ownership via the pre-existing CNAME, allowing immediate control for hosting malicious content like phishing pages.

## Requirements

1. Active Squarespace account
2. Identified dangling subdomain
3. DNS propagation time allowance

## Defense

Defensive measures and detection strategies:

- Audit and remove old DNS verification records
- Use domain shadowing detection tools
- Monitor DNS changes via services like Cloudflare

## Objectives

1. Hijack subdomain control
2. Redirect traffic to attacker-hosted content
3. Enable attacks like phishing or XSS

## Instructions

### Step 1: Navigate to Domain Claiming

**Context**: Access the UI for custom domain addition.

**Command** (UI):

In Squarespace: Settings > Domains > Use a Domain I Own.

> Enter the subdomain and proceed to verification.

### Step 2: Verify and Claim

**Context**: The system auto-verifies due to CNAME; claim succeeds.

**Command** (Post-claim DNS check with [[commands/dig-dns-lookup-for-subdomain-resolution]]):

```bash
dig 8ybhy85kld9zp9xf84x6.imgur.com
```

> Output: CNAME updated to attacker's site; A records for Squarespace IPs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup-for-subdomain-resolution]]

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[dns-hijacking]]
