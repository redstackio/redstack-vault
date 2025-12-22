---
id: proc-shopify-rte-settings-bypass-001
tags:
  - broken-access-control
  - rte
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
updated_at: '2025-12-14T17:28:58.868Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Verify-File-Access-Without-Settings-Permissions

## Summary

This procedure verifies that Shopify staff lacking 'Settings' permissions cannot access files directly but can still view and download them via the RTE in product descriptions, highlighting inconsistent permission enforcement.

## Description

Shopify's file management is centralized in Settings > Files, which requires specific permissions. However, the RTE asset listing in product editing pulls from the same backend without checks, allowing indirect access. This leads to unauthorized exposure of files on the public CDN, fixed post-discovery by aligning permissions across interfaces.

## Requirements

1. Staff account without 'Settings' access but with product editing permissions
2. Web browser access to admin panel
3. Pre-existing admin-uploaded files

## Defense

Defensive measures and detection strategies:

- Enforce uniform permission checks across all file access paths (direct and indirect)
- Audit logs for RTE usage by low-privilege users
- Use role-based access control (RBAC) to gate media asset endpoints

## Objectives

1. Confirm denial of direct file access
2. Demonstrate bypass via RTE for unauthorized viewing
3. Expose potential sensitive data leakage

## Instructions

### Step 1: Attempt Direct Settings Access

**Context**: Test expected permission denial.

Navigate to Settings > Files in the admin panel.

**Expected Output**: Access denied error or blank page due to missing permissions.

### Step 2: Access RTE in Product Description

**Context**: Use indirect path to access the same files.

Go to Products > Select product > Description > Click 'Add Image' in RTE.

**Expected Output**: 'Uploaded images' section loads with full file list.

### Step 3: Interact with Files

**Context**: Validate download capability.

Preview or download a file from the list.

**Expected Output**: File downloads successfully via CDN URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- broken-access-control
- file-bypass
- shopify
