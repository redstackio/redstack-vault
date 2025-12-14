---
tags:
  - redos
  - denial-of-service
  - node.js
  - regex
  - json-validation
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Vulnerable-Regex-in-is-my-json-valid]]'
  - '[[procedures/Exploit-ReDoS-with-Malicious-Email-Input]]'
step_count: 2
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.724Z'
description: >-
  A denial-of-service attack exploiting catastrophic backtracking in the email
  validation regex of the Node.js 'is-my-json-valid' module, blocking the event
  loop with specially crafted inputs.
skill_level: intermediate
impact_level: high
id: 11cbe85e-4bf7-4e97-a04b-463db5d3ab55
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# ReDoS Denial of Service via Malicious Email Input in is-my-json-valid Module

Multi-stage attack chain demonstrating a complete denial-of-service workflow against Node.js applications using the vulnerable 'is-my-json-valid' module.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~10 seconds per attempt |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Regex] --> B[Exploit with Malicious Input]
    B --> C[Event Loop Blockage]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on source code review and Node.js runtime)

### Target Environment

- Node.js runtime with 'is-my-json-valid' module installed (vulnerable versions prior to fixes post-2014)
- Access to application source or runtime for testing

### Initial Access Requirements

- Read access to module source code (e.g., via npm or GitHub)
- Ability to execute Node.js scripts for validation testing
- No network access required; local or server-side exploitation

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Regex
procedure: [[procedures/Identify-Vulnerable-Regex-in-is-my-json-valid]]

**Objective**: Locate the susceptible regex pattern in the module's source code to confirm the ReDoS vulnerability.

**Instructions**: Review the module's formats.js file to examine the email validation export. Search for the regex definition and analyze its structure for nested quantifiers that enable backtracking.

**Expected Output**: Confirmation of the regex `/^\S+@\S+$/` which lacks atomic grouping or possessive quantifiers, allowing exponential backtracking.

**Success Indicators**:
- Regex pattern identified in formats.js
- Analysis reveals potential for catastrophic backtracking on inputs with repeated characters

### Step 2: Exploit ReDoS with Malicious Input
procedure: [[procedures/Exploit-ReDoS-with-Malicious-Email-Input]]

**Objective**: Craft and test a malicious input string to trigger excessive CPU usage and block the Node.js event loop.

**Instructions**: Generate a ~90K character string designed to maximize backtracking, such as a long sequence of non-space characters followed by an '@' and more non-spaces. Use a Node.js script to invoke the module's validation on this input.

**Expected Output**: Regex matching takes ~10 seconds, causing high CPU usage and event loop delay.

**Success Indicators**:
- Validation attempt hangs for several seconds
- CPU utilization spikes during matching
- Application responsiveness is impaired

## Attack Chain Summary

### Key Achievements

1. Successful identification of the ReDoS vulnerability in the email regex from 2014 commit.
2. Demonstration of DoS impact with 90K character inputs blocking Node.js for 10 seconds.
3. Highlighted risks in third-party JSON validation modules.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
