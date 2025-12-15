---
tags:
  - authentication
  - request-generation
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
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:26:49.074Z'
sub_techniques: []
id: c4a346d4-7401-4771-9dbc-ab1d44a702aa
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Generate-Legitimate-Login-Request

## Summary

Submit a standard login form with valid credentials to produce a capturable POST request, establishing a baseline for modification in brute force attacks.

## Description

This step creates an authentic login attempt on the Lichess /login endpoint, which includes CSRF tokens and cookies. It's essential for replicating the request structure while preparing to strip protections. The procedure assumes access to test credentials; outcomes include a intercepted request ready for alteration, targeting the weak rate limiting vulnerability.

## Requirements

1. Valid test username and password for Lichess
2. Browser proxied through Burp Suite
3. Login page already accessed

## Defense

Defensive measures and detection strategies:

- Enforce CSRF token validation on all login attempts
- Ban common test credentials in automated checks
- Rate limit initial legitimate attempts per IP

## Objectives

1. Produce a genuine POST /login request
2. Ensure interception in proxy tools
3. Verify request completeness for modification

## Instructions

### Step 1: Fill Login Form

**Context**: Input credentials to trigger submission.

Enter username and password in the form fields on https://lichess.org/login.

### Step 2: Submit and Intercept

**Context**: Send the form to generate the request.

Click submit; in Burp Proxy, intercept the POST /login request.

> Forward the request to complete the action; note the full request details including headers and body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication
- request-generation
