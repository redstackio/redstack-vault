---
id: ac047b81-32de-405e-b54a-2479e2777a19
name: Claim-Unclaimed-Shopify-Instance
type: procedure
verified: false
submitted: true
created_at: '2025-12-14T04:38:39.742Z'
updated_at: '2025-12-14T04:38:39.742Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - subdomain-takeover
  - shopify
  - account-creation
commands: []
platforms:
  - Web
  - Shopify
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Claim-Unclaimed-Shopify-Instance

## Summary

This procedure exploits the vulnerability by creating a new Shopify account and adding the vulnerable custom domain to claim control over the subdomain.

## Description

Once verified, the attacker registers with Shopify and configures the subdomain as a custom domain, hijacking the DNS-linked instance. This targets web e-commerce integrations. Outcomes: Full control of the subdomain. Prerequisites: Verified unclaimed instance and a valid email for account creation.

## Requirements

1. Free email address for Shopify signup
2. Access to Shopify.com signup process
3. The exact subdomain name from DNS

## Defense

Defensive measures and detection strategies:

- Lock down custom domains in third-party services to prevent claims
- Monitor Shopify or similar service logs for new domain additions
- Use certificate pinning or HSTS to detect subdomain hijacks

## Objectives

1. Create and configure a Shopify account with the subdomain
2. Achieve resolution of the subdomain to the new instance
3. Establish persistence under the organization's domain

## Instructions

### Step 1: Create Shopify Account

**Context**: Sign up for a new store to gain admin access.

Visit shopify.com, click 'Start free trial', and complete registration with basic details (no payment needed for basic claim).

> Expected output: Access to Shopify admin dashboard for a new store.

### Step 2: Add Custom Domain

**Context**: Link the vulnerable subdomain to your store.

In the admin, go to Settings > Domains > Connect existing domain, enter the subdomain (e.g., shop.target.com), and follow prompts (Shopify handles verification via DNS).

> Expected output: Confirmation that the domain is connected; subdomain now points to your store.

### Step 3: Verify Claim

**Context**: Test if the subdomain resolves to your instance.

Visit the subdomain URL; it should load your new Shopify store template.

> Success if no errors and content is under your control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[shopify]]
- [[account-creation]]
