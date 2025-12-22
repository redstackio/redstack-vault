---
id: proc-repeater-follow-redirect-001
tags:
  - redirection
  - follow
type: procedure
tools:
  - '[[tools/Burp-Suite-Repeater]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Desktop Application
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:31:19.386Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Follow-Redirection-in-Burp-Repeater

## Summary

This procedure activates Burp Repeater's Follow Redirection feature on a redirect response, generating a new request to the external domain while forwarding the sensitive Authorization header.

## Description

After receiving a 302 response in Repeater, clicking 'Follow redirection' creates a follow-up request to the Location URL, preserving headers like Authorization from the original request. This exploits the tool's behavior of not stripping auth headers cross-domain (unlike cookies). Prerequisites: Initial request sent with redirect response visible. Expected outcome: New request to external domain with leaked credentials, demonstrating the vulnerability.

## Requirements

1. Burp Repeater with a pending 302 response
2. Configured auth that applies to the original domain
3. External domain set up to log incoming requests

## Defense

Defensive measures and detection strategies:

- Manually review and edit requests before following redirects in Repeater
- Configure Burp macros or extensions to block sensitive headers on cross-domain requests
- Train users on risks of automatic header forwarding in tools

## Objectives

1. Process the redirect to the external location
2. Preserve and forward the auth header unintentionally
3. Enable observation of the leak in the next step

## Instructions

### Step 1: Identify the Redirect Response

**Context**: Confirm the response in Repeater includes a 302 and Location header.

No command (GUI). Inspect the response pane for Location: http://evil.com.

> Ensure the original request had the Authorization header.

### Step 2: Activate Follow Redirection

**Context**: Trigger the automatic follow-up request.

No command (GUI). Click the 'Follow redirection' button in the Repeater interface.

> This generates and sends a new GET request to http://evil.com, including Authorization: Basic dXNlcjpwYXNz. Check the new request tab for confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Repeater]]

## Tags

- redirection
- follow
