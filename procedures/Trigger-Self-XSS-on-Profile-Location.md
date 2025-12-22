---
id: proc-trigger-profile-xss-001
tags:
  - xss
  - self-xss
  - ui-trigger
type: procedure
tools:
  - '[[tools/Web-Browser-Chrome]]'
  - '[[tools/Chrome-Developer-Tools]]'
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:30.972Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Self-XSS-on-Profile-Location

## Summary

This procedure navigates to Yelp's profile location page with a tampered cookie and interacts with the Address field to trigger a request that reflects the injected 'city' payload, executing JavaScript in the user's browser.

## Description

Upon accessing https://www.yelp.com/profile_location, clicking the Address field sends a GET to https://www.yelp.com/location_suggest/json?prefix=, incorporating the cookie's 'city' value into the JSON response without HTML escaping. When rendered, this executes the payload (e.g., debugger). Limited to self-impact; requires tampered cookie and authentication.

## Requirements

1. Tampered location cookie set
2. Active browser session
3. Developer tools for monitoring

## Defense

Defensive measures and detection strategies:

- Escape HTML entities in JSON responses (e.g., &lt; for <)
- Implement input validation on client-side cookie usage
- Log and alert on script-like content in location fields

## Objectives

1. Reflect payload via API call
2. Execute injected script
3. Confirm self-XSS via debugger pause

## Instructions

### Step 1: Navigate to Page

**Context**: Load the profile location page with the tampered cookie active.

Use [[tools/Web-Browser-Chrome]] to visit https://www.yelp.com/profile_location, ensuring authentication cookies are present.

### Step 2: Interact and Monitor

**Context**: Trigger the reflection by clicking the UI element while observing the network and console.

Open [[tools/Chrome-Developer-Tools]] console, then click the Address field. Monitor the Network tab for the /location_suggest/json request.

**Expected Output**: Response JSON with payload like {"suggestions": [{"name": "\u003cscript\u003edebugger\u003c/script\u003e, CA"}]}, triggering debugger in console.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser-Chrome]]
- [[tools/Chrome-Developer-Tools]]

## Tags

- xss
- self-xss
- ui-trigger
