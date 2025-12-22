---
id: proc-uuid-1234
name: Construct-Malicious-next_url-for-XSS
tags:
  - xss
  - url-crafting
  - payload-injection
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:49.936Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Construct-Malicious-next_url-for-XSS

## Summary

This procedure involves crafting a malicious URL for the next_url parameter on the Pixiv Sketch account resignation success page, injecting a javascript: URI payload that will be reflected and executable upon page interaction.

## Description

The next_url parameter on https://sketch.pixiv.net/resign_request/success is vulnerable to reflected XSS because it accepts arbitrary input without validation, allowing javascript: schemes to be reflected into links or redirects. This enables attackers to execute JavaScript in the context of the victim's authenticated session, potentially stealing cookies, session tokens, or performing actions like data exfiltration. The attack requires the victim to have just completed account resignation to reach the success page.

## Requirements

1. Access to a web browser for URL construction and testing
2. Knowledge of URL encoding to obfuscate the payload
3. Victim interaction post-account deletion process

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation to whitelist only http/https schemes for next_url
- Sanitize reflected parameters using HTML entity encoding
- Use Content Security Policy (CSP) to block inline JavaScript execution
- Monitor for anomalous JavaScript alerts or network requests from the page

## Objectives

1. Inject executable JavaScript payload into the next_url parameter
2. Ensure payload survives URL encoding and reflection
3. Prepare for delivery to victim to achieve code execution

## Instructions

### Step 1: Encode the JavaScript Payload

**Context**: Create a basic proof-of-concept payload using javascript:alert to test execution, encoding it to prevent parsing issues.

No specific command; manually construct in browser address bar or text editor.

Example payload: `javascript:alert//(document.domain)`

URL-encoded: `javascript%3Aalert%2F%2F(document.domain)`

> This step ensures the payload is safe for HTTP transport. Test by pasting into a URL decoder tool.

### Step 2: Append to Base URL

**Context**: Combine the encoded payload with the vulnerable endpoint to form the full malicious URL.

Base URL: `https://sketch.pixiv.net/resign_request/success?next_url=`

Full URL: `https://sketch.pixiv.net/resign_request/success?next_url=javascript%3Aalert%2F%2F(document.domain)`

> Verify the URL loads the success page without errors. The payload should appear in the 'Back To Page' link or redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-crafting]]
