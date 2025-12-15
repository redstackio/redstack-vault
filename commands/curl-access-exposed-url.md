---
id: cmd-uuid-001
data: 'curl -k https://crm.unikrn.com/███████'
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
updated_at: '2025-12-14T17:29:20.279Z'
verified: false
validated: true
submitted: true
---
# curl-access-exposed-url

## Command

```bash
curl -k https://crm.unikrn.com/███████
```

## Description

This command uses curl to fetch the contents of an exposed script file from the Unikrn CRM server, ignoring SSL verification to handle potential certificate issues. It is used to test for unauthorized access to sensitive web endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Insecure mode: skips SSL certificate verification | No |
| `https://crm.unikrn.com/███████` | Target URL of the exposed script | Yes |

## Examples

### Basic Usage

```bash
curl -k https://crm.unikrn.com/███████
```

### Header-Only Check

```bash
curl -I -k https://crm.unikrn.com/███████
```

## Expected Output

Raw script content or HTML/PHP code from the server, with a 200 OK status indicating successful access.

## Related

- [[Related Procedure: Access Exposed Script File]]
