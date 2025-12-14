---
id: proc-uuid-4
tags:
  - gem-server
  - web-ui
type: procedure
tools:
  - '[[tools/gem]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/gem-server-launch]]'
verified: false
platforms:
  - Ruby
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.014Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Launch-RubyGems-Server

## Summary

This procedure starts the built-in RubyGems web server, hosting installed gems including the malicious one, exposing the vulnerable UI for XSS exploitation.

## Description

The 'gem server' command launches a local HTTP server (default port 8808) that serves documentation and metadata for installed gems. The WWW link for each gem pulls from the homepage field, directly executing javascript: schemes without sanitization. This enables the stored XSS when viewed. Requires the malicious gem installed; runs on localhost.

## Requirements

1. Malicious gem installed
2. Port 8808 available (or configurable)
3. Local network access for UI

## Defense

Defensive measures and detection strategies:

- Disable or sandbox the gem server if not needed
- Apply URI sanitization patches to the server rendering
- Monitor local ports for unexpected gem server instances

## Objectives

1. Expose installed gems via web interface
2. Render vulnerable hyperlinks from metadata
3. Facilitate client-side payload delivery

## Instructions

### Step 1: Start the Server

**Context**: Initiate the web server to host the gem index.

**Command** ([[commands/gem-server-launch]]):
```bash
gem server
```

> Binds to localhost:8808 and serves content. Expected output: "Server running at http://0.0.0.0:8808".

### Step 2: Confirm Server Readiness

**Context**: Ensure the server is operational.

Access http://localhost:8808 in a browser.

> Expected output: RubyGems index page loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/gem-server-launch]]

## Tools Used

- [[tools/gem]]

## Tags

- gem-server
- web-ui
