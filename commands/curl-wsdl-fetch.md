---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: curl $1?wsdl
tags:
  - recon
  - soap
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:19.521Z'
verified: false
validated: true
submitted: true
---
# curl-wsdl-fetch

## Command

```bash
curl http://target.com/soap?wsdl
```

## Description

Fetches the WSDL file from a SOAP endpoint to confirm service details and PHP SOAP usage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (positional) | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl http://example.com/soap?wsdl
```

### Advanced Usage

```bash
curl -k https://target.com/secure-soap?wsdl
```

## Expected Output

XML WSDL document with schema definitions, often including PHP class references.

## Related

- [[Related Procedure: Identify PHP SOAP Service]]
