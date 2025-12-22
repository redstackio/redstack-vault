---
id: eae44e7e-a1b1-45b5-9306-bc98f1f8487e
name: Dependency Confusion in npm Leading to Potential RCE on Development Systems
type: attack_chain
description: >-
  Exploits dependency confusion in npm configurations to register malicious
  packages and potentially achieve RCE on internal development systems
verified: false
submitted: true
step_count: 3
created_at: '2025-12-11T03:48:06.055Z'
updated_at: '2025-12-11T03:48:06.055Z'
procedures:
  - '[[procedures/Identify-Internal-npm-Package-Names]]'
  - '[[procedures/Register-Packages-on-Public-npm-Registry]]'
  - '[[procedures/Monitor-Package-Downloads-from-Target-Systems]]'
techniques:
  - '[[Supply Chain Compromise]]'
  - '[[Compromise Software Supply Chain]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
tags:
  - dependency-confusion
  - npm
  - supply-chain
  - rce
platforms:
  - Node.js
  - Development Environments
tools: []
commands: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1195]]'
  - '[[T1195.002]]'
---

# Dependency Confusion in npm Leading to Potential RCE on Development Systems

Multi-stage attack chain demonstrating a complete attack workflow exploiting dependency confusion in npm configurations, where internal packages are mistakenly fetched from the public registry, potentially leading to malicious code execution on development systems.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Package Registration]
    B --> C[Monitoring and Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- #npm

### Target Environment

- Node.js development environments
- Access to public NPM registry
- Network access to monitor downloads

### Initial Access Requirements

- Knowledge of target's internal package names
- Ability to register packages on public npm registry
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Reconnaissance - [[procedures/Identify-Internal-npm-Package-Names]]

**Procedure**: [[procedures/Identify-Internal-npm-Package-Names]]

**Objective**: Discover internal npm package names that are not registered on the public registry and are defaulted to fetch from public sources.

**Expected Output**: A list of unregistered internal package names.

**Success Indicators**:
- List of package names confirmed missing from public registry
- Verification that they are referenced in target's configurations

First, analyze development projects or configurations to find package names intended for internal use. This can be done by reviewing public code repositories, error messages, or leaked configurations that reference these packages.

### Step 2: Package Registration - [[procedures/Register-Packages-on-Public-npm-Registry]]

**Procedure**: [[procedures/Register-Packages-on-Public-npm-Registry]]

**Objective**: Register the identified package names on the public npm registry with proof-of-concept or malicious code to exploit the dependency confusion.

**Expected Output**: Successfully published packages on the public registry.

**Success Indicators**:
- Packages appear in public npm search
- No errors during publication

Create a new package using [[commands/npm-init-package]]:

```bash
npm init -y
```

Then publish it using [[commands/npm-publish-package]]:

```bash
npm publish
```

Include tracking code or malicious payloads in the package to detect or exploit installations.

### Step 3: Monitoring and Exploitation - [[procedures/Monitor-Package-Downloads-from-Target-Systems]]

**Procedure**: [[procedures/Monitor-Package-Downloads-from-Target-Systems]]

**Objective**: Observe and confirm downloads from the target's systems, potentially leading to RCE if malicious code is executed.

**Expected Output**: Logs showing downloads from target's IP ranges or systems.

**Success Indicators**:
- Download logs confirm installations
- If malicious, evidence of code execution

Monitor npm package download logs or use embedded tracking mechanisms (e.g., a callback to a controlled server) to confirm fetches by the target's development environments.

## Attack Chain Summary

### Key Achievements

1. Identification of vulnerable internal packages
2. Successful registration and potential malicious code injection
3. Confirmation of exploitation through monitoring

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Supply Chain Compromise]]
- [[Compromise Software Supply Chain]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: [TIMESTAMP]*
