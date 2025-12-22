---
id: 54996d8f-7027-41f6-9664-723210c4002a
name: browser-enter-http-url
type: command
executor: browser
data: 'http://$_TARGET_URL'
output: null
created_at: '2023-04-06T03:56:17.451816+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
  - Browser
tags:
  - protocol-handler
  - browser-escape
verified: true
validated: true
---

# browser-enter-http-url

## Command

In the browser address bar, enter:

```text
http://$_TARGET_URL
```

## Description

This command invokes the HTTP protocol handler in the browser to access a web resource, testing or bypassing restrictions in a sandboxed environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The target website or IP (e.g., example.com) | Yes |

## Examples

### Basic Usage

```text
http://example.com
```

### Advanced Usage

```text
http://192.168.1.100:8080
```

## Expected Output

The browser loads the webpage or redirects to the HTTP resource. Success shows rendered content; failure may display an error like 'Access denied'.

## Related

- [[procedures/Browser-Escape-via-Unassociated-Protocols]]
