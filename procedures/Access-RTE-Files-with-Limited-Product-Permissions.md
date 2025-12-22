---
id: proc-shopify-rte-limited-001
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
updated_at: '2025-12-14T17:28:58.881Z'
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
# Access-RTE-Files-with-Limited-Product-Permissions

## Summary

This procedure tests and exploits missing permission checks in Shopify's rich text editor (RTE) to allow staff with only 'Products, Inventory, & Collections' permissions to view and download admin-uploaded files, demonstrating a privilege escalation vulnerability.

## Description

In Shopify's admin panel, the RTE used for product descriptions fetches uploaded assets without verifying the user's full permission set. An attacker with limited product access can navigate to a product description, open the image insertion tool, and access all admin-uploaded images. This bypasses restrictions on the Settings > Files section, potentially exposing sensitive files hosted on the CDN. The vulnerability was fixed by restricting RTE access to specific permission sets.

## Requirements

1. Valid Shopify staff account with only 'Products, Inventory, & Collections' permissions
2. Web browser with access to the Shopify admin panel
3. Existence of admin-uploaded files via RTE (e.g., product images)

## Defense

Defensive measures and detection strategies:

- Implement granular permission checks for all RTE endpoints and asset listings
- Log access to RTE assets and monitor for anomalous low-privilege requests
- Restrict RTE functionality to users with explicit file management permissions

## Objectives

1. Gain unauthorized access to admin-uploaded files using limited permissions
2. Download potentially sensitive images or documents
3. Escalate privileges to view files beyond assigned role

## Instructions

### Step 1: Log In and Navigate to Product Description

**Context**: Authenticate with the limited permissions account and reach the RTE interface.

Log in to https://*.myshopify.com/admin using the staff credentials. Go to Products > Select any product > Click into the Description field to open the RTE.

**Expected Output**: RTE editor loads without errors.

### Step 2: Access Uploaded Images Section

**Context**: Trigger the asset listing to reveal admin files.

In the RTE, click the 'Add Image' or media insertion button. Examine the 'Uploaded images' section.

**Expected Output**: List of all admin-uploaded images appears, including those not uploaded by the current user.

### Step 3: View and Download Files

**Context**: Confirm unauthorized access by interacting with files.

Select an admin-uploaded image and attempt to add it to the description or download it directly.

**Expected Output**: File previews load, and download links (to cdn.shopify.com) function, allowing retrieval.

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
- privilege-escalation
- shopify
