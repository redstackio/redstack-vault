---
tags:
  - go
  - http-server
  - poc
type: procedure
tools:
  - '[[tools/Go]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/go-run-burp-pckt-burst-memspy]]'
verified: false
platforms:
  - Linux
  - Desktop
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:22.437Z'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
id: 85b62453-f9f8-4249-9723-062ed0e394ac
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Build-and-Run-Custom-Go-HTTP-Server-for-Request-Bursting

## Summary

This procedure constructs and executes a Go-based HTTP server that accumulates connections (e.g., 20) before bursting responses with malformed Content-Length and doctype-starting bodies, reproducing race conditions in tools like Burp Suite.

## Description

The server listens on localhost:8000, handles /memspy endpoint by holding TCP connections until connLimit, then flushes HTTP/1.1 200 responses with Content-Length: -12000, custom headers, and random 1024-char bodies starting with '<!'. This targets Burp's proxy under load, causing async buffer races. Environment: Local dev setup with Go 1.18+. Outcomes: Controlled bursts for vuln repro, logs in hex for tracking.

## Requirements

1. Go runtime installed (go version >=1.18)
2. Basic Go knowledge for source editing (connLimit, random gen)
3. Local port 8000 free

## Defense

Defensive measures and detection strategies:

- Firewall local ports to prevent unauthorized access
- Validate Content-Length in proxies to reject negatives
- Monitor for bursty connection patterns in logs

## Objectives

1. Simulate concurrent malformed responses
2. Trigger client-side races reliably
3. Log bursts for analysis

## Instructions

### Step 1: Prepare Source Code

**Context**: Ensure burp-pckt-burst-memspy.go includes logic for connection counting, random body gen (a-z0-9), and burst on limit.

**Command** (Edit File):
```bash
# Assume source exists; edit connLimit := 20; body := "<!" + randString(1024) + ">"
```

> No execution; verify headers like Content-Type: text/html, malformed Length.

### Step 2: Compile and Run Server

**Context**: Start the server to listen and await connections.

**Command** ([[commands/go-run-burp-pckt-burst-memspy]]):
```bash
go run burp-pckt-burst-memspy.go
```

> Outputs server ready on 127.0.0.1:8000; logs hex counts (0.1.2...) and 'X' on flush. Expected: Handles bursts without crash.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/go-run-burp-pckt-burst-memspy]]

## Tools Used

- [[tools/Go]]

## Tags

- go
- poc-server
- bursting
