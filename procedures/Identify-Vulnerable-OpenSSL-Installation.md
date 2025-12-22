---
tags:
  - openssl
  - discovery
  - windows
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/check-openssl-version]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:26:17.504Z'
sub_techniques: []
id: 331e4373-86bf-4a6c-b924-ee8d52309451
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Identify Vulnerable OpenSSL Installation

## Summary

This procedure checks for vulnerable OpenSSL installations on Windows systems, focusing on versions 1.1.1, 1.1.0, or 1.0.2 built with mingw or Visual C, where the default OPENSSLDIR points to writable paths like C:/usr/local or C:/usr/local/ssl.

## Description

OpenSSL Windows builds often inherit Unix-like directory assumptions, leading to world-writable paths under C:\. This procedure verifies the version and config directory to confirm exploitability, enabling subsequent config injection for RCE. It targets local systems with low-privileged access and is a prerequisite for CVE-2019-1552 exploitation.

## Requirements

1. Local access to Windows command prompt (cmd.exe)
2. OpenSSL installed and in PATH
3. Low-privileged user account

## Defense

Defensive measures and detection strategies:

- Set proper ACLs on potential OPENSSLDIR paths to prevent writes by low-priv users
- Use custom --prefix during OpenSSL build with secure directories
- Monitor file creations/modifications in C:\usr\ paths via Windows auditing

## Objectives

1. Confirm vulnerable OpenSSL version and config path
2. Identify writable directories for injection
3. Validate target for full attack chain

## Instructions

### Step 1: Check OpenSSL Version and Config

**Context**: Retrieve detailed OpenSSL information to identify if the installation uses vulnerable defaults.

**Command** ([[commands/check-openssl-version]]):
```cmd
openssl version -a
```

> This command outputs the OpenSSL version, build details, and OPENSSLDIR. Look for versions 1.1.1, 1.1.0, or 1.0.2 and OPENSSLDIR like "C:/usr/local/ssl". If the path is writable (test with dir /q), it's vulnerable.

### Step 2: Verify Directory Writability

**Context**: Test if the OPENSSLDIR allows low-priv writes, confirming the root cause.

**Command** (built-in dir):
```cmd
dir "C:\usr\local\ssl" /q
```

> Expected output shows ownership and permissions; if writable by Everyone or low-priv users, proceed.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used

- [[commands/check-openssl-version]]

## Tools Used


## Tags

- [[openssl]]
- [[windows]]
- [[Discovery]]
