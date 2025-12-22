---
data: >-
  curl -X POST -H "Content-Type: application/xml" --data "<xml>test</xml>"
  https://target/endpoint
tags:
  - xxe
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: c0d65c6f-e22e-4a7c-8471-e12ada95c57d
created_at: '2025-12-13T09:00:27.347Z'
updated_at: '2025-12-13T09:00:27.347Z'
verified: false
validated: true
submitted: true
---
# Curl Scan for XXE

## Command

```bash
curl -X POST -H "Content-Type: application/xml" --data "<xml>test</xml>" https://target/endpoint
```

## Description

This command sends a basic XML payload to probe if a web endpoint accepts and processes XML, helping identify potential XXE vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: application/xml"` | Sets XML content type | Yes |
| `--data "<xml>test</xml>"` | Basic XML payload | Yes |
| `https://target/endpoint` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/xml" --data "<xml>test</xml>" https://subdomain.informatica.com/endpoint
```

### Advanced Usage

```bash
curl -X POST -H "Content-Type: application/xml" --data "<?xml version=\"1.0\"?><root>test</root>" -v https://subdomain.informatica.com/endpoint
```

## Expected Output

HTTP response with status code 200 or XML-related errors, indicating processing.

## Related
- [[procedures/Craft-and-Send-XXE-Payload]]
- [[procedures/Identify-Vulnerable-XML-Endpoint]]
