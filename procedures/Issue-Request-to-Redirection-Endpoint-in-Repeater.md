---
id: proc-repeater-request-issue-001
tags:
  - repeater
  - request
type: procedure
tools:
  - '[[tools/Burp-Suite-Repeater]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Desktop Application
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.389Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Issue-Request-to-Redirection-Endpoint-in-Repeater

## Summary

This procedure uses Burp Repeater to send an initial HTTP request to the open redirection endpoint, targeting an external domain to trigger a redirect response.

## Description

Burp Repeater allows manual crafting and sending of HTTP requests. Here, a GET request is issued to /redirect.php?url=http://evil.com on Host: example.com, leveraging the configured Platform Authentication to include the Authorization header. This step simulates an attacker probing a vulnerable endpoint. Prerequisites: Open redirection set up and auth configured in Burp. Expected outcome: A 302 response with Location header pointing to the external site, setting up for the follow-redirection action.

## Requirements

1. Burp Suite Repeater tab open
2. Prior setup of redirection endpoint and authentication
3. Attacker-controlled domain (evil.com) ready to receive redirects

## Defense

Defensive measures and detection strategies:

- Scope Burp requests to in-domain only to prevent cross-origin follows
- Use Burp extensions to strip sensitive headers on redirects
- Log all Repeater actions for audit trails

## Objectives

1. Deliver the redirection-triggering request
2. Confirm inclusion of auth header in the initial request
3. Receive the redirect response without following it yet

## Instructions

### Step 1: Craft the Request in Repeater

**Context**: Build the HTTP request targeting the vulnerable endpoint.

No command (GUI). In Repeater, enter:

GET /redirect.php?url=http://evil.com HTTP/1.1
Host: example.com

> Ensure the request includes the Authorization header from Platform Auth.

### Step 2: Send the Request

**Context**: Transmit the request and observe the response.

No command (GUI). Click Send in Repeater.

> Expected: 302 Found response with Location: http://evil.com. Verify no credentials leaked in this initial step.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Repeater]]

## Tags

- repeater
- request
