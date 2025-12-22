---
tags:
  - xss
  - self-xss
  - javascript
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
updated_at: '2025-12-14T03:15:36.136Z'
sub_techniques: []
id: 2c12cfbb-44a6-4b98-8dec-2dd483b1849d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Search-Box

## Summary

This procedure exploits the lack of input sanitization in the Jetpack.me search box by injecting a JavaScript payload, resulting in self-XSS where arbitrary code executes in the user's browser session.

## Description

The search functionality reflects user input directly into the HTML without escaping, allowing HTML tags and event handlers like onerror to execute. The payload `<img src=x onerror=alert(1)>` creates a broken image that triggers JavaScript on error, popping an alert. This is a self-XSS, impacting only the injector, with no cross-user effects. The attack targets the front page's 'Every feature!' search under http://jetpack.me/. Prerequisites include access to the search box from prior steps.

## Requirements

1. Located and focused search box on Jetpack.me
2. Web browser supporting JavaScript execution
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all reflected inputs
- Deploy Content Security Policy (CSP) to restrict inline script execution
- Monitor for suspicious JavaScript alerts or DOM manipulations in browser consoles

## Objectives

1. Deliver and execute malicious JavaScript via reflected input
2. Confirm vulnerability by observing alert execution
3. Demonstrate limited impact of self-XSS

## Instructions

### Step 1: Prepare Payload

**Context**: Construct a simple XSS payload to test injection.

Manual Action:

Copy the payload: `<img src=x onerror=alert(1)>`

> This payload uses an invalid image source to trigger the onerror event, executing alert(1).

### Step 2: Input and Submit

**Context**: Inject the payload into the vulnerable field to trigger reflection.

Manual Action:

Paste the payload into the search box and press Enter or click search.

> The input reflects immediately without sanitization, causing the alert to pop up, confirming successful self-XSS execution.

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
- [[self-xss]]
- [[JavaScript]]
