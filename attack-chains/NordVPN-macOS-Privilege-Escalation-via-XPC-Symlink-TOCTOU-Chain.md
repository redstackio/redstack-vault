---
tags:
  - xpc
  - symlink
  - toctou
  - race-condition
  - privilege-escalation
  - nordvpn
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - macOS
submitted: true
complexity: high
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Establish-XPC-Connection-with-Privileged-Helper]]'
  - '[[procedures/Send-Symlink-Binary-Open-Message-via-XPC]]'
  - '[[procedures/Exploit-TOCTOU-Race-by-Swapping-Symlink]]'
step_count: 3
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Dynamic Linker Hijacking]]'
updated_at: '2025-12-14T17:30:17.913Z'
description: >-
  A chain of 5 vulnerabilities exploited in Nord Security's NordVPN macOS
  application to achieve root privilege escalation through unauthorized XPC
  access, symlink manipulation, and a TOCTOU race condition.
skill_level: advanced
impact_level: critical
id: 07f72c03-9614-479c-90ae-44acf1a568aa
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Dynamic Linker Hijacking]]'
---
---

# NordVPN macOS Privilege Escalation via XPC Symlink TOCTOU Chain

Multi-stage attack chain demonstrating a complete privilege escalation workflow exploiting chained vulnerabilities in Nord Security's NordVPN macOS application.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1-5 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | Critical |

## Attack Flow Visualization

```mermaid
graph LR
    A[Establish XPC Connection] --> B[Send Symlink Message]
    B --> C[Win TOCTOU Race]
    C --> D[Execute Malicious File as Root]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- No specific external tools required; exploits built-in macOS mechanisms like XPC and symlinks.

### Target Environment

- Target OS/Platform: macOS with NordVPN application installed (version vulnerable to the chain, e.g., pre-patch releases).
- Required services/ports: Local XPC inter-process communication (no network ports needed).
- Network access requirements: Local access to the target machine.

### Initial Access Requirements

- Credential requirements: User-level access to the NordVPN application.
- Network position: Local attacker on the macOS system.
- Prior access needed: Installation or presence of NordVPN software.

## Detailed Attack Procedures

### Step 1: Establish XPC Connection
procedure: [[procedures/Establish-XPC-Connection-with-Privileged-Helper]]

**Objective**: Gain unauthorized access to the privileged helper process via XPC to enable further exploitation.

**Instructions**: Chain together 5 specific vulnerabilities in the NordVPN software to forge a valid XPC connection. This involves exploiting flaws in input validation, authentication, and process isolation within the application's XPC services. Use macOS development tools like `xpcproxy` or custom Mach-O binaries to simulate the connection, targeting the helper tool that runs with elevated privileges.

**Expected Output**: Successful establishment of an XPC session with the privileged helper, allowing message dispatch without rejection.

**Success Indicators**:
- XPC connection logs show acceptance from the helper process.
- No authentication errors in system logs (e.g., via `log stream --predicate 'subsystem == "com.nordvpn"'`).

### Step 2: Send Symlink Binary Open Message
procedure: [[procedures/Send-Symlink-Binary-Open-Message-via-XPC]]

**Objective**: Instruct the privileged helper to attempt opening a binary in a user-controlled directory using a symlink to bypass path restrictions.

**Instructions**: Once the XPC connection is active, craft and send a message payload requesting the helper to launch a binary at a path within a directory you control (e.g., `/tmp/nordvpn-binary`). Create a tiny symlink in this location pointing to the legitimate NordVPN binary path (e.g., `/Applications/NordVPN.app/Contents/MacOS/NordVPN`). The helper resolves this symlink during its security checks.

**Expected Output**: The helper process receives and begins processing the open request, resolving the symlink to the legitimate binary initially.

**Success Indicators**:
- Message acknowledged in XPC traces.
- Symlink resolution occurs without immediate failure, as seen in process monitoring tools like `fs_usage`.

### Step 3: Exploit TOCTOU Race
procedure: [[procedures/Exploit-TOCTOU-Race-by-Swapping-Symlink]]

**Objective**: Trick the helper into executing a malicious file instead of the legitimate binary by exploiting the time window between symlink check and use.

**Instructions**: During the brief window when the helper checks the symlink (time-of-check) but before it uses the resolved path to execute (time-of-use), rapidly swap the symlink target. Alternate between the legitimate NordVPN binary and your malicious file (e.g., a trojanized executable with root shellcode) using a script that loops file operations like `ln -sf`. Monitor the helper's process with `lsof` or `dtruss` to time the swaps precisely, ensuring the malicious file is loaded when execution occurs.

**Expected Output**: The malicious file executes with root privileges, potentially spawning a root shell or performing unauthorized actions.

**Success Indicators**:
- Root-owned process from the malicious binary appears in `ps aux`.
- Elevated actions succeed, such as writing to protected directories.

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to privileged XPC helper via vulnerability chain.
2. Symlink-based path manipulation to direct execution to controlled locations.
3. Successful TOCTOU exploitation for arbitrary code execution as root.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Dynamic Linker Hijacking]] Dynamic Linker Hijacking

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
