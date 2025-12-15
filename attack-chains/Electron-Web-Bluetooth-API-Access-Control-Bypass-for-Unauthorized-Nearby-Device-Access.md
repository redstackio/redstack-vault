---
tags:
  - electron
  - bluetooth
  - access-control-bypass
  - web-bluetooth-api
  - renderer-process
type: attack_chain
tools:
  - '[[tools/Electron]]'
  - '[[tools/electron-quick-start]]'
  - '[[tools/Developer-Tools]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Desktop
  - Electron
  - Windows
  - macOS
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Run-Vulnerable-Electron-Quick-Start-App]]'
  - '[[procedures/Request-Bluetooth-Device-via-Renderer-JS]]'
step_count: 2
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:36.013Z'
description: >-
  Demonstrates improper access control in Electron's Web Bluetooth API, allowing
  renderer processes to access nearby Bluetooth devices without permission using
  acceptAllDevices option.
skill_level: intermediate
impact_level: high
id: c9699156-6081-4f1e-a0c0-e9f183e68425
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
---
# Electron Web Bluetooth API Access Control Bypass for Unauthorized Nearby Device Access

Multi-stage attack chain demonstrating exploitation of improper access control in Electron's Web Bluetooth API, where renderer processes can bypass permission checks to gain read/write access to nearby Bluetooth devices using the acceptAllDevices option. This allows malicious content loaded in an Electron app to interact with user devices without consent, potentially leading to data theft or manipulation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Run Vulnerable Electron App] --> B[Execute JS in Renderer for Bluetooth Access]
    B --> C[Gain Unauthorized Device Read/Write Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Electron]]
- [[tools/electron-quick-start]]
- [[tools/Developer-Tools]]

### Target Environment

- Electron-based desktop application
- Vulnerable Electron version (e.g., before 17.0.0-alpha.6, 16.0.6, 15.3.5, 14.2.4, 13.6.6)
- Nearby Bluetooth devices discoverable
- No custom permission handlers in the app

### Initial Access Requirements

- Local machine with Node.js and Git installed
- Ability to run Electron apps
- Developer tools access in the renderer process

## Detailed Attack Procedures

### Step 1: Setup Vulnerable Electron Environment
procedure: [[procedures/Run-Vulnerable-Electron-Quick-Start-App]]

**Objective**: Launch a basic Electron application using a vulnerable version to create a renderer process susceptible to Bluetooth API exploitation.

**Instructions**: Clone the electron-quick-start repository and install dependencies using a vulnerable Electron version. Run the application to load the renderer process.

**Expected Output**: Electron app window opens with a basic HTML page, ready for developer tools interaction.

**Success Indicators**:
- Application launches without errors
- Renderer process is active and Bluetooth API is available

### Step 2: Bypass Permissions and Access Bluetooth Device
procedure: [[procedures/Request-Bluetooth-Device-via-Renderer-JS]]

**Objective**: Execute JavaScript in the renderer console to request access to nearby Bluetooth devices, bypassing expected permission checks.

**Instructions**: Open developer tools in the running Electron app and execute the Bluetooth request command in the console. The acceptAllDevices option forces acceptance of any nearby device without user selection or permission prompts.

**Expected Output**: Returns a BluetoothDevice object providing read/write access to a nearby device, instead of a permission denied error.

**Success Indicators**:
- No permission error thrown
- BluetoothDevice object returned with device details (e.g., name, ID)
- Ability to interact with device services

## Attack Chain Summary

### Key Achievements

1. Successfully run a vulnerable Electron app to expose the renderer process.
2. Bypassed Web Bluetooth API permission checks via JavaScript execution.
3. Gained unauthorized read/write access to nearby Bluetooth devices, enabling potential data exfiltration or manipulation.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T00:00:00Z*
