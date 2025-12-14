---
tags:
  - fastly
  - registration
  - takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: e457fc7c-a450-452b-8600-a0c3c76f8dec
created_at: '2025-12-14T04:38:39.953Z'
updated_at: '2025-12-14T04:38:39.953Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Subdomain-in-Fastly

## Summary

This procedure claims an unowned subdomain in a personal Fastly account, gaining control over DNS-pointed traffic to enable content serving on the victim's domain.

## Description

With verification complete, log into Fastly and register the target subdomain. Fastly allows claiming if not owned, routing traffic to the attacker's service. This exploits CDN trust models, allowing impersonation of the original owner like Mozilla, with risks of phishing or XSS.

## Requirements

1. Active Fastly account
2. Verified unclaimed subdomain
3. Browser access to Fastly dashboard

## Defense

Defensive measures and detection strategies:

- Proactively register all subdomains in CDN consoles
- Enable alerts for new domain additions in CDN logs
- Conduct regular subdomain inventory audits

## Objectives

1. Secure control of the subdomain
2. Route traffic to attacker resources
3. Enable subsequent exploitation

## Instructions

### Step 1: Log In to Fastly

**Context**: Access the Fastly management interface.

**Command** (Manual):
Navigate to https://manage.fastly.com and log in.

> Ensure account is verified and has service creation permissions.

### Step 2: Add Custom Domain

**Context**: Register the subdomain in domain settings.

**Command** (Manual):
In service settings, add 'addons-preview-cdn.mozilla.net' as a custom domain and validate DNS.

> Success shown by green validation status; traffic now routes to your service.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[fastly]]
- [[registration]]
- [[takeover]]
