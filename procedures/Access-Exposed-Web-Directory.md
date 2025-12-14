---
id: proc-uuid-002
tags:
  - directory-traversal
  - info-disclosure
  - web-misconfig
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-directory-list]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:56.878Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Access-Exposed-Web-Directory

## Summary

This procedure demonstrates accessing a publicly exposed web directory, such as /keys/ on a development server, to trigger the serving of sensitive files without authentication.

## Description

Development servers often have directory indexing enabled due to oversight, allowing attackers to browse and download files like json.json containing credentials. This targets HTTPS endpoints on port 443 and assumes no access controls. The outcome is direct exposure of resources, enabling further inspection. Use in scenarios where recon has identified potential paths.

## Requirements

1. Valid HTTPS URL to the target directory (e.g., https://cards-dev.twitter.com/keys/)
2. Tool for HTTP requests (browser or curl)
3. No credentials; relies on public exposure

## Defense

Defensive measures and detection strategies:

- Disable directory browsing in web server configs (e.g., Apache: Options -Indexes)
- Deploy access controls like IP whitelisting for dev environments
- Monitor access logs for unusual GET requests to sensitive paths

## Objectives

1. Gain access to unprotected directories
2. Trigger file serving or downloads
3. Confirm exposure of sensitive endpoints

## Instructions

### Step 1: Navigate to Directory Endpoint

**Context**: Use a browser or curl to request the directory URL, checking for listing or file response.

**Command** ([[commands/curl-directory-list]]):
```bash
curl -k -I https://cards-dev.twitter.com/keys/
```

> The -I flag shows headers; look for Content-Type: application/json or download headers. Expected output: 200 OK with file metadata.

### Step 2: Force File Retrieval

**Context**: If headers indicate a file, download it directly.

**Command** ([[commands/curl-directory-list]]):
```bash
curl -k https://cards-dev.twitter.com/keys/json.json
```

> This streams the file content. Expected output: Raw JSON with sensitive fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-directory-list]]

## Tools Used


## Tags

- directory-traversal
- web-misconfig
