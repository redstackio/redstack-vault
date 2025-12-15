---
tags:
  - csrf
  - recon
  - web-vulnerability
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.422Z'
sub_techniques: []
id: 8314ec71-4354-45f0-9838-80ccbff5bd1f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify CSRF Token in Udemy Course Creation Request

## Summary

This procedure involves inspecting network requests during legitimate course creation on Udemy to identify the CSRF token, confirming it is sent but not enforced by the server, setting the stage for bypass attempts.

## Description

In the context of Udemy's web application, the course creation endpoint includes a CSRF token in requests to prevent cross-site request forgery. However, if the server does not validate this token, attackers can forge requests. This procedure uses browser tools to observe the token's presence and behavior, typically in a development or testing environment with authenticated access to Udemy. Expected outcomes include extraction of token details and confirmation of bypass feasibility without causing harm.

## Requirements

1. Authenticated Udemy account
2. Modern web browser with developer tools (e.g., Chrome, Firefox)
3. Basic knowledge of HTTP requests and network inspection

## Defense

Defensive measures and detection strategies:

- Implement and enforce CSRF token validation on all state-changing endpoints
- Monitor for anomalous course creation requests from unusual sources
- Use Content Security Policy (CSP) to restrict form submissions

## Objectives

1. Confirm presence of CSRF token in course creation requests
2. Verify lack of server-side enforcement
3. Gather details for subsequent exploitation testing

## Instructions

### Step 1: Authenticate and Initiate Course Creation

**Context**: Log in to Udemy and start the course creation process to trigger the relevant request.

Navigate to the course creation page in the Udemy dashboard and fill in basic details to submit a test request.

**Expected Output**: Form submission triggers a POST request observable in dev tools.

### Step 2: Inspect Network Request

**Context**: Use browser developer tools to capture and analyze the request, focusing on the CSRF token.

Open DevTools (F12), go to the Network tab, and filter for POST requests. Submit the form and examine the request payload or headers for the CSRF token (e.g., named 'csrfmiddlewaretoken' or similar).

**Expected Output**: Request details showing token inclusion, e.g., Form Data: csrfmiddlewaretoken=abc123...

### Step 3: Test Token Omission

**Context**: Replay the request without the token to preliminarily check enforcement.

Copy the request as cURL from DevTools and remove the token parameter, then execute it to see if the server accepts it.

**Expected Output**: If bypass works, server processes the request without error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]

