---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - privilege-escalation
  - kernel
  - driver-installation
  - steam
  - remote-play
type: attack_chain
tools:
  - '[[tools/Steam]]'
  - '[[tools/SteamLink]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Prepare-Steam-Environment]]'
  - '[[procedures/Prepare-SteamLink-Device]]'
  - '[[procedures/Replace-Steam-Driver-Files]]'
  - '[[procedures/Initiate-Remote-Play-Connection]]'
  - '[[procedures/Authorize-Connection-and-Install-Malicious-Drivers]]'
step_count: 5
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Create or Modify System Process]]'
updated_at: '2025-12-14T17:29:36.157Z'
description: >-
  A multi-stage privilege escalation attack exploiting Steam's Remote Play
  feature on Windows 10 x64 by replacing legitimate driver files with malicious
  ones, resulting in the installation of arbitrary kernel-mode drivers and
  potential kernel-level code execution.
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Create or Modify System Process]]'
---
# Privilege Escalation via Steam Remote Play Driver Replacement Leading to Arbitrary Kernel Driver Installation

Multi-stage attack chain demonstrating a complete privilege escalation workflow in Steam's Remote Play feature on Windows 10 x64.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Environment] --> B[Replace Drivers]
    B --> C[Initiate Remote Play]
    C --> D[Authorize and Install]
    D --> E[Kernel Execution Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Steam]]
- [[tools/SteamLink]]

### Target Environment

- Windows 10 x64
- Steam installed and running
- Local network access for Remote Play
- Malicious driver files prepared (e.g., from fake_driver.zip)

### Initial Access Requirements

- Local user account on target Windows machine
- Valid Steam account credentials
- Android device on the same LAN

## Detailed Attack Procedures

### Step 1: Prepare Steam Environment
procedure: [[procedures/Prepare-Steam-Environment]]

**Objective**: Install and launch Steam to establish the baseline environment without triggering driver installation.

**Instructions**: Download and install Steam on the target Windows 10 x64 machine. Log in with a valid account. Verify in Device Manager (under Sound, video and game controllers) that Steam Streaming Microphone and Steam Streaming Speakers are not present, as they install only on first Remote Play use.

**Expected Output**: Steam running, no Remote Play drivers installed yet.

**Success Indicators**:
- Steam logged in successfully
- Device Manager shows no Steam audio devices

### Step 2: Prepare SteamLink Device
procedure: [[procedures/Prepare-SteamLink-Device]]

**Objective**: Set up a secondary device to initiate the Remote Play connection.

**Instructions**: Install the SteamLink app from the Google Play Store on an Android device connected to the same LAN. Log in using the same Steam account credentials.

**Expected Output**: SteamLink app ready for connection.

**Success Indicators**:
- App installed and logged in
- Device detects the host PC on the network

### Step 3: Replace Driver Files
procedure: [[procedures/Replace-Steam-Driver-Files]]

**Objective**: Swap legitimate driver files with malicious versions in the writable directory while Steam is running.

**Instructions**: With Steam running, navigate to `C:\Program Files (x86)\Steam\drivers\Windows10\x64`. Replace `SteamStreamingMicrophone.sys` and `SteamStreamingSpeakers.sys` with malicious files from `fake_driver.zip` (e.g., modified to 40KB and 8KB sizes). Ensure Steam is running to avoid auto-replacement on startup.

**Expected Output**: Directory contains modified driver files.

**Success Indicators**:
- File sizes changed (e.g., Microphone at 40KB, Speakers at 8KB)
- No integrity check triggered

### Step 4: Initiate Remote Play Connection
procedure: [[procedures/Initiate-Remote-Play-Connection]]

**Objective**: Start the Remote Play session from the secondary device to prepare for driver installation.

**Instructions**: From the Android SteamLink app, scan for and select the host PC running Steam. Initiate the Remote Play connection.

**Expected Output**: Connection request sent to the host PC.

**Success Indicators**:
- Host PC receives connection prompt
- No errors in connection initiation

### Step 5: Authorize Connection and Install Malicious Drivers
procedure: [[procedures/Authorize-Connection-and-Install-Malicious-Drivers]]

**Objective**: Approve the connection to trigger SteamServices to install the tampered drivers, achieving kernel-level execution.

**Instructions**: On the host PC, authorize the Remote Play connection in Steam. SteamServices will install the modified drivers without integrity verification.

**Expected Output**: Drivers installed; verify in Device Manager under Sound, video and game controllers that Steam Streaming Microphone (40KB) and Speakers (8KB) appear.

**Success Indicators**:
- Malicious drivers loaded in Device Manager
- Potential kernel code execution (e.g., via driver payload)

## Attack Chain Summary

### Key Achievements

1. Bypassed Steam's startup integrity checks by modifying files post-launch
2. Exploited writable driver directory for privilege escalation
3. Achieved arbitrary kernel-mode driver installation via legitimate Remote Play feature

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Create or Modify System Process]] Create or Modify System Process

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T12:00:00Z*
