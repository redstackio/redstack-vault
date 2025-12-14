---
id: ac-uuid-placeholder
tags:
  - command-injection
  - privilege-escalation
  - github-enterprise
  - syslog-ng
  - rce
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-GitHub-Enterprise-Management-Console]]'
  - '[[procedures/Inject-Command-in-syslog-ng-Configuration]]'
step_count: 2
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:27.205Z'
description: >-
  An attack chain exploiting a command injection vulnerability in the GitHub
  Enterprise Server Management Console's syslog-ng configuration editor to
  escalate from editor role privileges to full root SSH access on the Linux
  appliance.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Privilege Escalation to Root SSH Access via Command Injection in GitHub Enterprise Server syslog-ng Configuration

Multi-stage attack chain demonstrating privilege escalation in GitHub Enterprise Server (GHES) by exploiting insufficient input sanitization in the Management Console's syslog-ng configuration editor. An attacker with editor role access can inject arbitrary commands that execute with root privileges, leading to full SSH access on the appliance.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Management Console with Editor Role] --> B[Inject Malicious Command in syslog-ng Config]
    B --> C[Privilege Escalation to Root SSH Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for accessing the Management Console

### Target Environment

- GitHub Enterprise Server appliance running on Linux
- syslog-ng service enabled
- Management Console accessible

### Initial Access Requirements

- Valid editor role credentials for the GHES Management Console
- Network access to the GHES instance (typically internal or VPN)
- No prior root access required

## Detailed Attack Procedures

### Step 1: Access Management Console
procedure: [[procedures/Access-GitHub-Enterprise-Management-Console]]

**Objective**: Gain authenticated access to the GHES Management Console with editor privileges to reach the syslog-ng configuration editor.

**Instructions**: Log in to the GHES Management Console using editor role credentials. Navigate to the configuration section where syslog-ng settings can be edited. Verify access by attempting to view or edit the syslog-ng configuration file.

**Expected Output**: Successful login and visibility of the syslog-ng configuration editor interface.

**Success Indicators**:
- Editor role permissions confirmed
- syslog-ng config editor loaded without errors

### Step 2: Inject Command in syslog-ng Configuration
procedure: [[procedures/Inject-Command-in-syslog-ng-Configuration]]

**Objective**: Exploit the command injection vulnerability by inserting malicious commands into the syslog-ng configuration, triggering execution with root privileges to establish SSH access.

**Instructions**: In the syslog-ng configuration editor, append or modify the config to include injected commands, such as spawning a reverse shell or adding an SSH key. Save the changes to trigger processing. The injected command executes as root due to insufficient sanitization.

For example, inject a command to add an SSH authorized key:

```bash
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD... attacker_key' >> /root/.ssh/authorized_keys && chmod 600 /root/.ssh/authorized_keys
```

Trigger the config reload via the console or service restart.

**Expected Output**: Command executes silently; attacker can then SSH to the appliance using the injected key.

**Success Indicators**:
- SSH connection established as root
- No alerts or failures in console logs

## Attack Chain Summary

### Key Achievements

1. Escalated from editor role to root privileges without direct console exploits
2. Achieved persistent SSH access to the GHES Linux appliance
3. Demonstrated RCE via configuration file injection in syslog-ng

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]]
- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
