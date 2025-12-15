---
tags:
  - clickjacking
  - iframe
  - x-frame-options
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:12.342Z'
sub_techniques: []
id: 5bacbb96-ccd0-4af9-83dc-4bff1ede6c76
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-and-Demonstrate-Clickjacking

## Summary

This procedure inspects the HTTP response headers of the WakaTime embed page for missing X-Frame-Options and demonstrates the vulnerability by embedding the page in an external iframe, enabling potential UI redressing attacks.

## Description

Clickjacking exploits the lack of frame-busting headers like X-Frame-Options, allowing malicious sites to embed the target in an iframe and overlay invisible elements to hijack user interactions. On https://wakatime.com/share/embed, this could trick authenticated users into accessing or manipulating shared code data. The procedure uses curl for header inspection and a simple HTML file for proof-of-concept embedding. Outcomes include confirmation of frammability, highlighting risks like unauthorized dashboard actions. Requires local file editing and browser testing.

## Requirements

1. curl installed for header inspection
2. Text editor to create HTML demo file
3. Web browser to test iframe loading
4. Authenticated session (though demo works without for basic embedding)

## Defense

Defensive measures and detection strategies:

- Add X-Frame-Options: SAMEORIGIN to server responses
- Use Content-Security-Policy (CSP) frame-ancestors directive
- Log and alert on cross-origin iframe attempts

## Objectives

1. Verify absence of anti-framing headers
2. Demonstrate successful embedding from external context
3. Illustrate potential for UI overlay attacks

## Instructions

### Step 1: Inspect Response Headers

**Context**: Use curl to fetch and examine headers, confirming no X-Frame-Options is present.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://wakatime.com/share/embed
```

> Output should list headers like Server, Content-Type, but no X-Frame-Options. Absence confirms vulnerability. Pipe to grep if needed: `curl -I ... | grep -i frame` (expect no match).

### Step 2: Create and Test Iframe Demo

**Context**: Build a local HTML page to embed the target, simulating an attacker's malicious site.

**Command** (No command; file creation):

Create demo.html with:

```html
<!DOCTYPE html>
<html>
<head><title>Clickjacking PoC</title></head>
<body>
  <iframe src="https://wakatime.com/share/embed" width="100%" height="600"></iframe>
</body>
</html>
```

Open in browser.

> The iframe loads the WakaTime page fully. For advanced demo, add opacity and overlay: style="opacity:0.5; position:absolute;" and a fake button on top to capture clicks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-headers]]

## Tools Used


## Tags

- [[clickjacking]]
- [[iframe]]
- [[x-frame-options]]
