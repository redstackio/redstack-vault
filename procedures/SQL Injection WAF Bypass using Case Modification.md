---
id: 92d36a38-477d-46d2-b997-e0aa57924977
name: SQL Injection WAF Bypass using Case Modification
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.772362+00:00'
updated_at: '2023-04-10T20:24:24.723056+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Security Support Provider|T1101 - Security Support Provider]]'
tags:
- '[[Case modification]]'
- '[[SQL Injection]]'
- '[[WAF Bypass]]'
commands:
- '[[Data Conversion]]'
---

# SQL Injection WAF Bypass using Case Modification

## Summary

SQL Injection is a technique used to exploit a vulnerability in a web application by injecting malicious SQL code into a database query. WAFs are designed to prevent SQL Injection attacks by blocking malicious SQL queries. However, attackers can bypass WAFs by modifying the case of the injected SQL

## Description

# Description

SQL Injection is a technique used to exploit a vulnerability in a web application by injecting malicious SQL code into a database query. WAFs are designed to prevent SQL Injection attacks by blocking malicious SQL queries. However, attackers can bypass WAFs by modifying the case of the injected SQL code. By changing the case of the SQL keywords and identifiers, attackers can evade WAFs that are configured to detect only specific case patterns. This technique can be used to gain unauthorized access to sensitive data, modify data, or execute arbitrary code. The business value of this attack lies in the ability to gain access to confidential information, disrupt business operations, or steal intellectual property.

## Requirements

1. Access to a web application that is vulnerable to SQL Injection

1. Knowledge of SQL Injection techniques

1. Knowledge of case modification techniques

1. Access to a tool or script that can automate the injection process

## Defense

1. Implement strict input validation and sanitization to prevent SQL Injection attacks

1. Use a WAF that is configured to detect and block SQL Injection attacks

1. Regularly update the WAF rules to keep up with new attack techniques

## Objectives

1. Bypass the WAF to successfully inject malicious SQL code

1. Gain unauthorized access to sensitive data stored in the database

1. Modify data stored in the database

1. Execute arbitrary code on the web server

# Instructions

1. This command can be used to bypass SQL injection filters that are looking for specific keywords like 'AND' by using different combinations of uppercase and lowercase letters. The query parameter 'id' is used as an example, but this can be replaced with any vulnerable parameter. The payload '?id=1 AND 1=1#
?id=1 AnD 1=1#
?id=1 aNd 1=1#' sends three requests with the same injection payload but with different letter cases for 'AND', which increases the chances of bypassing the filter.

**Code**: [[?id=1 AND 1=1#
?id=1 AnD 1=1#
?id=1 aNd 1=1#]]

> The payload is using the SQL injection technique of injecting a logical expression that will always be true, such as '1=1'. The '#' character is used to comment out the rest of the query and prevent any syntax errors. By using different combinations of uppercase and lowercase letters for the keyword 'AND', the injection payload can bypass filters that are looking for specific letter cases. This technique should not be relied upon as the only means of bypassing filters, and additional techniques should be used in conjunction with this one.

2. To bypass using keywords in a SQL query, you can use the equivalent operator listed in the data field. For example, instead of using 'LIKE' you can use the equals sign '=', or instead of 'AND' you can use '&&'. This can also be useful for case-insensitive queries.

**Code**: [[AND   -> &&
OR    -> ||
=     -> LIKE,REGEXP, BETW]]

> The data field provides a list of equivalent operators that can be used in place of certain keywords in a SQL query. For example, instead of using 'LIKE' to search for a pattern in a string, you can use the equals sign '='. Similarly, instead of using 'AND' to combine multiple conditions in a WHERE clause, you can use '&&'. This can be useful for bypassing certain restrictions or for creating case-insensitive queries. The instruction field provides more details on how to use these equivalents in a SQL query.

**Command** ([[Data Conversion]]):

```bash
AND   -> &&
OR    -> ||
=     -> LIKE,REGEXP, BETWEEN, not < and not >
> X   -> not between 0 and X
WHERE -> HAVING
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Security Support Provider|T1101 - Security Support Provider]]

## Commands Used

- [[Data Conversion]]

## Tags

- [[Case modification]]
- [[SQL Injection]]
- [[WAF Bypass]]
