---
id: proc-uuid-004
tags:
  - credential-exposure
  - oauth
  - web
type: procedure
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:52.382Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Exposed-OAuth-Credentials

## Summary

This procedure inspects the page source of an authenticated session to extract plaintext client ID and secret from the OAuth workflow, enabling further exploitation.

## Description

After bypassing authentication, the application's OAuth integration stores sensitive credentials in client-side page source without protection. Attackers can view and copy these for impersonation or token generation in SSO-enabled web apps, leading to broader access or API abuse.

## Requirements

1. Successful authentication via prior bypass
2. Access to OAuth-involved pages
3. Browser developer tools for source inspection

## Defense

Defensive measures and detection strategies:

- Store client secrets server-side only; never expose in client code
- Obfuscate or encrypt any necessary client-side data
- Use short-lived secrets and rotate them regularly; monitor for anomalous OAuth usage

## Objectives

1. Retrieve exposed client ID and secret
2. Enable subsequent OAuth-based attacks
3. Demonstrate sensitive data exposure risk

## Instructions

### Step 1: Navigate to OAuth Page

**Context**: Access a page triggering the OAuth workflow post-authentication.

After login, go to a protected resource that loads OAuth elements, such as authorization endpoints.

> This ensures the page source contains the vulnerable data.

### Step 2: Inspect and Extract

**Context**: Use tools to view and copy the plaintext credentials.

Open Developer Tools (F12), go to the Elements or Sources tab, and search for 'clientid' or 'clientsecret' in the HTML/JS.

> Expected output: Strings like clientid: "abc123" and clientsecret: "xyz789" visible in plaintext.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[credential-exposure]]
- [[oauth]]
- [[web]]
