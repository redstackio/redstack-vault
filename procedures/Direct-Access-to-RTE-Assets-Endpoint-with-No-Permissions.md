---
id: proc-shopify-rte-endpoint-no-perm-001
tags:
  - broken-access-control
  - rte-endpoint
  - shopify
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:58.865Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Direct-Access-to-RTE-Assets-Endpoint-with-No-Permissions

## Summary

This procedure exploits the lack of authentication checks on the /admin/rte/assets endpoint in Shopify, allowing staff with no permissions to list and download all admin-uploaded files directly.

## Description

The /admin/rte/assets endpoint serves a JSON or HTML listing of all RTE-uploaded assets without validating user permissions beyond basic login. Even zero-permission staff can access it via direct URL navigation, retrieving download links to CDN-hosted files. This severe broken access control was remediated by adding permission gates.

## Requirements

1. Any valid Shopify staff login (even no permissions assigned)
2. Web browser
3. Admin-uploaded files present

## Defense

Defensive measures and detection strategies:

- Add explicit permission checks to all admin endpoints, including RTE assets
- Implement rate limiting and logging on sensitive endpoints
- Use session-based RBAC enforcement for asset retrieval

## Objectives

1. Bypass all permission requirements for file listing
2. Retrieve direct download links to sensitive files
3. Achieve full unauthorized data access

## Instructions

### Step 1: Log In with No Permissions

**Context**: Use the most restricted account to test endpoint security.

Log in to https://*.myshopify.com/admin with a no-permissions staff account.

**Expected Output**: Successful login to dashboard, but no section access.

### Step 2: Navigate to Endpoint

**Context**: Directly request the vulnerable endpoint.

Enter https://*.myshopify.com/admin/rte/assets in the browser address bar and load the page.

**Expected Output**: Page loads showing a list of all uploaded files.

### Step 3: Download Files

**Context**: Extract and save sensitive assets.

Click on file links to download from the CDN.

**Expected Output**: Files download without errors, exposing admin content.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- endpoint-access
- no-permissions
- shopify
