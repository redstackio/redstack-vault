---
tags:
  - idor
  - url-manipulation
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:44.870Z'
sub_techniques: []
id: 128de666-c041-437b-a4b5-2f12d5b7e968
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-Shop-Details-via-Predictable-IDOR-URL

## Summary

This procedure exploits IDOR by directly accessing shop details using predictable incremental IDs in the URL.

## Description

Shopify uses sequential IDs for stores, allowing brute-force or correlation to guess valid paths. With limited permissions, this bypasses checks, revealing unauthorized data.

## Requirements

1. Known business and store IDs
2. Limited user session active
3. Web browser

## Defense

Defensive measures and detection strategies:

- Implement indirect object references (UUIDs)
- Log anomalous URL access patterns

## Objectives

1. Bypass authorization via direct reference
2. Enumerate shop endpoints
3. Gain access to detail page

## Instructions

### Step 1: Identify IDs

**Context**: Gather predictable identifiers.

From prior steps, note business_id and store_id (e.g., incremental like 629528).

> IDs are visible in admin URLs or brute-forced.

### Step 2: Construct and Navigate URL

**Context**: Trigger IDOR access.

Enter https://partners.shopify.com/[business_id]/stores/[store_id] in the browser.

> Page loads without permission denial.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[url-manipulation]]
- [[shopify]]
