---
id: proc-003
tags:
  - browser-trigger
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:30:18.428Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Open-Attack-Page-in-Browser

## Summary

Navigate to the attack trigger page in a browser to initiate the postMessage sequence targeting an open admin tab.

## Description

Using Google Chrome, load the '/pages/xss-play' page and activate the attack function, which opens the admin and begins sending traversal payloads. This step bridges storefront and admin contexts.

## Requirements

1. Trigger page created
2. Chrome browser installed
3. Store URL known

## Defense

- Browser extensions to block suspicious window opens
- Admin session isolation from storefront
- Rate limiting on postMessage

## Objectives

1. Launch the exploitation sequence
2. Ensure admin tab is targeted
3. Monitor for trigger success

## Instructions

### Step 1: Navigate to Page

**Context**: Open Chrome and visit the trigger URL.

**Instructions**: Go to https://[STORE].myshopify.com/pages/xss-play.

> Page loads with black button; expected output: No errors.

### Step 2: Activate Attack

**Context**: Click to start postMessage.

**Instructions**: Click 'click me start attack'.

> New tab opens to /admin/themes; console shows intervals. Expected output: postMessage firing every 500ms.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- browser-trigger
