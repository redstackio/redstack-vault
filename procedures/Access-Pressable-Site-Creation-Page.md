---
tags:
  - web-access
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:32.027Z'
sub_techniques: []
id: 24626819-d2bd-4312-bce5-44b0945ac021
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Pressable-Site-Creation-Page

## Summary

This procedure involves navigating to the site creation page on try.pressable.com to initiate access to the vulnerable Display Name input field, serving as the entry point for the XSS and HTML injection attack.

## Description

In the context of exploiting web vulnerabilities, this step ensures the attacker reaches the public-facing site creation interface without authentication barriers. The target environment is the Pressable platform's try.pressable.com domain, where insufficient frontend validation allows subsequent payload injection. Expected outcomes include loading the form for further manipulation.

## Requirements

1. Web browser with JavaScript enabled
2. Internet connectivity to access https://try.pressable.com/
3. No special permissions or VPN needed

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on site creation endpoints to prevent abuse
- Monitor access logs for unusual patterns from the site creation page
- Use web application firewalls (WAF) to block suspicious navigation

## Objectives

1. Gain access to the vulnerable input interface
2. Confirm the page is publicly accessible
3. Prepare for payload injection without disruptions

## Instructions

### Step 1: Navigate to Target URL

**Context**: Directly access the site creation page to begin the workflow.

No command required; use browser navigation.

Open your web browser and enter the URL https://try.pressable.com/ in the address bar. Press Enter to load the page.

> This loads the interface. Expected output: The site creation form appears, including fields like Display Name.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[access]]
