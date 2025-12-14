---
tags:
  - malicious-server
  - proxy
  - rubygems
type: procedure
tools:
  - '[[tools/Geminabox]]'
  - '[[tools/Puma]]'
  - '[[tools/Rackup]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/start-evil-gem-server]]'
verified: false
platforms:
  - Web
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Compromise Hardware Supply Chain]]'
updated_at: '2025-12-14T17:23:41.233Z'
sub_techniques: []
id: 9dca408c-b17f-487e-a29f-13ccb843905e
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Compromise Hardware Supply Chain]]'
---
# Set-Up-Malicious-Gem-Server-to-Serve-Deserialization-Payload

## Summary

This procedure sets up a Geminabox-based server acting as a malicious RubyGems proxy, responding to /api/v1/dependencies with the crafted Marshal payload when query_gems is present, enabling the deserialization attack.

## Description

Modify the Geminabox server.rb to intercept GET /api/v1/dependencies requests and return the Marshal payload instead of JSON if query_gems parameter exists; otherwise, return a standard 200. Start with RUBYGEMS_PROXY=true to enable proxying, using Puma as the web server on port 9292.

## Requirements

1. Geminabox gem installed and configured
2. The malicious payload from previous procedure
3. Port 9292 available on localhost

## Defense

Defensive measures and detection strategies:

- Pin gem sources to official HTTPS endpoints
- Implement certificate pinning for RubyGems.org
- Log and alert on connections to non-standard gem servers

## Objectives

1. Deploy a functional proxy server mimicking RubyGems
2. Ensure payload delivery on dependency fetches
3. Verify server responsiveness

## Instructions

### Step 1: Modify Server Configuration

**Context**: Edit server.rb in Geminabox to inject the Marshal response logic.

No direct command; manually update the route handler to check for query_gems and return Marshal.dump of the gadget.

### Step 2: Launch the Server

**Context**: Start the Rack application with proxy enabled.

**Command** ([[commands/start-evil-gem-server]]):
```bash
RUBYGEMS_PROXY=true rackup
```

> Starts Puma in single mode on 127.0.0.1:9292. Expected output: "Puma starting... Listening on http://127.0.0.1:9292".

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Compromise Hardware Supply Chain]] Supply Chain Compromise: Compromise Software Dependencies and Development Tools

### Sub-Techniques


## Commands Used

- [[commands/start-evil-gem-server]]

## Tools Used

- [[tools/Geminabox]]
- [[tools/Puma]]
- [[tools/Rackup]]

## Tags

- malicious-server
- proxy
- rubygems
