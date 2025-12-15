---
id: ac-source-engine-rce-544096
tags:
  - rce
  - source-engine
  - path-truncation
  - game-exploit
  - windows
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Windows
  - Source Engine
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Prepare-PoC-Files-for-Source-Engine-Exploit]]'
  - '[[procedures/Launch-Game-and-Load-Malicious-Map]]'
  - '[[procedures/Enable-Cheats-in-Source-Engine]]'
  - '[[procedures/Trigger-Mat-Crosshair-Edit-for-RCE]]'
step_count: 5
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:26:27.127Z'
description: >-
  Exploits improper input validation in the Source Engine's mat_crosshair_edit
  command to achieve remote code execution via path truncation in
  Counter-Strike: Source.
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Windows Command Shell]]'
---
# Source Engine Material Path Truncation for Remote Code Execution

Multi-stage attack chain demonstrating a complete attack workflow exploiting a buffer truncation vulnerability in the Source Engine to achieve remote code execution on Windows clients running Counter-Strike: Source.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare PoC] --> B[Launch Game]
    B --> C[Load Map]
    C --> D[Enable Cheats]
    D --> E[Trigger RCE]
    E --> F[Code Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on game installation and PoC files)

### Target Environment

- Windows OS
- Counter-Strike: Source installed via Steam (default path: C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Source)
- Source Engine version vulnerable to mat_crosshair_edit truncation

### Initial Access Requirements

- Victim must run the game and connect to a server or load a map with the malicious material
- Attacker provides PoC files (e.g., via download or server hosting)
- No prior credentials needed; exploits client-side processing

## Detailed Attack Procedures

### Step 1: Prepare PoC Files
procedure: [[procedures/Prepare-PoC-Files-for-Source-Engine-Exploit]]

**Objective**: Download and place the proof-of-concept files in the game's download directory to set up the malicious material that triggers path truncation.

**Instructions**: Download the PoC archive (F472693) and extract it to the game's download folder. This places a malicious .vmt file with a long path designed to truncate to .js extension, associated with Windows Script Host for RCE.

**Expected Output**: Files extracted to C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Source\cstrike\download\, including the aim_path map and malicious material.

**Success Indicators**:
- PoC files visible in the download directory
- No extraction errors

### Step 2: Launch Game and Load Map
procedure: [[procedures/Launch-Game-and-Load-Malicious-Map]]

**Objective**: Start Counter-Strike: Source and load the map containing the malicious material file to prepare for exploitation.

**Instructions**: Launch the game from Steam. Once in-game, open the console (~ key) and execute [[commands/map-aim-path]] to load the aim_path map.

```bash
map aim_path
```

Wait for the map to fully load.

**Expected Output**: Game loads the aim_path map without errors.

**Success Indicators**:
- Map loads successfully
- Malicious material is processed client-side

### Step 3: Enable Cheats
procedure: [[procedures/Enable-Cheats-in-Source-Engine]]

**Objective**: Enable cheat mode in the game server to unlock the vulnerable mat_crosshair_edit command.

**Instructions**: With the console open, execute [[commands/sv-cheats-1]] to enable cheats.

```bash
sv_cheats 1
```

**Expected Output**: Console confirms cheats are enabled.

**Success Indicators**:
- "sv_cheats 1" output in console
- No permission errors

### Step 4: Trigger Vulnerable Command
procedure: [[procedures/Trigger-Mat-Crosshair-Edit-for-RCE]]

**Objective**: Invoke the mat_crosshair_edit command, exploiting the 256-byte buffer truncation against Windows MAX_PATH (260 bytes) to execute a .js file instead of .vmt, leading to RCE via calc.exe.

**Instructions**: In the console, execute [[commands/mat-crosshair-edit]].

```bash
mat_crosshair_edit
```

The command attempts to load a material but truncates the path, changing the extension to .js and executing the payload.

**Expected Output**: Calculator (calc.exe) launches on the victim's machine, indicating successful RCE.

**Success Indicators**:
- External application (calc.exe) starts
- No game crash or error in console

## Attack Chain Summary

### Key Achievements

1. Bypasses input validation via path truncation in Source Engine
2. Achieves arbitrary command execution on Windows clients
3. Demonstrates RCE in a multiplayer game environment, though limited by server filters

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Windows Command Shell]] Windows Command Shell

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
