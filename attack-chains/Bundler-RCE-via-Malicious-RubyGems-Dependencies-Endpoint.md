---
tags:
  - rce
  - deserialization
  - rubygems
  - bundler
  - ruby
  - supply-chain
type: attack_chain
tools:
  - '[[tools/Ruby]]'
  - '[[tools/Geminabox]]'
  - '[[tools/Puma]]'
  - '[[tools/Rackup]]'
  - '[[tools/Bundler]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Ruby
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - >-
    [[procedures/Prepare-Malicious-Marshal-Payload-for-Ruby-Deserialization-RCE]]
  - '[[procedures/Set-Up-Malicious-Gem-Server-to-Serve-Deserialization-Payload]]'
  - '[[procedures/Trigger-RCE-by-Configuring-Bundler-to-Use-Malicious-Source]]'
step_count: 3
techniques:
  - '[[Compromise Hardware Supply Chain]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:41.250Z'
description: >-
  Multi-stage attack exploiting deserialization vulnerability in RubyGems
  dependencies endpoint to achieve remote code execution on Bundler clients via
  a malicious gem server.
id: e3cda151-05cf-4e4a-82da-9545981adcb5
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Compromise Hardware Supply Chain]]'
  - '[[Exploitation for Client Execution]]'
---
# Bundler RCE via Malicious RubyGems Dependencies Endpoint

Multi-stage attack chain demonstrating exploitation of the RubyGems /api/v1/dependencies endpoint, which returns Marshal-serialized data that Bundler deserializes unsafely, enabling remote code execution through gadget chains when a client fetches dependencies from a malicious source.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Payload] --> B[Setup Malicious Server]
    B --> C[Trigger via Bundler]
    C --> D[RCE Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Ruby]]
- [[tools/Geminabox]]
- [[tools/Puma]]
- [[tools/Rackup]]
- [[tools/Bundler]]

### Target Environment

- Ruby environment with Bundler installed (version 2.x)
- Local network access for server setup (port 9292)
- RubyGems-compatible client machine

### Initial Access Requirements

- No prior credentials needed; assumes ability to control a gem source or MITM position
- Local attacker machine with Ruby development tools

## Detailed Attack Procedures

### Step 1: Prepare Malicious Payload
procedure: [[procedures/Prepare-Malicious-Marshal-Payload-for-Ruby-Deserialization-RCE]]

**Objective**: Create a deserialization gadget chain that executes arbitrary commands upon loading in Bundler.

**Instructions**: Develop and execute a Ruby script to generate the Marshal payload using classes like Gem::SpecFetcher and Net::WriteAdapter to invoke Kernel.system('date').

Use [[commands/ruby-create-rce-payload]] to generate the payload:

```bash
ruby create_rce.rb
```

**Expected Output**: A string representation of the Marshal payload, e.g., "\\x04\\b\\[\\bc\\x15Gem::SpecFetcher...".

**Success Indicators**:
- Payload string generated without errors
- Gadget chain verifiable by inspecting the output

### Step 2: Set Up Malicious Server
procedure: [[procedures/Set-Up-Malicious-Gem-Server-to-Serve-Deserialization-Payload]]

**Objective**: Host a fake RubyGems server that responds to /api/v1/dependencies with the malicious Marshal data.

**Instructions**: Modify a Geminabox instance to return the payload on relevant requests, then start the server with proxy mode enabled.

Launch using [[commands/start-evil-gem-server]]:

```bash
RUBYGEMS_PROXY=true rackup
```

**Expected Output**: Server startup message, e.g., "Puma starting in single mode... Listening on http://127.0.0.1:9292".

**Success Indicators**:
- Server listening on port 9292
- Test request to /api/v1/dependencies returns the payload

### Step 3: Trigger Exploit via Bundler
procedure: [[procedures/Trigger-RCE-by-Configuring-Bundler-to-Use-Malicious-Source]]

**Objective**: Configure a Bundler project to fetch from the malicious server, causing deserialization and RCE.

**Instructions**: Initialize a project, edit Gemfile to point to the evil server, and install dependencies.

First, verify Bundler with [[commands/bundle-version-check]]:

```bash
bundle -v
```

Then initialize with [[commands/bundle-init]]:

```bash
bundle init
```

Edit Gemfile to include `source 'http://127.0.0.1:9292'` and a gem like 'json'. Finally, run [[commands/bundle-install-exploit]]:

```bash
bundle install
```

**Expected Output**: Command execution output like timestamps from 'date', e.g., "2021年 3月 7日 日曜日 15時44分43秒 JST", along with potential errors like Bundler::MarshalError.

**Success Indicators**:
- Arbitrary command ('date') executed on client
- RCE confirmed via output or system logs

## Attack Chain Summary

### Key Achievements

1. Successful payload creation exploiting Ruby Marshal deserialization
2. Deployment of a malicious gem proxy server mimicking RubyGems.org
3. Achievement of RCE on Bundler client without authentication

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Compromise Hardware Supply Chain]] Supply Chain Compromise: Compromise Software Dependencies and Development Tools
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
