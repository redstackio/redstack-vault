---
tags:
  - rce
  - bundler
  - exploit-trigger
type: procedure
tools:
  - '[[tools/Bundler]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/bundle-version-check]]'
  - '[[commands/bundle-init]]'
  - '[[commands/bundle-install-exploit]]'
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:41.224Z'
sub_techniques: []
id: a0d56942-4876-4f80-a968-03958573305b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Trigger-RCE-by-Configuring-Bundler-to-Use-Malicious-Source

## Summary

This procedure configures a Bundler project to use the malicious gem server as its source, triggering the fetch of dependencies that deserializes the payload and executes arbitrary code on the client machine.

## Description

Initialize a new Bundler project, modify the Gemfile to specify the evil server URL (http://127.0.0.1:9292) as the source, add a dependency like 'json', and run bundle install. Bundler will query /api/v1/dependencies, deserialize the Marshal data, and execute the gadget chain, running 'date' (with retries causing multiple executions).

## Requirements

1. Bundler installed (version 2.2+)
2. Malicious server running from previous procedure
3. Local directory for the project

## Defense

Defensive measures and detection strategies:

- Audit Gemfile sources and restrict to trusted URLs
- Enable Bundler checksum verification
- Monitor for deserialization errors or unexpected command outputs in logs

## Objectives

1. Force Bundler to fetch from compromised source
2. Achieve RCE via deserialization
3. Confirm execution through observable effects

## Instructions

### Step 1: Verify Bundler Version

**Context**: Ensure Bundler is available and check its version.

**Command** ([[commands/bundle-version-check]]):
```bash
bundle -v
```

> Displays Bundler version, e.g., "Bundler version 2.2.13".

### Step 2: Initialize Project

**Context**: Create a new Gemfile.

**Command** ([[commands/bundle-init]]):
```bash
bundle init
```

> Generates Gemfile with default source; edit to change to http://127.0.0.1:9292 and add gem 'json'.

### Step 3: Install and Trigger

**Context**: Run installation to fetch and deserialize.

**Command** ([[commands/bundle-install-exploit]]):
```bash
bundle install
```

> Triggers RCE; expected output includes 'date' timestamps like "2021年 3月 7日 日曜日 15時44分43秒 JST" and errors like TypeError.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/bundle-version-check]]
- [[commands/bundle-init]]
- [[commands/bundle-install-exploit]]

## Tools Used

- [[tools/Bundler]]

## Tags

- rce
- bundler
- exploit-trigger
