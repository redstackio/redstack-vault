---
tags:
  - payload-update
  - xxe
type: procedure
tools:
  - '[[tools/Ruby]]'
  - '[[tools/Sinatra]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/ruby-server-rb]]'
  - '[[commands/puts-uri-unescape]]'
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Cloud Storage]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 703fa7cd-5827-4f16-be42-ae99e3e41341
created_at: '2025-12-13T09:00:27.295Z'
updated_at: '2025-12-13T09:00:27.295Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Cloud Storage]]'
---
# Update Payload for Multi-Line Exfiltration

## Summary

This procedure modifies the XXE payload to handle exfiltration of multi-line files and directory listings by updating the sitemap and adding a pingback endpoint.

## Description

The updated sitemap uses entities to concatenate file paths or contents, sending them to /pingback where they are unescaped and printed. This allows reading files like /etc/passwd, /app/instance_data.json, and private keys.

## Requirements

1. Existing attacker server
2. Knowledge of target file paths
3. Ruby scripting skills

## Defense

Defensive measures and detection strategies:

- Sanitize XML inputs and disable entity expansion
- Log and alert on entity resolution attempts

## Objectives

1. Exfiltrate complex data structures
2. Enumerate server filesystem
3. Escalate to sensitive data access

## Instructions

### Step 1: Modify Server Script

**Context**: Update routes and payload for multi-line handling.

Add /pingback endpoint with [[commands/puts-uri-unescape]] to unescape and print query strings.

### Step 2: Restart Server

**Context**: Apply changes by restarting.

**Command** ([[commands/ruby-server-rb]]):
```bash
ruby server.rb
```

> Server restarts with new payload; logs show exfiltrated multi-line data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Cloud Storage]]

### Sub-Techniques



## Commands Used

- [[commands/ruby-server-rb]]
- [[commands/puts-uri-unescape]]

## Tools Used

- [[tools/Ruby]]
- [[tools/Sinatra]]

## Tags

- [[payload-update]]
- [[xxe]]
