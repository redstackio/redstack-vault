---
id: cmd-curl-get-test-001
data: 'curl -X GET https://iris.lystit.com/models/default/classification/color'
tags:
  - recon
  - api
type: command
output: HTTP/1.1 405 Method Not Allowed or endpoint details
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.477Z'
verified: false
validated: true
submitted: true
---
# curl-get-endpoint-test

## Command

```bash
curl -X GET https://iris.lystit.com/models/default/classification/color
```

## Description

This command performs a GET request to test the accessibility of the vulnerable endpoint in the Lyst Iris API, helping identify if it accepts requests and reveals method requirements.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `https://iris.lystit.com/models/default/classification/color` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://iris.lystit.com/models/default/classification/color
```

### Advanced Usage

```bash
curl -X GET -v https://iris.lystit.com/models/default/classification/color
```

## Expected Output

HTTP response indicating method not allowed (405) or API schema, confirming the endpoint's existence.

## Related

- [[Related Procedure: Identify Vulnerable Image URL Endpoint in Lyst Iris]]
