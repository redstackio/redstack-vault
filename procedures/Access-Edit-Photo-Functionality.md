---
tags:
  - web
  - access
  - profile
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/fetch-autodesk-edit-page]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
id: fbdfbba6-a864-4486-b86c-daee6254618d
created_at: '2025-12-14T17:30:27.274Z'
updated_at: '2025-12-14T17:30:27.274Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Edit Photo Functionality

## Summary

This procedure accesses the photo editing feature in Autodesk's user profile system, identifying the 'id' parameter used for profile referencing and preparing for IDOR exploitation.

## Description

The Autodesk profile service at profile.autodesk.com allows authenticated users to edit their profile picture via a web interface. The endpoint uses a direct 'id' parameter without initial authorization checks, making it susceptible to manipulation. This step establishes the baseline request structure for subsequent tampering, typically involving a GET request to load the edit form.

## Requirements

1. Active Autodesk account login with session cookie or token
2. Web browser or curl for HTTP requests
3. Direct access to https://profile.autodesk.com

## Defense

Defensive measures and detection strategies:

- Require session-based ownership verification on all profile endpoints
- Rate-limit access to edit functions
- Log all requests to profile modification endpoints for anomaly detection

## Objectives

1. Load the authenticated user's photo edit interface
2. Extract the request format including the 'id' parameter
3. Confirm no immediate access restrictions

## Instructions

### Step 1: Authenticate and Navigate to Edit Photo

**Context**: This step loads the photo edit page to inspect the vulnerable parameter.

**Command** ([[commands/fetch-autodesk-edit-page]]):
```bash
curl -v -H "Cookie: your_session_cookie" "https://profile.autodesk.com/edit-photo?id=your_user_id"
```

> This sends a GET request to fetch the edit page. Replace 'your_session_cookie' with your actual session value (extract from browser dev tools) and 'your_user_id' with your profile ID. Expected output includes verbose HTTP details and the HTML form for photo upload, confirming the 'id' parameter presence.

### Step 2: Inspect Response

**Context**: Analyze the loaded page or response for upload form details.

**Instructions**: Use browser dev tools (F12 > Network tab) or parse the curl output to note the POST endpoint (likely /update-photo) and required fields like 'photo' for file upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/fetch-autodesk-edit-page]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- web
- profile-access
