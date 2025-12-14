---
tags:
  - package-install
  - ssh-keygen
  - dependencies
type: procedure
tools:
  - '[[tools/apt]]'
  - '[[tools/ssh-keygen]]'
  - '[[tools/python3-scapy]]'
  - '[[tools/openssh-client]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/apt-install-scapy-openssh]]'
  - '[[commands/ssh-keygen-ed25519]]'
verified: false
platforms:
  - Linux
  - Ubuntu
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Audio Capture]]'
updated_at: '2025-12-14T17:28:44.903Z'
sub_techniques: []
id: 54a8e774-2e7e-45d3-b82b-e28ad8788ed3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Audio Capture]]'
---
# Install-Dependencies-and-Generate-SSH-Key

## Summary

Inside the pod, installs Scapy for packet manipulation and OpenSSH client, then generates an ed25519 SSH key pair to be injected via the MITM attack.

## Description

The Ubuntu container requires python3-scapy for crafting and sniffing packets targeting the metadata service, and openssh-client for post-exploitation SSH. The key is generated without a passphrase for automated injection during the SSH provisioning request interception.

## Requirements

1. Interactive shell in the ubuntu-node pod
2. Internet access for apt repositories
3. Root privileges in the container (default)

## Defense

Defensive measures and detection strategies:

- Block apt installs in untrusted containers
- Monitor for SSH key generation in pods
- Use immutable containers without package managers

## Objectives

1. Equip the pod with tools for network attacks
2. Create authentication credentials for host access
3. Enable SSH connection post-injection

## Instructions

### Step 1: Update and Install Packages

**Context**: Prepare the environment with required libraries.

**Command** ([[commands/apt-install-scapy-openssh]]):
```bash
apt update && apt install -y python3-scapy openssh-client
```

> Installs dependencies. Expected output: Packages downloaded and configured.

### Step 2: Generate SSH Key Pair

**Context**: Produce a key for MITM injection into metadata.

**Command** ([[commands/ssh-keygen-ed25519]]):
```bash
ssh-keygen -t ed25519 -f /root/.ssh/id_ed25519 -N ""
```

> Creates key. Expected output: Your identification has been saved... (no passphrase).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Audio Capture]] Audio Capture (adapted to package install for tool acquisition)

### Sub-Techniques

- None

## Commands Used

- [[commands/apt-install-scapy-openssh]]
- [[commands/ssh-keygen-ed25519]]

## Tools Used

- [[tools/apt]]
- [[tools/ssh-keygen]]
- [[tools/python3-scapy]]
- [[tools/openssh-client]]

## Tags

- installation
- key-generation
