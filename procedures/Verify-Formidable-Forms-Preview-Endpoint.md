---
id: proc-verify-endpoint-001
tags:
  - wordpress
  - recon
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-verify-ajax-preview]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.011Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Formidable-Forms-Preview-Endpoint

## Summary

This procedure verifies the accessibility of the unauthenticated AJAX endpoint in the Formidable Pro WordPress plugin used for form previews, confirming the presence of the vulnerable frm_forms_preview action.

## Description

The Formidable Pro plugin exposes an AJAX endpoint at wp-admin/admin-ajax.php that handles form previews without authentication. By sending a POST request with action=frm_forms_preview, an attacker can render the first form in the database (default 'contact us' form). This step establishes the attack surface for subsequent shortcode injections leading to SQLi. The target environment is a WordPress site with the plugin active, and success indicates no access controls on the endpoint.

## Requirements

1. Network access to the target WordPress site (HTTPS/HTTP)
2. curl tool installed
3. Knowledge of the target URL (e.g., https://target.com)

## Defense

Defensive measures and detection strategies:

- Restrict admin-ajax.php to authenticated users via .htaccess or plugin config
- Monitor AJAX requests for unusual action parameters in web server logs
- Enable WordPress security plugins like Wordfence to block unauthenticated admin access

## Objectives

1. Confirm endpoint responsiveness and form rendering
2. Identify Formidable Pro as active
3. Prepare for parameter injection testing

## Instructions

### Step 1: Send POST Request to Preview Endpoint

**Context**: This sends a basic request to trigger the preview action and observe the default form output.

**Command** ([[commands/curl-verify-ajax-preview]]):
```bash
curl -s -i 'https://www.drivegrab.com/wp-admin/admin-ajax.php' --data 'action=frm_forms_preview'
```

> This command uses curl in silent mode (-s) to request headers (-i) and POST data for the action. Expected output is a 200 OK response with HTML form elements; failure indicates endpoint protection or plugin absence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-verify-ajax-preview]]

## Tools Used

- [[tools/curl]]

## Tags

- wordpress
- recon
