---
tags:
  - dos
  - infinite-loop
  - mruby
  - ruby
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
commands: []
platforms:
  - Linux
complexity: low
procedures:
  - '[[procedures/Exploit-MRuby-Infinite-Loop-Vulnerability]]'
step_count: 3
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
description: >-
  Exploits a vulnerability in the MRuby parser to cause an infinite loop,
  leading to denial-of-service by making the process unresponsive.
skill_level: beginner
impact_level: medium
id: 90d6f7a3-b2a1-4149-8ce9-b18a54733410
created_at: '2025-12-11T03:47:39.208Z'
updated_at: '2025-12-11T03:47:39.208Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1203]]'
  - '[[T1499]]'
---
# Infinite Loop DoS in MRuby via Zero-Length Heredoc Identifiers

Multi-stage attack chain demonstrating how to exploit a parsing vulnerability in MRuby to induce an infinite loop, causing denial-of-service.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare POC] --> B[Execute in MRuby] --> C[Observe DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- #mruby
- #sandbox

### Target Environment

- Linux
- mruby-engine sandbox service
- Ruby, MRuby, MRI tech stack

### Initial Access Requirements

- Local access to run scripts
- No credentials needed
- Ability to execute Ruby scripts

## Detailed Attack Procedures

### Step 1: Prepare POC Code - [[procedures/Exploit-MRuby-Infinite-Loop-Vulnerability]]

**Procedure**: [[procedures/Exploit-MRuby-Infinite-Loop-Vulnerability]]

**Objective**: Create the proof-of-concept Ruby script that triggers the vulnerability.

**Expected Output**: A file named infinite_heredoc.rb containing the malicious code.

Save the following code as infinite_heredoc.rb:

```
<<''.a begin
```

**Success Indicators**:
- File is created successfully.
- Code matches the POC: <<''.a begin

### Step 2: Execute POC in MRuby - [[procedures/Exploit-MRuby-Infinite-Loop-Vulnerability]]

**Procedure**: [[procedures/Exploit-MRuby-Infinite-Loop-Vulnerability]]

**Objective**: Run the POC script using MRuby to trigger the infinite loop.

**Expected Output**: The process enters an infinite loop and becomes unresponsive.

Execute the command [[commands/mruby-run-poc]]:

```bash
mruby infinite_heredoc.rb
```

Alternatively, use [[commands/sandbox-run-poc]] in the sandbox environment:

```bash
sandbox infinite_heredoc.rb
```

**Success Indicators**:
- Process consumes CPU and does not terminate.
- Unresponsive to SIGTERM signals.

### Step 3: Observe and Terminate - [[procedures/Exploit-MRuby-Infinite-Loop-Vulnerability]]

**Procedure**: [[procedures/Exploit-MRuby-Infinite-Loop-Vulnerability]]

**Objective**: Confirm the denial-of-service impact and forcefully terminate the process.

**Expected Output**: Process requires SIGABRT or SIGKILL to stop.

Attempt to terminate with SIGTERM (fails), then use SIGABRT or SIGKILL.

**Success Indicators**:
- Process unresponsive to SIGTERM.
- Successful termination only with forceful signals, confirming DoS potential.

## Attack Chain Summary

### Key Achievements

1. Triggered infinite loop in MRuby parser.
2. Caused unresponsiveness in sandbox and hosting process.
3. Demonstrated potential for denial-of-service attacks.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]]
- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Impact]]

*Last updated: 2023-10-01*
