---
tags:
  - curl
  - recon
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-version-check]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:26:06.314Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e2f223d8-5e63-4945-aa7f-c1057db24dff
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Verify-Curl-Version-and-Globbing-Support

## Summary

This procedure checks the installed curl version and supported features to confirm compatibility for URL globbing exploitation, ensuring the environment supports file protocol and globbing for subsequent bypass attacks.

## Description

In attack scenarios targeting systems with curl, verifying the version is crucial as globbing (enabled by default in versions like 7.83.1) allows URL pattern expansion. This step identifies if the target supports protocols like file:// and features like UnixSockets, setting the stage for LFI or SSRF via crafted URLs. It assumes local shell access on a Linux system.

## Requirements

1. Local shell access on Linux
2. Installed curl binary (e.g., version 7.83.1)
3. No elevated privileges needed

## Defense

Defensive measures and detection strategies:

- Monitor curl executions via process auditing (e.g., auditd on Linux)
- Restrict curl usage in security-sensitive applications
- Use wrapper scripts to disable globbing with --globoff flag

## Objectives

1. Confirm curl version and protocol support
2. Verify globbing feature availability
3. Establish baseline for exploitation feasibility

## Instructions

### Step 1: Execute Version Check

**Context**: Run the version command to output curl details, including supported protocols and features, confirming the environment is suitable for globbing-based attacks.

**Command** ([[commands/curl-version-check]]):
```bash
./curl -Version
```

> This command displays the curl and libcurl versions, release date, supported protocols (e.g., file, http), and features (e.g., globbing via URL expansion). Expected output includes: "curl 7.83.1 (x86_64-pc-linux-gnu) libcurl/7.83.1 ... Protocols: dict file ftp ... Features: ... UnixSockets".

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/curl-version-check]]

## Tools Used

- [[tools/curl]]

## Tags

- curl
- recon
