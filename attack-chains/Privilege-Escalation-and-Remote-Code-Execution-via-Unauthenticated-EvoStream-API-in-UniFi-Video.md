---
id: ac-ubiquiti-evostream-rce
tags:
  - rce
  - privilege-escalation
  - command-injection
  - unifi-video
  - evostream
type: attack_chain
tools:
  - '[[tools/poc.py]]'
  - '[[tools/rce0923234.html]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-EvoStream-Service-and-API-Exposure]]'
  - '[[procedures/Local-Privilege-Escalation-via-LaunchProcess-Command]]'
  - '[[procedures/Remote-RCE-via-JavaScript-WebSocket-Payload]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:58.572Z'
description: >-
  Multi-stage attack exploiting unauthenticated command execution in the
  EvoStream API of Ubiquiti UniFi Video, enabling local privilege escalation
  from user to SYSTEM and remote RCE via JavaScript payloads over WebSocket.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Privilege Escalation and Remote Code Execution via Unauthenticated EvoStream API in UniFi Video

Multi-stage attack chain demonstrating exploitation of the EvoStream API in Ubiquiti's UniFi Video software, which exposes an unauthenticated command execution endpoint on localhost:7440. This allows local privilege escalation to SYSTEM privileges and remote code execution when combined with user interaction or SSRF, leading to full system compromise (CVSS 9.6, CVE-2019-15595).

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Service] --> B[Local Escalation]
    B --> C[Remote Exploitation]
    C --> D[System Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/poc.py]]
- [[tools/rce0923234.html]]

### Target Environment

- Windows OS
- UniFi Video software installed with EvoStream service running
- Port 7440 accessible on localhost

### Initial Access Requirements

- Local user access for privilege escalation
- For remote: User interaction (visiting malicious page) or SSRF vulnerability to reach localhost
- No credentials required due to unauthenticated API

## Detailed Attack Procedures

### Step 1: Identify EvoStream Service and API Exposure
procedure: [[procedures/Identify-EvoStream-Service-and-API-Exposure]]

**Objective**: Locate the EvoStream service running as SYSTEM and confirm the unauthenticated API on localhost:7440.

**Instructions**: Use netstat or similar to check for listening services on port 7440. Verify the API endpoint by sending a test request to the launchprocess documentation reference (http://docs.evostream.com/2.0/launchProcess.html). No tools needed beyond basic system queries.

**Expected Output**: Confirmation of evostream.exe process running as SYSTEM with API exposed on localhost:7440.

**Success Indicators**:
- Port 7440 bound to localhost
- API responds without authentication

### Step 2: Local Privilege Escalation via LaunchProcess Command
procedure: [[procedures/Local-Privilege-Escalation-via-LaunchProcess-Command]]

**Objective**: Exploit the launchprocess API to execute arbitrary binaries as SYSTEM, escalating from local user privileges.

**Instructions**: Run the POC script [[tools/poc.py]] to send a launchprocess command via HTTP POST to localhost:7440, specifying a binary like cmd.exe with arguments for a reverse shell or calc.exe.

**Expected Output**: Successful execution of the binary as SYSTEM, e.g., calculator launches or shell access obtained.

**Success Indicators**:
- Process spawns with SYSTEM privileges (check via Task Manager)
- Arbitrary command output visible

### Step 3: Remote RCE via JavaScript WebSocket Payload
procedure: [[procedures/Remote-RCE-via-JavaScript-WebSocket-Payload]]

**Objective**: Achieve remote code execution by tricking the user into visiting a malicious page that injects JavaScript to connect via WebSocket to localhost:7440 and execute commands as SYSTEM.

**Instructions**: Host the HTML payload [[tools/rce0923234.html]] on a remote server. Ensure the target user visits it (e.g., via phishing). The script establishes a WebSocket connection to ws://localhost:7440 and sends a launchprocess command to run calc.exe.

**Expected Output**: WebSocket connection established, command sent, and payload executed on the target (e.g., calc.exe pops).

**Success Indicators**:
- WebSocket handshake successful in browser console
- SYSTEM-level process execution confirmed

## Attack Chain Summary

### Key Achievements

1. Identification of vulnerable EvoStream API without authentication
2. Local escalation to SYSTEM via arbitrary binary execution
3. Remote RCE with user interaction, enabling full compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]
- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
