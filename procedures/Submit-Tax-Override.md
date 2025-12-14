---
tags:
  - shopify
  - tax-override
  - data-exposure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:36.749Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
id: cfc5dba4-4442-4184-9a66-7a49c4f424d1
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Submit-Tax-Override

## Summary

This procedure submits the modified tax override form, resulting in the addition of an unauthorized entry and exposure of foreign collection names in the admin table.

## Description

After modifying the collection_id, submitting the form sends a POST to /admin/settings/taxes/*/override without validating ownership. Shopify's backend processes it, adding the override and populating the 'Tax overrides' table with the foreign collection's name—even if hidden. This demonstrates the full impact of the bypass in a web SaaS environment. Prerequisites: Modified form ready. Expected outcome: Visible unauthorized data in the UI.

## Requirements

1. Modified tax override form with foreign collection_id
2. Active admin session
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Enforce ShopID matching in backend models (e.g., Rails associations)
- Rate-limit override creations and alert on anomalies
- Sanitize and log all submitted collection_ids

## Objectives

1. Persist the unauthorized override
2. Exfiltrate collection names via UI display
3. Confirm bypass success

## Instructions

### Step 1: Review Form

**Context**: Ensure modifications are in place before submission.

Verify the hidden field value in DevTools remains altered.

### Step 2: Submit Form

**Context**: Trigger the POST request to exploit the vulnerability.

Click the 'Save' or 'Add tax override' button.

> The page refreshes, adding the entry to the table. The foreign collection name (e.g., from shop with ID 137861635) now appears, proving unauthorized access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- tax-override
- data-exposure
