---
id: proc-uuid-2
tags:
  - gitlab
  - snippet
  - upload
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
updated_at: '2025-12-14T17:24:14.954Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-GitLab-Snippet-for-File-Upload

## Summary

This procedure sets up a new snippet in GitLab to serve as a vector for attaching and uploading the malicious file, targeting the Workhorse's image processing endpoint.

## Description

GitLab snippets allow authenticated users to create code notes with attachments. The description field supports file uploads, which are processed by Workhorse using ExifTool. This step requires only basic authenticated access to the target GitLab instance.

## Requirements

1. Valid GitLab account with snippet creation permissions
2. Browser access to the GitLab web interface
3. Target URL: https://<target>/-/snippets/new

## Defense

Defensive measures and detection strategies:

- Restrict snippet attachments to trusted users
- Implement file type validation beyond extensions
- Rate-limit uploads and monitor for bulk snippet creation

## Objectives

1. Gain access to an upload endpoint via snippets
2. Prepare the form for malicious file attachment
3. Ensure submission triggers backend processing

## Instructions

### Step 1: Log In to GitLab

**Context**: Authenticate to access protected features like snippet creation.

Navigate to https://<target-gitlab> and log in with credentials.

> Expected: Dashboard accessible.

### Step 2: Navigate to New Snippet

**Context**: Open the snippet creation page.

Go to https://<target-gitlab>/-/snippets/new.

> Expected: Form loads with title, code, and description fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- web-upload
