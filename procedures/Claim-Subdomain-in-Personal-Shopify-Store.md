---
tags:
  - subdomain-takeover
  - shopify
  - account-compromise
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
updated_at: '2025-12-14T04:51:10.847Z'
sub_techniques: []
id: 4eabeb6e-173b-474f-8f4c-92fde85365c2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Subdomain-in-Personal-Shopify-Store

## Summary

This procedure exploits an unclaimed Shopify DNS record by adding the target subdomain to a personal Shopify store, effectively taking control and redirecting traffic to the attacker's content.

## Description

Once a dangling DNS record is identified, Shopify allows any user with an account to claim unassociated domains pointing to their infrastructure. This involves logging into a personal Shopify admin, adding the subdomain as a custom domain, and leveraging the existing DNS to bypass ownership verification. The attack scenario targets abandoned subdomains, with prerequisites including a valid Shopify account. Expected outcomes: Full control over the subdomain for hosting arbitrary content under the trusted parent domain.

## Requirements

1. Active personal Shopify store account
2. Identified unclaimed subdomain from prior reconnaissance
3. Internet access to Shopify admin panel

## Defense

Defensive measures and detection strategies:

- Monitor third-party service dashboards for unauthorized domain claims
- Use DNS security extensions (DNSSEC) to prevent unauthorized takeovers
- Conduct periodic subdomain audits to reclaim or remove dangling records

## Objectives

1. Associate the target subdomain with personal store
2. Gain control without altering target's DNS
3. Enable hosting of attacker-controlled content

## Instructions

### Step 1: Access Shopify Admin

**Context**: Log in to prepare for domain addition.

**Instructions**: Navigate to your Shopify store admin at admin.shopify.com and go to Settings > Domains.

> Expected: Dashboard loads with option to add custom domain.

### Step 2: Add Custom Domain

**Context**: Input the target subdomain to claim it.

**Instructions**: Click 'Connect existing domain', enter 'blog.exchangemarketplace.com', and follow prompts. Shopify will verify via the existing DNS record.

> Successful output: Domain added and status changes to 'Connected' after propagation.

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
