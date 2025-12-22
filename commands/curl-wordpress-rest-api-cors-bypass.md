---
data: >-
  curl -H "Origin: http://127.0.0.1:8080" -H "User-Agent: Mozilla/5.0 (Windows
  NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0" -H "Accept:
  application/json" https://blog.yelp.com/wp-json/
tags:
  - recon
  - cors
  - api
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: cd437602-5a03-41d5-8fc9-3e3fa2a73329
created_at: '2025-12-14T17:29:36.413Z'
updated_at: '2025-12-14T17:29:36.413Z'
verified: false
validated: true
submitted: true
---
# curl-wordpress-rest-api-cors-bypass

## Command

```bash
curl -H "Origin: http://127.0.0.1:8080" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0" -H "Accept: application/json" https://blog.yelp.com/wp-json/
```

## Description

This curl command sends a GET request to the WordPress REST API endpoint with a manipulated Origin header to exploit CORS misconfigurations, retrieving sensitive JSON data without authentication. Use it for initial reconnaissance on WordPress sites to discover exposed metadata and routes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Origin: http://127.0.0.1:8080"` | Sets a fake cross-origin header to bypass CORS validation | Yes |
| `-H "User-Agent: ..."` | Mimics a browser to avoid detection | Yes |
| `-H "Accept: application/json"` | Requests JSON response format | No |
| `https://blog.yelp.com/wp-json/` | Target API endpoint; replace with victim's URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "Origin: http://127.0.0.1:8080" https://target.com/wp-json/
```

### Advanced Usage

```bash
curl -H "Origin: http://127.0.0.1:8080" -H "Cookie: __cfduid=example" https://target.com/wp-json/wp/v2/users | jq '.[0].slug'
```

Add cookie for credentialed context if available; pipe to jq for parsing usernames.

## Expected Output

JSON object like: {"name":"Yelp Blog","description":"","url":"https://blog.yelp.com","namespaces":["oembed/1.0","wp/v2"],"routes":{"namespaces":[...],"/wp/v2/users":{...}}}. Look for user routes indicating enumeration.

## Related

- [[Related Procedure: Access-WordPress-REST-API-with-Manipulated-Origin]]
