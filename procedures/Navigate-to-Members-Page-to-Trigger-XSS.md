---
id: 123e4567-e89b-12d3-a456-426614174004
name: Navigate-to-Members-Page-to-Trigger-XSS
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.692Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - trigger
  - web
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Navigate-to-Members-Page-to-Trigger-XSS

## Summary

This procedure navigates back to the members page or a related feature to render the stored XSS payload, causing JavaScript execution in the browser.

## Description

After injection, the payload remains dormant until the affected data is retrieved and rendered. Navigating to https://sandbox.veris.in/portal/members/ or features like group member addition causes the backend to fetch and display the unsanitized Name/Description, triggering the onload event. This executes in the context of the authenticated user, allowing access to DOM, cookies, and local storage.

## Requirements

1. Successfully injected and stored payload
2. Active session to load protected pages
3. Browser with JavaScript execution enabled

## Defense

Defensive measures and detection strategies:

- Output encode all stored data before rendering (e.g., HTML entity encoding)
- Use strict CSP headers to block unsafe inline scripts
- Audit page loads for execution of unexpected scripts via browser monitoring

## Objectives

1. Retrieve and render the stored malicious content
2. Execute the JavaScript payload in the page context
3. Demonstrate impact through visible effects like alerts

## Instructions

### Step 1: Return to Members List

**Context**: Load the page that displays member data.

Navigate to https://sandbox.veris.in/portal/members/ by clicking the members link or refreshing the page.

> The page should load, fetching and rendering all members including the injected one.

### Step 2: Access Related Feature if Needed

**Context**: If no immediate trigger, use a secondary view.

Go to the groups section and attempt to add a member from the Member Book.

> This action queries and renders member data, potentially triggering the payload.

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
- [[trigger]]
- [[web]]
