---
id: 0e58d85e-8928-4fcd-adbb-756b746c7604
name: vulnerable-hql-constants-class
type: code
language: Java
verified: true
created_at: '2023-04-06T03:56:33.438007+00:00'
updated_at: '2023-04-10T20:22:27.357781+00:00'
platforms:
  - Java
tags:
  - hql-injection
  - vulnerable-code
validated: true
---

# vulnerable-hql-constants-class

## Code

```java
public class Constants {
    public static final String S_QUOTE = "'";
    public static final String HQL_PART = "select * from Post where name = '";
    public static final char C_QUOTE_1 = '\'';
    public static final char C_QUOTE_2 = '\047';
    public static final char C_QUOTE_3 = 39;
    public static final char C_QUOTE_4 = 0x27;
    public static final char C_QUOTE_5 = 047;
}
```

## Description

This Java class defines constants for single quotes in various formats (string, escaped, octal, decimal, hex), along with a partial HQL query. It exemplifies vulnerable code where attackers can reference these constants (e.g., Constants.C_QUOTE_1) in injection payloads to introduce quotes without direct input, exploiting poor parameterization in HQL construction.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| S_QUOTE | String representation of single quote | "'" |
| HQL_PART | Partial HQL query string | "select * from Post where name = '" |
| C_QUOTE_1 | Escaped char quote | '\''' |
| C_QUOTE_2 | Octal char quote | '\047' |
| C_QUOTE_3 | Decimal char quote | 39 |
| C_QUOTE_4 | Hex char quote | 0x27 |
| C_QUOTE_5 | Octal numeric quote | 047 |

## Usage

Decompile target JARs to find similar classes, then reference constants like hqli.persistent.Constants.C_QUOTE_1 in payloads delivered via HTTP parameters. Used in procedures like [[procedures/Exploit-HQL-Injection-via-Java-Constants]] for quote bypassing.

## Detection

- Static analysis tools (e.g., SonarQube) flagging dynamic HQL with constant concatenation.
- Runtime monitoring for anomalous HQL queries referencing internal constants.
- WAF rules matching constant paths in inputs (e.g., /Constants\.C_QUOTE/).

## Related

- [[procedures/Exploit-HQL-Injection-via-Java-Constants]]
