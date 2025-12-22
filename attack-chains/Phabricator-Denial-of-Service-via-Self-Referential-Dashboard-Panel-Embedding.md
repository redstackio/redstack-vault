---
tags:
  - dos
  - phabricator
  - recursion
  - remarkup
  - uncontrolled-resource-consumption
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Create-Malicious-Text-Panel-in-Phabricator-Dashboard]]'
  - '[[procedures/Embed-Self-Reference-in-Panel-Content-Using-Remarkup]]'
  - '[[procedures/Trigger-Infinite-Recursion-by-Rendering-Dashboard]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
description: >-
  A multi-step attack exploiting Phabricator's lack of cycle detection in
  dashboard rendering to cause infinite recursion and denial of service across
  affected pages.
skill_level: intermediate
impact_level: high
id: 3605c062-93dd-4c65-807d-abdd6dad2dd6
created_at: '2025-12-14T17:26:30.487Z'
updated_at: '2025-12-14T17:26:30.487Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Phabricator Denial of Service via Self-Referential Dashboard Panel Embedding

Multi-stage attack chain demonstrating a complete attack workflow exploiting a vulnerability in Phabricator's dashboard rendering engine.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Text Panel] --> B[Embed Self-Reference]
    B --> C[Trigger Rendering]
    C --> D[DoS Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (requires authenticated access to Phabricator instance with dashboard creation permissions)

### Target Environment

- Phabricator web application
- Required services/ports: HTTP/HTTPS on standard web ports (80/443)
- Network access requirements: Direct access to the Phabricator instance as an authenticated user

### Initial Access Requirements

- Valid user credentials with permissions to create and edit dashboards
- No prior elevated access needed, but dashboard creation must be enabled in the installation

## Detailed Attack Procedures

### Step 1: Create Text Panel
procedure: [[procedures/Create-Malicious-Text-Panel-in-Phabricator-Dashboard]]

**Objective**: Establish a dashboard panel that can be self-referenced for recursion.

**Instructions**: Navigate to the Dashboards section in Phabricator and create a new Text Panel. Upon creation, note the assigned object reference (e.g., W1).

**Expected Output**: A new Text Panel is created with a unique reference ID.

**Success Indicators**:
- Panel creation confirmation
- Object reference (e.g., {W1}) visible in the panel details

### Step 2: Embed Self-Reference
procedure: [[procedures/Embed-Self-Reference-in-Panel-Content-Using-Remarkup]]

**Objective**: Introduce a self-referential embed in the panel content to set up infinite recursion.

**Instructions**: Edit the newly created Text Panel and insert the Remarkup syntax for its own reference (e.g., {W1}) into the content field.

**Expected Output**: The panel content now includes the self-embed syntax, but rendering is not yet triggered.

**Success Indicators**:
- Self-reference syntax saved without immediate error
- Panel edit confirmation

### Step 3: Trigger Rendering
procedure: [[procedures/Trigger-Infinite-Recursion-by-Rendering-Dashboard]]

**Objective**: Cause the rendering engine to process the self-reference, leading to denial of service.

**Instructions**: Save the dashboard or view it, or embed the malicious panel in a comment on a task (e.g., in Maniphest). Attempt to render the affected page.

**Expected Output**: The page fails to render due to infinite recursion, choking the rendering engine.

**Success Indicators**:
- Rendering timeout or failure
- Affected pages (tasks, feeds, homepages) become inaccessible to all users

## Attack Chain Summary

### Key Achievements

1. Creation of a self-referential dashboard panel exploiting Remarkup syntax
2. Induction of infinite recursion in Phabricator's rendering engine
3. Widespread denial of service impacting all users on the installation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01*
