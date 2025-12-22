---
type: command
executor: bash
data: cat $_INPUT_FILE | iconv -f UTF-8 -t UTF-16BE > $_OUTPUT_FILE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - encoding
  - obfuscation
  - xxe
verified: true
validated: true
---

# iconv-convert-utf8-to-utf16be

## Command

```bash
cat $_INPUT_FILE | iconv -f UTF-8 -t UTF-16BE > $_OUTPUT_FILE
```

## Description

This command converts an XML payload from UTF-8 to UTF-16 Big Endian (BE) encoding using iconv. In the context of XXE WAF bypass, the big-endian byte order provides additional obfuscation, evading WAFs that only normalize standard UTF-16 little-endian formats.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INPUT_FILE | Path to the input UTF-8 encoded XML file (e.g., base_xxe.xml) | Yes |
| $_OUTPUT_FILE | Path for the output UTF-16BE encoded file (e.g., utf16be_xxe.xml) | Yes |
| -f UTF-8 | Specifies input encoding (from UTF-8) | Built-in |
| -t UTF-16BE | Specifies output encoding (to UTF-16 Big Endian) | Built-in |

## Examples

### Basic Usage

```bash
cat base_xxe.xml | iconv -f UTF-8 -t UTF-16BE > utf16be_xxe.xml
```

### Advanced Usage

With error suppression:

```bash
cat base_xxe.xml | iconv -f UTF-8 -t UTF-16BE//IGNORE > utf16be_xxe.xml 2>/dev/null
```

## Expected Output

Silent success; output file created. Verify:

```bash
file utf16be_xxe.xml
```

Output: `utf16be_xxe.xml: Big-endian UTF-16 Unicode text`

Error example: `iconv: cannot convert` if encoding mismatch.

## Related

- [[Related Procedure]]: [[procedures/xml-external-entity-waf-bypass-via-character-encoding]]
- [[Related Command]]: [[commands/iconv-convert-utf8-to-utf16]]
