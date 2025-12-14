---
tags:
  - domain-creation
  - saml
  - shopify-plus
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Shopify Plus
techniques:
  - '[[Valid Accounts]]'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: a5eebc54-4808-4db9-8d9c-9d541d23903c
created_at: '2025-12-14T17:29:20.191Z'
updated_at: '2025-12-14T17:29:20.191Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Organization-Domain-as-Admin

## Summary

This procedure sets up an organization domain in Shopify Plus security settings, necessary for testing SAML enforcement via GraphQL.

## Description

As part of the attack setup, an admin adds a domain to the organization's SAML configuration. This domain will later be queried and enforced by a low-priv user. The target environment is the Shopify Plus admin dashboard, requiring admin privileges.

## Requirements

1. Admin access to Shopify Plus organization
2. Valid domain name for SAML (e.g., example.com)
3. Browser for dashboard navigation

## Defense

Defensive measures and detection strategies:

- Restrict domain additions to verified admins only
- Audit logs for domain changes and alert on unusual additions
- Integrate with identity providers for domain validation

## Objectives

1. Prepare a target domain for unauthorized enforcement
2. Enable GraphQL queries to retrieve domain IDs
3. Simulate setup for auth configuration tampering

## Instructions

### Step 1: Access Security Settings

**Context**: Navigate to the user security page to add domains.

**Command** (Browser Navigation):

Visit https://shopify.plus/:id/users/security as admin.

> Locate the domain addition section and enter a new domain. Expected output: Domain saved and listed in organization settings.

### Step 2: Confirm Domain Addition

**Context**: Verify the domain is active for API queries.

**Command** (Manual Check):

Refresh the security page to see the added domain.

> Expected output: Domain appears with an associated ID (visible via later queries).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[domain-creation]]
- [[saml]]
