---
id: proc-uuid-2
tags:
  - xss
  - injection
  - json-manipulation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.866Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Project-JSON

## Summary

This procedure modifies the exported project.json file to inject a malicious XSS payload into the note_html field of Note objects, setting cached_markdown_version to 917504 to bypass GitLab's cache regeneration during import.

## Description

Exploiting flaws in GitLab's cache invalidation logic from the CacheMarkdownField concern, this step allows attackers to control attributes in project.json. By injecting HTML like an onerror alert into note_html and using a specific cached_markdown_version, the payload persists without regeneration from markdown, leading to stored XSS in discussions.

## Requirements

1. Downloaded project export archive with project.json
2. Text editor or JSON parser tool
3. Knowledge of GitLab's Note object structure

## Defense

Defensive measures and detection strategies:

- Validate imported project data for malicious HTML in note_html fields
- Enforce cache regeneration on all imports regardless of version
- Scan JSON imports for script tags or event handlers

## Objectives

1. Insert executable JavaScript payload into note_html
2. Bypass cache check to preserve injection
3. Enable persistent XSS execution on import

## Instructions

### Step 1: Extract and Open JSON

**Context**: Access the Note objects in the discussions section.

Unzip the export archive and open project.json in a text editor. Locate the 'notes' or 'discussions' array.

### Step 2: Modify Note Object

**Context**: Inject the payload and set cache version to prevent regeneration.

For a Note object, add or update: "note_html": "<img src=\"test\" onerror=\"alert(document.domain)\"></img>html overwritten", and set "cached_markdown_version": 917504. Save the file and repackage the archive.

**Expected Output**: Updated project.json with payload integrated.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
- [[json-manipulation]]
