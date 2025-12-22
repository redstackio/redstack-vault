---
tags:
  - cache-poisoning
  - spoofing
  - affiliate-hijack
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.369Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 5cd7d695-abfd-4c02-81ee-90fb5c7b5f74
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Poisoned-Cache-in-Victim-Account

## Summary

This procedure simulates or induces the victim to add their legitimate Amazon product to Linkpop, retrieving the poisoned cache and displaying the attacker's product, leading to spoofed promotion.

## Description

After cache poisoning, when the victim adds their product URL `https://www.amazon.ca/dp/[VICTIM-ID]`, Linkpop's backend fetches the manipulated cache entry, serving the attacker's product data (e.g., ID B0CYYYYYYY instead of B0BXXXXXXX). This results in the victim's account showing attacker-controlled images, descriptions, and affiliate links, tricking visitors into promoting the attacker's products and potentially earning commissions fraudulently.

## Requirements

1. Victim's Linkpop account access (or social engineering to induce addition)
2. Poisoned cache from prior procedure
3. Legitimate victim product URL

## Defense

Defensive measures and detection strategies:

- Implement cache invalidation on new additions or periodic refreshes from source
- Cross-verify product data against Amazon API on display
- User notifications for mismatched product details post-addition

## Objectives

1. Retrieve and display poisoned cache in victim's interface
2. Achieve spoofing of affiliate products
3. Realize impact through unintended promotions

## Instructions

### Step 1: Prepare Victim URL

**Context**: Use the clean, legitimate URL for the victim's product.

Format: `https://www.amazon.ca/dp/[VICTIM-ID]`, e.g., `https://www.amazon.ca/dp/B0BXXXXXXX`.

**Expected Output**: Standard Amazon product link.

### Step 2: Add to Victim Account

**Context**: Submit the URL to trigger cache hit.

Log in to victim's account, add product via the URL, and observe the result.

**Expected Output**: Interface shows attacker's product details; links redirect to attacker's affiliate page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cache-poisoning]]
- [[spoofing]]
