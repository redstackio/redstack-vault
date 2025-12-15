---
data: xml=`base64 response.xml`
tags:
  - encoding
  - saml
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:43.191Z'
id: 41ecd69b-8395-4a03-8045-bef99ff717fd
verified: false
validated: true
submitted: true
---
# base64-encode-saml

## Command

```bash
xml=`base64 response.xml`
```

## Description

This command base64-encodes the contents of a SAML XML file (response.xml) and stores the result in a shell variable 'xml' for use in HTTP requests, commonly in SAML exploitation workflows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `response.xml` | Input file containing the SAML XML to encode | Yes |

## Examples

### Basic Usage

```bash
xml=`base64 response.xml`
```

### Advanced Usage

To encode and immediately use:

```bash
xml=`base64 response.xml` && echo $xml | head -c 50
```

## Expected Output

The 'xml' variable will contain a base64 string representing the XML, e.g., 'PHNhb...==' with no errors if the file exists.

## Related

- [[Related Procedure: Base64-Encode-SAML-Response]]
