---
tags:
  - auth-bypass
  - response-tampering
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.511Z'
sub_techniques: []
id: 4fb39b6f-851d-4bd0-9a36-a9fff87a47e6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Modify-Server-Redirect-to-Success-Response

## Summary

This procedure bypasses authentication by altering the server's 302 redirect response to a 200 success code, tricking the client into loading the protected appeal form.

## Description

The DoD application's reliance on HTTP redirects for auth enforcement allows interception and modification. Using a proxy, change the response status from 302 (Found/Redirect) to 200 (OK), removing the need for login and exposing the form to unauthenticated users.

## Requirements

1. Active proxy interception on the request to /App/createappeal.aspx
2. Knowledge of HTTP response structure
3. Burp Suite or equivalent tool

## Defense

Defensive measures and detection strategies:

- Enforce server-side session validation on all POST/GET actions
- Log and alert on mismatched client-server response patterns
- Disable client-side redirect handling for sensitive flows

## Objectives

1. Simulate successful authentication
2. Access protected form
3. Enable further manipulation

## Instructions

### Step 1: Intercept Response

**Context**: Capture the server's response after forwarding the request.

In Burp Suite Repeater or Proxy, forward the GET request and intercept the incoming 302 response.

**Expected Output**: 302 response with Location header to login page.

### Step 2: Tamper and Forward

**Context**: Modify status to bypass redirect.

Edit the response status code from 302 to 200, remove or alter the Location header if present, then forward to the browser.

**Expected Output**: Browser displays the appeal creation form.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[auth-bypass]]
- [[response-tampering]]
