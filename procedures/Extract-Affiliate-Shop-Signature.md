---
id: proc-shopify-extract-signature-001
tags:
  - shopify
  - signature-extraction
  - web-inspection
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
updated_at: '2025-12-14T17:30:07.064Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Affiliate-Shop-Signature

## Summary

This procedure logs in as a staff member with 'Manage Shops' permission and extracts the persistent extra[affiliate_shop] signature from the development stores creation page source.

## Description

The signature is embedded in the HTML of the new development store page and is shared across all staff without expiration. It ties store creation to the organization. This extraction occurs during an authorized session and can be reused later. Target: https://partners.shopify.com/[org_id]/development_stores/new.

## Requirements

1. Staff account with 'Manage Shops' permission
2. Browser with developer tools
3. Organization ID (e.g., 641767)

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove signatures from client-side code
- Implement session-bound tokens that expire with access revocation
- Log access to development store pages

## Objectives

1. Access the signature-exposed page
2. Inspect and copy the extra[affiliate_shop] value
3. Store the signature for reuse

## Instructions

### Step 1: Log In as Staff Member

**Context**: Use the staff credentials to gain authorized access.

Log in to https://partners.shopify.com with staff email and password.

### Step 2: Navigate to Development Stores Creation

**Context**: Reach the page where the signature is loaded in the DOM.

Go to https://partners.shopify.com/[org_id]/development_stores/new.

### Step 3: Inspect Page Source

**Context**: Locate the hidden input or parameter containing the signature.

Right-click and select 'View Page Source' or use DevTools (F12) to search for 'extra[affiliate_shop]'.

**Expected Output**: Value like a long token string (e.g., 'eyJhbGciOiJIUzI1NiJ9...').

Copy the value.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- signature-extraction
