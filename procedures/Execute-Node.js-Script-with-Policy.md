---
tags:
  - node.js
  - execution
  - bypass
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/node-execute-with-experimental-policy]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:58.906Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e24837a7-99f8-4111-8217-99b2393f7a36
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Node.js-Script-with-Policy

## Summary

This procedure runs the exploit script under the restrictive Node.js policy, confirming the bypass by successfully loading and executing the 'os' module to disclose system information.

## Description

Using the --experimental-policy flag, Node.js enforces the policy while loading proc.js. The vulnerability allows the prototype chain access to succeed, leading to privilege escalation and execution of unauthorized code, as the policy only protects own properties set via setOwnProperty in the CJS loader.

## Requirements

1. policy.json and proc.js files from prior procedures
2. Node.js v19.6.1 binary accessible (e.g., in ../node-v19.6.1-linux-x64/bin/)
3. Execution privileges on the system

## Defense

Defensive measures and detection strategies:

- Disable experimental policies or use audited versions post-v19.6.1
- Monitor Node.js process arguments for --experimental-policy and log module loads
- Implement sandboxing or containerization for Node.js executions

## Objectives

1. Enforce policy while executing the script
2. Verify bypass through module loading and output
3. Achieve information disclosure as proof of escalation

## Instructions

### Step 1: Run Script with Policy

**Context**: Execute proc.js using Node.js with the policy flag to test the bypass.

**Command** ([[commands/node-execute-with-experimental-policy]]):

```bash
../node-v19.6.1-linux-x64/bin/node --experimental-policy=policy.json proc.js
```

> This command loads the policy and runs the script. Expected output includes Node.js version, OS version details, and an experimental warning, confirming 'os' loaded despite restrictions.

### Step 2: Validate Bypass Success

**Context**: Check output for unauthorized module execution.

Review console output for os.version() result:

> Success if OS information is printed, indicating policy evasion.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/node-execute-with-experimental-policy]]

## Tools Used

- [[tools/Node.js]]

## Tags

- node.js
- execution
- bypass
