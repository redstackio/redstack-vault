---
tags:
  - web
  - capture
  - idor
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.105Z'
sub_techniques: []
id: 58f0e10b-8839-47e0-91f9-f6b58016fb29
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Capture-Delete-Request-URL

## Summary

This procedure captures the HTTP request URL used for deleting a saved search, revealing the search_id parameter format essential for IDOR exploitation in the DoD web application.

## Description

As part of the IDOR attack on the DoD web app, this step involves triggering a delete action on the attacker's own saved search while monitoring network traffic. The goal is to extract the exact URL structure, such as `https://████/█████/████████={search_id}`, for modification in later steps. This assumes an authenticated session and focuses on non-destructive capture (e.g., cancel the delete if needed). Outcomes include the parameterized URL ready for ID tampering.

## Requirements

1. Authenticated session with saved searches available
2. Browser developer tools or proxy like Burp Suite
3. Ability to trigger and intercept HTTP requests

## Defense

Defensive measures and detection strategies:

- Rate-limit delete actions to prevent excessive request capturing
- Monitor for unusual network inspection patterns or proxy usage

## Objectives

1. Intercept the delete request for a personal saved search
2. Extract the search_id parameter from the URL
3. Document the endpoint format for exploitation

## Instructions

### Step 1: Enable Network Monitoring

**Context**: Set up tools to capture traffic before triggering the delete.

Open browser developer tools (F12) and go to the Network tab, or configure Burp Suite as a proxy.

> Expected output: Network tab active, ready to log requests.

### Step 2: Trigger Delete Action

**Context**: Perform the delete on a test item to capture the request.

Click the delete button/link for one of your saved searches.

> Expected output: Captured GET request in the format `https://████/█████/████████={search_id}`. Copy the URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[Burp-Suite]]

## Tags

- [[web]]
- [[capture]]
