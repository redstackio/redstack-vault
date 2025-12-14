---
tags:
  - shopify-claim
  - account-compromise
  - subdomain-takeover
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T04:38:39.440Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1078.004]]'
id: dc6ac27f-f134-435a-ab0b-c3c3859f65f8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Claim-Unclaimed-Shopify-Store

## Summary

This procedure details the process of claiming ownership of an unclaimed Shopify store associated with a target's misconfigured subdomain, granting control over the DNS-pointed resource.

## Description

Shopify allows creation and claiming of stores via their platform, and unclaimed instances linked to external DNS can be taken over by anyone. The attack leverages the existing DNS configuration to bypass ownership verification. Prerequisites include identifying the vulnerable subdomain. Outcomes: Full admin access to the store, enabling further exploitation like content manipulation.

## Requirements

1. Identified vulnerable subdomain with Shopify DNS pointer
2. Shopify account (free tier sufficient)
3. Basic understanding of Shopify's domain setup process

## Defense

Defensive measures and detection strategies:

- Remove or update dangling DNS records promptly
- Use Shopify's domain protection features
- Monitor Shopify partner logs for unauthorized claims

## Objectives

1. Gain ownership of the unclaimed store
2. Verify control over the subdomain
3. Enable subsequent configuration for malicious use

## Instructions

### Step 1: Access Shopify Claim Process

**Context**: Log into Shopify and initiate store claiming for the unclaimed instance.

Navigate to Shopify's store creation or partner dashboard and search for the unclaimed store using the subdomain details.

> No command; web-based process.

### Step 2: Verify and Claim Domain

**Context**: Use the DNS configuration to claim ownership.

Follow Shopify's prompts to add the subdomain as a custom domain, leveraging the existing CNAME record for verification.

> Expected output: Shopify confirms domain ownership and transfers store control.

### Step 3: Confirm Access

**Context**: Test admin access to the claimed store.

Log into the Shopify admin panel for the new store and check subdomain mapping.

> Expected output: Dashboard access with subdomain listed as primary domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[T1078.004]]

## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[shopify]]
