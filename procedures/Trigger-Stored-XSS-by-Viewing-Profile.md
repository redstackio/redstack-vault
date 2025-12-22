---
tags:
  - xss
  - execution
  - trigger
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0b143028-8919-4300-8ecd-9028bf85c483
created_at: '2025-12-14T03:16:37.334Z'
updated_at: '2025-12-14T03:16:37.334Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Viewing-Profile

## Summary

This procedure triggers the stored XSS payload by rendering the affected user profile in a browser, executing the injected JavaScript when interacting with the malicious element.

## Description

After injection, the payload in Address.FirstName is rendered unsanitized in the HTML of /account/profile, allowing breakout from attributes. Viewing the page loads the payload, and hovering (onmouseover) executes JS in the current context. This affects any viewer, including admins, leading to risks like keylogging or phishing via modified payloads.

## Requirements

1. Access to the affected Starbucks account or admin privileges to view profiles
2. Modern web browser to render and interact with the page
3. Valid session for authentication

## Defense

Defensive measures and detection strategies:

- Apply strict output encoding for user data in HTML contexts
- Implement role-based access controls for profile views
- Log and alert on JS errors or unusual DOM manipulations in profiles
- Use browser sandboxing or extensions to detect XSS

## Objectives

1. Render the stored payload to initiate execution
2. Demonstrate impact through JS alerts or actions
3. Highlight risks for support/admin access

## Instructions

### Step 1: Navigate to Profile

**Context**: Log in and access the profile page to load the address book, where the payload is rendered.

No command; use browser: Visit https://www.starbucks.com/account/profile while authenticated.

> Expected: Page loads with addresses displayed; inspect HTML to confirm payload in FirstName element.

### Step 2: Interact to Trigger

**Context**: Hover over the injected element (large fixed div from payload) to fire the onmouseover event.

No command; browser interaction: Move mouse over the anomalous large element on the page.

> Expected: Alert('Hackerone') pops up, confirming execution. Modify payload for real attacks like document.cookie theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[trigger]]
- [[web]]
