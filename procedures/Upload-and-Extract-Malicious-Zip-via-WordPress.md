---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - wordpress
  - upload
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.904Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload and Extract Malicious Zip via WordPress

## Summary

This procedure uploads a malicious ZIP to WordPress and triggers its extraction using the vulnerable unzip_file function, resulting in files being written to arbitrary directories due to path traversal.

## Description

Authenticated users can upload ZIPs via the admin 'Upload Plugin' interface or custom scripts calling unzip_file. The function processes entries without path validation, allowing traversal to locations like /tmp. Particularly exploitable in plugins like NextGen Gallery permitting non-admin uploads. Target: WordPress 4.7.2. Outcomes include arbitrary file writes, enabling RCE if payloads are PHP and placed in web root.

## Requirements

1. Valid WordPress admin credentials
2. Access to /wp-admin/ dashboard
3. Malicious ZIP prepared from prior procedure

## Defense

Defensive measures and detection strategies:

- Disable or patch unzip_file in custom plugins
- Validate all uploaded file types and scan contents
- Enable WordPress file upload restrictions and monitor access logs for ZIP processing

## Objectives

1. Successfully upload ZIP without rejection
2. Trigger extraction to exploit traversal
3. Achieve file write in target directory

## Instructions

### Step 1: Log In to WordPress Admin

**Context**: Gain authenticated access required for upload features.

Navigate to /wp-admin/ and log in with admin credentials.

### Step 2: Upload ZIP via Plugin Interface

**Context**: Use built-in upload to process the ZIP.

Go to Plugins > Add New > Upload Plugin, select zip_poc.zip, and install/activate. This calls unzip_file internally.

### Step 3: Alternative Custom Extraction

**Context**: If direct upload blocked, use a custom script.

Create poc.php with: require_once(ABSPATH . 'wp-admin/includes/file.php'); unzip_file('zip_poc.zip', '/wp-content/uploads/'); Upload and execute poc.php via browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[wordpress-upload]]
- [[path-traversal]]
- [[zip-extraction]]
