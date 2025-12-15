---
tags:
  - graphql
  - proxy
  - capture
type: procedure
tools:
  - '[[tools/Charles-Proxy]]'
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
updated_at: '2025-12-14T17:25:52.988Z'
sub_techniques: []
id: 56b10e0d-fafe-451a-bcd9-5ed1c77b844c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Capture-GraphQL-Password-Change-Request

## Summary

This procedure intercepts the GraphQL mutation request during a password change on HackerOne using a web proxy, capturing critical authentication artifacts like tokens and cookies for later replay.

## Description

The HackerOne password change triggers a GraphQL mutation to the backend, sent with an x-auth-token header and __Host-session cookie. By proxying the traffic, this step captures the full request payload, including password values. Post-submission, the user is signed out, but tokens remain valid briefly, creating a replay window. This is key to demonstrating the authentication bypass vulnerability.

## Requirements

1. Configured web proxy (Charles Proxy) intercepting browser traffic
2. Active session from prior login
3. Target at https://hackerone.com/settings/pass/edit

## Defense

Defensive measures and detection strategies:

- Enforce token invalidation on sensitive mutations like password changes
- Log and alert on proxy-like traffic patterns or repeated mutations
- Use certificate pinning to hinder MiTM interception

## Objectives

1. Intercept and store the GraphQL mutation request details
2. Confirm password change success and subsequent sign-out
3. Extract reusable auth tokens for replay testing

## Instructions

### Step 1: Configure Proxy for Interception

**Context**: Set up Charles Proxy to capture HTTPS traffic from the browser.

Install and run Charles Proxy, enable SSL proxying for hackerone.com, and configure the browser to use the proxy (e.g., localhost:8888). Ensure the Charles root certificate is trusted in the browser.

> Proxy dashboard shows incoming requests; no errors in certificate handling.

### Step 2: Submit Password Change Form

**Context**: Trigger the GraphQL request by changing the password.

On the password edit page, enter current password, a new temporary password, and confirmation, then click 'Change password'. Monitor the proxy for the outgoing POST request to the GraphQL endpoint.

> Request captured with mutation payload (e.g., variables including password hashes), x-auth-token, and __Host-session; response confirms success, followed by redirect to sign_in.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Charles-Proxy]]

## Tags

- graphql
- proxy
- capture
