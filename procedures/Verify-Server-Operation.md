---
id: proc-uuid-003
tags:
  - path-traversal
  - verification
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:16.725Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-Server-Operation

## Summary

This procedure confirms the angular-http-server is running and serving content correctly by accessing it via a web browser.

## Description

Before exploiting the vulnerability, verify the server responds to standard requests. Navigate to the local endpoint to ensure the index.html is served, confirming the setup is operational and the port is accessible. This step validates the environment without triggering the traversal.

## Requirements

1. Server running on port 8080
2. Web browser available
3. Localhost access

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected local server startups
- Use browser developer tools to inspect requests
- Log all HTTP access attempts

## Objectives

1. Confirm server accessibility
2. Validate content serving
3. Ensure no immediate errors

## Instructions

### Step 1: Access Server in Browser

**Context**: Load the served page to check if the server is operational.

**Command** (Browser navigation):
No CLI command; open http://127.0.0.1:8080 in a browser.

> Expected output: Basic HTML page displays 'Test SPA' or similar content from index.html.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- server-check
