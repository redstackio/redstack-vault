---
id: uuid-claim-subdomain
tags:
  - subdomain-takeover
  - hijacking
  - piwik-cloud
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
updated_at: '2025-12-14T05:32:31.152Z'
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
# Claim Dangling Subdomain

## Summary

This procedure claims control of a dangling Piwik Cloud subdomain by adding the parent domain to a newly created account, effectively hijacking the subdomain for malicious use.

## Description

Once a Piwik Cloud account is established, adding the parent domain (e.g., gratipay.com) associates the subdomain (e.g., gratipay.piwik.pro) with the account, transferring control due to the dangling status. This exploits the service's domain verification mechanism, allowing the attacker to host content or analytics under the victim's domain. Outcomes include full subdomain control, enabling phishing or impersonation.

## Requirements

1. Active Piwik Cloud account from previous step
2. Knowledge of the parent domain
3. Web access to account dashboard

## Defense

Defensive measures and detection strategies:

- Implement strict domain ownership verification (e.g., TXT records)
- Audit third-party service integrations and remove unused ones
- Monitor for unauthorized subdomain resolutions via DNS logs

## Objectives

1. Secure control over the dangling subdomain
2. Enable exploitation like content hosting
3. Achieve persistence under the victim's brand

## Instructions

### Step 1: Log In to Account

**Context**: Access the Piwik Cloud dashboard to manage domains.

No command; browser login.

> Log in using the created credentials at http://piwik.pro/cloud.

### Step 2: Add Parent Domain

**Context**: Submit the parent domain to claim the associated subdomain.

No command; form input.

> In account settings, enter and add "gratipay.com" (or target parent domain). Confirm the addition.

### Step 3: Verify Claim

**Context**: Test the subdomain to ensure control is gained.

No command; revisit URL.

> Reload https://gratipay.piwik.pro/ to see it now under your account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[hijacking]]
