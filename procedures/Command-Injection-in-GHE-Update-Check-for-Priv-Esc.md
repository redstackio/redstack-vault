---
id: proc-gh-cmd-inj-001
tags:
  - command-injection
  - privilege-escalation
  - rce
  - github-enterprise
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:35.707Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Command-Injection-in-GHE-Update-Check-for-Priv-Esc

## Summary

This procedure exploits a command injection vulnerability in the ghe-update-check feature of GitHub Enterprise Server during HTTP proxy configuration, allowing an authenticated editor user to execute arbitrary commands and escalate privileges to root-level SSH access on the appliance.

## Description

The vulnerability stems from insufficient input validation in the Management Console's HTTP proxy setup process, where user-supplied proxy details are passed to the ghe-update-check script without proper sanitization. An attacker with editor access can inject shell metacharacters (e.g., semicolons or pipes) into fields like the proxy URL to chain commands. This leads to remote code execution (RCE) on the underlying Linux appliance, enabling privilege escalation to root via techniques like spawning a shell or installing SSH keys. The attack requires initial access to a vulnerable GHE instance (versions before 3.12) and affects the entire appliance, potentially compromising all hosted repositories and data. Fixes were applied in patch releases for version 3.12 and later.

## Requirements

1. Editor role access to the GitHub Enterprise Server Management Console
2. Network access to the GHE appliance's admin interface (typically HTTPS on port 8443)
3. Vulnerable GHE version (prior to 3.12)
4. Basic knowledge of Linux shell commands for payload crafting

## Defense

Defensive measures and detection strategies:

- Upgrade to GitHub Enterprise Server 3.12 or later to apply input validation patches
- Restrict Management Console access to trusted administrators only; use role-based access control (RBAC) to limit editor privileges
- Monitor appliance logs for anomalous command executions in ghe-update-check or proxy setup events; enable audit logging for Management Console actions
- Implement web application firewall (WAF) rules to detect injection patterns in admin interfaces
- Regularly audit SSH access and disable unnecessary root logins

## Objectives

1. Execute arbitrary commands on the GHE appliance as root
2. Gain persistent SSH access for full administrative control
3. Exfiltrate sensitive data or pivot to other systems if chained with further exploits

## Instructions

### Step 1: Access Management Console and Navigate to Proxy Setup

**Context**: Log in with editor credentials and locate the vulnerable configuration to prepare the injection point.

Log in to the Management Console at `https://<ghe-host>/manage` using editor privileges. Navigate to **Settings > Network > HTTP Proxy** or the update check configuration section where ghe-update-check is invoked.

> Expected output: Form fields for proxy host, port, and URL become editable.

### Step 2: Craft and Inject Command Payload

**Context**: Insert a command injection payload into the proxy input field to execute shell commands during the update check process.

In the proxy URL or host field, enter a payload like `http://legit-proxy.com; /bin/bash -c 'echo "root:$(id)" > /tmp/esc.txt && chmod 777 /tmp/esc.txt' #` (adjust for actual escalation, e.g., adding SSH keys: `; mkdir -p /root/.ssh && echo 'ssh-rsa AAAAB3NzaC1yc2E... attacker_key' >> /root/.ssh/authorized_keys && chmod 600 /root/.ssh/authorized_keys #`). Save or trigger the proxy setup to invoke ghe-update-check.

> This exploits the lack of validation, passing the input to a shell command. Expected output: Injected command runs silently; verify by checking for side effects like file creation in /tmp or SSH access.

### Step 3: Escalate and Verify Root Access

**Context**: Use the executed command to gain root shell or SSH, confirming escalation.

If the payload installed an SSH key, connect via SSH: `ssh root@<ghe-host>`. Alternatively, if a reverse shell was injected (e.g., via netcat listener), capture the connection on the attacker's machine.

> Expected output: Root shell prompt (`root@ghe:~#`) or successful SSH login without password.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- command-injection
- rce
- privilege-escalation
- github-enterprise
- linux
