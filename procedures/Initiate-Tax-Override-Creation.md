---
tags:
  - shopify
  - tax-override
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:44.290Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
id: 702c2f6c-6a29-4270-9fac-fce9e22734d7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate-Tax-Override-Creation

## Summary

This procedure starts the tax override creation process in Shopify's admin, selecting a local collection to populate the form, which exposes manipulable HTML elements for the bypass.

## Description

Within the taxes settings page, clicking 'Add a tax override' triggers a form for specifying collections and tax rates. Selecting one of the user's own collections populates hidden fields like tax_override[collection_id]. This step is prerequisite for ID manipulation and assumes the page is already loaded. The technical approach relies on Shopify's form-based UI built on Ruby on Rails, where no server-side validation occurs at this stage. Expected outcome is a ready-to-modify form.

## Requirements

1. Access to taxes settings page
2. At least one owned collection in the shop
3. Standard web browser

## Defense

Defensive measures and detection strategies:

- Validate form inputs client-side before submission
- Log all tax override creation attempts with collection IDs

## Objectives

1. Populate the tax override form
2. Expose the collection_id field for modification
3. Set up for authorization bypass

## Instructions

### Step 1: Click Add Override

**Context**: Initiate the form to begin override setup.

Locate and click the 'Add a tax override' button on the taxes page.

### Step 2: Select Collection

**Context**: Choose a local collection to fill form fields.

From the dropdown or selector, pick one of your shop's collections.

> The form now includes hidden inputs like <input type="hidden" name="tax_override[collection_id]" value="local_id">, ready for inspection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- tax-override
