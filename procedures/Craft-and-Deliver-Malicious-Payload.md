---
id: proc-vk-payload-craft
tags:
  - xss
  - payload
  - delivery
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.389Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft and Deliver Malicious Payload

## Summary

This procedure details creating an encoded JavaScript payload for DOM-based XSS in vk.link and delivering it to victims via shared links, exploiting unsafe client-side handling for script injection.

## Description

Once the vulnerability is identified, craft payloads that execute in the browser context, such as stealing cookies. Delivery relies on social engineering, as vk.link shortens URLs that process params client-side. Reported in 2020, this allows low-impact attacks like session theft. Requires URL encoding to evade basic filters; test in isolated environment.

## Requirements

1. URL encoder (JS console or online tool)
2. Attacker-controlled domain for exfiltration
3. Victim interaction (clicking link)

## Defense

Defensive measures and detection strategies:

- URL validation and whitelisting on client-side
- Escape special characters in JS inputs
- Log and alert on suspicious URL patterns in access logs

## Objectives

1. Generate executable payload
2. Shorten and obfuscate via vk.link
3. Ensure delivery triggers execution

## Instructions

### Step 1: Encode Payload

**Context**: Create JS that runs on load.

In browser console: encodeURIComponent('alert(document.domain);') to get %27alert%28document.domain%29%3B%27. Build full payload: javascript: + encoded.

> Expected: Payload ready for URL insertion.

### Step 2: Integrate into vk.link

**Context**: Use the service to shorten malicious URL.

Go to vk.link, input base URL with payload param, e.g., https://example.com?x=<encoded>. Generate short link.

> Success: Shortened URL without rejection.

### Step 3: Deliver to Victim

**Context**: Simulate phishing.

Share link via email or message: "Check this VK link: [short_url]". Victim clicks, payload executes.

> Expected: Script runs in their session.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[JavaScript]]
- [[Phishing]]
