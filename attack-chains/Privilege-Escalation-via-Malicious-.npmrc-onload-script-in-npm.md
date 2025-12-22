---
tags:
  - npm
  - onload-script
  - privilege-escalation
  - rce
  - node.js
  - social-engineering
type: attack_chain
tools:
  - '[[tools/npm]]'
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
  - '[[procedures/Create-Malicious-npmrc-File]]'
  - '[[procedures/Trick-Victim-to-Run-npm]]'
  - '[[procedures/Load-and-Execute-onload-Script]]'
  - '[[procedures/Run-Arbitrary-Code-with-Escalated-Privileges]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:28:44.425Z'
description: >-
  Attack chain exploiting npm's onload-script in .npmrc for arbitrary Node.js
  code execution, potentially escalating to root privileges via social
  engineering.
skill_level: intermediate
impact_level: high
id: 6f6401e2-d16a-46f6-a1cd-487370fae498
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploitation for Client Execution]]'
---
# Privilege Escalation via Malicious .npmrc onload-script in npm

Multi-stage attack chain demonstrating exploitation of npm's .npmrc configuration for arbitrary code execution and privilege escalation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Place Malicious .npmrc] --> B[Trick User to Run npm]
    B --> C[Load and Execute Script]
    C --> D[Run Arbitrary Code]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]

### Target Environment

- Linux OS with npm versions 3.10 to 6.0 installed
- Node.js runtime
- Access to create files in target directories or repositories

### Initial Access Requirements

- Low-privilege write access to user directories or git repositories
- Ability to perform social engineering (e.g., via tutorials or phishing)
- No prior credentials needed beyond file write permissions

## Detailed Attack Procedures

### Step 1: Place Malicious .npmrc
procedure: [[procedures/Create-Malicious-npmrc-File]]

**Objective**: Create and position a malicious .npmrc file containing an onload-script that points to arbitrary Node.js code.

**Instructions**: Follow the procedure to write the .npmrc file in a target directory, such as a git repository folder or $HOME.

**Expected Output**: Malicious .npmrc file created with onload-script entry.

**Success Indicators**:
- .npmrc file exists in the target directory
- onload-script points to a controllable Node.js script

### Step 2: Trick Victim to Run npm
procedure: [[procedures/Trick-Victim-to-Run-npm]]

**Objective**: Use social engineering to lure the victim into executing an npm command in the directory with the malicious .npmrc.

**Instructions**: Craft a tutorial or message instructing the victim to clone a repository and run commands like [[commands/npm-help]] or [[commands/sudo-npm-i-g-eslint]].

**Expected Output**: Victim runs npm command, triggering .npmrc load.

**Success Indicators**:
- Victim executes npm in the controlled directory
- No suspicion raised by the command

### Step 3: Load and Execute onload-Script
procedure: [[procedures/Load-and-Execute-onload-Script]]

**Objective**: npm processes the .npmrc and executes the onload-script automatically.

**Instructions**: This occurs inherently when the victim runs the npm command; monitor for execution via the script's payload.

**Expected Output**: onload-script runs in the npm process context.

**Success Indicators**:
- Script execution logged or payload activates
- No errors in npm output blocking execution

### Step 4: Run Arbitrary Code with Escalated Privileges
procedure: [[procedures/Run-Arbitrary-Code-with-Escalated-Privileges]]

**Objective**: Achieve arbitrary code execution with user or root privileges depending on sudo usage.

**Instructions**: The onload-script executes attacker-controlled Node.js code; for escalation, ensure the tricked command uses sudo.

**Expected Output**: Arbitrary commands run, e.g., file creation or network exfiltration as user/root.

**Success Indicators**:
- Code executes successfully (e.g., reverse shell or persistence established)
- Privileges match the npm process (root if sudo used)

## Attack Chain Summary

### Key Achievements

1. Placement of malicious configuration without detection
2. Social engineering to trigger execution
3. Arbitrary Node.js code execution
4. Potential root privilege escalation via sudo npm

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploitation for Privilege Escalation]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Privilege Escalation]]

---

*Last updated: 2023-10-01T00:00:00Z*
