---
data: 'curl -v https://example.com'
tags:
  - http
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.710Z'
id: cd682982-5bec-4774-b191-5648d8bf8cf8
verified: false
validated: true
submitted: true
---
# curl HTTP Request

## Command

```bash
curl -v https://example.com
```

## Description

Curl sends HTTP requests to verify web content, useful for checking if a subdomain serves expected (or arbitrary) content post-takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output including headers | No |
| `URL` | Target URL to fetch | Yes |

## Examples

### Basic Usage

```bash
curl https://███████.target.com
```

### Advanced Usage

```bash
curl -v -H "User-Agent: Mozilla/5.0" https://███████.target.com
```

## Expected Output

HTML or content from the page, e.g., "<html>Takeover successful</html>" if verified.

## Related

- [[Related Procedure: Verify Subdomain Takeover]]
