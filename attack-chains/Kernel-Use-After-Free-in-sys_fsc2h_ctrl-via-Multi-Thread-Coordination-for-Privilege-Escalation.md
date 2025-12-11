---
tags:
  - use-after-free
  - kernel-exploit
  - privilege-escalation
  - playstation
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/CMD_WAIT-(0x10001)]]'
  - '[[commands/CMD_RESOLVE-(0x20005)]]'
  - '[[commands/CMD_COMPLETE-(0x20003)]]'
platforms:
  - PlayStation
  - Kernel
complexity: high
procedures:
  - '[[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]'
step_count: 5
techniques:
  - '[[Exploitation for Privilege Escalation]]'
description: >-
  Exploits a use-after-free vulnerability in the PlayStation kernel syscall
  sys_fsc2h_ctrl by coordinating multiple threads to manipulate path pointers,
  resulting in the freeing of a kernel stack buffer and subsequent memory
  corruption for privilege escalation.
skill_level: advanced
impact_level: high
id: 4b4dff1c-d4d6-4d6f-ab79-9b907be2e7c1
created_at: '2025-12-11T03:47:39.367Z'
updated_at: '2025-12-11T03:47:39.367Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1068]]'
---
# Kernel Use-After-Free in sys_fsc2h_ctrl via Multi-Thread Coordination for Privilege Escalation

Multi-stage attack chain demonstrating a use-after-free vulnerability exploitation in the PlayStation kernel syscall sys_fsc2h_ctrl, achieved through multi-threaded pointer manipulation leading to kernel memory corruption and privilege escalation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~1 minute |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Thread 1: Wait on Path 1] --> B[Thread 2: Wait on Path 2]
    B --> C[Thread 3: Resolve Path 2 to Stack]
    C --> D[Thread 4: Complete and Wake]
    D --> E[Thread 2: Free Kernel Stack]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#2ecc71
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None

### Target Environment

- PlayStation platform with vulnerable kernel
- Access to sys_fsc2h_ctrl syscall
- Multi-threading capabilities

### Initial Access Requirements

- Local access to the PlayStation system
- Ability to execute multi-threaded code in user space
- No prior elevated privileges required

## Detailed Attack Procedures

### Step 1: Thread 1 Waits on Path 1 - [[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]

**Procedure**: [[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]

**Objective**: Initiate waiting on path 1 to set up the race condition.

**Instructions**:

Execute [[commands/CMD_WAIT-(0x10001)]] in sys_fsc2h_ctrl to wait for path 1:

```c
// Pseudocode: Thread 1
sys_fsc2h_ctrl(CMD_WAIT, path1);
```

This puts thread 1 into a waiting state on path 1.

**Expected Output**: Thread enters wait state successfully.

**Success Indicators**:
- Thread 1 is blocked waiting for path 1 signal.

### Step 2: Thread 2 Waits on Path 2 - [[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]

**Procedure**: [[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]

**Objective**: Set up another waiting thread on path 2 for the race.

**Instructions**:

Execute [[commands/CMD_WAIT-(0x10001)]] in sys_fsc2h_ctrl to wait for path 2:

```c
// Pseudocode: Thread 2
sys_fsc2h_ctrl(CMD_WAIT, path2);
```

This puts thread 2 into a waiting state on path 2.

**Expected Output**: Thread enters wait state successfully.

**Success Indicators**:
- Thread 2 is blocked waiting for path 2 signal.

### Step 3: Thread 3 Resolves Path 2 to Stack Buffer - [[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]

**Procedure**: [[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]

**Objective**: Manipulate path 2 pointer to point to a kernel stack buffer and enter sleep.

**Instructions**:

Execute [[commands/CMD_RESOLVE-(0x20005)]] in sys_fsc2h_ctrl to set path 2 to local stack buffer:

```c
// Pseudocode: Thread 3
sys_fsc2h_ctrl(CMD_RESOLVE, path2, stack_buffer);
// Enter sleep
```

This redirects path 2 to kernel stack and sleeps.

**Expected Output**: Path pointer updated, thread sleeps.

**Success Indicators**:
- Path 2 now points to kernel stack instead of heap.

### Step 4: Thread 4 Completes Operation on Path 2 - [[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]

**Procedure**: [[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]

**Objective**: Write data to the buffer and wake thread 3.

**Instructions**:

Execute [[commands/CMD_COMPLETE-(0x20003)]] in sys_fsc2h_ctrl to write data and signal wakeup:

```c
// Pseudocode: Thread 4
sys_fsc2h_ctrl(CMD_COMPLETE, path2, data);
```

This writes to the stack buffer and wakes thread 3.

**Expected Output**: Data written, wakeup signal sent.

**Success Indicators**:
- Thread 3 is signaled to wake, but race allows thread 2 to wake first.

### Step 5: Thread 2 Frees Kernel Stack - [[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]

**Procedure**: [[procedures/Exploit-sys_fsc2h_ctrl-Use-After-Free-via-Thread-Coordination]]

**Objective**: Exploit the race to free the kernel stack pointer.

**Instructions**:

Upon wakeup, thread 2 frees the path 2 pointer (now kernel stack):

```c
// Pseudocode: Thread 2 (post-wakeup)
free(path2_pointer);
```

This causes use-after-free on kernel stack.

**Expected Output**: Kernel stack buffer freed, leading to memory corruption.

**Success Indicators**:
- Kernel memory corruption observed, enabling privilege escalation.

## Attack Chain Summary

### Key Achievements

1. Successful manipulation of path pointers to kernel stack.
2. Race condition exploitation leading to improper free operation.
3. Kernel memory corruption for privilege escalation.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

*Last updated: 2023-10-01T00:00:00Z*
