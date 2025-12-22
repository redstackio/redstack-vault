---
id: proc-line-zip-traversal-001
tags:
  - path-traversal
  - zip-exploit
  - macos
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:29.930Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Craft-Zip-with-Path-Traversal-Payload

## Summary

This procedure creates a zip file with a specially crafted filename using URL-encoded path traversal sequences to trick the LINE Mac client's parsing into targeting files outside the zip directory, such as the victim's ~/Downloads.

## Description

The LINE Mac client mishandles zip filenames with '..%2f' (encoded '../') and '#' to truncate extension recognition, allowing traversal to arbitrary paths like Applications or Downloads. An empty or dummy zip is sufficient, as the exploit is in filename resolution during handling. Requires macOS zip tools.

## Requirements

1. macOS Terminal or Finder for zip creation
2. Knowledge of URL encoding (%2f for /)
3. Target path knowledge (e.g., ~/Downloads/malicious.terminal)

## Defense

Defensive measures and detection strategies:

- Sanitize filenames in client-side parsing, normalizing and blocking traversal patterns
- Validate zip paths against sandbox boundaries
- Patch client to reject malformed filenames with # or % encodings

## Objectives

1. Create traversal filename targeting .terminal
2. Send zip via LINE without alteration
3. Set up for execution trigger

## Instructions

### Step 1: Prepare Dummy Zip Content

**Context**: Create a basic zip file.

Use Finder to zip an empty folder or run in Terminal:

```bash
mkdir dummy && zip traversal.zip dummy/
```

### Step 2: Rename with Traversal Payload

**Context**: Apply the malicious filename.

Rename the zip to: '..%2f..%2f..%2f..%2f..%2f..%2f..%2fDownloads%2fmalicious.terminal#.zip'. The multiple '..%2f' traverse up directories to reach ~/Downloads, and # blocks .zip recognition, causing launch of the targeted file.

**Expected Output**: Renamed zip file ready for sharing.

### Step 3: Send via LINE

**Context**: Deliver to victim.

Upload and send the zip in the same chat as the .terminal.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- path-traversal
- filename-exploit
