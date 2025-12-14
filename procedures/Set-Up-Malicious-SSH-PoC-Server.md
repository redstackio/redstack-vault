---
id: proc-setup-poc-server
tags:
  - ssh
  - poc
  - server-setup
type: procedure
tools:
  - '[[tools/poc-py]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/run-poc-server]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1587.001]]'
updated_at: '2025-12-14T17:30:58.708Z'
skill_level: intermediate
impact_level: low
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1587.001]]'
---
# Set-Up-Malicious-SSH-PoC-Server

## Summary

This procedure sets up a Python-based malicious SSH server using the poc.py script to simulate responses that exploit vulnerabilities in PuTTY clients during connection and file transfer.

## Description

The procedure involves downloading the PoC from the GitHub repository and running it to create an SSH server on port 22. This server authenticates incoming connections and prepares crafted packets for file size processing, SSH string parsing, and channel requests to trigger buffer overflows and null pointer dereferences in vulnerable PuTTY PSCP clients (versions <= 0.66). It targets Windows platforms and requires Python environment. Expected outcomes include successful server startup and readiness to handle exploit triggers upon client connection.

## Requirements

1. Python 2/3 installed on the attacker's machine
2. Network access to host on port 22 (TCP)
3. Git or direct download access to the PoC repository

## Defense

Defensive measures and detection strategies:

- Block inbound SSH on port 22 if not needed; monitor for unusual SSH servers
- Use network intrusion detection systems (NIDS) to flag Python-based SSH implementations
- Patch PuTTY to version >0.66 and avoid connecting to untrusted SSH servers

## Objectives

1. Deploy a functional malicious SSH server for client exploitation
2. Prepare environment for post-authentication triggers
3. Enable logging of client interactions for verification

## Instructions

### Step 1: Download PoC Script

**Context**: Obtain the poc.py script from the public repository to set up the exploit server.

Execute [[commands/git-clone-poc]] to clone the repository:

```bash
git clone https://github.com/tintinweb/pub/tree/master/pocs/cve-2016-2563
cd pocs/cve-2016-2563
```

> This downloads the script; verify the file is present.

### Step 2: Run the Malicious Server

**Context**: Launch the Python script to start listening for SSH connections and prepare malicious responses.

Execute [[commands/run-poc-server]]:

```bash
python poc.py
```

> The server binds to port 22 and outputs confirmation; it handles authentication and waits for client file transfer requests to send overflow payloads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1587.001]] Develop Capabilities: Malware

### Sub-Techniques

- N/A

## Commands Used

- [[commands/run-poc-server]]
- [[commands/git-clone-poc]]

## Tools Used

- [[tools/poc-py]]

## Tags

- ssh
- poc
- server-setup
