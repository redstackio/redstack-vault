---
tags:
  - information-disclosure
  - commandline
  - pprof
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-pprof-cmdline]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:48.362Z'
sub_techniques: []
id: 59e7956b-ccb6-47ea-816f-ef66f4d9fcc5
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Expose-Golang-Pprof-Commandline-Arguments

## Summary

This procedure extracts command-line arguments from a Golang application's pprof endpoint, revealing startup flags, paths, and secrets used in the server's invocation.

## Description

The /debug/pprof/cmdline?debug=1 endpoint dumps the os.Args slice, exposing how the binary was run. For Cortex, this disclosed internal configs in the Shopify exposure, aiding in understanding deployment details.

## Requirements

1. Access to pprof endpoints
2. HTTP GET with query param
3. Target running Golang service

## Defense

Defensive measures and detection strategies:

- Remove cmdline endpoint or require auth
- Sanitize debug outputs in production
- Audit logs for pprof access

## Objectives

1. Disclose startup arguments
2. Identify sensitive flags or paths
3. Support configuration reconnaissance

## Instructions

### Step 1: Request Cmdline with Debug

**Context**: Append ?debug=1 to fetch detailed command-line output.

**Command** ([[commands/curl-access-pprof-cmdline]]):
```bash
curl https://cortex-ingest.shopifycloud.com/debug/pprof/cmdline?debug=1
```

> Output shows space-separated args, e.g., "/path/to/cortex -config=/etc/cortex.yaml".

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-pprof-cmdline]]

## Tools Used

- [[tools/curl]]

## Tags

- [[information-disclosure]]
- [[commandline]]
- [[pprof]]
