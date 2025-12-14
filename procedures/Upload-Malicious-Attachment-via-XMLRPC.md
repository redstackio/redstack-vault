---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - xmlrpc
  - upload
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-xmlrpc-post-attachment]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.943Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-Malicious-Attachment-via-XMLRPC

## Summary

This procedure sends the prepared XMLRPC payload to WordPress to create a malicious attachment, storing the XSS payload in the filename for later execution.

## Description

Exploiting the stored XSS requires uploading via XMLRPC since direct media uploads may sanitize. The wp.newPost() call with post_type='attachment' stores the file path, and wp_basename($file) echoes it unescaped in the media list table (class-wp-media-list-table.php). Verified on themes like Twenty Fourteen. Assumes XMLRPC authentication succeeds.

## Requirements

1. Prepared xss.xml file from prior step
2. curl installed
3. Network access to target WordPress /xmlrpc.php
4. Valid credentials in XML

## Defense

Defensive measures and detection strategies:

- Apply WordPress patches (e.g., 4.2.5+ adds esc_html)
- Rate-limit XMLRPC endpoints
- Audit attachment filenames for script tags

## Objectives

1. Create attachment post via XMLRPC
2. Store malicious filename without sanitization
3. Confirm creation for triggering

## Instructions

### Step 1: Send POST Request

**Context**: Use curl to POST the binary XML to xmlrpc.php, setting Content-Type to application/xml.

**Command** ([[commands/curl-xmlrpc-post-attachment]]):
```bash
curl 'https://wordpress.site/xmlrpc.php' --data-binary "\`cat xss.xml\`" -H 'Content-type: application/xml'
```

> This sends the payload. --data-binary preserves XML formatting; backticks execute cat. Expected: XML response like <methodResponse><params><param><value><int>POST_ID</int></value></param></params></methodResponse>. If fault, check auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xmlrpc-post-attachment]]

## Tools Used

- [[tools/curl]]

## Tags

- xss
- xmlrpc
- wordpress
