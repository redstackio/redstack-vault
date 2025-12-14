---
id: cmd-curl-basic-get
data: 'curl -X GET https://target/xmlrpc.php'
tags:
  - recon
  - http
type: command
output: XML-RPC server accepts POST requests only.
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:46.005Z'
verified: false
validated: true
submitted: true
---
# curl-basic-get

## Command

```bash
curl -X GET https://target/xmlrpc.php
```

## Description

This command performs a basic GET request to probe the xmlrpc.php endpoint, confirming its presence and POST-only behavior in WordPress setups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `https://target/xmlrpc.php` | Target URL to query | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://example.com/xmlrpc.php
```

### Advanced Usage

```bash
curl -X GET -v https://target/xmlrpc.php
```

## Expected Output

HTTP response with body: "XML-RPC server accepts POST requests only." indicating the endpoint is active.

## Related

- [[commands/curl-xml-post]]
- [[procedures/Confirm-xmlrpc-Endpoint]]
