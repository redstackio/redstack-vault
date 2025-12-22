---
id: 123e4567-e89b-12d3-a456-426614174003
name: Claim-and-Control-Takeover-Domain
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.645Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Email Accounts]]'
sub_techniques: []
tags:
  - domain-claim
  - wix-hijack
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Email Accounts]]'
---

# Claim-and-Control-Takeover-Domain

## Summary

This procedure outlines claiming an unclaimed Wix site linked to a dangling CNAME, granting control over the domain for malicious activities.

## Description

With verification complete, use a Wix premium account to claim the site. Once controlled, the attacker can host arbitrary content, leading to phishing, malware, or XSS on the legitimate domain sifchain.finance.

## Requirements

1. Wix premium account
2. Verified unclaimed domain
3. Web browser for Wix dashboard

## Defense

Defensive measures and detection strategies:

- Monitor third-party service claims for owned domains
- Use domain monitoring services like Certificate Transparency
- Implement strict DNS change approvals

## Objectives

1. Gain administrative control of the domain
2. Deploy malicious payloads
3. Achieve impacts like authentication bypass or data exfiltration

## Instructions

### Step 1: Log In to Wix

**Context**: Access Wix with a premium account and navigate to site creation.

**Command** (Browser action):
No CLI command; use browser to log in at wix.com.

> Search for available sites and enter the target domain.

### Step 2: Claim and Configure

**Context**: Claim the site and upload custom content.

**Command** (Wix UI):
Upload HTML/JS for phishing or XSS via Wix editor.

> Publish changes to make the site live under the taken-over domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Email Accounts]] External Service Provider

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[domain-claim]]
- [[wix-hijack]]
