---
id: ac-cisco-ios-bypass-escalation-001
tags:
  - cve-2023-20198
  - cve-2023-20273
  - auth-bypass
  - rce
  - privilege-escalation
  - cisco-ios
  - network-device
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/exploit.py]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Network Device
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Reconnaissance-and-Target-Identification-on-MTN-Domains]]'
  - '[[procedures/Fuzzing-Web-UI-Path-Bypass-with-Burp-Suite]]'
  - >-
    [[procedures/Exploiting-Auth-Bypass-for-Command-Execution-and-User-Creation]]
  - '[[procedures/Privilege-Escalation-to-Linux-Root-via-CVE-2023-20273]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:24:44.960Z'
description: >-
  Multi-stage attack exploiting CVE-2023-20198 for auth bypass in Cisco IOS XE
  web UI, enabling arbitrary command execution and config changes, followed by
  CVE-2023-20273 for root escalation on the underlying Linux OS.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Cisco IOS XE Authentication Bypass and Root Privilege Escalation via Web UI Path Traversal

Multi-stage attack chain demonstrating exploitation of CVE-2023-20198 in Cisco IOS XE Software's web UI for authentication bypass, allowing arbitrary IOS command execution and configuration changes with Privilege 15, followed by escalation to Linux root via CVE-2023-20273 for malware implantation. The attack begins with reconnaissance on MTN Group's domains, fuzzing to bypass Nginx path filtering, and culminates in full system compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Path Bypass Fuzzing]
    B --> C[Auth Bypass and RCE]
    C --> D[Privilege Escalation]
    D --> E[Malware Implantation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/exploit.py]]

### Target Environment

- Cisco IOS XE Software (version 16.6.x or vulnerable releases)
- Web UI enabled on HTTP/HTTPS (typically port 443)
- Nginx as reverse proxy for webui_wsma_http endpoint
- Underlying Linux OS for escalation

### Initial Access Requirements

- Network access to the target's web UI
- No prior credentials needed due to auth bypass
- Ability to perform HTTP requests and fuzzing

## Detailed Attack Procedures

### Step 1: Reconnaissance and Target Identification
procedure: [[procedures/Reconnaissance-and-Target-Identification-on-MTN-Domains]]

**Objective**: Identify vulnerable Cisco IOS XE instances through domain reconnaissance and search queries.

**Instructions**: Log into any accessible application or portal and perform a search for target-related terms like 'MTN Innovation Centre' to discover associated domains. Manually inspect results to identify redacted hostnames owned by entities like MTN Cameroon.

**Expected Output**: List of potential target domains, including the vulnerable Cisco device hostname.

**Success Indicators**:
- Target domain confirmed (e.g., redacted hostname resolving to Cisco IOS XE web UI)
- No authentication barriers to initial search

### Step 2: Fuzzing Web UI Path Bypass
procedure: [[procedures/Fuzzing-Web-UI-Path-Bypass-with-Burp-Suite]]

**Objective**: Bypass Nginx filtering on the web UI to access unauthenticated SOAP endpoints like webui_wsma_http.

**Instructions**: Use [[tools/Burp-Suite]] to intercept requests to the web UI. Send to Repeater for manual path manipulation testing, then to Intruder for fuzzing with payloads like black box characters (e.g., '../' or null bytes) to traverse paths and reach wsma-exec or wsma-config endpoints.

**Expected Output**: Successful bypass response from the unfiltered endpoint, indicating access without auth.

**Success Indicators**:
- 200 OK or SOAP response from wsma-http without login prompt
- Fuzzing reveals vulnerable path (e.g., /webui/logoutconfirm.html%00../wsma/device)

### Step 3: Exploiting Auth Bypass for Command Execution and User Creation
procedure: [[procedures/Exploiting-Auth-Bypass-for-Command-Execution-and-User-Creation]]

**Objective**: Execute arbitrary IOS commands and modify configurations to create a Privilege 15 user.

**Instructions**: Verify vulnerability using [[commands/exploit-check]]:

```bash
exploit.py -t <target-hostname> -c
```

Then dump configuration with [[commands/exploit-dump-config]]:

```bash
exploit.py -t <target-hostname> -g
```

Use the wsma-config endpoint to add a new user 'baduser' with Privilege 15 via the exploit script.

**Expected Output**: Vulnerability confirmed (Vulnerable: True, IOS version details); config dump showing sensitive data like enable secrets; new user created successfully.

**Success Indicators**:
- Arbitrary command output received (e.g., 'sh run' config)
- New privileged user added and verifiable

### Step 4: Privilege Escalation to Linux Root
procedure: [[procedures/Privilege-Escalation-to-Linux-Root-via-CVE-2023-20273]]

**Objective**: Escalate from the created IOS privileged user to root on the underlying Linux OS for full compromise.

**Instructions**: Leverage the new local user account to exploit CVE-2023-20273 in the Web UI feature, elevating privileges and implanting malware on the Linux host.

**Expected Output**: Root shell access or malware persistence confirmed on the device.

**Success Indicators**:
- Root access granted on Linux OS
- Malware implanted and executing

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication to execute IOS commands and expose configs
2. Created persistent privileged access via user addition
3. Escalated to root for complete device compromise and malware deployment

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unix Shell]] Unix Shell
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
