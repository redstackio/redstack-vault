---
id: proc-shopify-verify-store-001
tags:
  - shopify
  - verification
  - dashboard
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
updated_at: '2025-12-14T17:29:57.383Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Unauthorized-Store-in-Organization-Dashboard

## Summary

This procedure checks the organization's development stores list in the Shopify Partners dashboard to confirm the unauthorized store creation.

## Description

After the bypass, the new store appears linked to the organization ID, demonstrating the vulnerability's impact: unauthorized resources visible to owners, potentially leading to abuse or exposure.

## Requirements

1. Owner credentials
2. Organization ID
3. Recent store creation via bypass

## Defense

Defensive measures and detection strategies:

- Alert on new stores created outside authorized sessions
- Review dashboard access logs for anomalies
- Implement ownership verification for created resources

## Objectives

1. Access development stores list
2. Identify the new unauthorized store
3. Confirm association with organization

## Instructions

### Step 1: Log In as Owner

**Context**: Use owner access to view dashboard.

Log in to https://partners.shopify.com.

### Step 2: Navigate to Development Stores

**Context**: Reach the list of organization stores.

Go to https://partners.shopify.com/[org_id]/development_stores.

### Step 3: Check for New Store

**Context**: Look for the created store by name or timestamp.

Scan the list for 'testdevstore' or recent additions.

**Expected Output**: New store entry with details like name and creation date.

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
- verification
