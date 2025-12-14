---
tags:
  - heroku
  - subdomain-takeover
  - cloud
type: procedure
tools:
  - '[[tools/Heroku-Dashboard]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Cloud (Heroku)
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Acquire Infrastructure]]'
updated_at: '2025-12-14T04:39:01.808Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1583.008]]'
id: cea26f61-c45c-4e6d-984f-3907e7b23e96
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Acquire Infrastructure]]'
---
# Claim-Unclaimed-Heroku-Subdomain

## Summary

This procedure claims a dangling subdomain by adding it as a custom domain to a new Heroku app, exploiting unclaimed DNS targets for takeover.

## Description

Attackers with a Heroku account can claim subdomains pointing to unclaimed herokudns.com targets. In the scenario, after discovering the dangling CNAME for competition.shopify.com, a new Heroku app is created, and the domain is added via the dashboard. The target environment is Heroku-integrated domains. Outcomes include full ownership, allowing content hosting. Prerequisites: Valid Heroku account and confirmed dangling record.

## Requirements

1. Active Heroku account with billing enabled if needed
2. Access to Heroku Dashboard
3. Verified dangling CNAME to herokudns.com

## Defense

Defensive measures and detection strategies:

- Promptly remove DNS records for decommissioned apps
- Use Heroku's domain verification and monitor for unauthorized claims
- Implement certificate transparency monitoring for subdomains

## Objectives

1. Register the subdomain to gain control
2. Verify ownership through DNS propagation
3. Enable further exploitation like content deployment

## Instructions

### Step 1: Create New Heroku App

**Context**: Set up a blank app to associate with the subdomain.

Log in to the Heroku Dashboard and create a new app.

> No CLI command; use the web interface to select 'Create new app' and name it arbitrarily.

### Step 2: Add Custom Domain

**Context**: Associate the dangling subdomain with the app.

In the app's settings, navigate to 'Domains' and add 'competition.shopify.com' as a custom domain.

> Heroku will automatically claim it if unowned.

> Expected output: Success message confirming domain addition; DNS instructions provided.

### Step 3: Verify Claim

**Context**: Confirm the subdomain now points to the new app.

Wait for DNS propagation and test resolution.

```bash
# Use dig or nslookup to verify
nslookup competition.shopify.com
```

> Expected output: Resolves to the new Heroku app's endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Acquire Infrastructure]]

### Sub-Techniques

- [[T1583.008]]

## Commands Used


## Tools Used

- [[tools/Heroku-Dashboard]]

## Tags

- [[heroku]]
- [[subdomain-takeover]]
- [[cloud]]
