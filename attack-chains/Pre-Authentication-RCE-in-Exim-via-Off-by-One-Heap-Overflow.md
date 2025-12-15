---
id: ac-exim-rce-2018-6789
tags:
  - exim
  - rce
  - heap-overflow
  - off-by-one
  - cve-2018-6789
  - smtp
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: high
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Detect-Exim-Vulnerability]]'
  - '[[procedures/Exploit-Exim-Heap-Overflow]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Proc Memory]]'
updated_at: '2025-12-14T17:23:28.389Z'
description: >-
  A multi-stage attack exploiting an off-by-one error in Exim MTA's utility
  function to achieve remote code execution on vulnerable mail servers.
skill_level: advanced
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Proc Memory]]'
---
# Pre-Authentication RCE in Exim via Off-by-One Heap Overflow

Multi-stage attack chain demonstrating exploitation of CVE-2018-6789, an off-by-one error in Exim MTA's utility function, leading to heap buffer overflow and pre-authentication remote code execution on affected mail servers.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~15 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Identify Exim Server] --> B[Exploitation: Trigger Heap Overflow]
    B --> C[Execution: Remote Code Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses built-in tools like nmap and telnet)

### Target Environment

- Target OS/Platform: Linux
- Required services/ports: SMTP on port 25
- Network access requirements: Direct internet access to target mail server

### Initial Access Requirements

- Credential requirements: None (pre-authentication)
- Network position: External attacker
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Detect Vulnerable Exim Server
procedure: [[procedures/Detect-Exim-Vulnerability]]

**Objective**: Identify if the target mail server is running a vulnerable version of Exim.

**Instructions**: Use [[commands/nmap-exim-detect]] to scan the target for Exim service on port 25:

```bash
nmap -p 25 --script smtp-commands target.example.com
```

Follow up with [[commands/telnet-smtp-banner]] to retrieve the server banner:

```bash
telnet target.example.com 25
```

Type `QUIT` to exit after observing the banner.

**Expected Output**: Banner indicating Exim version (e.g., "220 target.example.com ESMTP Exim 4.91" confirming vulnerable versions).

**Success Indicators**:
- Exim service detected on port 25
- Version banner shows affected release (all versions prior to patch)

### Step 2: Exploit Heap Overflow for RCE
procedure: [[procedures/Exploit-Exim-Heap-Overflow]]

**Objective**: Send a crafted SMTP message to trigger the off-by-one error, leading to heap manipulation and remote code execution.

**Instructions**: Connect to the SMTP port using [[commands/telnet-smtp-exploit]] and initiate an SMTP session:

```bash
telnet target.example.com 25
```

Send the following SMTP commands manually (replace with actual crafted payload for heap overflow, e.g., a long header exceeding buffer bounds by one byte):

```bash
HELO attacker.com
MAIL FROM: <attacker@domain.com>
RCPT TO: <victim@target.example.com>
DATA
From: "Long Header" <attacker@domain.com>
To: <victim@target.example.com>
Subject: [Crafted long string of ~1024+ bytes to trigger off-by-one in spool_write]

Body content here.
.
QUIT
```

The crafted header exploits the utility function's string length miscalculation, causing heap overflow. For full RCE, chain with heap grooming techniques (detailed in external resources like the reporter's blog).

**Expected Output**: Server accepts the message without error, but heap corruption occurs internally, enabling code execution (verify via reverse shell callback if payload includes it).

**Success Indicators**:
- Message accepted (250 OK response)
- Reverse shell or command execution on target (e.g., callback to attacker's listener)

## Attack Chain Summary

### Key Achievements

1. Detection of vulnerable Exim instance without authentication
2. Triggering of heap buffer overflow via crafted SMTP input
3. Achievement of pre-authentication remote code execution

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Proc Memory]] Proc Memory Loading (for heap manipulation leading to RCE)

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
