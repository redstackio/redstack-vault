---
tags:
  - clickjacking
  - verification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:05.240Z'
sub_techniques: []
id: b05395b9-4f65-43e7-969e-15f0692baa14
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Verify Site Loading in Iframe

## Summary

This procedure tests whether the target site can be embedded in an iframe without restrictions, confirming the clickjacking vulnerability due to missing frame protection headers.

## Description

To exploit clickjacking, attackers must verify that the site loads in iframes from external domains. This procedure involves loading the created HTML in a browser and inspecting the render. Target environment: Local browser on any OS. Expected outcomes: Unrestricted loading, indicating vulnerability to UI redressing where users can be tricked into interacting with hidden elements for sensitive actions like entering credentials.

## Requirements

1. Web browser
2. Created HTML file from prior step
3. Internet connection

## Defense

Defensive measures and detection strategies:

- Use browser developer tools to check for frame errors
- Implement frame-ancestors in CSP to block unauthorized framing

## Objectives

1. Confirm iframe embedding success
2. Identify any restrictions
3. Validate exploitation potential

## Instructions

### Step 1: Load HTML File

**Context**: Open the test page in a browser to initiate embedding.

Double-click clickjack_test.html or open via File > Open in browser.

> The page should display with the iframe visible.

### Step 2: Inspect Iframe Content

**Context**: Verify the target site renders fully.

Check if https://sifchain.finance/ loads inside the iframe without blocking. Use browser dev tools (F12) to inspect network requests and console for errors.

> Expected output: Site content visible in iframe, no X-Frame-Options enforcement messages.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[verification]]
