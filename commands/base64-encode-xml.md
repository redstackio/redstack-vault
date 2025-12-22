---
data: xml=`base64 response.xml`
tags:
  - encoding
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 24a0fda4-458a-4f3a-b7aa-c1824c17de18
created_at: '2025-12-11T03:47:39.217Z'
updated_at: '2025-12-11T03:47:39.217Z'
verified: false
validated: true
submitted: true
---
# base64-encode-xml

## Command

```bash
xml=`base64 response.xml`
```

## Description

Base64 encodes the response.xml file and stores it in the xml variable for use in HTTP requests, preparing SAML payloads for exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `base64` | Encodes the input file to base64 format | Yes |
| `response.xml` | Input XML file | Yes |

## Examples

### Basic Usage

```bash
xml=`base64 response.xml`
```

### Advanced Usage

```bash
xml=`base64 -w 0 response.xml`
```

## Expected Output

Base64-encoded string of the XML content stored in xml variable.

## Related

- [[commands/curl-send-forged-saml]]
- [[procedures/Base64-Encode-SAML-Response-XML]]
