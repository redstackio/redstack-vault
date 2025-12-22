---
tags:
  - subdomain-takeover
  - shopify
  - dns
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - DNS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d1da6e60-ab8c-436a-9d1e-afd29f4479e4
created_at: '2025-12-14T04:51:10.897Z'
updated_at: '2025-12-14T04:51:10.897Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim Unclaimed Shopify Subdomain

## Summary

This procedure allows an attacker to claim control of a dangling subdomain by associating it with their own Shopify store through the partner dashboard, exploiting the unclaimed status.

## Description

Once a dangling CNAME is identified, the attacker uses Shopify's domain management features to claim the subdomain. This involves logging into the Partner Dashboard and initiating the domain association process, which succeeds because the record points to an unclaimed resource. Post-claim, DNS propagation updates the resolution to the attacker's store, granting full hosting control. This vulnerability arises from incomplete decommissioning of third-party integrations.

## Requirements

1. Free Shopify Partner account
2. Access to the unclaimed subdomain's DNS record
3. Understanding of Shopify's domain claiming workflow

## Defense

Defensive measures and detection strategies:

- Monitor third-party service APIs for unclaimed domains linked to your subdomains
- Automate DNS cleanup during service decommissioning
- Set up alerts for DNS changes on staging subdomains

## Objectives

1. Gain ownership of the subdomain via Shopify
2. Verify control through DNS resolution
3. Prepare for content hosting

## Instructions

### Step 1: Access Shopify Partner Dashboard

**Context**: Log in to initiate the claiming process.

Create or log into a Shopify Partner account at partners.shopify.com.

> Dashboard access confirmed upon login.

### Step 2: Claim the Domain

**Context**: Associate the dangling subdomain with a store.

Navigate to the Domains section, enter the subdomain (e.g., de-headless.staging.gymshark.com), and follow the claiming prompts to link it to a new or existing store.

> Success is indicated by a confirmation message and the domain appearing as active in your account.

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
- [[DNS]]
