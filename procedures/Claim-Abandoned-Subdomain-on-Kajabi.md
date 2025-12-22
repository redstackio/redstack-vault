---
id: proc-claim-kajabi-subdomain
tags:
  - subdomain-takeover
  - kajabi
  - domain-hijacking
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.321Z'
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
# Claim Abandoned Subdomain on Kajabi

## Summary

This procedure registers a new site on Kajabi using the abandoned subdomain name, hijacking control via the dangling DNS record.

## Description

Since the original Kajabi site for course.oberlo.com is deleted, creating a new one with the same name allows Kajabi to associate it with the incoming DNS traffic, granting full control for hosting malicious content.

## Requirements

1. Free Kajabi account
2. Verified dangling subdomain
3. Access to Kajabi dashboard for domain setup

## Defense

Defensive measures and detection strategies:

- Monitor third-party service logs for new site claims on old domains
- Implement domain locking or verification challenges
- Conduct regular subdomain audits with takeover scanners

## Objectives

1. Register and configure new Kajabi site
2. Assign the target subdomain
3. Gain control over traffic

## Instructions

### Step 1: Create Kajabi Account and Site

**Context**: Sign up and set up a basic site.

No command; use Kajabi signup at kajabi.com and create a site named matching the subdomain (e.g., 'course').

### Step 2: Configure Custom Domain

**Context**: Add and verify the subdomain in settings.

In dashboard: Settings > Domains > Add Custom Domain > Enter course.oberlo.com > Verify via DNS (automatic since dangling).

Test with browser access post-setup.

```bash
curl https://course.oberlo.com
```

> Should now resolve to your new site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[subdomain-takeover]]
- [[kajabi]]
