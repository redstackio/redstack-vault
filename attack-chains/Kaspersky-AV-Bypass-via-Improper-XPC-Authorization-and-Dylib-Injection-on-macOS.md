---
id: ac-kaspersky-xpc-bypass-001
tags:
  - av-bypass
  - xpc
  - dylib-injection
  - macos
  - kaspersky
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
  - '[[Defense Evasion]]'
verified: false
platforms:
  - macOS
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Identify-and-Analyze-XPC-Service]]'
  - '[[procedures/Prepare-Vulnerable-Installer]]'
  - '[[procedures/Create-Custom-Dylib-Proxy]]'
  - '[[procedures/Execute-Dylib-Injection-and-XPC-Connection]]'
  - '[[procedures/Verify-AV-Bypass-Effect]]'
step_count: 5
techniques:
  - '[[Hijack Execution Flow]]'
  - '[[Dynamic-link Library Injection]]'
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:29:10.027Z'
description: >-
  Multi-stage attack exploiting improper client authorization in Kaspersky
  Internet Security's XPC service and insecure entitlements in an old installer
  to inject code and disable AV protections as a normal user.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
  - '[[Dynamic-link Library Injection]]'
  - '[[Disable or Modify Tools]]'
---
# Kaspersky AV Bypass via Improper XPC Authorization and Dylib Injection on macOS

Multi-stage attack chain demonstrating exploitation of Kaspersky Internet Security (KIS) on macOS Big Sur, where improper Team ID verification in the XPC service allows unauthorized connections, combined with dylib proxying in an old installer version (20.0.0.829) to inject code and control AV functions like disabling read-only volume scans. This leads to full AV bypass and potential local privilege escalation as a normal user.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify XPC Service] --> B[Prepare Installer]
    B --> C[Create Dylib Proxy]
    C --> D[Inject and Connect XPC]
    D --> E[Verify Bypass]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Xcode or similar for compiling dylibs
- codesign for signing binaries

### Target Environment

- macOS Big Sur or compatible
- Kaspersky Internet Security installed (any version post-installer exploitation)
- Access to download old KIS installer (20.0.0.829)

### Initial Access Requirements

- Local user access on target macOS machine
- No elevated privileges required initially
- Internet access to download installer

## Detailed Attack Procedures

### Step 1: Identify and Analyze XPC Service
procedure: [[procedures/Identify-and-Analyze-XPC-Service]]

**Objective**: Locate the Mach service name and verify the authorization flaw in the XPC handler to confirm exploitability.

**Instructions**: Examine the system extension's Info.plist for the NEMachServiceName and disassemble the shouldAcceptNewConnection method to identify the weak Team ID check.

**Expected Output**: Mach service name '2Y8XE5CQ94.com.kaspersky.kav.sysext' and confirmation of insufficient verification (only processIdentifier compared to Team ID string).

**Success Indicators**:
- Service name extracted
- Authorization flaw confirmed via disassembly

### Step 2: Prepare Vulnerable Installer
procedure: [[procedures/Prepare-Vulnerable-Installer]]

**Objective**: Download and verify the old KIS installer with insecure entitlements to enable dylib injection.

**Instructions**: Download the specific DMG file and mount it, then use [[commands/list-macos-directory]] to inspect contents and confirm entitlements via codesign.

```bash
ls -l /Volumes/Kaspersky Internet Security/Kaspersky Downloader.app/Contents/MacOS
codesign -d --entitlements :- /Volumes/Kaspersky Internet Security/Kaspersky Downloader.app
```

**Expected Output**: Listing shows libkl_appkit.dylib; entitlements include com.apple.security.cs.disable-library-validation set to true.

**Success Indicators**:
- Installer mounted successfully
- Entitlements verified for injection

### Step 3: Create Custom Dylib Proxy
procedure: [[procedures/Create-Custom-Dylib-Proxy]]

**Objective**: Compile and prepare a proxy dylib that reexports original symbols and injects XPC connection code.

**Instructions**: Rename original dylib, compile custom one with constructor for XPC setup, sign it, and replace in the app bundle.

**Expected Output**: Custom libkl_appkit.dylib placed in the MacOS directory, signed and ready.

**Success Indicators**:
- Dylib compiles without errors
- Reexports match original symbols

### Step 4: Execute Dylib Injection and XPC Connection
procedure: [[procedures/Execute-Dylib-Injection-and-XPC-Connection]]

**Objective**: Run the modified installer to load the proxy dylib and establish unauthorized XPC connection to control AV.

**Instructions**: Copy modified app to /Users/Shared, execute it to trigger dylib load, which connects to XPC service and invokes DisableReadonlyVolumeScan:1.

**Expected Output**: XPC connection established; method invoked successfully.

**Success Indicators**:
- Installer runs and loads custom dylib
- No crashes during injection

### Step 5: Verify AV Bypass Effect
procedure: [[procedures/Verify-AV-Bypass-Effect]]

**Objective**: Confirm the AV function disable via logs and observe impact on protections.

**Instructions**: Monitor system logs for confirmation message from com.kaspersky.kav.sysext.

**Expected Output**: Log entry 'FileMonitor: disabling read-only volume scan'.

**Success Indicators**:
- Log confirms disable
- AV scan protections bypassed (e.g., test with read-only volume)

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to KIS XPC service via weak authorization
2. Code injection into installer process using insecure entitlements
3. Full control over AV functions, disabling key scans as normal user
4. Potential for local privilege escalation through AV bypass

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow (dylib proxying)
- [[Dynamic-link Library Injection]] Dynamic-link Library Injection (dylib injection)
- [[Disable or Modify Tools]] Disable or Modify Tools (AV function disable)

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Defense Evasion]] Defense Evasion

---
*Last updated: 2023-10-01T12:00:00Z*
