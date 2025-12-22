---
tags:
  - information-disclosure
  - heap-profile
  - memory-allocation
type: procedure
tools:
  - '[[tools/go-tool-pprof]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-download-heap-profile]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Software]]'
updated_at: '2025-12-14T17:26:17.237Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a118835c-9c32-44a3-a724-f06a253bdf27
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Software]]'
---
# Download-Heap-Profile

## Summary

This procedure downloads a gzip-compressed heap profile from the InfluxDB pprof endpoint, sampling live memory allocations for offline analysis using tools like go tool pprof.

## Description

The /debug/pprof/heap endpoint provides a profile of object allocations in the Go heap, useful for identifying memory-intensive functions. In unauthenticated setups, this exposes potential leaks or configurations. Download the file for later inspection in Kubernetes-deployed Go apps.

## Requirements

1. Access to /debug/pprof/heap endpoint
2. curl for download
3. Go toolchain for analysis

## Defense

Defensive measures and detection strategies:

- Remove pprof import or set http.DefaultServeMux to exclude /heap
- Rate-limit or IP-whitelist debug endpoints
- Scan logs for heap profile requests

## Objectives

1. Obtain memory allocation profile
2. Enable analysis of heap usage
3. Identify potential memory-based attack vectors

## Instructions

### Step 1: Download Heap Profile

**Context**: Fetch the binary profile file.

**Command** ([[commands/curl-download-heap-profile]]):
```bash
curl -o heap.pprof.gz https://influxdb.quality.gitlab.net/debug/pprof/heap
```

> Saves the gzip file locally. Verify download with file heap.pprof.gz showing gzip format.

### Step 2: Analyze Profile (Optional)

**Context**: Use Go tool to inspect the profile.

**Command** ([[commands/go-tool-pprof-analyze]]):
```bash
go tool pprof heap.pprof.gz
```

> Interactive session shows top allocators; expected output includes call graphs and memory stats.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Software]] Gather Victim Host Information: Software

### Sub-Techniques


## Commands Used

- [[commands/curl-download-heap-profile]]
- [[commands/go-tool-pprof-analyze]]

## Tools Used

- [[tools/go-tool-pprof]]

## Tags

- [[information-disclosure]]
- [[heap-profile]]
- [[memory-allocation]]
