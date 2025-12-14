---
id: uuid-for-chain
tags:
  - rce
  - memory-corruption
  - underflow
  - counter-strike
  - gaming
  - rop
type: attack_chain
tools:
  - '[[tools/AMX-Mod-X]]'
  - '[[tools/AMXX-Compiler]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Windows
  - Gaming (Counter-Strike 1.6)
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Malicious-CS-Server-with-AMXX]]'
  - '[[procedures/Compile-and-Deploy-PoC-Plugin]]'
  - '[[procedures/Prepare-Crafted-Weapon-Sprite-File]]'
  - '[[procedures/Start-Malicious-CS-Dedicated-Server]]'
  - '[[procedures/Connect-Client-to-Trigger-RCE]]'
step_count: 5
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Process Injection]]'
updated_at: '2025-12-14T17:24:14.457Z'
description: >-
  Multi-stage attack exploiting an unchecked signed char weapon ID in the
  Counter-Strike 1.6 client to achieve remote code execution through memory
  corruption and ROP chaining.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Process Injection]]'
---
# Remote Code Execution in Counter-Strike 1.6 Client via WeaponList Underflow

Multi-stage attack chain demonstrating exploitation of an array index underflow in the WeaponList message parser of the Counter-Strike 1.6 client, leading to arbitrary memory overwrite and remote code execution. The attack leverages a malicious server to send crafted messages that corrupt the gEngfuncs function table, chaining ROP gadgets to execute arbitrary code like launching calc.exe on the victim client.

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
    A[Set Up Server] --> B[Compile Plugin]
    B --> C[Prepare Sprites]
    C --> D[Start Server]
    D --> E[Client Connection and RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/AMX-Mod-X]]
- [[tools/AMXX-Compiler]]
- Counter-Strike 1.6 dedicated server binaries
- Counter-Strike 1.6 client

### Target Environment

- Windows OS
- Counter-Strike 1.6 game environment (HLSDK-based)
- Network access to host a public server

### Initial Access Requirements

- Administrative access to a Windows machine for server setup
- Victim must connect to the malicious server using a vulnerable CS 1.6 client
- No prior credentials needed; exploitation occurs on connection

## Detailed Attack Procedures

### Step 1: Set Up Malicious CS Server
procedure: [[procedures/Set-Up-Malicious-CS-Server-with-AMXX]]

**Objective**: Establish the server environment to host the exploit plugin.

**Instructions**: Install the Counter-Strike 1.6 dedicated server and integrate AMX Mod X for plugin support. Download and extract the CS server files, then install AMX Mod X by copying its modules to the appropriate directories.

**Expected Output**: Functional CS dedicated server with AMX Mod X loaded.

**Success Indicators**:
- Server starts without errors
- AMX Mod X logs show successful initialization

### Step 2: Compile and Deploy PoC Plugin
procedure: [[procedures/Compile-and-Deploy-PoC-Plugin]]

**Objective**: Create and enable the malicious plugin that sends crafted WeaponList messages.

**Instructions**: Use the AMXX compiler to build the poc_calc_pop.sma script into a .amxx file, then place it in the plugins folder and add it to plugins.ini.

**Expected Output**: Compiled .amxx plugin loaded by the server.

**Success Indicators**:
- Compilation succeeds without errors
- Plugin appears in server logs on startup

### Step 3: Prepare Crafted Weapon Sprite File
procedure: [[procedures/Prepare-Crafted-Weapon-Sprite-File]]

**Objective**: Create the sprite file containing data for memory overwrite in the WEAPON struct.

**Instructions**: Generate weapon_pwn.txt with specific binary data targeting memory addresses, and place it in the cstrike/sprites folder.

**Expected Output**: Sprite file ready for server use in exploitation.

**Success Indicators**:
- File is correctly placed and readable by the server
- No file permission issues

### Step 4: Start Malicious CS Dedicated Server
procedure: [[procedures/Start-Malicious-CS-Dedicated-Server]]

**Objective**: Launch the server to load the plugin and prepare for client connections.

**Instructions**: Execute the server binary with appropriate configuration to bind to a port and load the malicious setup.

**Expected Output**: Server running and accepting connections.

**Success Indicators**:
- Server console shows 'Server running'
- Plugin is active in the modules list

### Step 5: Connect Client to Trigger RCE
procedure: [[procedures/Connect-Client-to-Trigger-RCE]]

**Objective**: Induce the client to connect and receive crafted messages leading to code execution.

**Instructions**: Launch the CS 1.6 client and connect to the malicious server IP. Upon connection, the plugin sends the exploited messages.

**Expected Output**: calc.exe launches on the client machine.

**Success Indicators**:
- Client connects successfully
- calc.exe window appears (or other executed payload)

## Attack Chain Summary

### Key Achievements

1. Successful server setup with exploit infrastructure
2. Memory corruption via underflow in WeaponList parser
3. ROP chain execution for arbitrary code on client

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Process Injection]] Process Injection

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
