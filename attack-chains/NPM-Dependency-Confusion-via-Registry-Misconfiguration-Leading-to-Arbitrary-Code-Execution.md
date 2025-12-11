---
id: f0b68032-ccd3-477c-8331-79a0061d760f
name: >-
  NPM Dependency Confusion via Registry Misconfiguration Leading to Arbitrary
  Code Execution
type: attack_chain
description: >-
  Exploits a misconfiguration in private NPM registries to install malicious
  packages from the public registry, resulting in arbitrary code execution.
verified: false
submitted: true
step_count: 4
created_at: '2025-12-11T03:47:40.610Z'
updated_at: '2025-12-11T03:47:40.610Z'
procedures:
  - '[[procedures/Reconnaissance-of-Private-NPM-Module-Names]]'
  - '[[procedures/Publishing-Malicious-Packages-to-Public-NPM-Registry]]'
  - '[[procedures/Triggering-Malicious-Package-Installation-in-Node.js-Builds]]'
  - '[[procedures/Executing-Arbitrary-Code-via-Malicious-NPM-Package]]'
techniques:
  - '[[Supply Chain Compromise]]'
  - '[[Command-Line Interface]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
tags:
  - dependency-confusion
  - npm
  - rce
  - supply-chain
platforms:
  - Node.js
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
  - '[[T1059]]'
---

# NPM Dependency Confusion via Registry Misconfiguration Leading to Arbitrary Code Execution

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~X minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Publish Malicious Packages]
    B --> C[Trigger Installation]
    C --> D[Execute Code]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- #npm

### Target Environment

- Node.js
- Private NPM registry, Global NPM registry

### Initial Access Requirements

- Knowledge of private module names
- Access to public NPM registry for publishing

## Detailed Attack Procedures

### Step 1: Reconnaissance - [[procedures/Reconnaissance-of-Private-NPM-Module-Names]]

**Procedure**: [[procedures/Reconnaissance-of-Private-NPM-Module-Names]]

**Objective**: Identify names of internal private NPM modules used by the target.

**Expected Output**: List of private module names.

**Success Indicators**:
- Obtained module names through reconnaissance.
- Verified names are used in target's projects.

First, perform reconnaissance to discover private module names, possibly through leaked information or public sources.

### Step 2: Publishing - [[procedures/Publishing-Malicious-Packages-to-Public-NPM-Registry]]

**Procedure**: [[procedures/Publishing-Malicious-Packages-to-Public-NPM-Registry]]

**Objective**: Register malicious packages with the same names but higher versions in the public NPM registry.

**Expected Output**: Malicious packages published to npmjs.com.

**Success Indicators**:
- Packages successfully uploaded with higher versions.
- No conflicts or rejections from the registry.

Create malicious modules and publish them using [[commands/npm-publish-malicious]]:

```bash
npm publish
```

Ensure the version is higher than the private ones and include malicious scripts.

### Step 3: Installation - [[procedures/Triggering-Malicious-Package-Installation-in-Node.js-Builds]]

**Procedure**: [[procedures/Triggering-Malicious-Package-Installation-in-Node.js-Builds]]

**Objective**: Victim's Node.js project builds and installs the malicious package from the public registry.

**Expected Output**: Malicious package installed during build.

**Success Indicators**:
- Build process pulls from public registry.
- Higher version prioritized over private.

The misconfiguration causes the build to install via [[commands/npm-install]]:

```bash
npm install
```

### Step 4: Execution - [[procedures/Executing-Arbitrary-Code-via-Malicious-NPM-Package]]

**Procedure**: [[procedures/Executing-Arbitrary-Code-via-Malicious-NPM-Package]]

**Objective**: Malicious script in the package executes on the host machine.

**Expected Output**: Arbitrary code execution on affected hosts.

**Success Indicators**:
- Code executes during installation.
- Attacker achieves objectives like data exfiltration or persistence.

The embedded script runs automatically upon installation.

## Attack Chain Summary

### Key Achievements

1. Identified private modules.
2. Published malicious versions.
3. Triggered installation via misconfiguration.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Supply Chain Compromise]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: [TIMESTAMP]*
