---
id: proc-uuid-1
tags:
  - javascript-inspection
  - endpoint-discovery
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:29:57.090Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Inspect JavaScript to Discover Hidden Endpoint

## Summary

This procedure involves inspecting client-side JavaScript files in a web application to uncover hidden or undocumented API endpoints, such as the invite endpoint in HackerOne's sandbox organization feature, enabling further exploitation of business logic flaws.

## Description

In the context of HackerOne's platform, the UI restricts inviting new team members due to a rate limit, but the backend lacks equivalent checks. By examining loaded JavaScript bundles, attackers can identify endpoints like `/organizations/hackycorp_demo/users/new_invite` that are not exposed in the frontend. This reconnaissance step is crucial for identifying bypass opportunities in web applications where frontend and backend validations differ. Prerequisites include access to the organization's page and browser developer tools.

## Requirements

1. Valid login to the target HackerOne organization (e.g., hackycorp_demo).
2. Browser with developer tools enabled (e.g., Chrome, Firefox).
3. Network access to hackerone.com.

## Defense

Defensive measures and detection strategies:

- Obfuscate or minify JavaScript to hide endpoint strings.
- Implement consistent validation on both frontend and backend.
- Monitor for unusual API calls via web application firewall (WAF).

## Objectives

1. Uncover hidden API endpoints for potential bypasses.
2. Map backend functionality not restricted by UI.
3. Enable subsequent exploitation steps.

## Instructions

### Step 1: Navigate to Organization User Management

**Context**: Load the page where user invitations would normally occur to trigger relevant JavaScript files.

Go to the HackerOne organization settings, specifically the team members or users section.

### Step 2: Inspect Network and Sources in Developer Tools

**Context**: Capture and analyze loaded resources to find endpoint references.

Open browser developer tools (F12), go to the Network tab, and reload the page. Filter for JS files, then in the Sources tab, search for terms like "invite" or "users/new_invite".

**Expected Output**: Reference to `/organizations/hackycorp_demo/users/new_invite` found in `https://hackerone.com/assets/static/js/30.8f8e2bc5.chunk.js`.

### Step 3: Extract and Verify Endpoint

**Context**: Confirm the endpoint's existence and purpose.

Copy the endpoint path and note its context in the code, such as form submission handlers.

**Expected Output**: Full URL constructed as `https://hackerone.com/organizations/hackycorp_demo/users/new_invite`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[javascript-inspection]]
- [[endpoint-discovery]]
- [[Reconnaissance]]
