---
tags:
  - xss
  - navigation
  - openfolio
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:36.315Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 79d57aa3-b626-41c9-afdb-28de201cfa98
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Navigate-to-Contacts-Page-in-Openfolio

## Summary

This procedure accesses the vulnerable contacts browsing page in Openfolio to display the imported malicious contacts, preparing for payload execution.

## Description

After syncing, the /browse/contacts/ endpoint renders the contact list, including unsanitized names from Google. Navigating here loads the data into the DOM, but execution requires further interaction. This step positions the attack in the victim's session. Prerequisites: Synced contacts. Outcomes: Page loads with vulnerable data exposed.

## Requirements

1. Logged-in Openfolio session
2. Synced malicious contacts
3. Standard web access

## Defense

Defensive measures and detection strategies:

- Escape user-generated content in list views
- Implement client-side validation before rendering
- Monitor page access logs for unusual patterns

## Objectives

1. Load the contact list containing the payload
2. Expose the unsanitized data in the browser
3. Set up for interaction-based trigger

## Instructions

### Step 1: Ensure Logged In

**Context**: Authentication is required to access personal contacts.

If not already, log in to https://openfolio.com.

### Step 2: Access Contacts URL

**Context**: Directly navigate to the browsing endpoint to view synced contacts.

Enter or click to visit https://openfolio.com/browse/contacts/ in the browser.

> This page queries and displays the imported contacts, injecting names into HTML without sanitization.

**Expected Output**: List of contacts loads, including the malicious name.

### Step 3: Inspect List

**Context**: Confirm the payload is visible but not yet executed.

Scroll through the contacts to locate the malicious entry; no execution should occur on load.

**Expected Output**: Payload string displays in the UI.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[navigation]]
- [[openfolio]]
