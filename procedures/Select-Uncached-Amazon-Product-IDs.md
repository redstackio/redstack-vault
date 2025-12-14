---
tags:
  - reconnaissance
  - amazon
  - product-id
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:28:36.385Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3f14c556-77ae-426b-9bda-3f4470d9714e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Select-Uncached-Amazon-Product-IDs

## Summary

This procedure identifies uncached Amazon product IDs for use in cache poisoning attacks, ensuring the manipulation targets fresh cache entries in services like Shopify Linkpop.

## Description

In the context of exploiting cache poisoning vulnerabilities in affiliate link services, selecting uncached product IDs is crucial. Attackers browse Amazon.ca for products without prior integration into the target service. Cache status is verified by timing the addition process in Linkpop: uncached IDs take longer (>1 second) to process. This step sets up the foundation for path traversal-based poisoning, targeting Amazon ASINs like B0BXXXXXXX for victims and B0CYYYYYYY for attackers.

## Requirements

1. Access to Amazon.ca search functionality
2. Linkpop account for verification
3. Basic understanding of Amazon ASIN format (10-character strings starting with B0)

## Defense

Defensive measures and detection strategies:

- Implement cache validation on product ID addition to detect anomalies in processing time
- Monitor for repeated failed or timed additions of the same IDs
- Use rate limiting on affiliate link integrations

## Objectives

1. Gather valid, uncached victim and attacker product IDs
2. Verify cache absence to maximize poisoning success
3. Prepare IDs for URL crafting in subsequent steps

## Instructions

### Step 1: Research Product IDs

**Context**: Browse Amazon.ca to find suitable products for victim and attacker roles.

Search for products and extract ASINs from URLs (e.g., /dp/B0BXXXXXXX).

**Expected Output**: List of candidate ASINs.

### Step 2: Verify Cache Status

**Context**: Test each ID in Linkpop to confirm uncached.

Attempt to add a test URL like `https://amazon.ca/dp/[ID]` and time the response.

**Expected Output**: Addition completes in >1 second for uncached IDs.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[amazon]]
