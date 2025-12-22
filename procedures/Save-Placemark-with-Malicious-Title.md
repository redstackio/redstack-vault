---
tags:
  - xss
  - data-storage
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.198Z'
sub_techniques: []
id: 08f480bf-69a3-43bc-80cf-6452edfe9621
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Placemark-with-Malicious-Title

## Summary

This procedure covers submitting the placemark form to store the injected JavaScript payload in the WordPress database, persisting the vulnerability for later execution.

## Description

After injecting the payload, submitting the form via the plugin's save mechanism stores the title without server-side sanitization. The data is saved to the WordPress posts or custom tables used by the plugin. This step confirms the 'stored' aspect of the XSS. No errors should occur if other fields are minimally completed (e.g., map coordinates). Expected outcome: payload retrievable from the admin list.

## Requirements

1. Payload entered in title field
2. Required fields (e.g., latitude/longitude) populated
3. Active WordPress session

## Defense

Defensive measures and detection strategies:

- Server-side input sanitization using wp_kses() or similar
- Database auditing for script tags in titles
- Rate limiting on placemark saves

## Objectives

1. Persist the malicious title in storage
2. Verify save without rejection
3. Enable front-end triggering

## Instructions

### Step 1: Complete Form

**Context**: Ensure all mandatory fields are filled to allow submission.

Enter basic details like placemark location coordinates if required.

> Form validation passes for non-title fields.

### Step 2: Submit Form

**Context**: Store the payload by saving.

Click the 'Save' or 'Publish' button.

> Success message appears; placemark added to list.

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
- [[data-storage]]
