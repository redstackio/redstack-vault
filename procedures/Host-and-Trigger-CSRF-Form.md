---
tags:
  - csrf
  - hosting
  - browser-trigger
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:15.430Z'
sub_techniques: []
id: eca655dc-3331-4b57-a267-be8af5dd2892
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host-and-Trigger-CSRF-Form

## Summary

This procedure covers hosting the malicious HTML form and triggering its submission in a browser to simulate the CSRF attack against the WordPress endpoint.

## Description

After creating the HTML file, the attacker hosts it locally or remotely and loads it in a browser. If the browser session is authenticated to the target site, clicking submit (or auto-submission) sends the forged POST request, changing the post password. This exploits the absence of origin validation on the form.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Optional: Simple HTTP server for remote hosting
3. Authenticated session on target site for testing

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and check request origins
- Log and alert on POST requests without valid referer
- Use Content Security Policy to block inline scripts

## Objectives

1. Deliver the payload via browser execution
2. Confirm the forged request reaches the server
3. Validate password change in a test environment

## Instructions

### Step 1: Load the HTML File

**Context**: Open the file in a browser to prepare for submission.

Navigate to the local file or hosted URL (e.g., file:///path/to/submit.html or http://attacker.com/submit.html).

> The page loads with the form. Expected output: Form visible or auto-submits if scripted.

### Step 2: Trigger Submission

**Context**: Initiate the POST request by interacting with the form.

Click the "Submit request" button or allow auto-submission.

> Monitor browser network tab for the POST to the WordPress URL with parameters. Expected output: 200 OK response or redirect indicating successful submission.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[drive-by]]
- [[web]]
