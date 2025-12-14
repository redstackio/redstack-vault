---
tags:
  - shopify
  - domain-creation
  - security-settings
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:36.331Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e333f8a7-6239-4f7f-be74-a0d527418b01
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Create-Organization-Domain-in-Shopify

## Summary

This procedure creates a new domain in the Shopify Plus organization security settings, establishing a target for testing domain enforcement state changes via unauthorized API access.

## Description

Shopify Plus organizations manage domains for verification and enforcement to prevent unauthorized usage. Creating a domain as an admin sets it to ENFORCED state initially, allowing subsequent queries and mutations to demonstrate bypasses by low-privileged users.

## Requirements

1. Admin credentials for organization security settings
2. Valid domain name to add
3. Access to https://shopify.plus/:org_id/users/security

## Defense

Defensive measures and detection strategies:

- Restrict domain creation to verified admins only
- Log all domain additions and monitor for rapid changes
- Enforce multi-factor approval for security setting modifications

## Objectives

1. Add a new domain to the organization
2. Ensure initial ENFORCED state for testing
3. Generate a domain ID for API targeting

## Instructions

### Step 1: Access Security Settings

**Context**: Navigate to the domain management UI as admin.

Visit https://shopify.plus/:org_id/users/security and click 'Add Domain'.

> Expected output: Form to input domain details.

### Step 2: Add and Verify Domain

**Context**: Submit the domain and confirm creation.

Enter the domain name (e.g., example.com) and save. Verify it appears with ENFORCED status.

> Expected output: Domain listed in security settings with ID and status.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- domain-management
- enforcement-bypass
