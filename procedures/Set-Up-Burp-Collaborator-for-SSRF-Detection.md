---
id: abf6c79e-0397-43a0-afd9-8bc6be15dca6
name: Set-Up-Burp-Collaborator-for-SSRF-Detection
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.427Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Vulnerability Scanning]]'
sub_techniques: []
tags:
  - ssrf
  - monitoring
  - dns-recon
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Collaborator]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---

# Set-Up-Burp-Collaborator-for-SSRF-Detection

## Summary

This procedure sets up Burp Collaborator to generate a unique out-of-band monitoring domain, enabling the detection of server-side requests in SSRF scenarios by observing DNS resolutions and HTTP interactions from the target server.

## Description

In SSRF attacks, especially blind ones, attackers cannot see direct responses from internal requests. Burp Collaborator acts as an external beacon: the attacker embeds a Collaborator-generated URL in the vulnerable parameter, and any server-side fetch triggers observable DNS lookups or HTTP pings. This is ideal for confirming SSRF in GraphQL endpoints like 'allTicks' on pwapi.ex2b.com, where the 'source' parameter accepts arbitrary URLs. Prerequisites include Burp Suite Professional and network access to generate payloads.

## Requirements

1. Burp Suite Professional installed with Collaborator enabled.
2. Internet access for Collaborator server communication.
3. Basic knowledge of Burp interface.

## Defense

Defensive measures and detection strategies:

- Monitor outbound DNS queries from web servers for unusual domains.
- Implement URL allowlisting in application code to restrict server-side fetches.
- Use web application firewalls (WAFs) to block suspicious URL patterns in inputs.

## Objectives

1. Generate a unique monitoring domain for SSRF detection.
2. Start polling for interactions to capture blind requests.
3. Prepare for embedding the payload in vulnerable parameters.

## Instructions

### Step 1: Launch Burp Collaborator

**Context**: Open the Collaborator tool within Burp Suite to initialize monitoring.

No specific command; navigate via GUI: Burp Suite > Collaborator > Copy to clipboard (generates payload).

> This creates a unique domain like `abc123.oastify.com`. Expected output: Payload URL ready for use.

### Step 2: Start Polling

**Context**: Enable continuous monitoring for incoming interactions.

No specific command; in Collaborator tab, click "Poll now" and set to auto-poll.

> Burp will listen for DNS/HTTP hits. Expected output: Empty log initially, ready for events.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[ssrf]]
- [[monitoring]]
- [[dns-recon]]
