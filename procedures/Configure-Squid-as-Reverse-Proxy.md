---
id: proc-config-squid-proxy-2023
tags:
  - configuration
  - reverse-proxy
  - squid
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:33.004Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Squid-as-Reverse-Proxy

## Summary

This procedure creates a configuration file for Squid to operate in reverse proxy mode, enabling the vulnerable Host header parsing that leads to the buffer overflow.

## Description

The configuration sets Squid to listen on port 9999 as an accelerator proxy, forwarding to a local backend on port 80. This mode triggers the overflow during Host header processing. Manual file creation is used since no command-line tool is involved. Outcomes: A functional config that exposes the vulnerability when requests are processed.

## Requirements

1. Installed Squid binary in local path
2. Text editor access (e.g., vi or nano) for config creation
3. Understanding of Squid ACLs and peer directives

## Defense

Defensive measures and detection strategies:

- Validate Squid configs for insecure proxy modes
- Use WAF to inspect Host headers for anomalies
- Log and alert on reverse proxy configurations in production

## Objectives

1. Enable reverse proxy functionality to mimic production setup
2. Define ACLs to allow controlled access
3. Prepare for vulnerability triggering without errors

## Instructions

### Step 1: Create Configuration File

**Context**: Manually write the squid.conf to set reverse proxy parameters.

**Command** (Manual):
No direct command; use a text editor to create `squid.conf` with:
```conf
http_port 9999 accel defaultsite=127.0.0.1 vhost vport=1
cache_peer 127.0.0.1 parent 80 0 no-query originserver name=myAccel
acl our_sites dstdomain your.main.website.name
http_access allow our_sites
cache_peer_access myAccel allow our_sites
cache_peer_access myAccel deny all
```

> Saves the file in the sbin directory. Expected output: Valid config file; test by running `squid -f squid.conf -k parse` (if available).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- configuration
- reverse-proxy
- squid
