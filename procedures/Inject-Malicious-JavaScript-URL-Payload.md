---
tags:
  - xss
  - stored-xss
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.543Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 3c8c525a-3a03-4db7-9cfe-1005abc43d15
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-JavaScript-URL-Payload

## Summary

This procedure details injecting a javascript: URI payload into the bookmark URL field of the TopCoder wiki, exploiting lack of sanitization to store executable code for later XSS triggering.

## Description

The updatebookmark.action endpoint processes URL inputs without stripping or escaping javascript: schemes, storing them directly in the wiki database. When a victim clicks the bookmark link on a viewing page, the payload executes in their browser context, potentially leading to data theft or session manipulation. This is a classic stored XSS vector in Confluence plugins.

## Requirements

1. Access to the bookmark creation form (from previous procedure)
2. Web browser
3. Target wiki page title for association (e.g., an existing or new page)

## Defense

Defensive measures and detection strategies:

- Sanitize all URL inputs to block javascript: and other dangerous schemes
- Validate and escape stored links before rendering
- Log and alert on anomalous URL submissions

## Objectives

1. Store the malicious payload without rejection
2. Associate it with a visible wiki page
3. Confirm storage for later verification

## Instructions

### Step 1: Fill Form Fields

**Context**: Prepare the bookmark with the payload in the URL field.

In the URL input, enter `javascript:alert(document.domain)`. Set the title to something innocuous like "powerpuff_hackerone_test" and add a description if required.

> Fields are populated; no client-side errors appear.

### Step 2: Submit Bookmark

**Context**: Send the data to the endpoint for storage.

Click the submit button to create the bookmark.

> Submission succeeds, potentially redirecting to the wiki page or showing a success message.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[JavaScript]]
