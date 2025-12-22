---
tags:
  - command-injection
  - nomad-template
  - smtp-config
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:30:27.187Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: db80c6ac-6efc-4717-924a-1673b73cf83a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Inject-Malicious-Nomad-Template-in-SMTP-Configuration

## Summary

This procedure involves crafting and submitting a malicious Nomad template payload into the SMTP configuration fields of the GitHub Enterprise Server Management Console, exploiting insufficient input sanitization to enable command injection during template rendering.

## Description

The SMTP configuration interface in the Management Console uses Nomad for rendering templates in settings like email templates or config values. Due to lack of proper validation, an editor can inject payloads that execute arbitrary Unix shell commands when Nomad processes the template. This targets versions prior to 3.12 and prepares for privilege escalation by embedding commands that modify access controls.

## Requirements

1. Active editor session in the Management Console
2. Knowledge of Nomad template syntax (e.g., {{ exec "command" }}) for injection
3. Target SMTP configuration form accessible

## Defense

Defensive measures and detection strategies:

- Input sanitization: Validate and escape all user inputs in template fields
- Template whitelisting: Restrict Nomad template functions to safe operations only
- Audit config changes: Log all SMTP modifications and review for anomalies

## Objectives

1. Embed command injection payload in SMTP fields
2. Save configuration to queue rendering
3. Avoid immediate detection during input

## Instructions

### Step 1: Access SMTP Configuration

**Context**: Navigate to the vulnerable SMTP settings form.

In the Management Console dashboard, go to Settings > Email > SMTP. The form includes fields for host, port, username, password, and custom templates.

> Form loads with current config; identify fields that accept template-like inputs.

### Step 2: Craft Malicious Payload

**Context**: Design a Nomad template that injects and executes a command, such as adding an SSH key.

In a vulnerable field (e.g., custom email from address), enter a payload like: "From: {{ exec \"echo 'ssh-rsa AAAAB3NzaC1yc2E... attacker_key\" >> /root/.ssh/authorized_keys\" }}" <example@domain.com>. This uses Nomad's exec function to run a shell command.

> Payload must be URL-encoded if needed; test syntax in a local Nomad environment if possible.

### Step 3: Submit and Save Configuration

**Context**: Apply the changes to trigger backend processing.

Fill other required fields with valid values, then click Save. The system queues the template for rendering.

> Expected output: Success message; no errors indicate payload acceptance.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- command-injection
- nomad-template
- smtp-config
