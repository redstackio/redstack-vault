---
tags:
  - cipher-analysis
  - ssl-tls
  - smtp
type: procedure
tools:
  - '[[tools/sslyze]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/sslyze-analyze-smtp]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:31:11.056Z'
sub_techniques: []
id: 4944ed94-25ff-4419-8dd1-396b43a4fd74
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Analyze-SMTP-Cipher-Suites-with-Sslyze

## Summary

This procedure employs sslyze to examine cipher suites, certificates, and vulnerabilities on SMTP services using STARTTLS, confirming anonymous ciphers for MITM risks.

## Description

For apps.owncloud.com:587, it listed AECDH-AES256-SHA and ADH-AES256-SHA as supported, along with self-signed cert issues and renegotiation vulnerabilities. Ideal for detailed post-scan analysis. Requires Python and sslyze.

## Requirements

1. Sslyze installed (Python-based)
2. Target domain/port accessible
3. STARTTLS support on target service

## Defense

Defensive measures and detection strategies:

- Restrict ciphers to authenticated-only in config
- Monitor for sslyze-like probes via logs
- Implement certificate validation in clients

## Objectives

1. List all supported cipher suites
2. Identify anonymous and weak ciphers
3. Assess certificate trust and other flaws

## Instructions

### Step 1: Run Sslyze on SMTP

**Context**: Scan with STARTTLS to analyze ciphers.

**Command** ([[commands/sslyze-analyze-smtp]]):
```bash
./sslyze.py --regular apps.owncloud.com:587 --starttls=smtp
```

> Outputs ciphers (e.g., anonymous listed), cert details (self-signed), and vulnerabilities like client renegotiation.

### Step 2: Validate Anonymous Support

**Context**: Check for aNULL ciphers in results.

**Command** (No execution; parse):

> Success if anonymous ciphers appear; indicates MITM feasibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Identify Business Context

### Sub-Techniques

- None

## Commands Used

- [[commands/sslyze-analyze-smtp]]

## Tools Used

- [[tools/sslyze]]

## Tags

- [[cipher-analysis]]
- [[ssl-tls]]
- [[smtp]]
