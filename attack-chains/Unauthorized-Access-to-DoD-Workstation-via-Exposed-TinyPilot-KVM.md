---
tags:
  - kvm
  - exposure
  - no-auth
  - dod
  - remote-access
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Hardware
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Exposed-TinyPilot-KVM-Interface]]'
step_count: 1
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:42.802Z'
description: >-
  Attack chain exploiting an exposed TinyPilot KVM device connected to a DoD
  workstation, allowing unauthenticated remote access to view and control the
  system.
skill_level: beginner
impact_level: high
id: 38030313-7874-40b2-8a1d-a43459ca7e71
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Unauthorized Access to DoD Workstation via Exposed TinyPilot KVM

Multi-stage attack chain demonstrating a complete attack workflow.

A TinyPilot KVM device, connected to a U.S. Department of Defense (DoD) workstation, was exposed to the internet without authentication. Accessing the device's IP address directly loads the KVM interface, granting full remote viewing and control of the workstation's screen, mouse, and keyboard. This compromises confidentiality by exposing screen content, integrity by allowing manipulation, and availability by enabling disruptions, all without user notification.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Exposed KVM] --> D[Remote Control and Exfiltration]

    style A fill:#e74c3c
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Target OS/Platform: Any (TinyPilot KVM connected to DoD workstation)
- Required services/ports: HTTP/HTTPS on default TinyPilot port (typically 80 or 443)
- Network access requirements: Direct internet access to the exposed IP address

### Initial Access Requirements

- Credential requirements: None (no authentication)
- Network position: External internet
- Prior access needed: Knowledge of the exposed IP address

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Access-Exposed-TinyPilot-KVM-Interface]]

**Objective**: Gain unauthenticated remote access to the DoD workstation via the exposed TinyPilot KVM interface, enabling full viewing and control.

**Instructions**: Open a web browser and navigate directly to the exposed IP address of the TinyPilot KVM device (e.g., https://<exposed-ip>). The interface loads immediately without prompting for credentials, connecting to the attached DoD workstation.

**Expected Output**: The KVM interface displays the live screen of the DoD workstation, with options to control mouse and keyboard inputs.

**Success Indicators**:
- KVM interface loads without authentication prompt
- Live view of the workstation screen is visible
- Mouse and keyboard controls respond to inputs

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access to sensitive DoD workstation
2. Real-time viewing of user sessions and screen content
3. Remote control capabilities for manipulation or disruption

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[External Remote Services]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
