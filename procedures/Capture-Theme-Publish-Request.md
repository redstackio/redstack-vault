---
id: proc-shopify-capture-publish-request
tags:
  - shopify
  - xhr-intercept
  - graphql
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
  - '[[tools/Google-Chrome-Developer-Tools]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.804Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Theme-Publish-Request

## Summary

This procedure intercepts the GraphQL ThemePublishLegacy mutation request during a legitimate theme publish to obtain reusable fetch code for the race condition exploit.

## Description

Using browser developer tools, this step monitors network traffic on the Shopify admin/themes page while publishing a free theme. The ThemePublishLegacy XHR request is copied as JavaScript fetch code, which includes the GraphQL mutation for publishing a theme by ID. This code is stored in the console for later modification with the temporary ID of an installing paid theme, exploiting the lack of validation during installation.

## Requirements

1. Free theme already installed and ready to publish
2. Developer tools open in browser
3. Admin/themes page loaded

## Defense

Defensive measures and detection strategies:

- Log all GraphQL mutations and validate request timing
- Detect repeated fetch executions from console

## Objectives

1. Obtain the exact GraphQL publish mutation structure
2. Capture headers and body for authenticated requests
3. Prepare code for race-timed execution

## Instructions

### Step 1: Open Developer Tools

**Context**: Enable network monitoring on the admin page.

Load https://yourshop.myshopify.com/admin/themes, open Developer Tools (F12), and switch to the Network/XHR tab.

### Step 2: Perform Publish Action

**Context**: Trigger the request to intercept it.

Select the free theme and click "Publish" to initiate the action.

### Step 3: Copy Request as Fetch

**Context**: Extract the request details.

Filter the Network tab for "ThemePublishLegacy", right-click the request, select "Copy > Copy as fetch", and paste into the Console tab for storage.

**Expected Output**: JavaScript fetch code block with POST to GraphQL endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome-Developer-Tools]]

## Tags

- graphql
- request-capture
