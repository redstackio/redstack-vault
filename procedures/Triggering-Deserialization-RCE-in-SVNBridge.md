---
id: proc-uuid-9012
tags:
  - deserialization
  - rce
  - svnbridge
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-svnbridge-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation of Remote Services]]'
updated_at: '2025-12-14T17:23:32.114Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation of Remote Services]]'
---
# Triggering-Deserialization-RCE-in-SVNBridge

## Summary

This procedure triggers unsafe deserialization of untrusted data from memcached in the SVNBridge component of GitHub Enterprise Server, leading to remote code execution when the SSRF-chained payload is processed.

## Description

SVNBridge in GitHub Enterprise Server deserializes data from sources like memcached without proper validation, allowing arbitrary object instantiation and code execution. After SSRF delivers the malicious serialized payload (e.g., a gadget chain exploiting Java deserialization), triggering an SVN operation invokes the deserializer on the untrusted input. This affects versions prior to 3.6, where patches added validation. The attack assumes SVNBridge is enabled for SVN repository bridging.

## Requirements

1. SVNBridge component active on the target GitHub Enterprise Server
2. Prior SSRF success to populate memcached with payload
3. Network access to SVNBridge endpoints
4. Understanding of deserialization gadgets (e.g., for .NET or Java runtime)

## Defense

Defensive measures and detection strategies:

- Apply patches for GitHub Enterprise Server >= 3.6 to include deserialization validation
- Avoid deserializing untrusted data; use safe formats like JSON with schema validation
- Enable runtime protections like .NET serializers with type whitelisting or Java's SerialFilter
- Log and alert on deserialization errors or unusual object instantiations in application logs

## Objectives

1. Process the memcached payload through SVNBridge deserializer
2. Achieve RCE via gadget chain execution
3. Verify impact without full compromise if possible

## Instructions

### Step 1: Invoke SVNBridge Operation

**Context**: Send a request to SVNBridge that sources data from the memcached key set via SSRF, triggering deserialization.

**Command** ([[commands/curl-svnbridge-trigger]]):
```bash
curl -X POST 'https://target-github-enterprise/svnbridge/deserialize-endpoint' \
  -d '<svn-op><source>memcached://malicious-key</source></svn-op>' \
  -H 'Content-Type: application/xml'
```

> This XML payload directs SVNBridge to fetch and deserialize from memcached. Expected output: RCE execution (e.g., command output in response or reverse shell); errors may indicate 'deserialization failed' if payload invalid.

### Step 2: Validate RCE

**Context**: Check for signs of execution, such as a listener for reverse shell if payload includes one.

**Command** (use netcat listener):
```bash
nc -lvnp 4444
```

> Run this on attacker machine before triggering. Expected output: Incoming connection with shell if RCE succeeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation of Remote Services]]

### Sub-Techniques


## Commands Used

- [[commands/curl-svnbridge-trigger]]

## Tools Used


## Tags

- deserialization
- rce
- svnbridge
