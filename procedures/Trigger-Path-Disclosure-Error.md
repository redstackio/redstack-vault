---
tags:
  - information-disclosure
  - error-trigger
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
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:00.622Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 795b5324-f1f3-4da3-94eb-10db36247287
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Trigger-Path-Disclosure-Error

## Summary

This procedure triggers an unhandled error in the Airship CMS /my/cabins endpoint, resulting in the disclosure of the server's full installation path via PHP error reporting.

## Description

The vulnerability stems from inadequate error handling in the Airship CMS application, where loading the cabins page without proper data or configuration causes a PHP exception or warning to expose the file system path. This is useful for reconnaissance, aiding in potential follow-on attacks like path traversal. The target is a web-based PHP application, and success is confirmed by observing the path in the error output.

## Requirements

1. Authenticated session from previous steps
2. Access to the /my/cabins endpoint
3. Browser developer tools for inspecting errors (optional)

## Defense

Defensive measures and detection strategies:

- Disable verbose error reporting in production (e.g., set display_errors=Off in PHP)
- Log and monitor error messages for path exposures
- Implement custom error handlers to sanitize output

## Objectives

1. Induce application error
2. Capture disclosed server path
3. Gather reconnaissance data

## Instructions

### Step 1: Load the Vulnerable Page

**Context**: Access the endpoint to initiate the error condition.

**Instructions**: Ensure you are logged in, then refresh or directly visit https://airship.paragonie.com/my/cabins.

> The page fails to load properly, displaying an error message.

### Step 2: Observe and Capture Disclosure

**Context**: Inspect the error output for the full server path.

**Instructions**: View the error in the browser; it will show a PHP warning or exception revealing the installation directory, such as "/var/www/html/airship/...".

> Screenshot or note the path for analysis. This confirms the information disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[path-disclosure]]

