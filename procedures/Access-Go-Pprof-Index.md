---
tags:
  - information-disclosure
  - pprof
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-pprof-index]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:17.244Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e53537e5-d16a-4217-8fbd-2a7b96903b72
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Access-Go-Pprof-Index

## Summary

This procedure accesses the main Go pprof debugging endpoint to retrieve an index of available runtime profiles, enabling attackers to identify and target specific types of sensitive internal data without authentication.

## Description

In scenarios where Go applications like InfluxDB expose pprof endpoints publicly, navigating to /debug/pprof reveals a listing of profiles such as allocs, heap, and goroutines. This disclosure provides an entry point for deeper runtime reconnaissance, potentially revealing application internals on Kubernetes-hosted services. Prerequisites include public access to the target URL; no credentials are needed due to the misconfiguration.

## Requirements

1. Network access to the target InfluxDB instance (e.g., https://influxdb.quality.gitlab.net)
2. HTTP client like curl installed
3. Basic understanding of Go runtime profiling

## Defense

Defensive measures and detection strategies:

- Disable or restrict pprof endpoints in production (e.g., via Go flags like -pprof=false or firewall rules)
- Implement authentication/authorization on debug paths using reverse proxies like Nginx
- Monitor access logs for /debug/pprof requests and alert on anomalous patterns

## Objectives

1. Enumerate available pprof profiles for targeted information gathering
2. Confirm unauthenticated access to runtime debugging features
3. Gather initial insights into the target's Go application structure

## Instructions

### Step 1: Fetch Pprof Index

**Context**: This step retrieves the pprof index page, listing all exposable profiles.

**Command** ([[commands/curl-access-pprof-index]]):
```bash
curl https://influxdb.quality.gitlab.net/debug/pprof
```

> This command sends a GET request to the pprof root endpoint. Expected output is a plain text or HTML list of profiles (e.g., "allocs		Profile of memory allocations by function"), confirming exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-access-pprof-index]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[pprof]]
- [[Reconnaissance]]
