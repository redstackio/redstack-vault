---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss-trigger
  - search-exploitation
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.652Z'
skill_level: intermediate
impact_level: low
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-via-Search-Results

## Summary

This procedure covers searching for the injected group in Concrete CMS to render the unsanitized Name field, then clicking the result to execute the stored JavaScript payload, confirming the XSS.

## Description

Due to missing output encoding in search results display, the stored payload executes in the browser context of authenticated users (e.g., admins). This targets the User Groups search feature in Concrete CMS 8.2.0 RC2, leading to arbitrary JS like alerts or cookie theft. Scenario assumes prior injection; outcomes include payload execution on interaction.

## Requirements

1. Stored XSS payload from previous injection
2. Authenticated session with view permissions for User Groups
3. Access to the search functionality in the UI

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity encoding) when displaying user-controlled data in search results
- Use strict CSP headers to prevent onclick and other event handlers
- Audit search queries and result clicks for anomalous behavior in application logs

## Objectives

1. Render the vulnerable group name in search results
2. Execute JavaScript via user interaction (click)
3. Demonstrate impact like session data access

## Instructions

### Step 1: Return to User Groups List

**Context**: Prepare to search for the injected group.

Navigate back to Members > User Groups.

> List reloads. Expected output: Search field visible.

### Step 2: Execute Search

**Context**: Trigger rendering of unsanitized data.

Enter 'locals' and press Enter.

> Results populate. Expected output: Group appears in list with payload in name.

### Step 3: Interact with Result

**Context**: Cause execution of the onclick handler.

Click the group link in results.

> JS runs. Expected output: Alert('XSS!') pops up.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
