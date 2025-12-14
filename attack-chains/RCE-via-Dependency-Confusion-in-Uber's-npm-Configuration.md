---
tags:
  - dependency-confusion
  - npm
  - rce
  - supply-chain
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Orphaned-npm-Package-Names]]'
  - '[[procedures/Claim-Orphaned-Packages-on-npm]]'
  - '[[procedures/Publish-Malicious-Code-to-Claimed-Packages]]'
  - '[[procedures/Demonstrate-RCE-via-npm-Installation]]'
step_count: 4
techniques:
  - '[[Compromise Software Dependencies and Development Tools]]'
updated_at: '2025-12-14T17:24:14.768Z'
description: >-
  A supply chain attack exploiting misconfigured internal npm packages, allowing
  an attacker to claim orphaned names and publish malicious code leading to
  remote code execution on build servers.
skill_level: intermediate
impact_level: high
id: d78d482e-c181-420c-8685-0443f0056878
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Compromise Software Dependencies and Development Tools]]'
---
# RCE via Dependency Confusion in Uber's npm Configuration

Multi-stage attack chain demonstrating a complete supply chain compromise workflow targeting misconfigured npm dependencies.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Orphaned Packages] --> B[Claim Packages]
    B --> C[Publish Malicious Code]
    C --> D[Demonstrate RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for npm registry access
- npm CLI for package publishing (requires account)

### Target Environment

- Node.js development environment
- Public npm registry access
- Internal build systems using npm without private registry enforcement

### Initial Access Requirements

- No prior credentials needed for discovery
- npm account for claiming and publishing
- Knowledge of target's internal package naming conventions

## Detailed Attack Procedures

### Step 1: Discover Orphaned Packages
procedure: [[procedures/Discover-Orphaned-npm-Package-Names]]

**Objective**: Identify internal package names referenced in public sources but not protected on the npm registry.

**Instructions**: Search public repositories, documentation, or error messages for Uber-specific package names like 'uber-internal-lib'. Verify absence on npmjs.com by searching the registry.

**Expected Output**: List of unused package names that match internal references.

**Success Indicators**:
- Package names found in public sources
- Confirmed as unregistered on npm

### Step 2: Claim Packages
procedure: [[procedures/Claim-Orphaned-Packages-on-npm]]

**Objective**: Register ownership of the discovered orphaned package names on the public npm registry.

**Instructions**: Create an npm account if needed, then use the npm website or CLI to register each package name.

**Expected Output**: Confirmation of package ownership in npm dashboard.

**Success Indicators**:
- Packages successfully claimed
- No conflicts with existing owners

### Step 3: Publish Malicious Code
procedure: [[procedures/Publish-Malicious-Code-to-Claimed-Packages]]

**Objective**: Upload packages containing proof-of-concept code that executes arbitrary commands when installed.

**Instructions**: Create a malicious Node.js module (e.g., with a post-install script running 'whoami' or fetching external payloads), then publish using npm publish.

**Expected Output**: Packages visible and downloadable from npmjs.com.

**Success Indicators**:
- Malicious packages published
- Code verifiable by inspecting package contents

### Step 4: Demonstrate RCE
procedure: [[procedures/Demonstrate-RCE-via-npm-Installation]]

**Objective**: Show how the target's build process installs the malicious package, leading to RCE.

**Instructions**: Simulate the target's npm install command in a test environment to pull and execute the package, observing command execution on the build server.

**Expected Output**: Execution of malicious code, such as command output or system compromise indicators.

**Success Indicators**:
- Package installed from public registry
- RCE achieved without authentication

## Attack Chain Summary

### Key Achievements

1. Discovery of misconfigured internal dependencies
2. Control over supply chain via package claiming
3. Potential compromise of build infrastructure
4. Proof of high-impact RCE in production pipelines

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Compromise Software Dependencies and Development Tools]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
