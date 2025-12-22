---
tags:
  - rails
  - server
type: procedure
tools:
  - '[[tools/rails-cli]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/start-rails-server]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:49.400Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 261ab3c8-564d-4c72-8e8b-37a9197eb44e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Start-Rails-Development-Server

## Summary

Launches the Rails server in development mode to expose vulnerable Active Storage endpoints on localhost:3000.

## Description

Runs the app server, using dev config with guessable secrets, making signed URLs exploitable without auth.

## Requirements

1. App setup complete
2. Dependencies installed
3. Port 3000 free

## Defense

Defensive measures and detection strategies:

- Run in production mode with secure secrets
- Firewall restrict port 3000
- Monitor server logs for suspicious requests

## Objectives

1. Host the vulnerable app
2. Enable URL access for exploitation

## Instructions

### Step 1: Launch Server

**Context**: Start Puma/WEBrick server.

**Command** ([[commands/start-rails-server]]):
```bash
bin/rails s
```

> Starts on 0.0.0.0:3000. Expected: "=> Booting Puma" and listening message.

Keep terminal open.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/start-rails-server]]

## Tools Used

- [[tools/rails-cli]]

## Tags

- rails
- server
