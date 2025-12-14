---
tags:
  - idor
  - discovery
  - browser
  - network-inspection
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:34.372Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 42756708-e616-442a-abba-e8aa7c292e43
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-IDOR-Endpoint-via-Browser-Inspection

## Summary

This procedure involves inspecting network traffic in a web browser while interacting with the Semrush marketing calendar tool to identify the vulnerable API endpoint that exposes user status without proper access controls.

## Description

In the context of testing the Semrush platform, load a marketing calendar in the browser and monitor network requests using developer tools. This reveals the /api/v1/ga/user_status/ endpoint, which accepts a calendar_id parameter and returns the owner's user_id and Google Analytics connection status without verifying if the requester owns or is invited to the calendar. This initial discovery step sets the stage for IDOR exploitation by confirming the lack of authorization checks.

## Requirements

1. Valid Semrush account with access to the marketing calendar tool
2. Web browser with developer tools (e.g., Firefox Developer Tools or Chrome DevTools)
3. Network access to https://ec.semrush.com

## Defense

Defensive measures and detection strategies:

- Implement client-side request monitoring or WAF rules to detect unusual API probing
- Log and alert on repeated accesses to user_status endpoint from non-owners
- Enforce server-side ownership verification for all object references

## Objectives

1. Identify the vulnerable endpoint and its parameters
2. Confirm exposure of sensitive data in responses
3. Establish baseline for further testing

## Instructions

### Step 1: Load Marketing Calendar

**Context**: Access the Semrush marketing calendar interface to trigger relevant API calls.

Navigate to the marketing calendar tool in Semrush and load an existing calendar.

**Expected Output**: Calendar loads normally, triggering background API requests.

### Step 2: Inspect Network Requests

**Context**: Use browser tools to capture and analyze the API call.

Open developer tools (F12), go to the Network tab, and filter for XHR/Fetch requests. Reload the calendar and locate the GET request to https://ec.semrush.com/api/v1/ga/user_status/?calendar_id=YOUR_CALENDAR_ID.

Examine the response JSON for fields like 'id' (user_id) and 'status' (e.g., AUTHORISED).

**Expected Output**: JSON response revealing owner details without additional auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- reconnaissance
