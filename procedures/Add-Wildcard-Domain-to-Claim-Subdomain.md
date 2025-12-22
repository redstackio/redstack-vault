---
id: proc-add-wildcard-claim
tags:
  - wildcard-dns
  - subdomain-takeover
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
updated_at: '2025-12-14T04:51:26.595Z'
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
# Add Wildcard Domain to Claim Subdomain

## Summary

This procedure claims a dangling subdomain by adding a wildcard domain (*.legalrobot.com) in the Modulus.io dashboard, bypassing restrictions on specific subdomain claims and gaining control over the target.

## Description

When direct subdomain addition fails due to partial registration, attackers use wildcard configurations to capture unmatched subdomains. Here, after account creation, adding *.legalrobot.com succeeds because the specific api.legalrobot.com lacks an active app. This exploits Modulus.io's domain verification logic. Target: Modulus.io dashboard. Prerequisites: Active Modulus account. Expected outcome: Control over the subdomain for further configuration.

## Requirements

1. Active Modulus.io account from previous steps
2. Target domain knowledge (legalrobot.com)
3. Dashboard access

## Defense

Defensive measures and detection strategies:

- Avoid wildcard DNS delegations to third parties
- Verify all subdomains are actively configured or removed
- Implement certificate transparency monitoring for subdomain changes

## Objectives

1. Secure control of the dangling subdomain via wildcard
2. Enable application hosting on the subdomain
3. Prepare for content serving or exploitation

## Instructions

### Step 1: Navigate to Domain Settings

**Context**: Access the domain management section in Modulus.io.

Log in and go to the application domains or settings page.

> Expected output: Interface for adding custom domains.

### Step 2: Add Wildcard Domain

**Context**: Input the wildcard to claim unconfigured subdomains.

Enter '*.legalrobot.com' and confirm addition.

> Expected output: Success confirmation, with the wildcard now associated with your application.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[wildcard-dns]]
- [[subdomain-takeover]]
