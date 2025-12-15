---
id: proc-2255750-3
tags:
  - rce
  - exfiltration
  - secret-leak
  - ci-cd
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Cloud
  - CI/CD
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:23:54.343Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Trigger RCE via Poisoned Cache and Exfiltrate Secrets

## Summary

This procedure activates the poisoned NX Cloud cache during a CI build, executing injected code to achieve remote code execution and exfiltrate sensitive environment variables like secret tokens.

## Description

Once the cache is poisoned, triggering a build in the fxa repository causes NX to restore the malicious artifact, running the injected code in the CI environment. The payload captures env vars (e.g., API tokens) and sends them to an external server. This targets cloud CI runners with elevated access; outcomes include proof-of-concept leaks without direct repo write access, relying on public triggers or timing.

## Requirements

1. Poisoned cache already uploaded to NX Cloud.
2. Ability to trigger or observe a CI build (e.g., via public repo push if possible).
3. Attacker-controlled endpoint for receiving exfiltrated data.

## Defense

Defensive measures and detection strategies:

- Isolate CI environments with minimal secrets exposure.
- Verify cache integrity with checksums before restore.
- Monitor outbound traffic from CI runners for anomalies.

## Objectives

1. Execute arbitrary code in the CI build process via cache restoration.
2. Capture and exfiltrate sensitive env vars containing tokens.
3. Demonstrate full compromise of the development pipeline.

## Instructions

### Step 1: Trigger CI Build Process

**Context**: Initiate a build to force cache restoration and payload execution.

If authorized, push a innocuous commit to the public repo. Alternatively, wait for an automated build or use repo features to trigger. The CI (e.g., GitHub Actions) will invoke NX cache restore.

### Step 2: Execute Payload and Capture Secrets

**Context**: The restored cache runs the injected code, accessing env vars.

The payload (e.g., a script) executes commands like `env | grep TOKEN` and exfils via HTTP POST to attacker server.

### Step 3: Receive and Verify Exfiltration

**Context**: Collect leaked data as proof.

Monitor the attacker endpoint for incoming requests containing secrets from the fxa env.

**Expected Output**: Server logs showing received tokens, e.g., {"fxa_token": "secretvalue"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- exfiltration
- secret-leak
- ci-cd
