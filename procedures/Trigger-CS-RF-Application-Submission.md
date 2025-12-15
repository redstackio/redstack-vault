---
id: proc-csrf-trigger-hackerone
tags:
  - csrf
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-trigger-csrf]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:49.908Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-CS RF-Application-Submission

## Summary

This procedure exploits a CSRF vulnerability in HackerOne's program application feature by sending a GET request with the ?apply=true parameter, automatically submitting the application without any token validation or user confirmation.

## Description

The attack targets the program application endpoint on HackerOne, where accessing a URL like https://hackerone.com/{program}?apply=true triggers submission for logged-in users. No CSRF token is checked, allowing attackers to embed this in phishing links or iframes to spam applications en masse. This works for programs requiring manual approval and impacts user accounts by cluttering program queues with unwanted applications.

## Requirements

1. Victim's browser session on HackerOne (logged in or able to login)
2. Knowledge of target program handle (e.g., 'hackthedts')
3. Internet access for link delivery (e.g., email or social engineering)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing actions, even GET requests
- Add user confirmation dialogs for applications
- Monitor for unusual application spikes from single IPs or referrers
- Use Content-Security-Policy to block cross-origin requests

## Objectives

1. Force unauthorized application submission to target programs
2. Enable mass spamming of applications via social engineering
3. Demonstrate lack of validation in web endpoints

## Instructions

### Step 1: Craft Malicious URL

**Context**: Identify the target program and construct the exploitable URL.

**Command** ([[commands/curl-trigger-csrf]]):
```bash
curl -X GET "https://hackerone.com/hackthedts?apply=true" -H "Cookie: session=your-victim-cookie" -v
```

> This command simulates the GET request; in a real attack, deliver the URL via link. Expected output: HTTP 200 or redirect with success indicators like "Application submitted".

### Step 2: Deliver to Victim

**Context**: Trick the victim into accessing the URL in their authenticated session.

No specific command; use social engineering to send the link. Verify post-click by checking victim's HackerOne dashboard for new application.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-csrf]]

## Tools Used


## Tags

- [[csrf]]
- [[web]]
