---
tags:
  - clickjacking
  - recon
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
updated_at: '2025-12-14T17:28:05.245Z'
sub_techniques: []
id: f104f7d8-90ed-4395-9e15-6f79d32c5027
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Acquire Target URL for Clickjacking Test

## Summary

This procedure involves identifying and copying the URL of a web application potentially vulnerable to clickjacking, serving as the initial step in demonstrating UI redressing attacks.

## Description

In a clickjacking attack, the first step is to select a target site lacking proper frame protection, such as the X-Frame-Options header. This procedure focuses on obtaining the exact URL, like https://sifchain.finance/, through manual inspection or prior reconnaissance. The target environment is any publicly accessible web application. Expected outcomes include a confirmed accessible URL ready for embedding tests, enabling attackers to proceed to iframe exploitation and trick users into interacting with hidden elements for actions like authorizing transactions.

## Requirements

1. Internet access to verify URL
2. Web browser for initial site visit
3. Basic knowledge of the target application

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) with frame-ancestors directive
- Regularly scan response headers for X-Frame-Options presence using tools like securityheaders.com

## Objectives

1. Secure the target URL for exploitation testing
2. Confirm site accessibility
3. Prepare for iframe embedding

## Instructions

### Step 1: Identify and Copy Target URL

**Context**: Locate the URL of the site to test for clickjacking vulnerability.

No specific command required; manually copy the URL https://sifchain.finance/ from browser address bar or documentation.

> Verify by pasting into a new browser tab and ensuring the site loads.

### Step 2: Document the URL

**Context**: Store the URL for use in subsequent steps.

Save the URL in a text file or note it down for reference in HTML iframe src.

> Expected output: URL string ready for embedding.

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
- [[recon]]
