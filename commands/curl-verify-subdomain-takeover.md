---
id: cmd-curl-verify-takeover
data: 'curl https://api.legalrobot.com'
tags:
  - verification
  - web
  - recon
type: command
output: Hello World!<!--FRANS ROSEN-->\n
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.583Z'
verified: false
validated: true
submitted: true
---
# curl-verify-subdomain-takeover

## Command

```bash
curl https://api.legalrobot.com
```

## Description

This command retrieves the HTTP response from the target subdomain to verify if the takeover was successful by checking for custom injected content rather than the original error page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://api.legalrobot.com` | The URL of the subdomain to fetch | Yes |

## Examples

### Basic Usage

```bash
curl https://api.legalrobot.com
```

### Advanced Usage

```bash
curl -v https://api.legalrobot.com
```

## Expected Output

Custom content such as 'Hello World!<!--FRANS ROSEN-->', confirming the subdomain now serves attacker-controlled material.

## Related

- [[Related Procedure: Verify Subdomain Takeover with Curl]]
