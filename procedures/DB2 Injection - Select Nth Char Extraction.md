---
id: 4233e7f2-57a8-4dc6-ae17-634fbe110544
name: DB2 Injection - Select Nth Char Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.888911+00:00'
updated_at: '2023-04-10T20:21:57.956923+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Data Obfuscation|T1001 - Data Obfuscation]]'
- '[[Modify Registry|T1112 - Modify Registry]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[Select Nth Char]]'
commands:
- '[[Select Substring]]'
---

# DB2 Injection - Select Nth Char Extraction

## Summary

DB2 Injection is a type of SQL Injection attack that targets IBM DB2 databases. This specific procedure, Select Nth Char Extraction, is used to extract a specific character from a string in the database. This can be useful for extracting sensitive information such as passwords or credit card number

## Description

# Description

DB2 Injection is a type of SQL Injection attack that targets IBM DB2 databases. This specific procedure, Select Nth Char Extraction, is used to extract a specific character from a string in the database. This can be useful for extracting sensitive information such as passwords or credit card numbers.

To execute this procedure, an attacker would first identify a vulnerable parameter in a web application that interacts with a DB2 database. The attacker would then inject a specially crafted SQL query that includes the Select Nth Char command to extract the desired character. The result of the query would be sent back to the attacker, who could then use the extracted information for malicious purposes.

This procedure can be used by attackers to gain access to sensitive information stored in DB2 databases, such as personally identifiable information or financial data. It can also be used to escalate privileges or execute further attacks against the target system.

## Requirements

1. Access to a vulnerable web application that interacts with a DB2 database

1. Knowledge of SQL Injection techniques

1. Access to a tool that can automate the injection process

## Defense

1. Implement input validation and sanitization techniques to prevent SQL Injection attacks

1. Use parameterized queries to prevent SQL Injection attacks

1. Monitor database activity for suspicious queries or behavior

## Objectives

1. Extract a specific character from a string in a DB2 database

1. Obtain sensitive information such as passwords or credit card numbers

1. Escalate privileges or execute further attacks against the target system

# Instructions

1. The SUBSTR function is used to extract a substring from a given string. The function takes three arguments: the input string, the starting position of the substring, and the length of the substring. In this example, the input string is 'abc', the starting position is 2, and the length is 1. Therefore, the function returns the substring 'b'.

**Code**: [[select substr('abc',2,1) FROM sysibm.sysdummy1 -- ]]

> The SUBSTR function is commonly used in SQL queries to extract specific parts of a string. It is particularly useful when working with large strings or when you only need a small portion of a string. The function can be customized to extract substrings of varying lengths and starting positions, making it a versatile tool for data analysis and manipulation.

**Command** ([[Select Substring]]):

```bash
select substr('abc',2,1) FROM sysibm.sysdummy1
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Data Obfuscation|T1001 - Data Obfuscation]]
- [[Modify Registry|T1112 - Modify Registry]]

## Commands Used

- [[Select Substring]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[Select Nth Char]]
