---
data: 'curl -s https://█████████.jetblue.com/sap/public/info'
tags:
  - recon
  - http
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 5177e4a0-802f-4c83-b721-2d4083e2d5fc
created_at: '2025-12-14T17:25:13.457Z'
updated_at: '2025-12-14T17:25:13.457Z'
verified: false
validated: true
submitted: true
---
# curl-access-sap-info

## Command

```bash
curl -s https://█████████.jetblue.com/sap/public/info
```

## Description

Retrieves exposed SAP system information from public endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| URL | SAP info endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -s https://█████████.jetblue.com/sap/public/info
```

### Advanced Usage

```bash
curl -s https://████.jetblue.com/sap/public/info | grep 'IP'
```

## Expected Output

Text or HTML with internal IPs and OS details.

## Related

- [[Related Procedure: Expose-SAP-Internal-Information-via-Public-Endpoints]]
