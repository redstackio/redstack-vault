---
tags:
  - buffer-overflow
  - rce
  - goldsrc
  - valve
  - bsp
  - game-exploit
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Windows
  - Game Engine (GoldSrc)
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-GoldSrc-Buffer-Overflow-with-Malformed-BSP]]'
step_count: 4
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[T1203.001]]'
updated_at: '2025-12-14T17:23:37.501Z'
description: >-
  A multi-stage attack exploiting a buffer overflow vulnerability in the GoldSrc
  engine's TEX_InitFromWad function to achieve remote code execution by loading
  a crafted malformed BSP map file in Valve games like Counter-Strike or Team
  Fortress Classic.
skill_level: intermediate
impact_level: high
id: 5b64ec3a-c1bb-48b6-93e5-882d1083e66a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[T1203.001]]'
---
# GoldSrc Engine RCE via Buffer Overflow in Malformed BSP File

Multi-stage attack chain demonstrating a complete attack workflow exploiting a buffer overflow in the GoldSrc engine to achieve arbitrary code execution on Windows machines running vulnerable Valve games.

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
    A[Prepare Malformed BSP] --> B[Deploy to Target Directory]
    B --> C[Launch Game and Load Map]
    C --> D[Execute Arbitrary Code]

    style A fill:#e74c3c
    style B fill:#f39c3c
    style C fill:#f39c12
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual file placement and game interaction)

### Target Environment

- Target OS/Platform: Windows
- Required services/ports: None (local file system access to game directories)
- Network access requirements: Local access to victim's machine or social engineering to place file

### Initial Access Requirements

- Credential requirements: User-level access to game installation directory
- Network position: Local or remote file drop (e.g., via shared folders or drive-by download)
- Prior access needed: Ability to place files in game maps directory (e.g., czero/maps, cstrike/maps, tfc/maps)

## Detailed Attack Procedures

### Step 1: Prepare and Place Malformed BSP File
procedure: [[procedures/Exploit-GoldSrc-Buffer-Overflow-with-Malformed-BSP]]

**Objective**: Craft and deploy a specially malformed BSP file to the game's maps directory to set up the buffer overflow trigger.

**Instructions**: Obtain or create a malformed BSP file (e.g., de_RCE.bsp) that exploits the buffer overflow in TEX_InitFromWad by providing a pszWadFile longer than 260 bytes. Copy the file to the appropriate game directory such as czero/maps, cstrike/maps, or tfc/maps.

**Expected Output**: Malformed BSP file successfully placed in the maps directory, ready for loading.

**Success Indicators**:
- File exists in target directory without errors
- No immediate crashes or detections during placement

### Step 2: Launch GoldSrc-Based Game and Open Console
procedure: [[procedures/Exploit-GoldSrc-Buffer-Overflow-with-Malformed-BSP]]

**Objective**: Start the vulnerable game and access the console to prepare for map loading.

**Instructions**: Launch a GoldSrc-based game such as Counter-Strike 1.6 or Team Fortress Classic. Once in-game, press the tilde key (~) to open the console.

**Expected Output**: Game window opens with console accessible.

**Success Indicators**:
- Game launches without issues
- Console opens (prompt appears)

### Step 3: Load the Malformed Map via Console
procedure: [[procedures/Exploit-GoldSrc-Buffer-Overflow-with-Malformed-BSP]]

**Objective**: Trigger the vulnerability by loading the crafted map, causing the buffer overflow during WAD file processing.

**Instructions**: In the console, enter the map load command using [[commands/map-load-game]] to process the BSP file:

```console
map de_RCE
```

**Expected Output**: The game attempts to load the map, processing the BSP and triggering the overflow in COM_FileBase copy to wadName buffer.

**Success Indicators**:
- Map loading initiates
- Buffer overflow occurs (potential crash or silent execution)

### Step 4: Observe Remote Code Execution
procedure: [[procedures/Exploit-GoldSrc-Buffer-Overflow-with-Malformed-BSP]]

**Objective**: Confirm successful exploitation through arbitrary code execution on the victim's machine.

**Instructions**: Monitor for the execution of embedded payload, such as the launch of calc.exe as a proof-of-concept.

**Expected Output**: Arbitrary code runs, e.g., Windows Calculator (calc.exe) pops up.

**Success Indicators**:
- calc.exe or specified payload executes
- No game crash preventing execution

## Attack Chain Summary

### Key Achievements

1. Successful placement of malformed BSP file in game directory
2. Triggering of buffer overflow via map load command
3. Achievement of remote code execution without additional privileges
4. Demonstration of RCE impact on Windows via game client

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[T1203.001]] Exploitation for Client Execution: Malicious File

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
