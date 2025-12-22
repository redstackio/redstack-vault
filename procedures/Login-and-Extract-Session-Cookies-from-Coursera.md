---
tags:
  - session-extraction
  - authentication
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/EditThisCookie]]'
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
updated_at: '2025-12-14T17:31:19.373Z'
sub_techniques: []
id: ed99b454-165d-40ed-8cc1-9e8b0a9c8670
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-and-Extract-Session-Cookies-from-Coursera

## Summary

This procedure authenticates to the Coursera web application and extracts session cookies using interception tools, setting up for session hijacking exploitation.

## Description

In the context of testing broken session management, log in to a Coursera account to establish an authenticated session. Use tools like Burp Suite to intercept traffic or EditThisCookie to view and export cookies. This captures tokens like session IDs that remain valid even after logout due to improper invalidation. Prerequisites include valid credentials and browser access to coursera.org. Expected outcome is a set of exportable cookies enabling session replay.

## Requirements

1. Valid Coursera account credentials.
2. Web browser with developer tools or extensions.
3. Network access to coursera.org.

## Defense

Defensive measures and detection strategies:

- Implement proper session invalidation on logout by server-side token revocation.
- Use short-lived session cookies with HttpOnly and Secure flags.
- Monitor for anomalous session reuse via logging cookie access patterns.

## Objectives

1. Establish authenticated session.
2. Capture all relevant session cookies.
3. Prepare cookies for external storage and reuse.

## Instructions

### Step 1: Navigate and Authenticate

**Context**: Access the login page and enter credentials to create a session.

No specific command; use browser UI to navigate to coursera.org and log in with username/password.

> Successful login redirects to dashboard, confirming session establishment.

### Step 2: Intercept and Extract Cookies

**Context**: Capture cookies during or post-authentication using tools.

Configure [[tools/Burp-Suite]] as a proxy to intercept requests, or use [[tools/EditThisCookie]] extension to export cookies.

> Extracted cookies include session identifiers; save in a format like JSON for later import.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/EditThisCookie]]
