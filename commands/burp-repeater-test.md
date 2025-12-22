---
data: 'In Burp Repeater: Craft and send request'
tags:
  - http
  - testing
type: command
executor: gui
platforms:
  - Web
id: fdab729c-3feb-4040-94f2-e7a63a37aae7
created_at: '2025-12-13T09:01:26.184Z'
updated_at: '2025-12-13T09:01:26.184Z'
verified: false
validated: true
submitted: true
---
# burp-repeater-test

## Command

```bash
# Manual in Burp Suite Repeater: Paste request and send
```

## Description

This involves using Burp Suite's Repeater tab to manually craft, modify, and send HTTP requests for testing vulnerabilities like request smuggling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Request Body` | Custom HTTP request | Yes |

## Examples

### Basic Usage

Paste a standard GET request and send.

### Advanced Usage

Craft a smuggling payload and observe response.

## Expected Output

Server response in the Repeater interface, showing headers and body.

## Related

- [[tools/Burp-Suite]]
- [[procedures/Exploit-HTTP-Request-Smuggling-via-HTTP2]]
