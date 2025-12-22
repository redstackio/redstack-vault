---
id: cmd-xmllint-parse
data: ./xmllint --valid test000
tags:
  - xml-parsing
  - dos
  - exploitation
type: command
output: >-
  AddressSanitizer allocation failure: ERROR: AddressSanitizer failed to
  allocate 0x100002000 (4294975488) bytes; followed by stack trace showing
  failure in lzma_code and xmlParseDocument
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.410Z'
verified: false
validated: true
submitted: true
---
# xmllint-parse-valid

## Command

```bash
./xmllint --valid test000
```

## Description

Parses and validates an XML file using libxml2's xmllint tool, triggering LZMA decompression on compressed inputs; used to exploit DoS by causing excessive memory allocation in liblzma.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--valid` | Enables DTD validation during parsing | Yes |
| `test000` | Path to the malicious LZMA-compressed XML file | Yes |

## Examples

### Basic Usage

```bash
./xmllint --valid test000
```

### Advanced Usage

```bash
./xmllint --valid --debug test000
```

## Expected Output

AddressSanitizer failure: "ERROR: AddressSanitizer failed to allocate 0x100002000 (4294975488) bytes", with stack trace from lzma_code in liblzma and xmlParseDocument in libxml2.

## Related

- [[Related Procedure|procedures/Trigger-libxml2-DoS-with-xmllint]]
