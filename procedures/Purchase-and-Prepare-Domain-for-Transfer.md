---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - shopify
  - domain-setup
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
updated_at: '2025-12-14T17:27:42.900Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Purchase-and-Prepare-Domain-for-Transfer

## Summary

This procedure involves purchasing a domain through Shopify's system and configuring it with DNS records, email forwarders, and subdomains to prepare for a malicious inter-store transfer via CSRF.

## Description

In the context of exploiting Shopify's domain transfer CSRF vulnerability, the attacker first acquires a domain that can be transferred between stores. This setup allows the transfer to copy all configurations to the victim's store, enabling control over email, DNS, and potential escalation to steal store data and payments. Prerequisites include an active Shopify account with purchasing capabilities.

## Requirements

1. Valid Shopify account with admin access
2. Sufficient funds/credits for domain purchase
3. Knowledge of DNS configuration (MX, A, NS records)

## Defense

Defensive measures and detection strategies:

- Monitor domain purchases and transfers in Shopify audit logs
- Implement rate limiting on transfer initiations
- Educate users on verifying transfer emails

## Objectives

1. Acquire a transferable domain
2. Configure malicious DNS and email setups
3. Prepare for CSRF exploitation

## Instructions

### Step 1: Purchase Domain

**Context**: Log into Shopify and buy a domain to enable inter-store transfer.

No specific command; perform via web interface:

Navigate to Shopify admin > Settings > Domains > Buy new domain, select and purchase (e.g., example.com).

> Expected: Domain added to your store, transfer feature enabled.

### Step 2: Configure DNS Records

**Context**: Set up records to hijack victim's infrastructure post-transfer.

Via Shopify admin > Settings > Domains > DNS settings:

- Add MX records for email control
- Set A/NS records pointing to attacker infrastructure
- Configure email forwarders and custom subdomains

> Expected: All configurations saved and visible in admin panel.

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
- [[domain-transfer]]
