---
id: 8ccdd409-dc33-438c-b990-39a1fb37fc06
name: reference-quote-constant
type: command
executor: bash
data: org.eclipse.help.internal.webapp.utils.JSonHelper.QUOTE
output: null
created_at: '2023-04-06T03:56:33.438441+00:00'
updated_at: '2023-04-10T20:22:27.355781+00:00'
platforms:
  - Java
tags:
  - hql-injection
  - java-constants
verified: true
validated: true
---

# reference-quote-constant

## Command

```bash
org.eclipse.help.internal.webapp.utils.JSonHelper.QUOTE
```

## Description

References the QUOTE constant from Eclipse Help's JSonHelper, used for JSON string quoting. Useful for injecting into HQL in web help or JSON-integrated apps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Constant path | No |

## Examples

### Basic Usage

```bash
org.eclipse.help.internal.webapp.utils.JSonHelper.QUOTE
```

## Expected Output

Path resolving to "'" or '"'.

## Related

- [[procedures/Exploit-HQL-Injection-via-Java-Constants]]
