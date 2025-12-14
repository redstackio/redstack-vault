---
tags:
  - reconnaissance
  - information-disclosure
  - javascript
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b7b00ea0-a706-43af-b515-9d0760155295
created_at: '2025-12-14T17:28:52.110Z'
updated_at: '2025-12-14T17:28:52.110Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-Vulnerable-JavaScript-File

## Summary

This procedure involves locating and inspecting a publicly accessible JavaScript file on the target site that inadvertently exposes user-specific data, such as the logged-in user_id, enabling further exploitation in cross-origin contexts.

## Description

In the Badoo vulnerability, the service worker script at https://badoo.com/worker-scope/chrome-service-worker.js?ws=1 is loaded without authentication and includes a global user_id variable tied to the user's session. This can be discovered by direct access while logged in, revealing the leak. The procedure targets web applications where static assets like JS files are not properly sanitized for sensitive data, allowing reconnaissance for information disclosure attacks. Prerequisites include a Badoo account for verification, but the endpoint is public.

## Requirements

1. Web browser for accessing and inspecting scripts
2. Logged-in session to Badoo to observe user-specific content
3. Basic knowledge of JavaScript and browser dev tools

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script sources
- Sanitize JS files to remove user-specific data or use server-side rendering with tokens
- Monitor access logs for unusual requests to internal JS endpoints

## Objectives

1. Confirm presence of user_id in the script
2. Document the exposure mechanism
3. Prepare for cross-origin exploitation

## Instructions

### Step 1: Access the Script URL

**Context**: Directly load the suspected vulnerable endpoint to inspect its content.

Navigate to https://badoo.com/worker-scope/chrome-service-worker.js?ws=1 in your browser while logged into Badoo.

> View the page source or use dev tools to search for 'user_id'. Expected output: A global variable declaration like `var user_id = 'specific_user_value';`.

### Step 2: Verify Cross-Origin Accessibility

**Context**: Test if the script can be loaded from another domain without restrictions.

Create a simple HTML test page on a local server with `<script src="https://badoo.com/worker-scope/chrome-service-worker.js?ws=1"></script>` and open it. Check console for errors.

> No CORS errors should appear, confirming public loadability. Expected output: Script executes, populating user_id if logged in.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[web-vulnerability]]
