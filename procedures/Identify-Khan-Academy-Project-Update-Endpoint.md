---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - reconnaissance
  - api-endpoint
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:16:37.227Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify-Khan-Academy-Project-Update-Endpoint

## Summary

This procedure involves inspecting network traffic on Khan Academy to identify the API endpoint used for updating document projects, revealing opportunities for input injection due to lack of sanitization.

## Description

In the context of Khan Academy's web application, document projects allow users to create and edit content. By monitoring network requests during project edits, attackers can locate the PUT endpoint at https://www.khanacademy.org/api/internal/scratchpads/ID, which processes HTML without proper sanitization, enabling stored XSS. Prerequisites include a Khan Academy account and browser access.

## Requirements

1. Valid Khan Academy user account for authentication
2. Browser with developer tools enabled (e.g., Chrome DevTools)
3. Optional: Proxy tool like Burp Suite for request interception

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script execution
- Log and monitor API requests for anomalous payloads
- Sanitize all user inputs rendering as HTML

## Objectives

1. Locate the project update API endpoint
2. Confirm endpoint accepts unsanitized HTML
3. Prepare for payload injection

## Instructions

### Step 1: Create or Edit a Project

**Context**: Start a document project to trigger relevant network requests.

Log in to Khan Academy, navigate to a course like Physics, and create a new document project. Edit the content with benign HTML.

**Expected Output**: Project editor loads, network tab shows requests.

### Step 2: Inspect Network Requests

**Context**: Capture the update request to identify the endpoint.

Open browser developer tools (F12), go to the Network tab, and save the project changes. Filter for PUT requests and examine the one to /api/internal/scratchpads/ID.

**Expected Output**: Endpoint details, including URL and request body format.

### Step 3: Verify HTML Handling

**Context**: Test if HTML is passed through without sanitization.

Submit a test edit with simple HTML like <b>test</b> and check if it renders boldly in the project view.

**Expected Output**: HTML renders as intended, confirming lack of sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[Reconnaissance]]
- [[api-endpoint]]
