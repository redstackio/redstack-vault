---
tags:
  - command-injection
  - cgi
  - rce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Embedded Network Switch
  - Linux
techniques:
  - '[[Unix Shell]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 15777c43-0104-43cf-9a0f-69b66a4acf07
created_at: '2025-12-14T17:29:44.358Z'
updated_at: '2025-12-14T17:29:44.358Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Inject-OS-Command-via-CGI-Script

## Summary

This procedure exploits the lack of input sanitization in the EdgeSwitch Web GUI's CGI script to inject and execute arbitrary OS commands, achieving remote code execution as root.

## Description

The vulnerable CGI script processes user input from web forms or parameters without proper escaping, allowing attackers to append shell metacharacters (e.g., semicolons) followed by commands. This is tested by injecting simple commands like `id` into fields during legitimate operations, such as configuration submissions. The target is the web interface of EdgeSwitch firmware <1.7.1, running on an embedded Linux system. Prerequisites include an active operator session.

## Requirements

1. Active Privilege-1 session from prior login
2. Knowledge of the vulnerable CGI endpoint (e.g., via form inspection)
3. Ability to craft HTTP requests with modified parameters

## Defense

Defensive measures and detection strategies:

- Upgrade to firmware version 1.7.1 or later, which patches sanitization
- Implement input validation and whitelisting in web applications
- Log and monitor anomalous HTTP requests and command executions in device syslog

## Objectives

1. Inject OS command into unsanitized input
2. Achieve initial code execution
3. Confirm injection success via output

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate a CGI script handling user input, such as a diagnostic or config page.

Use browser dev tools to inspect forms. Look for POST requests to CGI paths like `/cgi-bin/script.cgi`.

> Note parameters that are reflected or processed without escaping.

### Step 2: Craft Injection Payload

**Context**: Modify the request to include a command injection payload.

Intercept the request (e.g., via proxy or direct edit) and append `; <command>` to a vulnerable parameter, e.g., `param=value; id`.

> Submit the modified request. The command executes server-side as root due to CGI privileges.

### Step 3: Observe Execution

**Context**: Verify the injection by checking response or side effects.

Look for command output in the HTTP response body or error messages.

> Expected: Output like `uid=0(root)` indicating root execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[command-injection]]
- [[cgi]]
- [[rce]]
