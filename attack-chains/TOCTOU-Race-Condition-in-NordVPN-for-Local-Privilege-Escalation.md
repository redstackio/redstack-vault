---
tags:
  - race-condition
  - toctou
  - privilege-escalation
  - nordvpn
  - openvpn
  - dll-loading
  - ntfs-locks
type: attack_chain
tools:
  - '[[tools/BaitAndSwitch]]'
  - '[[tools/Invoke-ExploitNordVPNConfigLPE]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Supply-Arbitrary-Path-via-ServerDomain-Parameter]]'
  - '[[procedures/Trigger-OpenVPN-Configuration-Validation]]'
  - '[[procedures/Exploit-TOCTOU-Race-Condition-with-BaitAndSwitch]]'
  - '[[procedures/Launch-OpenVPN-with-Swapped-Malicious-Configuration]]'
  - '[[procedures/Execute-Arbitrary-Commands-as-SYSTEM-via-Exploit-Module]]'
step_count: 5
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[T1068.001]]'
  - '[[Hijack Execution Flow]]'
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:29:28.623Z'
description: >-
  Exploits a time-of-check-to-time-of-use race condition in the NordVPN Windows
  service to swap OpenVPN configuration files and load an arbitrary DLL with
  SYSTEM privileges, enabling local privilege escalation.
id: b68cdd65-89f4-4f77-9ad2-3d5d824216b8
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[T1068.001]]'
  - '[[Hijack Execution Flow]]'
  - '[[DLL Search Order Hijacking]]'
---
# TOCTOU Race Condition in NordVPN for Local Privilege Escalation

Multi-stage attack chain demonstrating a complete local privilege escalation workflow via a race condition in the NordVPN Windows service.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~2-5 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | Critical |

## Attack Flow Visualization

```mermaid
graph LR
    A[Supply Arbitrary Path] --> B[Trigger Validation]
    B --> C[Exploit Race Condition]
    C --> D[Launch OpenVPN with Malicious Config]
    D --> E[Execute Commands as SYSTEM]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/BaitAndSwitch]]
- [[tools/Invoke-ExploitNordVPNConfigLPE]]

### Target Environment

- Windows OS (tested on Windows 10/11)
- NordVPN service running as SYSTEM
- Local low-privileged user access
- OpenVPN and WCF (Windows Communication Foundation) components installed via NordVPN

### Initial Access Requirements

- Local user account with ability to interact with NordVPN service
- No network access required; fully local attack
- NordVPN version vulnerable to CVE-2019-17565 or similar (pre-mitigation)

## Detailed Attack Procedures

### Step 1: Supply Arbitrary Path
procedure: [[procedures/Supply-Arbitrary-Path-via-ServerDomain-Parameter]]

**Objective**: Control the OpenVPN configuration file path by injecting an arbitrary path through the ServerDomain parameter in the VpnConnectionProxy WCF model.

**Instructions**: Use the NordVPN client or direct WCF interaction to pass a controlled path via the ServerDomain parameter. The service uses Path.Combine to build the full config path, allowing directory traversal or arbitrary location specification.

**Expected Output**: The service accepts the parameter and proceeds to construct the path without immediate rejection.

**Success Indicators**:
- Parameter accepted in WCF call
- Config path logged or verifiable in service traces

### Step 2: Trigger Validation
procedure: [[procedures/Trigger-OpenVPN-Configuration-Validation]]

**Objective**: Force the NordVPN service to validate the benign configuration file at the supplied path before the race window opens.

**Instructions**: Initiate a VPN connection attempt through the NordVPN interface or API, which triggers the service to check the config file's validity (e.g., syntax and allowed options) without launching OpenVPN yet.

**Expected Output**: Validation passes for the initial benign file, with service logs indicating successful parse.

**Success Indicators**:
- Service logs show config validation success
- No errors in OpenVPN config parsing

### Step 3: Exploit Race Condition
procedure: [[procedures/Exploit-TOCTOU-Race-Condition-with-BaitAndSwitch]]

**Objective**: Use NTFS opportunistic locks to detect file access during the time gap and swap the validated benign config with a malicious one containing an OpenSSL engine directive.

**Instructions**: Deploy [[tools/BaitAndSwitch]] to monitor the target file path. Upon detecting the service's read access for validation, replace the file with a new config that includes `engine dynamic_path:/path/to/malicious.dll` to load an arbitrary DLL.

**Expected Output**: File swap completes within the race window, undetected by the service.

**Success Indicators**:
- BaitAndSwitch logs confirm file access detection and swap
- Original file restored or backed up post-swap

### Step 4: Launch OpenVPN
procedure: [[procedures/Launch-OpenVPN-with-Swapped-Malicious-Configuration]]

**Objective**: Have the NordVPN service launch OpenVPN with the swapped malicious config, causing it to load the arbitrary DLL via OpenSSL engine as SYSTEM.

**Instructions**: The service automatically proceeds to start OpenVPN after validation. Monitor process creation to confirm OpenVPN.exe launches with the tampered config path.

**Expected Output**: OpenVPN process starts, loads the DLL, and executes the injected code with SYSTEM privileges.

**Success Indicators**:
- OpenVPN process observed running as SYSTEM
- DLL execution confirmed via process monitoring or callbacks

### Step 5: Execute Arbitrary Commands
procedure: [[procedures/Execute-Arbitrary-Commands-as-SYSTEM-via-Exploit-Module]]

**Objective**: Leverage the escalated privileges to run commands like adding a backdoor user to the administrators group.

**Instructions**: Import the exploit module and invoke it with payload commands. For example, use [[commands/import-module-invoke-exploitnordvpnconfiglpe]] followed by [[commands/invoke-exploitnordvpnconfiglpe-add-backdoor-user]] and [[commands/net-localgroup-administrators-backdoor-add]].

```powershell
Import-Module .\Invoke-ExploitNordVPNConfigLPE.psd1
Invoke-ExploitNordVPNConfigLPE "net user backdoor P@ssword /add" "net localgroup administrators backdoor /add"
```

**Expected Output**: Commands execute successfully, creating the backdoor account.

**Success Indicators**:
- New user 'backdoor' added and elevated to admins
- Login with backdoor/P@ssword grants admin access

## Attack Chain Summary

### Key Achievements

1. Bypassed path validation in NordVPN service via arbitrary ServerDomain input
2. Exploited TOCTOU gap using NTFS locks to inject malicious OpenVPN config
3. Achieved arbitrary DLL execution as SYSTEM through OpenSSL engine directive
4. Demonstrated full local privilege escalation by adding persistent admin user

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[T1068.001]] Exploitation for Privilege Escalation: Vulnerability in Software
- [[Hijack Execution Flow]] Hijack Execution Flow
- [[DLL Search Order Hijacking]] DLL Search Order Hijacking

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
