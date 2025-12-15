---
id: proc-shopify-initiate-purchase
tags:
  - payment-bypass
  - shopify
  - staging-environment
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
updated_at: '2025-12-14T17:30:18.147Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Purchase-of-Paid-Theme-on-Staging

## Summary

This procedure selects and initiates the purchase of a paid theme within the staging environment, exploiting the lack of payment enforcement to trigger a test charge flow.

## Description

After authentication, the staging site allows browsing and 'buying' paid themes without real payment validation, as it uses test mode. This step identifies a paid theme (e.g., one priced at $180) and simulates purchase, leading to a dashboard redirect. The technical flaw is the public accessibility of staging, intended for internal use only. Outcomes include initiation of free installation path.

## Requirements

1. Active session in staging environment
2. Web browser access to theme catalog
3. Knowledge of paid vs. free themes

## Defense

Defensive measures and detection strategies:

- Restrict staging theme store to internal IPs
- Log and audit all theme purchase attempts in staging
- Disable purchase functionality in non-production environments

## Objectives

1. Select a paid theme for exploitation
2. Trigger purchase process without cost
3. Redirect to charge approval

## Instructions

### Step 1: Browse Themes

**Context**: Explore the staging theme store to locate paid content.

Once logged in, navigate through the theme listings on themes.shopify.io.

> Paid themes are marked with prices; free ones are not.

### Step 2: Click Buy Theme

**Context**: Initiate the purchase to exploit the test charge bypass.

Select a paid theme and click the 'buy theme' button.

> This starts the process without prompting for payment details, due to staging configuration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[payment-bypass]]
- [[shopify]]
- [[staging-environment]]
