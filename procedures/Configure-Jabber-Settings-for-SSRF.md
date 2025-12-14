---
id: proc-phpbb-configure-jabber-001
tags:
  - ssrf
  - configuration-manipulation
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:10.149Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Jabber-Settings-for-SSRF

## Summary

This procedure involves setting the 'jabber server' to 127.0.0.1 and specifying a target port in the phpBB Jabber settings form, bypassing lack of validation to prepare for SSRF exploitation.

## Description

The phpBB ACP's Jabber settings allow input for server hostname and port without server-side validation, permitting localhost targets. This step manipulates these fields to point to internal resources, such as port 2222 for a demo SSH service or standard ports like 3306 for MySQL. In a vulnerable phpBB 3.3.1 setup, this enables the server to attempt connections on behalf of the attacker. Prerequisites: Admin access to ACP. Outcomes: Form ready for submission to trigger internal connections.

## Requirements

1. Active admin session in phpBB ACP
2. Knowledge of target internal ports (e.g., 2222 for SSH demo)
3. Web form interaction capability

## Defense

Defensive measures and detection strategies:

- Implement server-side allowlisting for hostnames/IPs in configuration forms
- Log all ACP form submissions with parameter values
- Use WAF rules to block localhost/internal IP submissions in admin panels

## Objectives

1. Input unvalidated localhost parameters
2. Target specific internal ports for testing
3. Set up for connection trigger

## Instructions

### Step 1: Enter Jabber Server as Localhost

**Context**: Set the server field to force connections to the local machine.

In the 'Jabber server' input field, enter `127.0.0.1`.

> Expected output: Field accepts the value without client-side rejection.

### Step 2: Specify Target Port

**Context**: Choose a port to probe for open services.

In the 'Jabber port' field, input a port number, e.g., `2222` for SSH or `3306` for MySQL.

> Expected output: Port field populated; form remains valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- configuration-manipulation
