---
id: b8dd061c-16c1-4a13-95e0-ba34c6b80c3f
name: reference-single-quote-char-constant
type: command
executor: bash
data: ch.qos.logback.core.CoreConstants.SINGLE_QUOTE_CHAR
output: null
created_at: '2023-04-06T03:56:33.438303+00:00'
updated_at: '2023-04-10T20:22:27.355781+00:00'
platforms:
  - Java
tags:
  - hql-injection
  - java-constants
verified: true
validated: true
---

# reference-single-quote-char-constant

## Command

```bash
ch.qos.logback.core.CoreConstants.SINGLE_QUOTE_CHAR
```

## Description

References the SINGLE_QUOTE_CHAR constant from Logback's CoreConstants, a char representation of a single quote. Helps in payload construction for HQL injection in logging-integrated Java apps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Constant reference | No |

## Examples

### Basic Usage

```bash
ch.qos.logback.core.CoreConstants.SINGLE_QUOTE_CHAR
```

## Expected Output

Path to constant, value is the char '.

## Related

- [[procedures/Exploit-HQL-Injection-via-Java-Constants]]
