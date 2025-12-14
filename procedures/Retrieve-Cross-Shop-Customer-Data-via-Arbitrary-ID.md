---
tags:
  - idor
  - data-disclosure
  - privacy-breach
  - shopify
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.620Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: ae98ccc8-d5ae-4900-acf2-501bf353f747
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve-Cross-Shop-Customer-Data-via-Arbitrary-ID

## Summary

This procedure exploits the lack of authorization checks in Shopify's customer search to query arbitrary user IDs and retrieve first and last names from customers across all shops, enabling mass unauthorized data collection.

## Description

Shopify's customer search feature, intended for merchants to find their own customers by ID, does not validate that the queried ID belongs to the authenticated shop. By inputting any valid customer ID, an attacker with merchant access can view personal details from unrelated shops, affecting privacy for millions. This is a classic insecure direct object reference (IDOR) combined with improper authentication, requiring only a browser and known or guessed IDs. Outcomes include bulk data exfiltration, potentially leading to further attacks like phishing or identity theft.

## Requirements

1. Active session in Shopify merchant dashboard with access to customer search
2. Arbitrary customer user IDs (can be sequential integers starting from 1 or sourced externally)
3. Web browser for manual queries; scripting possible for automation but not required here

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization to restrict search results to the authenticated shop's customers only
- Log and alert on search queries for non-existent or out-of-scope IDs in a merchant's context
- Use data masking or anonymization for search previews to limit exposure

## Objectives

1. Bypass shop isolation to access unauthorized customer records
2. Collect first and last names for privacy violation
3. Demonstrate scalability for affecting large user bases

## Instructions

### Step 1: Input Arbitrary User ID into Search

**Context**: Use the search field to submit a query without shop-specific restrictions, triggering the vulnerability.

In the customer search bar, enter an arbitrary user ID (e.g., "123456" for a test customer). Select the "Search by ID" option if available and submit.

> The system processes the query without checking shop ownership, returning results if the ID exists anywhere on the platform.

### Step 2: Observe and Collect Results

**Context**: Review the output to confirm cross-shop access and extract personal information.

Examine the search results for first and last names. Repeat with multiple IDs to gather data from various shops, noting any lack of error messages for foreign IDs.

> Results display names from unrelated shops, validating the improper authentication flaw.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[data-disclosure]]
- [[privacy-breach]]
- [[shopify]]
