---
id: proc-nextcloud-logo-upload-231524
tags:
  - file-upload
  - html-injection
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:13.873Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Arbitrary-HTML-as-Site-Logo-in-Nextcloud

## Summary

This procedure exploits the unsecured logo upload endpoint in Nextcloud v12.0.0 to store arbitrary HTML files server-side, bypassing any image validation and setting the stage for HTML injection.

## Description

Nextcloud's theming app allows admins to upload logos via AJAX without checking file types or contents, accepting any extension. The uploaded file is stored and served directly at the logo endpoint without sanitization, enabling HTML rendering. This requires admin privileges and targets the PHP-based web app, leading to stored content that can be accessed publicly.

## Requirements

1. Administrator login credentials for Nextcloud.
2. Access to the admin theming interface (e.g., via http://[server]/nextcloud/settings/admin/theming).
3. Prepared HTML file from prior payload creation.
4. Network connectivity to the Nextcloud server.

## Defense

Defensive measures and detection strategies:

- Validate uploads server-side for image MIME types (e.g., image/png) and scan contents.
- Serve uploaded files with strict Content-Type: image/* headers.
- Log and alert on non-image uploads in admin panels.

## Objectives

1. Successfully store malicious HTML as the site logo.
2. Confirm no validation blocks the upload.
3. Enable subsequent rendering at the logo URL.

## Instructions

### Step 1: Log In as Admin

**Context**: Gain access to the upload interface.

Navigate to http://[server]/nextcloud and log in with admin credentials.

> Expected: Dashboard loads; proceed to Settings > Administration > Theming.

### Step 2: Submit HTML File

**Context**: Use the logo upload form to inject the file.

In the Theming section, select the logo upload field and choose the prepared `logo.html` file. Submit via the interface, which POSTs to http://[server]/nextcloud/index.php/apps/theming/ajax/updateLogo.

> The endpoint accepts the file without validation; watch for success message in the UI.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[html-injection]]
