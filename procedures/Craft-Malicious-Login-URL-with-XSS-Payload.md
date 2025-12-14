---
tags:
  - xss
  - url-crafting
  - javascript-uri
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.753Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 961a5bf1-3394-48c5-8d2c-233c8d3e678c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-Login-URL-with-XSS-Payload

## Summary

This procedure involves constructing a malicious URL for Avito.ru that embeds a reflected XSS payload in the 'next' parameter of the login redirect, exploiting the lack of sanitization to prepare for JavaScript execution upon authentication.

## Description

In the context of Avito.ru's login flow, the 'next' parameter after the #login fragment is reflected without validation, allowing attackers to inject javascript: URIs. This sets up a phishing attack where victims are directed to login, and post-authentication, the payload executes in their browser. The target environment is the web platform, specifically Avito.ru, requiring no special tools beyond a browser. Expected outcomes include a functional URL that loads the login page with the payload intact, leading to alert() execution or more malicious JS like cookie theft.

## Requirements

1. Access to a web browser for URL construction and testing
2. Knowledge of the target site's URL structure (e.g., https://www.avito.ru/...#login)
3. Optional: Social media accounts for testing login flows

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation and sanitization for redirect parameters, blocking javascript: and data: schemes
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for unusual login redirect patterns in server logs

## Objectives

1. Create a URL that injects XSS payload without triggering client-side errors
2. Ensure the payload survives the login redirect
3. Enable post-authentication JS execution for data exfiltration

## Instructions

### Step 1: Identify Base URL

**Context**: Start with a legitimate Avito.ru page URL that can lead to login, such as a location-specific page.

**Instructions**: Use the base URL like https://www.avito.ru/sankt-peterburg?verifyUserLocation=1.

> Append #login?next= to inject the payload.

### Step 2: Inject Payload

**Context**: Craft the javascript: URI to execute on redirect, e.g., alert(document.cookie) for testing cookie access.

**Instructions**: Full URL: https://www.avito.ru/sankt-peterburg?verifyUserLocation=1#login?next=javascript:alert(document.cookie);/

> Test by pasting into browser; it should load the login page with payload in address bar.

### Step 3: Validate URL

**Context**: Ensure the URL directs to login without immediate execution.

**Instructions**: Visit the URL in an incognito browser window and confirm the login prompt appears.

> No alert should pop yet; execution happens post-login.

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
- [[url-injection]]
