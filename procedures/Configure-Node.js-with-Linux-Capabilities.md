---
id: proc-configure-node-capabilities
tags:
  - linux
  - capabilities
  - nodejs
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/setcap-configure-capabilities]]'
  - '[[commands/getcap-check-capabilities]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:36.350Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Configure Node.js with Linux Capabilities

## Summary

This procedure sets Linux capabilities on the Node.js binary to grant it elevated privileges without full root access, creating the setup for exploiting environment variable handling flaws in Node.js on Linux systems.

## Description

In scenarios where Node.js services need to bind to low ports (e.g., 80) or perform other privileged operations, administrators often use Linux capabilities like CAP_NET_BIND_SERVICE via the setcap utility. However, this procedure highlights the vulnerability context where such configurations can be abused if environment variables are not properly sanitized. The target environment is a Linux system with Node.js installed, and the outcome is a capable binary ready for exploitation testing. Prerequisites include root access for initial setup simulation.

## Requirements

1. Root or sudo access on the Linux system to apply capabilities
2. Node.js installed (e.g., /usr/bin/node)
3. libcap2-bin package for setcap and getcap utilities

## Defense

Defensive measures and detection strategies:

- Avoid using capabilities on Node.js binaries; run services as non-root or use containers
- Audit environment variables in service definitions (e.g., systemd units) to sanitize untrusted inputs
- Monitor setcap usage via auditd rules on capability changes

## Objectives

1. Apply specific Linux capabilities to Node.js for privileged operations
2. Verify the configuration to ensure exploit conditions are met
3. Simulate a vulnerable service setup for testing privilege escalation paths

## Instructions

### Step 1: Apply Capabilities to Node.js Binary

**Context**: Use setcap to grant the Node.js executable the CAP_NET_BIND_SERVICE capability, which is commonly misconfigured and leads to the environment variable exception flaw.

**Command** ([[commands/setcap-configure-capabilities]]):
```bash
sudo setcap 'cap_net_bind_service=+ep' /usr/bin/node
```

> This command sets the effective (e) and permitted (p) bits for CAP_NET_BIND_SERVICE on the Node.js binary, allowing it to bind to privileged ports. Expected output is no error message, indicating success.

### Step 2: Verify Capabilities Application

**Context**: Confirm the capabilities are correctly applied to ensure the binary is in a vulnerable state for environment variable injection.

**Command** ([[commands/getcap-check-capabilities]]):
```bash
getcap /usr/bin/node
```

> This checks the capabilities on the binary. Expected output: `/usr/bin/node = cap_net_bind_service+eip`, confirming the setup.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques

- None

## Commands Used

- [[commands/setcap-configure-capabilities]]
- [[commands/getcap-check-capabilities]]

## Tools Used

- None

## Tags

- [[linux]]
- [[capabilities]]
- [[nodejs]]
