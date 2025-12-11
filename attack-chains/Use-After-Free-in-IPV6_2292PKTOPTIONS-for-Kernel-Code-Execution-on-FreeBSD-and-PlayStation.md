---
tags:
  - use-after-free
  - kernel-exploit
  - ipv6
  - privilege-escalation
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - FreeBSD
  - PlayStation
complexity: high
procedures:
  - '[[procedures/Exploit-Race-Condition-in-setsockopt-for-IPV6_2292PKTOPTIONS]]'
  - '[[procedures/Achieve-Arbitrary-Kernel-Read/Write-Primitives]]'
  - '[[procedures/Escalate-to-Kernel-Code-Execution]]'
step_count: 3
techniques:
  - '[[Exploitation for Privilege Escalation]]'
description: >-
  Exploitation of a use-after-free vulnerability in IPv6 socket options leading
  to arbitrary kernel read/write and code execution
skill_level: advanced
impact_level: high
id: 5ee8fd57-8242-4d85-bce2-d6d1a6eb1de9
created_at: '2025-12-11T03:47:39.589Z'
updated_at: '2025-12-11T03:47:39.589Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1068]]'
---
# Use-After-Free in IPV6_2292PKTOPTIONS for Kernel Code Execution on FreeBSD and PlayStation

Multi-stage attack chain demonstrating exploitation of a use-after-free vulnerability in the IPV6_2292PKTOPTIONS option of setsockopt on FreeBSD and PlayStation firmware up to 7.02. This allows a race condition to free a buffer while in use, leading to pointer hijacking, arbitrary kernel read/write, and ultimately kernel code execution for local privilege escalation or chained remote attacks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~Variable (depends on PoC) minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Exploit Race Condition] --> B[Achieve Kernel R/W] --> C[Kernel Code Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None explicitly identified; custom PoC exploit required

### Target Environment

- FreeBSD or PlayStation (FW up to 7.02)
- IPv6 socket options enabled in kernel
- Local access for exploitation

### Initial Access Requirements

- Local user access to the system
- Ability to execute code with socket operations
- No prior elevated privileges needed

## Detailed Attack Procedures

### Step 1: Exploit Race Condition - [[procedures/Exploit-Race-Condition-in-setsockopt-for-IPV6_2292PKTOPTIONS]]

**Procedure**: [[procedures/Exploit-Race-Condition-in-setsockopt-for-IPV6_2292PKTOPTIONS]]

**Objective**: Trigger a race condition in setsockopt handling of IPV6_2292PKTOPTIONS to free the struct ip6_pktopts buffer while it is being processed by ip6_setpktopt, due to missing locks.

**Expected Output**: Successful freeing of the buffer during processing, allowing pointer hijacking.

**Success Indicators**:
- Verification through kernel dumps showing buffer freed in race
- Pointers like ip6po_pktinfo become controllable

### Step 2: Achieve Kernel R/W - [[procedures/Achieve-Arbitrary-Kernel-Read/Write-Primitives]]

**Procedure**: [[procedures/Achieve-Arbitrary-Kernel-Read/Write-Primitives]]

**Objective**: Hijack pointers in the freed structure, such as ip6po_pktinfo, to gain arbitrary read/write access in kernel space.

**Expected Output**: Ability to read/write arbitrary kernel memory locations.

**Success Indicators**:
- Successful manipulation of kernel memory via hijacked pointers
- No kernel panic or detection during R/W operations

### Step 3: Kernel Code Execution - [[procedures/Escalate-to-Kernel-Code-Execution]]

**Procedure**: [[procedures/Escalate-to-Kernel-Code-Execution]]

**Objective**: Leverage the read/write primitives to execute arbitrary code in kernel mode, achieving full system compromise.

**Expected Output**: Kernel-level code execution, enabling privilege escalation.

**Success Indicators**:
- Successful execution of PoC code in kernel context
- Ability to run unauthorized operations like pirated games on PlayStation or escalate privileges on FreeBSD

## Attack Chain Summary

### Key Achievements

1. Triggered use-after-free via race condition for pointer control
2. Obtained arbitrary kernel read/write capabilities
3. Achieved kernel code execution for privilege escalation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

*Last updated: [TIMESTAMP]*
