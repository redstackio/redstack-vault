---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - csrf
  - url-modification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:42.875Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Transfer-Link-to-Target-Victim

## Summary

Alter the received transfer link to redirect to the victim's Shopify store subdomain, enabling CSRF targeting.

## Description

By changing the redirect parameter in the link, the attacker repurposes the legitimate transfer URL to hit the victim's `/admin/settings/domains/initiate_inter_shop_domain_transfer` endpoint. This exploits the lack of origin checks, allowing cross-site initiation when embedded in HTML.

## Requirements

1. Transfer link from previous step
2. Victim's store subdomain (e.g., victimstore.myshopify.com)
3. Text editor for URL editing

## Defense

Defensive measures and detection strategies:

- Validate redirect origins on server-side
- Use CSRF tokens in all state-changing endpoints
- Monitor for unexpected transfer attempts

## Objectives

1. Target victim's store in URL
2. Preserve transfer_code integrity
3. Prepare for payload embedding

## Instructions

### Step 1: Edit Redirect Parameter

**Context**: Locate and modify the redirect URL in the link.

Open the link in a text editor, find `redirect=settings/domains/...` and change the base domain to victim's, e.g., `https://victimstore.myshopify.com/admin/settings/domains/initiate_inter_shop_domain_transfer?transfer_code=6fa6d18a-d2d1-4114-b11e-236b20f81398`.

> Expected: Updated URL pointing to victimstore.myshopify.com.

### Step 2: Validate Modification

**Context**: Ensure the code remains unchanged.

Compare original and modified links; confirm transfer_code matches.

> Expected: No alterations to sensitive parameters.

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

- [[csrf]]
- [[url-tampering]]
