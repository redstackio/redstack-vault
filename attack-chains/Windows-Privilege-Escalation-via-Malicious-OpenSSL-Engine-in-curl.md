---
id: ac-curl-openssl-privesc-001
tags:
  - privilege-escalation
  - dll-injection
  - curl
  - openssl
  - windows-vulnerability
type: attack_chain
tools:
  - '[[tools/x86_64-w64-mingw32-gpp]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-OpenSSL-Configuration-Path]]'
  - '[[procedures/Build-and-Deploy-Malicious-DLL]]'
  - '[[procedures/Trigger-curl-Vulnerability]]'
step_count: 3
techniques:
  - '[[DLL Side-Loading]]'
  - '[[Dynamic-link Library Injection]]'
updated_at: '2025-12-14T17:29:44.254Z'
description: >-
  Multi-stage privilege escalation exploiting insecure OPENSSLDIR path in curl
  Windows binaries to load a malicious OpenSSL Engine DLL, enabling arbitrary
  code execution with the privileges of the running process.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Side-Loading]]'
  - '[[Dynamic-link Library Injection]]'
---
# Windows Privilege Escalation via Malicious OpenSSL Engine in curl

Multi-stage attack chain exploiting CVE-2019-5443 in curl version 7.65.1 on Windows 10, where an insecure OPENSSLDIR build parameter ('c:\usr\local\ssl') allows low-privileged users to create directories and place a malicious openssl.cnf file. This file loads a custom OpenSSL Engine DLL containing arbitrary code, resulting in code execution with the privileges of the user running curl. If curl is executed by a higher-privileged account, this enables privilege escalation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Configuration Path] --> B[Build Malicious DLL]
    B --> C[Trigger Execution]
    C --> D[Privilege Escalation]

    style A fill:#f39c12
    style B fill:#e67e22
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/x86_64-w64-mingw32-gpp]]
- Standard Windows command prompt access

### Target Environment

- Windows 10 (tested with curl 7.65.1)
- Low-privileged user account with write access to C:\ root
- curl.exe installed with vulnerable OPENSSLDIR ('c:\usr\local\ssl')
- No elevated privileges required for setup; escalation occurs on trigger

### Initial Access Requirements

- Local low-privileged access to the target Windows machine
- Ability to compile C code (cross-compilation environment)
- No network access needed

## Detailed Attack Procedures

### Step 1: Setup OpenSSL Configuration Path

procedure: [[procedures/Setup-OpenSSL-Configuration-Path]]

**Objective**: Create the directory structure matching curl's insecure OPENSSLDIR and place a malicious openssl.cnf to reference a custom OpenSSL Engine DLL.

**Instructions**: As a low-privileged user, create the directories using [[commands/mkdir-create-c-usr]]:

```cmd
mkdir c:\usr
```

Follow with [[commands/mkdir-create-c-usr-local]]:

```cmd
mkdir c:\usr\local
```

Then [[commands/mkdir-create-c-usr-local-ssl]]:

```cmd
mkdir c:\usr\local\ssl
```

Create a staging directory with [[commands/mkdir-create-c-stage]]:

```cmd
mkdir c:\stage
```

Manually create the malicious openssl.cnf in c:\usr\local\ssl\ with content specifying dynamic_path = c:\stage\calc.dll for the OpenSSL Engine.

**Expected Output**: Directories created; openssl.cnf file in place referencing the future DLL path.

**Success Indicators**:
- Directories exist under C:\usr\local\ssl
- openssl.cnf file is writable and correctly configured

### Step 2: Build and Deploy Malicious DLL

procedure: [[procedures/Build-and-Deploy-Malicious-DLL]]

**Objective**: Compile a malicious OpenSSL Engine DLL that executes arbitrary code (PoC: launches calculator) and place it in the referenced staging path.

**Instructions**: Compile the C source (calc.c with DllMain calling system("calc")) using [[tools/x86_64-w64-mingw32-gpp]] via [[commands/compile-calc-dll]]:

```bash
x86_64-w64-mingw32-g++ calc.c -o calc.dll -shared
```

Copy the DLL to the staging directory with [[commands/copy-calc-dll-to-stage]]:

```cmd
copy calc.dll c:\stage
```

**Expected Output**: calc.dll compiled and copied to c:\stage.

**Success Indicators**:
- DLL file exists in c:\stage
- DLL loads without errors (test with dependency walker if available)

### Step 3: Trigger curl Vulnerability

procedure: [[procedures/Trigger-curl-Vulnerability]]

**Objective**: Execute curl.exe to load the malicious openssl.cnf, which triggers the DLL load and arbitrary code execution.

**Instructions**: Run curl.exe (any command will do, e.g., curl --version) using [[commands/execute-curl-exe]]:

```cmd
curl.exe --version
```

This causes curl to load OpenSSL config from the insecure path, executing the DLL's code.

**Expected Output**: Arbitrary code runs (e.g., Windows calculator launches) with the privileges of the curl process.

**Success Indicators**:
- Calculator (or payload) executes
- If run as admin, confirms privilege escalation

## Attack Chain Summary

### Key Achievements

1. Exploited insecure build path in curl to allow low-priv user control over OpenSSL config
2. Loaded and executed malicious DLL via OpenSSL Engine mechanism
3. Achieved arbitrary code execution, enabling privilege escalation on admin-run curl

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[DLL Side-Loading]] DLL Side-Loading
- [[Dynamic-link Library Injection]] Dynamic-link Library Injection

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
