---
tags:
  - information-disclosure
  - execution-trace
  - runtime-analysis
type: procedure
tools:
  - '[[tools/go-tool-trace]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-download-execution-trace]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:26:17.231Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: f986700e-c628-4f06-94a1-553025925eb9
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
---
# Download-Execution-Trace

## Summary

This procedure captures and downloads an execution trace from the pprof endpoint, recording program runtime events like goroutine scheduling for detailed concurrency analysis.

## Description

The /debug/pprof/trace endpoint generates a trace of syscalls, blocks, and GC events in Go apps like InfluxDB. Unprotected access allows downloading this octet-stream file, useful for debugging or reverse-engineering in exposed Kubernetes setups.

## Requirements

1. Exposed /debug/pprof/trace
2. HTTP downloader (curl)
3. Go trace tool for viewing

## Defense

Defensive measures and detection strategies:

- Conditionally import runtime/trace and restrict endpoint
- Use service mesh like Istio to secure internal paths
- Detect trace downloads via access logs

## Objectives

1. Record runtime execution events
2. Visualize goroutine and syscall behavior
3. Gather data for performance or exploit analysis

## Instructions

### Step 1: Download Trace File

**Context**: Retrieve the binary trace.

**Command** ([[commands/curl-download-execution-trace]]):
```bash
curl -o trace.out https://influxdb.quality.gitlab.net/debug/pprof/trace
```

> Downloads the trace; confirm with file trace.out showing data format.

### Step 2: View Trace (Optional)

**Context**: Analyze the trace events.

**Command** ([[commands/go-tool-trace-view]]):
```bash
go tool trace trace.out
```

> Launches trace viewer; output displays timelines of goroutines, syscalls, and blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-download-execution-trace]]
- [[commands/go-tool-trace-view]]

## Tools Used

- [[tools/go-tool-trace]]

## Tags

- [[information-disclosure]]
- [[execution-trace]]
- [[runtime-analysis]]
