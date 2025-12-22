---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - xss
  - sanitizer-analysis
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
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:55:20.934Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-HTML-Sanitizer-in-Messaging-Functionality

## Summary

This procedure involves inspecting and testing the HTML sanitizer used in MercadoLibre's messaging functionality to understand its tag whitelisting and identify potential weaknesses for XSS exploitation.

## Description

In the context of web applications like MercadoLibre's messaging system, HTML sanitizers filter user input to prevent XSS by allowing only safe tags. This procedure requires a valid account to send test messages and uses browser tools to analyze rendering. The goal is to map allowed tags (e.g., <p>) and blocked ones (e.g., <script>), setting the stage for bypass techniques. Expected outcome: A documented list of sanitizer behaviors confirming limited tag support.

## Requirements

1. Valid MercadoLibre account with messaging access.
2. Modern web browser with developer tools (e.g., Chrome DevTools).
3. Recipient account or incognito mode for testing received messages.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation beyond basic sanitization.
- Monitor for unusual message content patterns in logs.
- Use Content Security Policy (CSP) to restrict script execution.

## Objectives

1. Identify allowed and blocked HTML tags in the sanitizer.
2. Understand parser behavior for future bypass attempts.
3. Confirm the vulnerability scope in messaging inputs.

## Instructions

### Step 1: Inspect Messaging Interface

**Context**: Examine the input field and submission process to locate sanitization points.

Open the messaging interface on www.mercadolibre.com.ar, right-click the input field, and select "Inspect Element" in DevTools. Look for any client-side sanitization scripts or attributes like contenteditable.

### Step 2: Test Basic Tags

**Context**: Submit simple payloads to observe filtering.

Send messages with tags like <p>Test</p>, <script>alert(1)</script>, and <img src=x onerror=alert(1)>. View the received message in another session and inspect the HTML source.

> The sanitizer will strip <script> and <img> events but preserve <p>.

### Step 3: Document Behaviors

**Context**: Record findings for analysis.

Note allowed tags (e.g., <p>, <br>) and how attributes/events are handled. Test edge cases like nested tags.

**Expected Output**: Log showing <p> allowed, others blocked.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[sanitizer-analysis]]
