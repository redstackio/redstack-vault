---
tags:
  - payload-generation
  - redis-injection
  - deserialization
type: procedure
tools:
  - '[[tools/Ruby]]'
  - '[[tools/Flask]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: e6adc038-d3ca-4a7e-903a-79ce5479ffd1
created_at: '2025-12-11T03:48:06.043Z'
updated_at: '2025-12-11T03:48:06.043Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Generate Malicious Redis Injection Payload

## Summary

This procedure generates a malicious payload exploiting the Sawyer library in GitLab to inject arbitrary Redis commands, setting up a deserialization gadget for remote command execution during GitHub imports.

## Description

The payload overrides methods like to_s and bytesize in Sawyer::Resource objects, allowing injection into Redis without validation. This leads to setting a crafted session that, when loaded, executes arbitrary commands via Marshal.load. Target environment includes GitLab 15.3.1-ee with Ruby 2.7.5.

## Requirements

1. Ruby 2.7.5 installed
2. gen_payload3.rb script modified with desired command
3. Local development environment

## Defense

Defensive measures and detection strategies:

- Patch GitLab to versions beyond 15.3.1 with fixes for CVE-2022-2884 bypass
- Monitor Redis commands for anomalies like unexpected MULTI/EXEC blocks
- Validate and sanitize JSON responses in import features

## Objectives

1. Create injectable Redis payload
2. Include deserialization gadget for RCE
3. Prepare for fake server integration

## Instructions

### Step 1: Modify Payload Script

**Context**: Edit gen_payload3.rb to set the command (e.g., 'echo id > /tmp/vakzz22') and update session key to a unique value like 'jjjj'.

No command executed; manual file edit.

> Ensure the command is safe for testing and matches the deserialization structure.

### Step 2: Generate Payload

**Context**: Run the script to produce the payload string.

**Command** ([[commands/ruby-generate-payload]]):
```bash
ruby ./gen_payload3.rb
```

> This outputs the payload for copying into fake_server3.py.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/ruby-generate-payload]]

## Tools Used

- [[tools/Ruby]]

## Tags

- #payload-generation
- #redis-injection
