---
id: ac-nodejs-capabilities-escalation
tags:
  - nodejs
  - linux
  - privilege-escalation
  - code-injection
  - capabilities
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Configure-Node.js-with-Linux-Capabilities]]'
  - '[[procedures/Inject-Code-via-Environment-Variables]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:36.353Z'
description: >-
  An attack chain exploiting a flaw in Node.js environment variable handling on
  Linux systems with elevated capabilities, allowing unprivileged users to
  inject and execute code with privileged access.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Node.js Code Injection and Privilege Escalation via Environment Variable Mishandling with Linux Capabilities

Multi-stage attack chain demonstrating exploitation of a Node.js vulnerability on Linux systems where improper handling of environment variables with Linux capabilities allows unprivileged code injection leading to privilege escalation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Configure Privileged Node.js Process] --> B[Inject Malicious Environment Variable]
    B --> C[Execute Injected Code with Elevated Privileges]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None (uses built-in Linux utilities like setcap)

### Target Environment

- Linux OS with Node.js runtime
- Node.js process configured with Linux capabilities (e.g., via setcap)
- Elevated privileges on the Node.js binary (e.g., CAP_NET_BIND_SERVICE or others)
- Unprivileged user access to set environment variables

### Initial Access Requirements

- Local access to the system as an unprivileged user
- Ability to influence environment variables for the Node.js process (e.g., via cron, service files, or shared environment)
- No network access required

## Detailed Attack Procedures

### Step 1: Configure Node.js with Linux Capabilities
procedure: [[procedures/Configure-Node.js-with-Linux-Capabilities]]

**Objective**: Set up the Node.js binary with elevated Linux capabilities to create the conditions for the vulnerability, simulating a privileged service setup.

**Instructions**: Use the [[commands/setcap-configure-capabilities]] command to apply capabilities to the Node.js executable. This mimics a common setup where Node.js binds to privileged ports without full root privileges.

```bash
sudo setcap 'cap_net_bind_service=+ep' /usr/bin/node
```

Verify the capabilities with [[commands/getcap-check-capabilities]]:

```bash
getcap /usr/bin/node
```

**Expected Output**: Confirmation that the Node.js binary has the specified capabilities applied, e.g., `/usr/bin/node = cap_net_bind_service+eip`.

**Success Indicators**:
- Capabilities successfully set on Node.js binary
- No errors from setcap command

### Step 2: Inject Code via Environment Variables
procedure: [[procedures/Inject-Code-via-Environment-Variables]]

**Objective**: Exploit the flaw by setting a malicious environment variable that Node.js fails to ignore, leading to code injection and execution with the process's elevated privileges.

**Instructions**: As an unprivileged user, set the NODE_OPTIONS environment variable to load a malicious module. Due to the bug, when other capabilities are present or the exception is misapplied, Node.js processes this variable and executes the injected code.

First, create a malicious JavaScript file:

```bash
echo 'console.log(\"Injected code executing with privileges!\"); require(\"fs\").writeFileSync(\"/tmp/escalated.txt\", \"Priv esc success\");' > /tmp/malicious.js
```

Then, export the environment variable and run Node.js:

```bash
export NODE_OPTIONS=\"--require=/tmp/malicious.js\"
node -e \"console.log('Running Node.js')\"
```

**Expected Output**: The Node.js process executes the injected code, logging the message and creating `/tmp/escalated.txt` with elevated privileges if capabilities allow further escalation.

**Success Indicators**:
- Malicious code executes without errors
- File written or other privileged actions performed (e.g., binding to port 80 if CAP_NET_BIND_SERVICE is active)
- No environment variable ignored as expected in secure setups

## Attack Chain Summary

### Key Achievements

1. Bypassed environment variable sanitization in Node.js with capabilities
2. Achieved arbitrary code injection as an unprivileged user
3. Escalated privileges to those of the Node.js process, potentially enabling further system compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]] JavaScript (Node.js code execution via environment injection)
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation (via capabilities flaw)

### MITRE ATT&CK Tactics

- [[Execution]] Execution (injecting and running code)
- [[Privilege Escalation]] Privilege Escalation (inheriting elevated capabilities)

---
*Last updated: 2023-10-01T00:00:00Z*
