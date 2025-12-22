---
id: 331e8d5f-fa52-4690-b3e4-d8132debb1fd
name: reference-single-quote-constant
type: command
executor: bash
data: jodd.util.StringPool.SINGLE_QUOTE
output: null
created_at: '2023-04-06T03:56:33.438240+00:00'
updated_at: '2023-04-10T20:22:27.355781+00:00'
platforms:
  - Java
tags:
  - hql-injection
  - java-constants
verified: true
validated: true
---

# reference-single-quote-constant

## Command

```bash
jodd.util.StringPool.SINGLE_QUOTE
```

## Description

References the SINGLE_QUOTE constant from the Jodd library's StringPool, representing a single quote string. Useful for identifying bypass opportunities in HQL injection by using library-defined quotes instead of direct input.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Constant path reference | No |

## Examples

### Basic Usage

```bash
jodd.util.StringPool.SINGLE_QUOTE
```

## Expected Output

Constant path, resolving to the string "'" in Java execution.

## Related

- [[procedures/Exploit-HQL-Injection-via-Java-Constants]]
- [[commands/reference-xml-char-apos-constant]]
