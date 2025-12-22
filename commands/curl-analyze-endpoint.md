---
data: 'curl -X GET https://mobile.starbucks.com.sg/upload.ashx -v'
tags:
  - recon
  - http-probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 893abb6d-2f05-4b84-8e92-9bd048de0cf8
created_at: '2025-12-14T05:32:13.790Z'
updated_at: '2025-12-14T05:32:13.790Z'
verified: false
validated: true
submitted: true
---
# curl-analyze-endpoint

## Command

```bash
curl -X GET https://mobile.starbucks.com.sg/upload.ashx -v
```

## Description

This command performs a verbose GET request to the target .ashx endpoint to analyze its response headers, status, and any exposed information about file handling in the ASP.NET environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `https://mobile.starbucks.com.sg/upload.ashx` | Target endpoint URL | Yes |
| `-v` | Verbose output for headers and details | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://mobile.starbucks.com.sg/upload.ashx -v
```

### Advanced Usage

```bash
curl -X GET https://mobile.starbucks.com.sg/upload.ashx -v -H "User-Agent: Mozilla/5.0"
```

## Expected Output

HTTP/1.1 200 OK or 405 Method Not Allowed, with headers like Server: Microsoft-IIS, indicating ASP.NET. No body content expected for GET on upload handler.

## Related

- [[Related Procedure: Analyze-File-Upload-Endpoint]]
