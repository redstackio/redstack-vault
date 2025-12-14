---
tags:
  - product-setup
  - web-app
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:10.048Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 7074afb0-1dc3-4462-9628-1d3186e0952e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-New-Product

## Summary

This procedure creates a new product within the authenticated web application, which is necessary to access the LRS Configurations feature where the SSRF vulnerability resides.

## Description

Post-authentication, the application allows users to manage products, each serving as a container for configurations like LRS endpoints. By creating a minimal product, attackers position themselves to inject malicious URLs. This step assumes standard web form interactions and targets apps with user-generated content workflows. Success leads to the product page, ready for LRS setup.

## Requirements

1. Active authenticated session
2. Access to https://████/products/create/
3. Basic product details (e.g., name, description)

## Defense

Defensive measures and detection strategies:

- Audit product creation logs for anomalous patterns
- Require approval workflows for new products in sensitive environments
- Monitor for rapid product creation post-registration

## Objectives

1. Unlock LRS Configurations access
2. Prepare environment for SSRF payload injection
3. Maintain legitimate user behavior to avoid detection

## Instructions

### Step 1: Navigate to Product Creation

**Context**: Access the form for adding a new product.

From the dashboard, visit https://████/products/create/.

**Expected Output**: Product creation form loaded.

### Step 2: Submit Product Details

**Context**: Fill and submit the form to instantiate the product.

Enter required fields such as product name and any optional descriptions, then submit.

**Expected Output**: Success message; product listed in user's inventory.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- product-setup
- web-app
