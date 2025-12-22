---
tags:
  - xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:30.877Z'
sub_techniques: []
id: e7b9a436-3e5b-4613-b375-3d127feaeb26
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Filename

## Summary

This procedure creates a file with a malicious filename designed to inject an HTML iframe tag into the buttle directory listing, exploiting the lack of sanitization.

## Description

Filenames in buttle are rendered directly in HTML without escaping, allowing breakout from attributes (e.g., <a href="filename">) to inject tags like <iframe>. The filename "><iframe src="malware_frame.html"> closes the attribute and adds the iframe, which loads a separate malicious file. This is a stored XSS as the payload persists in the file system.

## Requirements

1. Local file system write access
2. Buttle module installed (from prior procedure)
3. Text editor or shell for file creation

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled inputs in file names
- Disable directory listings or use secure templating (e.g., escape HTML entities)
- Scan for suspicious filenames with regex for HTML tags

## Objectives

1. Inject HTML payload via filename
2. Set up for iframe loading
3. Enable stored XSS persistence

## Instructions

### Step 1: Craft and Create File

**Context**: Manually create an empty file with the payload name to exploit the rendering.

No command; use touch or editor:

```bash
touch "><iframe src=\"malware_frame.html\">
```

> In practice, escape quotes if needed in shell. The file can be empty; the name is the payload. Expected output: File created successfully.

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
