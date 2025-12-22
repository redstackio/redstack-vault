---
tags:
  - cache-poisoning
  - path-traversal
  - url-manipulation
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
updated_at: '2025-12-14T17:28:36.381Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 8877ddb1-a5b6-4b70-a248-edb2f8ac4642
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Poison-Cache-with-Path-Traversal-URL

## Summary

This procedure crafts and submits a path traversal URL in the attacker's Shopify Linkpop account to poison the cache for a victim's Amazon product ID, overwriting it with attacker-controlled data.

## Description

Exploiting the vulnerability in Linkpop's URL parsing for amazon.ca/dp/ paths, which fails to sanitize ../ sequences, this procedure allows cache entries to be manipulated. By adding a URL like `https://amazon.ca/dp/[VICTIM-ID]/../[ATTACKER-ID]`, the cache for the victim's ID is poisoned to serve the attacker's product details, such as images and affiliate links. This occurs because the backend normalizes the path incorrectly, storing the final ID in the cache key.

## Requirements

1. Attacker's Linkpop account credentials
2. Uncached victim and attacker Amazon product IDs from prior procedure
3. Web browser for account interaction

## Defense

Defensive measures and detection strategies:

- Sanitize URL paths with strict regex to block ../ traversal (e.g., reject any /../ in dp/ segments)
- Use unique cache keys incorporating full normalized paths, not just final IDs
- Log and alert on unusual URL patterns in affiliate additions

## Objectives

1. Submit manipulated URL to poison specific cache entry
2. Confirm poisoning by verifying displayed product matches attacker's
3. Set up for victim-side trigger

## Instructions

### Step 1: Craft Malicious URL

**Context**: Combine IDs into traversal format to target victim's cache.

Construct: `https://amazon.ca/dp/[VICTIM-ID]/../[ATTACKER-ID]`, e.g., `https://amazon.ca/dp/B0BXXXXXXX/../B0CYYYYYYY`.

**Expected Output**: Valid URL ready for submission.

### Step 2: Add to Attacker Account

**Context**: Integrate the URL into Linkpop to trigger cache write.

Log in, go to 'Add Product', paste URL, and submit.

**Expected Output**: Product added successfully; inspect to see attacker's details cached under victim's ID.

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
- [[path-traversal]]
