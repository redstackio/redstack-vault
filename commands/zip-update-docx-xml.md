---
type: command
executor: bash
data: 'zip -u xxe.docx [Content_Types].xml'
tags:
  - xxe
  - docx
  - zip
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# zip-update-docx-xml

## Command

```bash
zip -u $_DOCX_FILE $_XML_FILE
```

## Description

This command updates a specific XML file within a DOCX ZIP archive without recompressing the entire file, useful for injecting XXE payloads while maintaining file integrity during exploitation preparation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOCX_FILE | Path to the target DOCX file (ZIP archive) | Yes |
| $_XML_FILE | Path to the modified XML file to update (e.g., [Content_Types].xml) | Yes |
| -u | Update mode: Replace existing file in archive | Built-in |

## Examples

### Basic Usage

```bash
zip -u xxe.docx [Content_Types].xml
```

### Advanced Usage

```bash
zip -u -q malicious.docx word/document.xml
```

(The -q flag quiets output for scripting.)

## Expected Output

Updating: [Content_Types].xml (deflated 80%)

No errors; the archive size remains similar, indicating successful update without corruption.

## Related

- [[Related Procedure: Exploit-XXE-in-DOCX-Files]]
- [[Related Tool: OXML-XXE]]
