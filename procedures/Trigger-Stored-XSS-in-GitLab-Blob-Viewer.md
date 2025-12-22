---
tags:
  - xss
  - trigger
  - blob-viewer
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.699Z'
sub_techniques: []
id: 295a7b68-2493-4b87-8037-98561cf1e90a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-in-GitLab-Blob-Viewer

## Summary

This procedure exploits the stored XSS by having a victim access the malicious OpenAPI file in GitLab's blob viewer, where rendering via SwaggerUIBundle and a subsequent click executes the injected JavaScript, bypassing CSP.

## Description

GitLab's blob viewer loads openapi_viewer.js, which passes the file content to SwaggerUIBundle for rendering. The unsanitized 'description' field injects HTML attributes that jQuery-ujs binds to click events, allowing globalEval to run scripts. This can lead to UI manipulation, arbitrary HTTP requests (GET, PUT, DELETE), or alerts. The attack requires the victim to view the file and interact (click anywhere).

## Requirements

1. Malicious file already committed to accessible repository
2. Victim with read access to the project
3. Modern web browser to render the viewer

## Defense

Defensive measures and detection strategies:

- Update GitLab to patched version with improved sanitization
- Enable logging for blob viewer accesses and anomalous requests
- Educate users on avoiding untrusted project files

## Objectives

1. Render the payload in the blob viewer
2. Trigger execution via user interaction
3. Perform actions like data exfiltration or requests as the victim

## Instructions

### Step 1: Access Blob Viewer

**Context**: Direct the victim to the file's blob viewer URL to initiate rendering.

No command; use URL like https://gitlab.com/group/project/-/blob/master/xss-openapi.json.

> The viewer loads and renders the OpenAPI with SwaggerUIBundle, injecting the payload attributes.

### Step 2: Interact to Execute

**Context**: Victim clicks anywhere on the rendered document to trigger the event handlers.

No command; upon click, jQuery-ujs processes data-remote=true and class attributes, executing <script>alert(0)</script> via globalEval.

> Expected: JavaScript runs, e.g., alert dialog or network requests with victim credentials.

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
- execution
- gitlab
