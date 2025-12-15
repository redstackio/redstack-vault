---
tags:
  - ios
  - pin-bypass
  - runtime-manipulation
  - objective-c
  - auth-bypass
  - debugger
type: attack_chain
tools:
  - '[[tools/SnoopIt]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - iOS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-and-Configure-SnoopIt-for-iOS-Analysis]]'
  - '[[procedures/Bypass-iOS-App-PIN-via-Runtime-Method-Invocation]]'
step_count: 7
techniques:
  - '[[Modify Authentication Process]]'
  - '[[Execution through API]]'
updated_at: '2025-12-14T17:28:20.216Z'
description: >-
  A multi-step attack exploiting the lack of anti-debugging protections in the
  Coinbase iOS app to bypass PIN authentication by attaching a runtime debugger
  and invoking an internal Objective-C method.
skill_level: intermediate
impact_level: high
id: 3a5ebe25-4da0-4386-a684-eba8047c4940
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
  - '[[Execution through API]]'
---
# Bypass Coinbase iOS App PIN Authentication via Runtime Manipulation with SnoopIt

Multi-stage attack chain demonstrating runtime manipulation of an iOS app to bypass local authentication mechanisms. This exploits the Coinbase app's lack of protections against debugger attachment, allowing unauthorized access to app features by directly invoking internal methods.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install SnoopIt] --> B[Configure for Coinbase App]
    B --> C[Set PIN in App]
    C --> D[Launch App and Trigger PIN]
    D --> E[Access SnoopIt Interface]
    E --> F[Navigate to Objective-C Classes]
    F --> G[Invoke userAuthenticated Method]
    G --> H[Bypass Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#3498db
    style G fill:#3498db
    style H fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/SnoopIt]]

### Target Environment

- iOS device (jailbroken, as root access is required for debugger attachment)
- Coinbase iOS app installed
- No specific services or ports; local device access only

### Initial Access Requirements

- Physical or remote access to a jailbroken iOS device
- App installed and functional
- No network credentials needed; operates locally

## Detailed Attack Procedures

### Step 1: Install SnoopIt
procedure: [[procedures/Install-and-Configure-SnoopIt-for-iOS-Analysis]]

**Objective**: Prepare the runtime analysis tool on the target iOS device.

**Instructions**: Install SnoopIt on the jailbroken iOS device. SnoopIt enables attachment to running app processes for inspection and manipulation.

**Expected Output**: SnoopIt installed and ready for configuration.

**Success Indicators**:
- Tool installation completes without errors
- Device confirms SnoopIt is accessible

### Step 2: Configure SnoopIt to Target Coinbase App
procedure: [[procedures/Install-and-Configure-SnoopIt-for-iOS-Analysis]]

**Objective**: Set up SnoopIt to monitor and control the Coinbase app process.

**Instructions**: In SnoopIt settings, select the Coinbase app as the target for runtime monitoring and control.

**Expected Output**: Coinbase app process attached and controllable via SnoopIt.

**Success Indicators**:
- Target app selected in tool interface
- No attachment errors reported

### Step 3: Set PIN in Coinbase App
procedure: [[procedures/Bypass-iOS-App-PIN-via-Runtime-Method-Invocation]]

**Objective**: Establish PIN protection as a prerequisite for bypass testing.

**Instructions**: Open the Coinbase app and configure a PIN for authentication.

**Expected Output**: App prompts for PIN on subsequent launches.

**Success Indicators**:
- PIN successfully set
- App requires PIN entry

### Step 4: Open Coinbase App to Trigger PIN Prompt
procedure: [[procedures/Bypass-iOS-App-PIN-via-Runtime-Method-Invocation]]

**Objective**: Initiate the authentication flow to prepare for manipulation.

**Instructions**: Launch the Coinbase app, which will display the PIN entry screen.

**Expected Output**: PIN prompt appears, blocking access.

**Success Indicators**:
- App launches and shows PIN screen
- Authentication is enforced

### Step 5: Access SnoopIt Controlled Window via Browser
procedure: [[procedures/Bypass-iOS-App-PIN-via-Runtime-Method-Invocation]]

**Objective**: Connect to the SnoopIt web-based interface for control.

**Instructions**: Browse to the SnoopIt control panel URL on the device or connected machine.

**Expected Output**: Web interface loads, showing attached app details.

**Success Indicators**:
- Interface accessible
- Coinbase app process visible

### Step 6: Navigate to Objective-C Classes in SnoopIt
procedure: [[procedures/Bypass-iOS-App-PIN-via-Runtime-Method-Invocation]]

**Objective**: Inspect runtime classes to identify manipulation targets.

**Instructions**: In the SnoopIt interface, navigate to the Objective-C classes section for the attached Coinbase process.

**Expected Output**: List of classes, including coinbase.CBPINViewController, displayed.

**Success Indicators**:
- Classes explorable
- Relevant controller class found

### Step 7: Invoke userAuthenticated Method
procedure: [[procedures/Bypass-iOS-App-PIN-via-Runtime-Method-Invocation]]

**Objective**: Simulate successful authentication to bypass the PIN screen.

**Instructions**: Locate and invoke the userAuthenticated method in the coinbase.CBPINViewController class without arguments.

**Expected Output**: PIN screen dismissed; app grants access to main features.

**Success Indicators**:
- Method call succeeds
- Unauthorized access achieved without entering PIN

## Attack Chain Summary

### Key Achievements

1. Attached debugger to running iOS app process without detection
2. Explored and manipulated Objective-C runtime classes
3. Bypassed local PIN authentication, enabling potential unauthorized transactions or data access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Modify Authentication Process]] Modify Authentication Process
- [[Execution through API]] Native API

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---

*Last updated: 2023-10-01T00:00:00Z*
