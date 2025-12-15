---
tags:
  - information-disclosure
  - goroutine
  - stack-trace
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-retrieve-goroutine-traces]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:26:17.241Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 729848aa-062d-407f-9624-97e00575c595
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
---
# Retrieve-Goroutine-Stack-Traces

## Summary

This procedure requests detailed stack traces from all current goroutines on a Go-based InfluxDB instance, exposing memory addresses, file paths, and runtime details to facilitate analysis of application behavior.

## Description

By appending ?debug=1 to the goroutine endpoint, attackers can dump full stack traces without authentication, revealing internal paths like /usr/local/go-1.18.3/src/runtime/netpoll.go. This aids in identifying vulnerabilities or crafting targeted exploits in Kubernetes environments. The procedure assumes prior confirmation of pprof exposure.

## Requirements

1. Valid target URL with exposed /debug/pprof/goroutine
2. curl or similar HTTP tool
3. Knowledge of Go concurrency model

## Defense

Defensive measures and detection strategies:

- Block external access to /debug/pprof/* via WAF or network ACLs
- Use runtime flags to disable goroutine profiling in production
- Log and monitor for debug=1 parameter usage

## Objectives

1. Capture runtime stack traces for all goroutines
2. Extract internal file paths and memory details
3. Support further analysis for potential exploits

## Instructions

### Step 1: Request Goroutine Dump

**Context**: This fetches verbose stack traces of active goroutines.

**Command** ([[commands/curl-retrieve-goroutine-traces]]):
```bash
curl "https://influxdb.quality.gitlab.net/debug/pprof/goroutine?debug=1"
```

> The command uses quotes to handle the query parameter. Output includes goroutine IDs, stacks, and references to Go source files, indicating successful disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-retrieve-goroutine-traces]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[goroutine]]
- [[stack-trace]]
