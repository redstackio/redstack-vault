---
id: proc-upload-ruby-payload-snippet
tags:
  - gitlab
  - file-upload
  - payload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:24:15.074Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-Ruby-Payload-via-GitLab-Snippet

## Summary

This procedure uploads a malicious Ruby payload file via GitLab's snippet feature to a predictable filesystem path, enabling later exploitation through directory traversal.

## Description

In GitLab, snippets allow users to create and attach files, storing them in /var/opt/gitlab/gitlab-rails/uploads. The path is controllable and predictable based on user ID and hash. The payload is a simple Ruby script that executes on load, writing to /tmp for verification. This sets up the initial access vector for RCE in the wiki rendering pipeline using Kramdown and Rouge.

## Requirements

1. Valid GitLab user account with snippet creation permissions
2. Access to GitLab UI for file upload
3. Knowledge of target upload path format (/uploads/-/system/user/[ID]/[hash]/payload.rb)

## Defense

Defensive measures and detection strategies:

- Restrict file uploads in snippets to non-executable types
- Monitor upload paths for .rb files
- Implement path validation in storage

## Objectives

1. Store malicious Ruby code on the server
2. Obtain exact filesystem path for traversal
3. Prepare for payload loading via require mechanism

## Instructions

### Step 1: Create New Snippet

**Context**: Initiate snippet creation to attach the payload file.

No command; use GitLab UI: Navigate to Snippets > New Snippet, enter any title and file name (e.g., payload.rb).

> Click 'Attach a file' and upload the Ruby file.

### Step 2: Upload Payload File

**Context**: Attach the malicious Ruby code to the snippet description.

Payload content:

```ruby
puts 'hello from ruby'; `echo vakzz was here > /tmp/vakzz`;
```

> Upload via UI; note the generated path like /uploads/-/system/user/1/c4119c5b144037f708ead7295cea4dd0/payload.rb.

### Step 3: Save Snippet and Note Path

**Context**: Finalize and record the upload location.

No command; save the snippet and inspect the attachment URL or filesystem if accessible.

> Expected: Path stored for use in traversal string.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- file-upload
- payload
