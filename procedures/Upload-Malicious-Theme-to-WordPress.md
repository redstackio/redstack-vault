---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - wordpress
  - theme-upload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-05T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-13T23:55:20.334Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-Theme-to-WordPress

## Summary

This procedure uploads a custom theme ZIP file to a WordPress installation via the admin interface, extracting it to the wp-content/themes/ directory as a prerequisite for further manipulation in XSS exploitation.

## Description

In a WordPress environment, authenticated administrators can upload themes through the dashboard, which unzips and places files in the themes directory. This step sets up a theme that can later be broken and renamed to inject an XSS payload. It requires admin privileges and targets the web-based upload functionality, assuming no file upload restrictions are in place.

## Requirements

1. Authenticated access to WordPress admin dashboard with theme upload permissions
2. A prepared ZIP file containing a basic theme (e.g., empty folder with style.css)
3. Network access to the WordPress site

## Defense

Defensive measures and detection strategies:

- Restrict theme upload to trusted admins via role-based access control
- Enable file upload validation to scan ZIP contents for malware
- Monitor filesystem changes in wp-content/themes/ for unauthorized uploads

## Objectives

1. Place a modifiable theme in the themes directory
2. Establish a base for theme corruption and payload injection
3. Prepare for self-XSS execution in admin context

## Instructions

### Step 1: Prepare Theme ZIP

**Context**: Create a simple theme ZIP to avoid detection during upload.

Include a basic style.css file with theme headers (e.g., Theme Name: Test). Zip the theme folder.

### Step 2: Upload via Admin Interface

**Context**: Use the WordPress UI to install the theme.

Log in to /wp-admin/, navigate to Appearance > Themes > Add New > Upload Theme, select the ZIP, and install.

> The theme extracts to wp-content/themes/[theme-folder]/.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- wordpress
- theme-upload
