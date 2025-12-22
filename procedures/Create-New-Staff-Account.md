---
tags:
  - shopify
  - staff-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:39.253Z'
sub_techniques: []
id: df973e32-29c7-4e77-b6b3-f8a492346f42
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-New-Staff-Account

## Summary

This procedure details initiating the creation of a new staff account in Shopify's admin, exposing vulnerable input fields for first and last names that lack proper sanitization.

## Description

Within the Shopify admin settings, users can add staff members by filling out a form with details like names and permissions. This step targets the form initiation, where subsequent payload injection can occur. The process assumes authenticated access and results in a savable form state, enabling persistence of malicious inputs.

## Requirements

1. Access to the admin settings account page from prior step
2. Permissions to add staff members
3. Standard web browser for form interaction

## Defense

Defensive measures and detection strategies:

- Enforce input validation on form submission
- Log and alert on rapid or anomalous staff account creations

## Objectives

1. Open the new staff form
2. Prepare fields for payload entry
3. Ensure form submission is possible without errors

## Instructions

### Step 1: Locate Add Staff Option

**Context**: Identify the interface element to start account creation.

On the account settings page, find and click the 'Add staff' or 'Invite staff' button.

**Expected Output**: Modal or new page with form fields loads.

### Step 2: Prepare Form Fields

**Context**: Review fields to confirm name inputs are present and editable.

Verify first name, last name, email, and permission fields are available.

**Expected Output**: Empty form ready for data entry.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[staff-creation]]
