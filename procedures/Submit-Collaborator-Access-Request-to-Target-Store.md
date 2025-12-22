---
tags:
  - shopify
  - access-request
  - web
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:01.283Z'
sub_techniques: []
id: 51184867-0ebe-4f72-8198-71cb545166f1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
---

# Submit Collaborator Access Request to Target Store

## Summary

This procedure submits a pending collaborator access request to a target Shopify store using a partner account, creating the exploitable pending state.

## Description

From the Shopify Partners dashboard, users can request collaborator access to stores, which normally requires merchant approval. This step leverages the first partner account to initiate such a request, resulting in a pending status that can later be manipulated.

## Requirements

1. Active first partner account with shared email
2. Knowledge of target store name or ID
3. Access to partners.shopify.com dashboard

## Defense

Defensive measures and detection strategies:

- Limit collaborator requests per partner account
- Require additional verification for requests
- Alert merchants on all incoming requests

## Objectives

1. Create a pending collaborator request
2. Associate it with the shared email account
3. Set up for unauthorized activation

## Instructions

### Step 1: Access Partner Dashboard

**Context**: Log in to the first partner account.

Visit https://partners.shopify.com and log in with the first account credentials.

> Expected output: Dashboard loads with access to stores section.

### Step 2: Submit Request

**Context**: Target the store and request access.

Search for the target store in the dashboard, select 'Request Access' as collaborator, specify role (e.g., full permissions), and submit.

> Expected output: Confirmation of pending request; status shows 'Pending Approval'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[access-request]]
