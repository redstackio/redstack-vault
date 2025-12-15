---
tags:
  - open-redirect
  - phishing
  - xss-chain
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/inject-open-redirect-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:32:11.121Z'
sub_techniques: []
id: 8c539a20-7057-46f4-99d8-ea12acd67c31
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate-Open-Redirect-via-XSS

## Summary

This procedure chains the XSS vulnerability to perform an open redirect, allowing attackers to lure victims to phishing sites or bypass restrictions.

## Description

By injecting a <script> tag after URL breakout, the payload can redirect the browser to an arbitrary domain. This combines with XSS for stealthy attacks, such as after cookie theft, to deliver malware or harvest credentials.

## Requirements

1. Successful XSS execution confirmed
2. Target external site for redirect (e.g., google.com for POC)
3. Browser context for testing

## Defense

Defensive measures and detection strategies:

- Validate redirect URLs against a whitelist
- Use HTTP response headers like Content-Security-Policy for navigation
- Detect chained anomalies in session logs

## Objectives

1. Redirect to external site without user interaction
2. Enable phishing escalation
3. Show combined impact of XSS and redirect

## Instructions

### Step 1: Inject Redirect Script

**Context**: Use window.location in a script tag to force navigation.

**Command** ([[commands/inject-open-redirect-payload]]):
```bash
curl "https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=████:vwt2u5wngbk&siteBaseUrl=http://googl.com/%0a<script>window.location='https://google.com';</script>"
```

> Upon loading in a browser, the page redirects to google.com, confirming the open redirect vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/inject-open-redirect-payload]]

## Tools Used


## Tags

- open-redirect
- phishing
- xss-chain
