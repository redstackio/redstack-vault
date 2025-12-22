---
tags:
  - xss
  - injection
  - meta-tag
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
  - WebView
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:55.815Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d942eec9-afa1-4b13-98fc-aa1a77995f6e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Load-Malicious-Webpage-with-Author-Meta-Injection

## Summary

This procedure involves hosting or accessing a webpage that embeds a malicious <meta name="author"> tag containing an escaped script payload, setting up the initial vector for XSS exploitation in Brave iOS ReaderMode.

## Description

The attack relies on the ReaderMode feature's use of the page's <meta name='author'> content, which is inserted unescaped into the %READER-CREDITS% template. By crafting a meta tag with content like "Evil <script nonce=%READER-TITLE-NONCE%>alert(document.location);</script><!--", the script evades initial detection and prepares for execution upon ReaderMode activation. This targets Brave iOS versions with the relaxed CSP allowing nonce-based scripts. Expected outcomes include payload delivery without triggering browser defenses, leading to subsequent XSS.

## Requirements

1. Control over a web server to host the malicious HTML (e.g., https://csrf.jp/2021/brave/author_xss.php)
2. Brave iOS browser on a test device
3. Network access to load the external URL

## Defense

Defensive measures and detection strategies:

- Sanitize and escape meta tag content before template insertion in ReaderMode
- Strengthen CSP to disallow inline scripts without valid nonces
- Monitor for anomalous meta tags in web traffic

## Objectives

1. Deliver the malicious author meta tag to the victim's browser
2. Ensure the page loads without immediate script execution
3. Position for ReaderMode trigger

## Instructions

### Step 1: Prepare Malicious HTML

**Context**: Create or access a webpage embedding the payload in the <head> section.

Embed the following in the HTML:

```html
<meta name="author" content="Evil &lt;script nonce=%READER-TITLE-NONCE%&gt;alert(document.location);&lt;/script&gt;!--">
```

> This escapes the script tags to prevent immediate execution while preserving the payload for later unescaping in ReaderMode.

### Step 2: Load in Brave iOS

**Context**: Navigate to the malicious URL using Brave iOS to simulate victim interaction.

Open Brave iOS and enter the URL, e.g., https://csrf.jp/2021/brave/author_xss.php.

> The page should render normally; use browser dev tools (if available on iOS) to verify the meta tag in the source.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection
- meta-tag
