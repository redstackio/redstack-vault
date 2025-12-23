---
url: 'https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API'
tags:
  - http
  - upload
  - javascript
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.687Z'
id: 2e0eb0e4-2301-4fa6-af64-ab2ab24d69f3
validated: true
submitted: true
---
# Fetch-API

**Status**: Unverified

## Overview

The Fetch API is a modern JavaScript interface for making HTTP requests, commonly used in browsers for uploading data like FormData to APIs during security testing.

## Description

Fetch provides a promise-based way to perform network requests, ideal for POSTing multipart data such as malicious files in web exploits. It's native to browsers, requiring no installation.

## Features

- Feature 1: Promise-based asynchronous requests
- Feature 2: Support for FormData and various content types
- Feature 3: Easy handling of responses and errors

## Installation

### Requirements

- Modern browser (Chrome, Firefox, etc.)

### Install Commands

No installation needed; available via window.fetch.

## Basic Usage

```javascript
fetch(url, options).then(response => response.text())
```

### Common Options

| Option | Description |
|--------|-------------|
| method | HTTP method (e.g., POST) |
| body | Request body (e.g., FormData) |
| headers | Custom headers |

## Examples

### Example 1: Basic Usage

```javascript
fetch('https://example.com/api', {method: 'POST', body: new FormData()})
```

### Example 2: Advanced Usage

```javascript
fetch('http://graphie-to-png.kasandbox.org/svg', {method: 'POST', body: form})
  .then(r => r.text())
  .then(data => console.log(data));
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Remote File Copy]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing POST requests with FormData to internal APIs
- Browser console activity during testing

## Related Procedures

- [[procedures/Upload-Malicious-Graphie-via-Legacy-API]]

## Related Tools

- [[XMLHttpRequest]]

## References

- MDN Fetch API Documentation
