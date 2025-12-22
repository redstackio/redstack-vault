---
id: 2d2619cf-cd8f-45d2-bd03-5b74db5580e9
name: reference-string-opening-constant
type: command
executor: bash
data: cz.vutbr.web.csskit.OutputUtil.STRING_OPENING
output: null
created_at: '2023-04-06T03:56:33.438337+00:00'
updated_at: '2023-04-10T20:22:27.355781+00:00'
platforms:
  - Java
tags:
  - hql-injection
  - java-constants
verified: true
validated: true
---

# reference-string-opening-constant

## Command

```bash
cz.vutbr.web.csskit.OutputUtil.STRING_OPENING
```

## Description

References the STRING_OPENING constant from jStyleParser's OutputUtil, typically a quote for string delimiters. Applicable for HQL payloads in CSS/web parsing contexts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters | No |

## Examples

### Basic Usage

```bash
cz.vutbr.web.csskit.OutputUtil.STRING_OPENING
```

## Expected Output

Constant path, value is '"' or "'" depending on context.

## Related

- [[procedures/Exploit-HQL-Injection-via-Java-Constants]]
