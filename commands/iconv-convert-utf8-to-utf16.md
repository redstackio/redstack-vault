---
type: command
executor: bash
data: cat $_INPUT_FILE | iconv -f UTF-8 -t UTF-16 > $_OUTPUT_FILE
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

# iconv-convert-utf8-to-utf16

## Command

```bash
cat $_INPUT_FILE | iconv -f UTF-8 -t UTF-16 > $_OUTPUT_FILE
```

## Description

This command converts an XML payload file from UTF-8 to UTF-16 encoding using iconv, a standard utility for character set conversion. It is used in XXE attack scenarios to obfuscate payloads and bypass WAF detection by changing the byte representation of the XML, making signature matching ineffective.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INPUT_FILE | Path to the input UTF-8 encoded XML file (e.g., base_xxe.xml) | Yes |
| $_OUTPUT_FILE | Path for the output UTF-16 encoded file (e.g., utf16_xxe.xml) | Yes |
| -f UTF-8 | Specifies input encoding (from UTF-8) | Built-in |
| -t UTF-16 | Specifies output encoding (to UTF-16) | Built-in |

## Examples

### Basic Usage

```bash
cat base_xxe.xml | iconv -f UTF-8 -t UTF-16 > utf16_xxe.xml
```

### Advanced Usage

For verbose output or error handling:

```bash
cat base_xxe.xml | iconv -f UTF-8 -t UTF-16//IGNORE > utf16_xxe.xml 2>/dev/null
```

(The //IGNORE ignores invalid characters.)

## Expected Output

No stdout output if successful; the output file is created. Verify with:

```bash
file utf16_xxe.xml
```

Output: `utf16_xxe.xml: Little-endian UTF-16 Unicode text`

If errors occur (e.g., invalid input), iconv prints to stderr: `iconv: incomplete character or shift sequence at end of input.`

## Related

- [[Related Procedure]]: [[procedures/xml-external-entity-waf-bypass-via-character-encoding]]
- [[Related Command]]: [[commands/iconv-convert-utf8-to-utf16be]]
