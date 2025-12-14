---
tags:
  - code-audit
  - open-source
  - flyte
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:53:38.197Z'
sub_techniques: []
id: 5fcbefb7-9207-4212-ad1c-f551565c7146
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Audit Flyte Open-Source Code

## Summary

This procedure details reviewing the open-source Flyte codebase on GitHub to identify vulnerabilities, specifically unauthenticated routes like the CORS proxy that enable SSRF.

## Description

Flyte's repository contains the console implementation. Attackers search for proxy logic in routes handling CORS bypasses, noting the absence of auth or URL validation. This audit reveals the SSRF flaw, allowing arbitrary server-side requests. Prerequisites include Git access; outcomes provide exploit paths for internal resource access.

## Requirements

1. Access to GitHub and ability to clone repositories
2. Basic knowledge of Go/Python web frameworks used in Flyte
3. Text editor or IDE for code searching

## Defense

Defensive measures and detection strategies:

- Conduct regular code reviews and SAST scans on open-source dependencies
- Restrict deployment of unpatched versions
- Monitor for code audit patterns in threat intel

## Objectives

1. Locate unauthenticated proxy routes in codebase
2. Confirm lack of input validation for requests
3. Document vulnerable endpoints for exploitation

## Instructions

### Step 1: Clone Repository

**Context**: Obtain the Flyte source code for local review.

Use git to clone: git clone https://github.com/flyteorg/flyte.git

> This pulls the full codebase including console components.

### Step 2: Search for Proxy Routes

**Context**: Identify CORS proxy implementations by searching for keywords like 'proxy', 'cors', 'fetch'.

Review files in the console directory, focusing on HTTP handlers that forward requests without checks.

> Note routes like /proxy that accept arbitrary URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[code-audit]]
- [[open-source]]
- [[flyte]]
