---
id: tool-react-autolinker-001
url: 'https://www.npmjs.com/package/react-autolinker-wrapper'
tags:
  - react
  - xss
  - wrapper
type: tool
verified: false
platforms:
  - Web
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.608Z'
validated: true
submitted: true
---
# react-autolinker-wrapper

**Status**: Unverified

## Overview

A React component wrapper for Autolinker.js designed to automatically convert URLs, emails, and mentions in text to HTML anchors; vulnerable to XSS in version 1.1.0 due to unsanitized innerHTML.

## Description

This NPM package provides a simple React component for integrating Autolinker.js functionality into React apps. It processes text props via Autolinker.link() and sets them as innerHTML without sanitization, enabling injection attacks. Commonly used in text rendering features like chat or comments.

## Features

- Feature 1: Auto-links URLs, emails, Twitter handles, and phone numbers
- Feature 2: Configurable options for linking behavior
- Feature 3: React component integration for seamless use

## Installation

### Requirements

- Node.js >= 8
- React >= 16

### Install Commands

```bash
npm install react-autolinker-wrapper@1.1.0
```

## Basic Usage

```javascript
import AutolinkerWrapper from 'react-autolinker-wrapper';
<AutolinkerWrapper text="Visit example.com" />
```

### Common Options

| Option | Description |
|--------|-------------|
| text | Input text to link | 
| options | Autolinker config object |

## Examples

### Example 1: Basic Usage

```javascript
<AutolinkerWrapper text="Hello world https://example.com" />
```

### Example 2: Advanced Usage

```javascript
<AutolinkerWrapper text="Email: test@example.com" options={{email: true}} />
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of react-autolinker-wrapper in package.json
- innerHTML assignments in React components
- XSS alerts in browser console

## Related Procedures

- [[procedures/Trigger-XSS-with-Malicious-Input]]

## Related Tools

- [[tools/Autolinker.js]]
- [[tools/React]]

## References

- NPM page: https://www.npmjs.com/package/react-autolinker-wrapper
- HackerOne report: https://hackerone.com/reports/592525
