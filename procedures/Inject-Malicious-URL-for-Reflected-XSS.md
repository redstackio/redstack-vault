---
id: proc-reddit-xss-inject-001
tags:
  - xss
  - url-injection
  - payload-crafting
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:56:19.894Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Inject-Malicious-URL-for-Reflected-XSS

## Summary

This procedure crafts a malicious URL that injects an HTML event attribute into Reddit's sh.reddit.com comments API response, setting up a reflected XSS payload for subsequent execution.

## Description

The sh.reddit.com endpoint at /svc/shreddit/api/comments/askreddit/{thread_id} fails to sanitize URL parameters, allowing attackers to append payloads like 'onmouseover=alert(document.domain)' to the thread ID. When a victim navigates to this URL, the payload is reflected into the page HTML, embedding the event handler in elements like comment links. This enables client-side JavaScript execution in the browser context, potentially leading to session theft or data exfiltration. The attack requires no authentication and targets public-facing web applications with similar sanitization flaws.

## Requirements

1. Access to a web browser for URL construction and navigation
2. Knowledge of the target thread ID (e.g., t3_u9po1l from askreddit)
3. Victim interaction (visiting the URL)

## Defense

Defensive measures and detection strategies:

- Implement strict URL parameter sanitization and output encoding (e.g., HTML entity escaping)
- Use Content Security Policy (CSP) to block inline JavaScript execution
- Monitor for anomalous alert() calls or DOM manipulations in browser logs
- Deploy Web Application Firewall (WAF) rules to detect event handler injections like 'onmouseover='

## Objectives

1. Embed malicious JavaScript event handler in the page DOM
2. Prepare for payload trigger via user interaction
3. Achieve reflected injection without server-side execution

## Instructions

### Step 1: Identify Target Endpoint and Thread

**Context**: Locate a vulnerable comments thread on sh.reddit.com to base the payload on.

Use the base URL: https://sh.reddit.com/svc/shreddit/api/comments/askreddit/

Append a known thread ID, such as t3_u9po1l.

### Step 2: Craft the Payload

**Context**: Modify the URL to inject the XSS payload into the parameter.

Construct the full URL by encoding the payload and appending it:

https://sh.reddit.com/svc/shreddit/api/comments/askreddit/t3_u9po1l%20onmouseover=alert(document.domain)%20y=/t1_i5sxroa

> This URL injects the onmouseover event into the response, targeting elements rendered from the API.

### Step 3: Navigate to the URL

**Context**: Deliver the URL to the victim (e.g., via phishing link) and have them access it.

Open the crafted URL in a browser. Inspect the page source to confirm reflection.

> Expected: Payload appears in HTML as an attribute on a DOM element.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[JavaScript]]
