---
tags:
  - rce
  - info-leak
  - oob-read
  - aslr-bypass
  - rop
  - protobuf
  - csgo
  - source-engine
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/Python]]'
tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Windows
  - Linux
submitted: true
complexity: high
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Malicious-CS-GO-Server-with-Exploited-HTTP-Responses]]'
  - '[[procedures/Trigger-Client-Download-and-Info-Leak-via-Curl]]'
  - '[[procedures/Upload-and-Analyze-Leaked-Memory-Files-via-NETMsg_File]]'
  - '[[procedures/Spray-Heap-with-Sendprop-Objects-to-Enable-ASLR-Break]]'
  - '[[procedures/Parse-Leaked-Files-to-Extract-Engine-DLL-Base-Address]]'
  - '[[procedures/Set-Up-Fake-Objects-Using-Convars-for-OOB-Control]]'
  - '[[procedures/Trigger-OOB-Access-in-SplitScreen-to-Hijack-RIP]]'
  - '[[procedures/Execute-ROP-Chain-for-Arbitrary-Code-Execution]]'
step_count: 8
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic-link Library Injection]]'
  - '[[LSASS Memory]]'
updated_at: '2025-12-14T17:23:54.667Z'
description: >-
  Multi-stage exploit chain achieving remote code execution on CS:GO clients by
  leaking uninitialized heap memory through malformed HTTP headers and
  exploiting an out-of-bounds read in the SplitScreen protobuf message to bypass
  ASLR and hijack control flow.
skill_level: advanced
impact_level: critical
id: e13bedbd-a475-4713-9e23-a0d89832a0f2
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic-link Library Injection]]'
  - '[[LSASS Memory]]'
---
# CS:GO Client RCE via HTTP Content-Length Leak and OOB Access in SplitScreen Protobuf

Multi-stage attack chain exploiting vulnerabilities in CS:GO clients to achieve remote code execution from a malicious server. The chain combines an information disclosure via mishandled HTTP headers in curl-based downloads to leak heap memory and break ASLR, with an out-of-bounds read in the CSVCMsg_SplitScreen protobuf message to control pointers and execute a ROP chain.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 8 |
| Execution Time | ~5-10 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | Critical |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Malicious Server] --> B[Client Connects and Leaks Memory]
    B --> C[Upload and Parse Leak for ASLR Break]
    C --> D[Heap Spray and Fake Object Setup]
    D --> E[Trigger OOB for RIP Hijack]
    E --> F[Execute ROP Chain for RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#e67e22
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Python]]
- [[tools/curl]]

### Target Environment

- CS:GO client on Windows or Linux
- Network access to join custom servers (LAN or internet)
- Attacker controls a CS:GO dedicated server

### Initial Access Requirements

- Victim must connect to attacker's server via in-game console
- No credentials required; exploits client parsing logic
- Prior access: Attacker IP reachable by victim

## Detailed Attack Procedures

### Step 1: Set Up Malicious Server

procedure: [[procedures/Set-Up-Malicious-CS-GO-Server-with-Exploited-HTTP-Responses]]

**Objective**: Host custom files and prepare HTTP responses to trigger heap memory leak on client download.

**Instructions**: Use Python to launch the exploit server, configuring it to serve files with dual case-variant Content-Length headers.

**Expected Output**: Server listening on port 1337, ready for client connections.

**Success Indicators**:
- Server logs confirm HTTP response preparation with 'Content-Length: 1337' and 'content-length: 0'
- No errors in server startup

### Step 2: Trigger Client Download and Info Leak

procedure: [[procedures/Trigger-Client-Download-and-Info-Leak-via-Curl]]

**Objective**: Induce client to download files, exploiting curl's header handling to write uninitialized heap memory to disk.

**Instructions**: Victim connects to server using in-game console with [[commands/connect-to-csgo-server]]:

```bash
connect YOUR_IP:1337
```

Client automatically downloads .res-listed files via curl.

**Expected Output**: Files written to client disk containing uninitialized memory.

**Success Indicators**:
- Client joins server without crash
- Downloaded files exist on client filesystem

### Step 3: Upload and Analyze Leaked Memory

procedure: [[procedures/Upload-and-Analyze-Leaked-Memory-Files-via-NETMsg_File]]

**Objective**: Retrieve leaked files from client to server for ASLR analysis.

**Instructions**: Server sends NETMsg_File request post-download; client uploads files automatically.

**Expected Output**: Server receives binary files with heap contents.

**Success Indicators**:
- Upload messages received on server
- Files parsable without corruption

### Step 4: Spray Heap with Sendprop Objects

procedure: [[procedures/Spray-Heap-with-Sendprop-Objects-to-Enable-ASLR-Break]]

**Objective**: Allocate controlled objects on client heap to mix with leaked memory for pointer recovery.

**Instructions**: Server sends 256 CSVCMsg_SendTable messages with unique sendprop_t props (e.g., type=0x1337ee00).

**Expected Output**: Client heap filled with sprayed objects.

**Success Indicators**:
- No client desync or crash during message flood
- Leaked files later contain sprayed patterns

### Step 5: Parse Leaked Files for Engine Base

procedure: [[procedures/Parse-Leaked-Files-to-Extract-Engine-DLL-Base-Address]]

**Objective**: Extract engine.dll base address from leaked memory using known spray patterns.

**Instructions**: Use Python's struct module to scan files:

Scan for prop values, unpack vtable_ptr at offset 0, subtract OFFSET_VTABLE.

**Expected Output**: Computed engine_base address (e.g., 0x12340000).

**Success Indicators**:
- Valid pointer found matching expected offsets
- ASLR bypass confirmed

### Step 6: Set Up Fake Objects Using Convvars

procedure: [[procedures/Set-Up-Fake-Objects-Using-Convars-for-OOB-Control]]

**Objective**: Craft convar strings on heap to form fake vtable and objects for OOB exploitation.

**Instructions**: Send CMsg_CVars with controlled strings/integers to allocate and point to fake structures.

**Expected Output**: Client heap contains attacker-controlled pointers in global convar array.

**Success Indicators**:
- Convar messages processed without error
- Heap inspection (if possible) shows crafted data

### Step 7: Trigger OOB Access to Hijack RIP

procedure: [[procedures/Trigger-OOB-Access-in-SplitScreen-to-Hijack-RIP]]

**Objective**: Use unchecked 'slot' index to read OOB and dereference fake vtable for control flow hijack.

**Instructions**: Send CSVCMsg_SplitScreen with slot > array bounds (e.g., slot=0x100).

**Expected Output**: RIP points to attacker-controlled address at offset 0xAC.

**Success Indicators**:
- Client executes controlled call without immediate crash
- ROP gadgets reachable

### Step 8: Execute ROP Chain for Arbitrary Code

procedure: [[procedures/Execute-ROP-Chain-for-Arbitrary-Code-Execution]]

**Objective**: Use RIP control to pivot stack and call ShellExecuteA for code execution.

**Instructions**: Build ROP chain via consecutive messages to set up parameters for system command (e.g., calc.exe).

**Expected Output**: Calculator or arbitrary payload executes on client.

**Success Indicators**:
- External process spawns on client (e.g., calc.exe)
- No client termination

## Attack Chain Summary

### Key Achievements

1. Leaked uninitialized heap to break ASLR via HTTP header mishandling
2. Controlled OOB read in protobuf for pointer manipulation and vtable faking
3. Achieved full RCE on CS:GO client without user interaction beyond connecting

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Dynamic-link Library Injection]] Dynamic-link Library Injection (via ROP)
- [[LSASS Memory]] OS Credential Dumping (memory leak analogy)

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Persistence]] Persistence (potential via RCE)
- [[Defense Evasion]] Defense Evasion (ASLR bypass)

---

*Last updated: 2023-10-01T00:00:00Z*
