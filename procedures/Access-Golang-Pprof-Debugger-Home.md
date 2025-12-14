---
tags:
  - debugging
  - golang
  - pprof
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-pprof-home]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:48.364Z'
sub_techniques: []
id: b35bd919-6484-4676-8110-4274a932b365
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Access-Golang-Pprof-Debugger-Home

## Summary

This procedure accesses the Golang pprof debugging interface on an exposed Cortex server, allowing inspection of runtime profiles and setting up for potential resource exhaustion attacks.

## Description

Golang's pprof is a built-in profiler for debugging, but when exposed via /debug/pprof/, it lists heap, goroutines, and other metrics. In exposed services like Cortex, this enables attackers to download profiles or trigger CPU-intensive operations without auth.

## Requirements

1. Access to the target server's debug path
2. Basic HTTP client
3. Knowledge of Golang pprof endpoints

## Defense

Defensive measures and detection strategies:

- Disable or password-protect pprof in production
- Firewall debug paths from public access
- Monitor for high CPU from pprof requests

## Objectives

1. View available debugging profiles
2. Prepare for DoS via profile downloads
3. Gather runtime information

## Instructions

### Step 1: Access Pprof Index

**Context**: GET the pprof root to list available debug options.

**Command** ([[commands/curl-access-pprof-home]]):
```bash
curl https://cortex-ingest.shopifycloud.com/debug/pprof/
```

> Response includes links to /heap, /goroutine, etc., confirming exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-pprof-home]]

## Tools Used

- [[tools/curl]]

## Tags

- [[debugging]]
- [[golang]]
- [[pprof]]
