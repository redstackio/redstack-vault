---
tags:
  - path-traversal
  - ruby
  - tempfile
type: procedure
tools:
  - '[[tools/IRB]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/tempfile-open-traversal-poc]]'
platforms:
  - Windows
  - Ruby
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: cd46ea1b-b546-42f5-88c6-b4b3bd7051ff
created_at: '2025-12-14T17:26:22.908Z'
updated_at: '2025-12-14T17:26:22.908Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate Path Traversal with Tempfile.open

## Summary

This procedure exploits the path traversal vulnerability in Ruby's Tempfile.open method on Windows by providing a malicious basename with escaped backslashes, allowing file creation in arbitrary directories like C:\Users\rootx\.

## Description

The Tempfile.open method in lib/bundler/vendor/tmpdir/lib/tmpdir.rb (lines 118-138) uses String.delete(UNUSABLE_CHARS) to sanitize inputs, but on Windows, it fails to handle escaped backslashes properly due to implementation in string.c (rb_str_delete_bang). This leaves traversal sequences (e.g., \\..\\) intact, enabling attackers to navigate outside the temp directory. In a Rails app, this could place a .rb file for RCE. Prerequisites include a Windows Ruby environment and IRB access.

## Requirements

1. Windows OS with Ruby installed
2. Access to IRB shell
3. Write permissions in target directories (e.g., C:\Users)

## Defense

Defensive measures and detection strategies:

- Upgrade Ruby to a patched version addressing the String.delete flaw
- Implement additional input validation in applications using Tempfile, stripping all path separators explicitly
- Monitor file creation events in sensitive directories via Windows auditing

## Objectives

1. Create a temporary file outside the intended temp directory using traversal
2. Validate the vulnerability in a controlled Ruby environment
3. Demonstrate potential for malicious file placement

## Instructions

### Step 1: Launch IRB and Invoke Tempfile.open

**Context**: Start an interactive Ruby session and call Tempfile.open with a basename array containing traversal payload to bypass sanitization.

**Command** ([[commands/tempfile-open-traversal-poc]]):
```ruby
Tempfile.open(["\\..\\..\\..\\..\\..\\Users\\rootx\\malicious",".rb"])
```

> This command creates a Tempfile with basename "\\..\\..\\..\\..\\..\\Users\\rootx\\malicious" and ext ".rb". The escaped backslashes allow traversal from %TEMP% to C:\Users\rootx\. Expected output is a Tempfile object at the traversed path, e.g., #<Tempfile:C:/Users/rootx/AppData/Local/Temp\..\..\..\..\..\Users\rootx\malicious20210321-22472-fvuodx.rb>.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/tempfile-open-traversal-poc]]

## Tools Used

- [[tools/IRB]]

## Tags

- path-traversal
- ruby
- tempfile
