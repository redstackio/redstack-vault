---
tags:
  - subdomain-takeover
  - unbounce
  - phishing
  - impersonation
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
updated_at: '2025-12-14T04:38:49.360Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e01c8925-3f82-4507-aef2-02650495a61b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Research-and-Attempt-Unbounce-Takeover

## Summary

This procedure researches the third-party service (Unbounce) linked by the dangling CNAME and attempts to claim the subdomain by creating a new configuration, enabling hosting of fake content for phishing or impersonation.

## Description

After confirming the CNAME to unbouncepages.com, investigate Unbounce's policies on subdomain claiming. If the original page is deleted, attackers can sign up, create a new landing page, and add the CNAME, redirecting traffic to malicious content. This leads to phishing attacks impersonating the legitimate service (e.g., Greenhouse.io), with impacts including credential theft and reputation harm. Full PoC may require a paid subscription.

## Requirements

1. Access to the internet and Unbounce signup
2. Knowledge of the service's DNS integration
3. The dangling subdomain CNAME value

## Defense

Defensive measures and detection strategies:

- Monitor third-party service integrations and revoke inactive ones
- Use certificate transparency logs to detect unauthorized subdomain usage
- Implement domain shadowing detection tools

## Objectives

1. Confirm takeover eligibility
2. Claim and configure the subdomain
3. Deploy malicious payload (e.g., fake login)

## Instructions

### Step 1: Research Service Documentation

**Context**: Review Unbounce docs for subdomain claiming process and conditions for dangling records.

**Instructions**: Visit Unbounce support pages and search for "CNAME subdomain setup". Note requirements like page creation and DNS verification.

> Expected output: Understanding that deleted pages allow new claims with matching CNAME.

### Step 2: Verify Page Deletion

**Context**: Check if the original Unbounce page linked to the CNAME is active.

**Instructions**: Attempt to access https://demo.greenhouse.io or query Unbounce API if available. Look for 404 or deletion confirmation.

> Expected output: Confirmation of inactive status, enabling claim.

### Step 3: Attempt Claim

**Context**: Sign up for Unbounce and configure the takeover.

**Instructions**: Create an account, build a new page, and add CNAME: demo.greenhouse.io pointing to your Unbounce page URL. Wait for DNS propagation and verify control.

> Expected output: Successful subdomain resolution to attacker-hosted content. Note: Subscription may be needed for full features.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[service-takeover]]
- [[phishing-setup]]
