---
tags:
  - execution
  - rce
  - npm
  - pipeline
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - Windows
  - macOS
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Compromise Software Supply Chain]]'
updated_at: '2025-12-14T17:24:17.919Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 545addf8-8620-4a66-8741-442f2d943b86
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Compromise Software Supply Chain]]'
---
# Trigger Package Installation in Target Pipeline

## Summary

This procedure observes or induces the installation of malicious NPM packages in a misconfigured development pipeline, leading to execution of injected code and potential RCE.

## Description

Once malicious packages are published, the attack relies on the target's NPM install process defaulting to public sources. In misconfigured setups, `npm install` pulls the attacker's version, running post-install scripts. The PayPal incident showed pipeline downloads; outcomes include code execution in build environments, mitigated only by additional checks.

## Requirements

1. Published malicious packages
2. Knowledge of target's CI/CD triggers (e.g., GitHub Actions, Jenkins)
3. Monitoring capabilities for deployment signals

## Defense

Defensive measures and detection strategies:

- Configure CI/CD to use exclusive internal registries
- Scan install logs for unexpected public pulls
- Implement runtime sandboxing for builds and monitor for anomalous executions

## Objectives

1. Confirm package pull from public registry
2. Execute malicious payload
3. Achieve RCE in internal systems

## Instructions

### Step 1: Monitor Target Pipeline

**Context**: Watch for builds that might install the package.

Subscribe to target's public repo updates or use webhooks to detect commits triggering NPM install.

**Expected Output**: Alerts on pipeline runs.

### Step 2: Simulate or Induce Installation

**Context**: Test the misconfig by simulating the target's environment.

Clone a similar project and run:

```bash
npm install @target/internal-lib
```

Observe if public version is pulled.

**Expected Output**: Malicious package installed; script executed (e.g., network beacon).

### Step 3: Validate Impact

**Context**: Confirm RCE in a controlled setup.

Check for payload execution, e.g., file drops or outbound connections.

**Expected Output**: Evidence of code run, like server logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Compromise Software Supply Chain]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Execution]]
- [[rce]]
- [[ci-cd]]
