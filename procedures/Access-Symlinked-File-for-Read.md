---
tags:
  - file-read
  - exfiltration
  - web-access
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:30:18.607Z'
skill_level: basic
impact_level: high
detection_risk: high
sub_techniques: []
id: a4bc25e3-3309-412b-a993-761cd066bfbf
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Access-Symlinked-File-for-Read

## Summary

This procedure describes accessing the symlinked file via its web URL post-restore to read the contents of the targeted arbitrary file, such as /etc/passwd.

## Description

After restore, the symlink in /uploads/ resolves to the target file during extraction, making it servable via Discourse's static file serving. Browser access displays raw contents. Limited to server-readable files; impactful for config/secrets in multisite setups.

## Requirements

1. Successful restore completion
2. Known URL path for the symlinked file (e.g., /uploads/default/original/1X/hash.png)
3. Web access to the site

## Defense

Defensive measures and detection strategies:

- Block direct access to /uploads/ for non-image files or validate MIME types
- Monitor access logs for unusual /uploads/ requests
- Use web application firewall (WAF) to detect raw text in image URLs

## Objectives

1. Retrieve sensitive file contents via browser
2. Verify exploitation success
3. Potentially chain to read other files

## Instructions

### Step 1: Construct the URL

**Context**: Build the access path based on symlink location.

Use format: https://target.com/uploads/default/original/1X/[hash].png

> Expected: URL ready; no command needed.

### Step 2: Access in Browser

**Context**: Trigger the read by fetching the file.

Navigate to the URL in a web browser.

> Expected: Browser renders /etc/passwd contents as text.

### Step 3: Verify Contents

**Context**: Confirm arbitrary read achieved.

Inspect displayed data for expected format (e.g., user:pass:uid:gid lines).

> Expected: Sensitive info visible; copy for analysis.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- arbitrary-read
- symlink-access
