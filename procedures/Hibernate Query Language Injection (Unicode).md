---
id: 10d8f2b2-9076-4389-b2b0-8bfec3d84bde
name: Hibernate Query Language Injection (Unicode)
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.408822+00:00'
updated_at: '2023-04-10T20:22:25.393338+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Hibernate Query Language Injection]]'
- '[[Unicode]]'
commands:
- '[[Length of Result of Subquery]]'
---

# Hibernate Query Language Injection (Unicode)

## Summary

Hibernate is an open-source Object-Relational Mapping (ORM) tool used by many Java applications. Hibernate Query Language (HQL) is a powerful query language used to retrieve data from databases. HQL Injection is a technique used to exploit vulnerabilities in HQL-based applications that could allow 

## Description

# Description

Hibernate is an open-source Object-Relational Mapping (ORM) tool used by many Java applications. Hibernate Query Language (HQL) is a powerful query language used to retrieve data from databases. HQL Injection is a technique used to exploit vulnerabilities in HQL-based applications that could allow attackers to execute arbitrary SQL commands. This specific procedure involves using Unicode encoding to bypass input validation and execute malicious SQL commands. Attackers can use this technique to steal sensitive data, modify or delete data, or execute other malicious actions.

From a technical perspective, this procedure involves injecting malicious input into an HQL query, which is then executed by the application. By using Unicode encoding, attackers can bypass input validation and execute arbitrary SQL commands. This can be accomplished by injecting Unicode characters into the query that represent SQL commands, or by using Unicode characters to modify the behavior of the query itself.

From a business perspective, this procedure represents a serious threat to organizations that rely on HQL-based applications to store and manage sensitive data. Attackers can use this technique to steal sensitive data, modify or delete data, or execute other malicious actions. This can result in significant financial losses, damage to reputation, and legal liabilities.

## Requirements

1. Access to an HQL-based application

1. Knowledge of SQL injection techniques

1. Knowledge of Unicode encoding

## Defense

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Regularly update and patch HQL-based applications to address known vulnerabilities

## Objectives

1. Exploit vulnerabilities in HQL-based applications

1. Execute arbitrary SQL commands

1. Steal sensitive data

1. Modify or delete data

# Instructions

1. To get the length of a select statement in Microsoft SQL Server, use the LEN function and pass the select statement as an argument.

**Code**: [[SELECT LEN([U+00A0](select[U+00A0](1))]]

> The LEN function in SQL Server returns the number of characters in a string expression. By passing a select statement as an argument to the LEN function, we can get the length of the select statement as a string. In this example, we are using the select statement 'select(1)' and passing it to the LEN function. The '[U+00A0]' character is a non-breaking space and is used to prevent SQL Server from trimming the select statement. The result of this query will be the length of the select statement as a string, which is 10.

2. This command returns the length of the result from a subquery.

**Code**: [[SELECT LEN((SELECT(1)))]]

> The subquery (SELECT(1)) returns a single value of 1. The LEN function then returns the length of this result, which is 1.

**Command** ([[Length of Result of Subquery]]):

```bash
SELECT LEN((SELECT(1)))
```

3. This command is a malicious SQL injection attack. It attempts to exploit a vulnerability in the application's code by injecting malicious code into a database query. The attacker can potentially gain unauthorized access to sensitive data or perform unauthorized actions on the database. It is important to ensure that all user input is properly sanitized and validated to prevent SQL injection attacks.

The 'SELECT' statement is used to retrieve data from a database. In this case, the query is selecting data from the 'hqli.persistent.Post' table. The 'WHERE' clause is used to filter the results based on certain conditions. The first condition is checking if the 'name' field of the 'Post' table is equal to 'dummy'. The second condition is checking if the length of the first name in the 'users' table is greater than 1. This is achieved by using the 'LEN' function to get the length of the name and comparing it to 1 using the '<' operator. The third condition is checking if the string '1' is equal to the string '11'. This condition will always evaluate to true and is used to ensure that the entire query is always true, regardless of the other conditions.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Length of Result of Subquery]]

## Tags

- [[Hibernate Query Language Injection]]
- [[Unicode]]
