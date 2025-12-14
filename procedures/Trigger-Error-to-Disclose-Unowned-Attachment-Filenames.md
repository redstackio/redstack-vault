---
id: proc-uuid-placeholder
tags:
  - information-disclosure
  - filename-leak
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:25:12.567Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
---

# Trigger-Error-to-Disclose-Unowned-Attachment-Filenames

## Summary

This procedure exploits an information disclosure vulnerability in Mavenlink's mobile site (m.mavenlink.com) by attempting to delete attachments on expenses that are not owned by the authenticated user, triggering an error message that reveals the filenames of those unowned attachments. This allows unauthorized discovery of file information, classified as medium severity due to potential privacy implications.

## Description

In the context of Mavenlink's expense management feature, users can attach files to expenses. The deletion functionality on the mobile site lacks proper access controls in error handling, exposing filenames when a non-owner attempts deletion. This occurs because the backend processes the delete request and includes the target filename in the error response without sanitizing for unauthorized users. Prerequisites include a valid authenticated session with access to view expenses containing attachments. Expected outcomes include obtaining filenames that could reveal sensitive document names, aiding further reconnaissance or social engineering.

## Requirements

1. Valid authenticated user account on Mavenlink with permissions to view expenses
2. Access to the mobile site m.mavenlink.com via a web browser
3. An expense record containing attachments owned by another user
4. Network connectivity to the target site

## Defense

Defensive measures and detection strategies:

- Sanitize error messages to avoid including sensitive data like filenames
- Implement strict access controls on attachment deletion endpoints to prevent non-owners from triggering errors
- Log and monitor delete attempts on attachments, alerting on failures from unauthorized users
- Use web application firewalls (WAF) to detect anomalous error patterns

## Objectives

1. Disclose filenames of unowned attachments without direct access
2. Gather information for potential further exploitation or reconnaissance
3. Demonstrate the impact of improper error handling in web applications

## Instructions

### Step 1: Authenticate and Navigate to Expenses

**Context**: Log in to the mobile site and locate an expense with attachments to target for deletion attempt.

Access m.mavenlink.com in a mobile browser, log in with your credentials, and navigate to the expenses section. Select an expense that includes attachments, ensuring at least one is not owned by your account (e.g., from a shared workspace or another user's submission).

> Successful login and navigation will display the expense details with attachment options.

### Step 2: Attempt Deletion of Unowned Attachment

**Context**: Initiate the delete action on a non-owned attachment to trigger the vulnerable error response.

Click the delete option for the target unowned attachment. The request will fail due to ownership mismatch, and the error message will populate with the filename.

> The error dialog or page will show a message embedding the filename, such as "Unable to delete [filename.ext] - insufficient permissions."

### Step 3: Capture and Analyze Disclosure

**Context**: Record the revealed filename for verification of the disclosure.

Inspect the error message, extract the filename, and note any additional details. Repeat with multiple attachments to gather more information if needed.

> Expected output includes the exact filename, confirming unauthorized access to file metadata.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[information-disclosure]]
- [[filename-leak]]
- [[web-vulnerability]]
