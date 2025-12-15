---
id: proc-uuid-6
tags:
  - sso
  - integration
  - account-discovery
  - shopify
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:58.658Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Initiate-SSO-Integration-for-Linked-Accounts

## Summary

This procedure detects and starts the process of linking other Shopify accounts tied to the hijacked email via SSO.

## Description

With the target email confirmed, Shopify's SSO prompts for integration of shared-email accounts, revealing stores and partners.

## Requirements

1. Target email confirmed on account
2. Profile access

## Defense

Defensive measures and detection strategies:

- Separate SSO for partners vs. stores
- Require explicit owner consent for integrations
- Monitor for sudden multi-account links

## Objectives

1. Identify linked accounts
2. Begin takeover integration

## Instructions

### Step 1: Check Profile for Prompt

**Context**: Look for SSO indicators.

Reload the profile page after confirmation.

> Notice banner or section: 'Other accounts linked to this email'.

### Step 2: Click Integrate

**Context**: Start SSO flow.

Select 'Integrate accounts' or similar option.

> List of stores/partners loads for connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sso]]
- [[integration]]
- [[account-discovery]]
- [[shopify]]
