---
id: proc-identify-nordvpn-endpoint
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:57.526Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Password Change Endpoint

## Summary

This procedure involves observing legitimate password change requests in the NordVPN web application to identify the vulnerable endpoint lacking CSRF protection, enabling subsequent exploit crafting.

## Description

In the context of testing web applications like NordVPN, attackers first need to understand the structure of sensitive actions such as password changes. By performing a normal password update while monitoring network traffic (e.g., via browser dev tools), the POST endpoint, parameters, and request format are revealed. This endpoint (https://nordvpn.com/profile/) uses parameters like tmpl=settings, password, and password_confirmation but omits CSRF tokens, making it susceptible to forgery from external sources when the user is authenticated.

## Requirements

1. Access to a NordVPN account for legitimate testing
2. Browser with developer tools (e.g., Chrome DevTools Network tab)
3. Basic knowledge of HTTP requests and web forms

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Monitor for anomalous password change requests from unusual referers
- Enable logging of form submissions with user agent and origin checks

## Objectives

1. Capture the exact endpoint URL and parameters for password changes
2. Confirm absence of CSRF protections
3. Prepare data for exploit replication

## Instructions

### Step 1: Perform Legitimate Password Change

**Context**: Log into NordVPN and initiate a password change to capture the request.

Navigate to the profile settings and attempt to change the password, then inspect the network tab.

**Expected Output**: POST request details including URL https://nordvpn.com/profile/ and form data.

### Step 2: Analyze Request Parameters

**Context**: Extract and document the required fields from the captured request.

Note parameters: tmpl=settings, password=newpassword, password_confirmation=newpassword.

**Expected Output**: List of parameters needed for replication.

### Step 3: Verify Lack of CSRF Token

**Context**: Check the request headers and body for any anti-CSRF measures.

Confirm no token field or header like X-CSRF-Token is present.

**Expected Output**: Documentation confirming vulnerability to forged requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-recon]]
