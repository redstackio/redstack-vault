---
id: proc-trigger-rce
tags:
  - rce
  - trigger
  - render
type: procedure
tools:
  - '[[tools/WikiCloth]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/execute-id]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
updated_at: '2025-12-14T17:23:50.165Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
---
# Trigger-RCE-by-Visiting-Wiki-Page

## Summary

This procedure accesses the malicious wiki page in GitLab, causing WikiCloth to render the MediaWiki content and execute the embedded Lua payload for RCE.

## Description

Visiting the wiki URL triggers GitLab's markup rendering pipeline, which uses WikiCloth to parse <lua> blocks. The payload bypasses the sandbox, running io.popen commands as the gitlab-www user. Prerequisites: Deployed payload; outcomes: Command output displayed, confirming execution.

## Requirements

1. Browser or curl access to GitLab wiki URL
2. Authenticated session if wiki is private
3. Deployed hello.wiki page

## Defense

Defensive measures and detection strategies:

- Log rendering errors or Lua execution attempts
- Rate-limit wiki page views
- Disable Lua in WikiCloth or use safe alternatives

## Objectives

1. Invoke server-side Lua execution
2. Observe RCE output in page content
3. Validate sandbox bypass success

## Instructions

### Step 1: Access Wiki Page

**Context**: Load the page to initiate rendering.

**Command** (Browser):
Navigate to https://gitlab.example.com/group/project/wikis/hello

> Triggers GET request. Expected output: Page loads with Lua print results, e.g., 'uid=33(gitlab-www)'.

### Step 2: Verify Execution

**Context**: Check for command output from payload.

**Command** ([[commands/execute-id]]):
Embedded in payload; observes via page render.

> io.popen('id') output displayed. Expected output: User/group info.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Python]] Lua

### Sub-Techniques


## Commands Used

- [[commands/execute-id]]

## Tools Used

- [[tools/WikiCloth]]

## Tags

- rce
- trigger
- render
