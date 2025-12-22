---
id: proc-claim-freshdesk-subdomain
tags:
  - subdomain-claim
  - freshdesk-takeover
  - impersonation
type: procedure
tools:
  - '[[tools/Freshdesk]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1583.001]]'
updated_at: '2025-12-14T04:38:39.895Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1583.001]]'
---
# Claim-Subdomain-on-Freshdesk

## Summary

This procedure claims a dangling subdomain on Freshdesk by registering the associated custom domain, gaining control over fddkim.zomato.com for malicious use.

## Description

Freshdesk allows custom subdomain mapping; with a dangling DNS, an attacker registers it to hijack traffic. For fddkim.zomato.com, this enabled potential phishing. Prerequisites: Free Freshdesk account. Outcomes: Full control for hosting fake support pages or redirects.

## Requirements

1. Free Freshdesk account
2. Verified dangling subdomain
3. Basic web configuration knowledge

## Defense

Defensive measures and detection strategies:

- Monitor DNS changes and subdomain resolutions
- Use certificate pinning or HSTS to prevent hijacks
- Audit third-party accounts regularly for inactivity

## Objectives

1. Register the subdomain on Freshdesk
2. Configure custom domain mapping
3. Verify control and propagate changes

## Instructions

### Step 1: Create Freshdesk Account and Claim

**Context**: Sign up and initiate domain claim for the dangling pointer.

**Instructions**: Log into Freshdesk, go to Admin > Domains > Add Custom Domain, enter fddkim.freshdesk.com, and follow verification (automatic via DNS match).

> Expected: Claim success; DNS propagates in minutes.

### Step 2: Configure and Test

**Context**: Upload content to the claimed subdomain.

**Instructions**: In Freshdesk portal, customize the helpdesk page with malicious HTML (e.g., phishing form). Test resolution:

```bash
nslookup fddkim.zomato.com
```

> Expected: Resolves to attacker's Freshdesk IP; browser shows custom page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1583.001]] Acquire Infrastructure: Domains

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Freshdesk]]

## Tags

- [[subdomain-claim]]
- [[freshdesk-takeover]]
