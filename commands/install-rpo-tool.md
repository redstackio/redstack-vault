---
id: 0a699acd-a1f6-40e2-9c03-df7b8b01dc86
name: install-rpo-tool
type: command
executor: bash
data: >-
  wget
  https://github.com/Netflix/recipes-rss/blob/master/eng/tools/rpo-2.0.0-SNAPSHOT-jar-with-dependencies.jar?raw=true
  -O rpo.jar
output: null
created_at: '2023-04-06T03:56:43.833214+00:00'
updated_at: '2023-04-06T03:56:43.857469+00:00'
platforms:
  - Linux
tags:
  - rpo
  - tool
verified: true
validated: true
---

# install-rpo-tool

## Command

```bash
wget https://github.com/Netflix/recipes-rss/blob/master/eng/tools/rpo-2.0.0-SNAPSHOT-jar-with-dependencies.jar?raw=true -O rpo.jar
```

## Description

Downloads the RPO testing tool JAR from Netflix repository.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -O rpo.jar | Output file name | Yes |
| URL | Source JAR URL | Yes |

## Examples

### Basic Usage

```bash
wget https://github.com/Netflix/recipes-rss/blob/master/eng/tools/rpo-2.0.0-SNAPSHOT-jar-with-dependencies.jar?raw=true -O rpo.jar
```

## Expected Output

--2023-...-- downloaded rpo.jar

## Related

- [[tools/RPO-Tool]]
- [[procedures/Exploit-RPO-for-Stored-XSS-via-CSS-Injection-in-IE]]
