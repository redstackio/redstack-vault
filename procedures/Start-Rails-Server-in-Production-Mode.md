---
id: proc-uuid-4
name: Start Rails Server in Production Mode
tags:
  - dos
  - rails
  - server
type: procedure
tools:
  - '[[tools/rails]]'
  - '[[tools/Puma]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/start-rails-server-production]]'
verified: false
platforms:
  - Ruby on Rails
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:36.513Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Start Rails Server in Production Mode

## Summary

This procedure launches the Rails application using Puma in a production-like configuration, limiting threads and enabling static file serving to mimic deployment environments like Heroku.

## Description

Production mode activates optimized settings, including the vulnerable middleware stack. With RAILS_MAX_THREADS=2, resource exhaustion is more pronounced during the attack, leading to quicker crash.

## Requirements

1. Configured Rails app
2. Puma server (default in Rails)
3. Environment variables set

## Defense

Defensive measures and detection strategies:

- Increase thread limits and monitor stack usage
- Use clustered Puma instances for resilience
- Deploy behind a load balancer

## Objectives

1. Simulate production deployment
2. Expose port 3000 for requests
3. Enable logging for observation

## Instructions

### Step 1: Start Server with Env Vars

**Context**: Use specific environment variables to run in production mode with Puma.

**Command** ([[commands/start-rails-server-production]]):
```bash
RAILS_ENV=production RACK_ENV=production SECRET_KEY_BASE=foo RAILS_SERVE_STATIC_FILES=enabled RAILS_MAX_THREADS=2 RAILS_LOG_TO_STDOUT=enabled rails s
```

> Run this in the app directory. Expected output: Puma startup logs, listening on http://localhost:3000.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/start-rails-server-production]]

## Tools Used

- [[tools/rails]]
- [[tools/Puma]]

## Tags

- dos
- rails
- server
