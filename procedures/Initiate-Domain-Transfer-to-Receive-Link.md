---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - shopify
  - transfer-link
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:42.887Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Domain-Transfer-to-Receive-Link

## Summary

Initiate the inter-store domain transfer in Shopify to trigger an email containing the transfer link and code, which will later be modified for CSRF exploitation.

## Description

This step requests a domain transfer to another store (typically the attacker's own), generating a unique transfer_code. The email link normally secures the process but lacks CSRF protection on the endpoint, allowing later abuse. Expected outcome: Receipt of the link for modification.

## Requirements

1. Prepared domain from previous step
2. Access to Shopify email inbox
3. Another Shopify store for transfer target (can be self)

## Defense

Defensive measures and detection strategies:

- Require multi-factor approval for transfers
- Log all transfer initiations with IP tracking
- Scan emails for anomalous links

## Objectives

1. Generate transfer link and code
2. Ensure email delivery
3. Prepare for link tampering

## Instructions

### Step 1: Request Transfer

**Context**: Start the transfer process to obtain the link.

Via Shopify admin > Settings > Domains > Transfer domain to another store, select target store and initiate.

> Expected: Confirmation message, followed by email.

### Step 2: Retrieve Email Link

**Context**: Access the sent email to extract the URL.

Check inbox for email from Shopify with subject like "Domain Transfer Request", copy link e.g., `https://www.shopify.com/login?redirect=settings/domains/initiate_inter_shop_domain_transfer?transfer_code=6fa6d18a-d2d1-4114-b11e-236b20f81398`.

> Expected: Valid link with transfer_code parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[shopify]]
- [[email-phishing]]
