---
id: ac-goldsrc-spk-rce-001
name: RCE via Stack Buffer Overflow in GoldSrc 'spk' Console Command
type: attack_chain
description: >-
  A multi-stage exploit chain targeting a stack-based buffer overflow in the
  GoldSrc engine's 'spk' command to achieve remote code execution on Windows
  clients via a malicious configuration file.
verified: false
submitted: true
step_count: 4
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:37.286Z'
procedures:
  - '[[procedures/Exploit-GoldSrc-spk-Buffer-Overflow]]'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Windows Command Shell]]'
tactics:
  - '[[Execution]]'
tags:
  - rce
  - buffer-overflow
  - goldsrc
  - valve
  - game-engine
platforms:
  - Windows
  - Game Engine
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Windows Command Shell]]'
---

# RCE via Stack Buffer Overflow in GoldSrc 'spk' Console Command

Multi-stage attack chain demonstrating a complete attack workflow exploiting a buffer overflow in the GoldSrc engine to execute arbitrary code on the client machine.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Malicious CFG] --> B[Launch Game and Console]
    B --> C[Execute CFG for Overflow]
    C --> D[RCE Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on manual file creation and game client)

### Target Environment

- GoldSrc-based game (e.g., Half-Life)
- Windows OS
- Game installed and executable
- No specific ports or services required (client-side exploit)

### Initial Access Requirements

- Physical or remote access to place the .cfg file in the game's root directory
- Victim must launch the game
- No credentials needed beyond game access

## Detailed Attack Procedures

### Step 1: Prepare Malicious CFG File

procedure: [[procedures/Exploit-GoldSrc-spk-Buffer-Overflow]]

**Objective**: Craft a configuration file containing a long string in an 'spk' command to trigger the buffer overflow in VOX_GetDirectory.

**Instructions**: Create a file named `rce.cfg` in the game's root directory (e.g., `C:\Program Files\Half-Life\`). The file should contain a line like `spk <long_string_payload>` where the string exceeds 32 bytes to overflow the szpath buffer during memcpy in VOX_GetDirectory. For demonstration, use a payload that writes shellcode to execute calc.exe.

**Expected Output**: Malicious .cfg file ready in the game directory.

**Success Indicators**:
- File created and placed correctly
- Payload string length > 32 bytes verified

### Step 2: Launch Game and Open Console

procedure: [[procedures/Exploit-GoldSrc-spk-Buffer-Overflow]]

**Objective**: Start the vulnerable GoldSrc-based game and access the console to prepare for command execution.

**Instructions**: Launch the game executable (e.g., `hl.exe`). Once in-game, press the tilde key (`~`) to open the console.

**Expected Output**: Game running with console visible.

**Success Indicators**:
- Game launches without errors
- Console opens successfully

### Step 3: Execute Malicious CFG File

procedure: [[procedures/Exploit-GoldSrc-spk-Buffer-Overflow]]

**Objective**: Load and run the .cfg file via console to trigger the 'spk' command and cause the buffer overflow leading to RCE.

**Instructions**: In the console, enter the command to execute the file using [[commands/exec-game-config-file]]:

```bash
exec rce.cfg
```

This loads the 'spk' command from the .cfg, invoking VOX_LoadSound and VOX_GetDirectory, where memcpy copies the long path into the 32-byte szpath buffer without bounds checking.

**Expected Output**: The command executes, potentially crashing the game or silently overwriting stack memory with shellcode.

**Success Indicators**:
- Command accepted in console
- No immediate error; overflow occurs

### Step 4: Observe Exploitation Impact

procedure: [[procedures/Exploit-GoldSrc-spk-Buffer-Overflow]]

**Objective**: Verify RCE by observing arbitrary code execution on the client machine.

**Instructions**: After execution, monitor for signs of code execution, such as the Windows Calculator (calc.exe) popping up if the payload is a simple test.

**Expected Output**: calc.exe launches, confirming stack overflow led to control flow hijacking and shellcode execution.

**Success Indicators**:
- Calculator window appears
- Game may crash or hang due to overflow

## Attack Chain Summary

### Key Achievements

1. Successful placement and execution of malicious .cfg file
2. Triggering of buffer overflow in VOX_GetDirectory via unchecked memcpy
3. Achievement of arbitrary code execution (RCE) on the Windows client

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Windows Command Shell]] Windows Command Shell

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T12:00:00Z*
