---
tags:
  - store-creation
  - development
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
updated_at: '2025-12-14T17:29:44.879Z'
sub_techniques: []
id: da9721ec-144f-4ca8-be77-1782c1a2908b
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Create-Development-Store

## Summary

This procedure creates a new development store in the Shopify Partner dashboard, generating a predictable ID for IDOR exploitation.

## Description

Development stores are used for app testing and are assigned incremental IDs, making them vulnerable to enumeration. This step prepares the target object for unauthorized access testing in the IDOR scenario.

## Requirements

1. Logged in as partner admin
2. Associated business entity
3. Dashboard access

## Defense

Defensive measures and detection strategies:

- Use non-predictable IDs (UUIDs) for resources
- Rate limit store creation

## Objectives

1. Generate test store with ID
2. Associate with business
3. Enable transfer testing

## Instructions

### Step 1: Access Store Creation

**Context**: Initiate store setup.

In the partner dashboard, select 'Stores' and click 'Create development store'.

> Form appears for store details.

### Step 2: Configure and Create

**Context**: Finalize under the business.

Enter store name and save; note the generated store ID.

> Store listed with URL like https://partners.shopify.com/[business_id]/stores/[store_id].

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[store-creation]]
- [[development]]
- [[shopify]]
