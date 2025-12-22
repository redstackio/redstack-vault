---
tags:
  - domain-claiming
  - takeover
type: procedure
tools:
  - '[[tools/Mashery-Dashboard]]'
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
updated_at: '2025-12-14T04:38:39.527Z'
sub_techniques: []
id: 15869dd8-a8d4-42bf-bf98-6c9d507682c2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Subdomain-on-Mashery-Dashboard

## Summary

Add the dangling subdomain to the Mashery dashboard as a custom domain, exploiting lack of validation to gain control.

## Description

In the 'Portal Settings', adding developer.openapi.starbucks.com succeeds without errors due to the dangling CNAME, transferring control to the attacker.

## Requirements

1. Active Mashery account
2. Dashboard access
3. Target subdomain details

## Defense

Defensive measures and detection strategies:

- Enforce domain ownership verification (e.g., DNS TXT)
- Audit custom domain additions
- Expire dangling records immediately

## Objectives

1. Associate subdomain with attacker portal
2. Bypass any validation
3. Enable content serving

## Instructions

### Step 1: Access Portal Settings

**Context**: Navigate to domain configuration.

Log into Mashery dashboard and go to 'Portal Settings'.

**Expected Output**: Settings interface.

### Step 2: Add Custom Domain

**Context**: Input the target subdomain.

Enter developer.openapi.starbucks.com and save.

**Expected Output**: Domain added without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mashery-Dashboard]]

## Tags

- [[domain-claiming]]
- [[takeover]]
