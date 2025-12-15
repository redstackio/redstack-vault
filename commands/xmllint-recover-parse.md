---
data: ./xmllint --recover test00.xml
tags:
  - xml
  - parse
  - recover
  - libxml2
type: command
output: >-
  Parser errors (e.g., 'xmlParseDocTypeDecl : no DOCTYPE name !', 'Space
  required after \'ELEMENT\'', 'Input is not proper UTF-8'), followed by
  'Segmentation fault' and SIGSEGV at address 0x0
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.846Z'
id: ba75c9cb-8346-4843-86f0-2909f9c49bbc
verified: false
validated: true
submitted: true
---
# xmllint-recover-parse

## Command

```bash
./xmllint --recover test00.xml
```

## Description

This command uses the xmllint utility from libxml2 to parse an XML file in recover mode, attempting to handle errors but triggering CVE-2017-5969 when the input is malformed, leading to memory issues and a crash. Use it to demonstrate denial of service in XML parsing applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--recover` | Enables recovery mode to continue parsing despite errors | Yes |
| `test00.xml` | Path to the input XML file with malformed DOCTYPE | Yes |

## Examples

### Basic Usage

```bash
./xmllint --recover test00.xml
```

### Advanced Usage

```bash
valgrind ./xmllint --recover test00.xml
```

## Expected Output

Parser warnings on DOCTYPE and UTF-8 issues, Valgrind alerts for uninitialized values and invalid reads if used, terminating in 'Segmentation fault (core dumped)' due to NULL pointer dereference.

## Related

- [[procedures/Trigger-libxml2-Recover-Mode-Vulnerability]]
