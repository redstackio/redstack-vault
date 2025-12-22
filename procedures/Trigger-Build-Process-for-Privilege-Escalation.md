---
id: proc-004
tags:
  - build-trigger
  - privilege-escalation
  - container
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/setpasswd-id-execute]]'
verified: false
platforms:
  - Linux
  - Container
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Setuid and Setgid]]'
updated_at: '2025-12-14T17:30:58.226Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Setuid and Setgid]]'
---
# Trigger-Build-Process-for-Privilege-Escalation

## Summary

This procedure initiates the Semmle build, executing the prepare step to install the malicious package and achieve root via the setuid backdoor, even if the build fails.

## Description

Triggering the build runs the configured apt install, invoking postinst for backdoor deployment. The setuid binary persists, allowing root commands like 'id' via /usr/bin/setpasswd. This grants root in the container for DoS, evasion, or escape attempts.

## Requirements

1. Configured YAML with malicious steps
2. Uploaded artifacts in place
3. Build trigger permissions

## Defense

Defensive measures and detection strategies:

- Isolate build containers with no persistent storage
- Monitor for setuid binaries and ownership changes
- Fail builds on local package installs

## Objectives

1. Execute postinst for escalation
2. Confirm root access
3. Maintain backdoor post-failure

## Instructions

### Step 1: Initiate Build

**Context**: Start the Semmle build process.

Use Semmle UI or API to queue the build with the modified config.

> Prepare step runs apt, postinst deploys backdoor.

### Step 2: Monitor Execution

**Context**: Watch logs for installation and markers.

Check /opt/out/snapshot/log/build.log for 'pwned'.

### Step 3: Verify Escalation

**Context**: Test backdoor even if build fails.

Execute [[commands/setpasswd-id-execute]] manually or via log:

```bash
/usr/bin/setpasswd 'id'
```

> Expected: uid=0(root), confirming escalation.

**Success Indicators**: Root output, persistent binary.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Setuid and Setgid]]

### Sub-Techniques


## Commands Used

- [[commands/setpasswd-id-execute]]

## Tools Used


## Tags

- build-trigger
- privilege-escalation
- container
