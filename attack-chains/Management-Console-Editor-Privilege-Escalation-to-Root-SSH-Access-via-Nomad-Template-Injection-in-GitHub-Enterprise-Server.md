---
tags:
  - command-injection
  - privilege-escalation
  - nomad
  - github-enterprise
  - smtp
  - ssh
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-GitHub-Enterprise-Management-Console-with-Editor-Role]]'
  - '[[procedures/Inject-Malicious-Nomad-Template-in-SMTP-Configuration]]'
  - '[[procedures/Exploit-Nomad-Template-Injection-for-Root-SSH-Access]]'
step_count: 3
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:27.191Z'
description: >-
  A command injection vulnerability in the GitHub Enterprise Server Management
  Console allows an editor-role user to escalate privileges to root SSH access
  by injecting malicious Nomad templates during SMTP configuration.
skill_level: intermediate
impact_level: high
id: 85be33ac-09be-4b83-aff7-7c75187fdc6f
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Management Console Editor Privilege Escalation to Root SSH Access via Nomad Template Injection in GitHub Enterprise Server

Multi-stage attack chain demonstrating a complete attack workflow exploiting a command injection vulnerability in the GitHub Enterprise Server Management Console.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Editor Role Login] --> B[Execution: Inject Nomad Template]
    B --> C[Privilege Escalation: Root SSH Access]
    C --> D[Objective: Full Appliance Control]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for Management Console access
- SSH client for post-exploitation access

### Target Environment

- GitHub Enterprise Server appliance (versions prior to 3.12)
- Linux-based OS
- Services: SMTP configuration interface, SSH
- Tech stack: Nomad for template rendering

### Initial Access Requirements

- Valid editor-role credentials for the Management Console
- Network access to the GitHub Enterprise Server web interface (typically internal)
- No prior root/admin access required

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Access-GitHub-Enterprise-Management-Console-with-Editor-Role]]

**Objective**: Gain authenticated access to the Management Console with editor privileges to reach the SMTP configuration section.

**Instructions**: Open a web browser and navigate to the GitHub Enterprise Server Management Console URL (e.g., https://<appliance-ip>/manage). Log in using provided editor-role credentials. Once logged in, verify access to configuration settings, including SMTP options.

**Expected Output**: Successful login dashboard displaying editor-level options, including SMTP configuration.

**Success Indicators**:
- Dashboard loads without errors
- SMTP configuration menu is accessible

### Step 2: Execution
procedure: [[procedures/Inject-Malicious-Nomad-Template-in-SMTP-Configuration]]

**Objective**: Inject a malicious payload into the SMTP configuration fields that leverages Nomad's template rendering engine to prepare for command execution.

**Instructions**: In the Management Console, navigate to the SMTP settings under configuration. In fields such as server address, port, or authentication details, craft and input a Nomad template payload that includes arbitrary command execution syntax, e.g., using Nomad's `exec` or template functions to run shell commands. Save the configuration to trigger initial rendering.

**Expected Output**: Configuration saves without immediate errors, but template rendering is queued for processing.

**Success Indicators**:
- Payload accepted in SMTP fields
- No validation errors on save

### Step 3: Privilege Escalation
procedure: [[procedures/Exploit-Nomad-Template-Injection-for-Root-SSH-Access]]

**Objective**: Trigger the Nomad template rendering to execute the injected commands, escalating privileges to root and enabling SSH access.

**Instructions**: After saving the SMTP configuration, trigger the rendering process by attempting to send a test email or refreshing the SMTP settings. The malicious template will execute arbitrary commands on the appliance, such as adding an SSH key or modifying sudoers for root access. Monitor for execution indicators, then attempt SSH login to the appliance using the escalated credentials.

**Expected Output**: Commands execute silently during rendering; successful SSH connection to the appliance as root.

**Success Indicators**:
- SSH login succeeds with root privileges
- Arbitrary commands can be run on the appliance

## Attack Chain Summary

### Key Achievements

1. Gained editor access to the Management Console
2. Injected and triggered command execution via Nomad templates in SMTP config
3. Escalated to root SSH access, compromising the entire GitHub Enterprise Server appliance

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]]
- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
