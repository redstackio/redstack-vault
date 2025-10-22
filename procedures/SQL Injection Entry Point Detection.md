---
id: 25642eb6-18fd-42a6-a9e6-f3bf7a62c65b
name: SQL Injection Entry Point Detection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.114951+00:00'
updated_at: '2023-04-10T20:24:20.634816+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Entry point detection]]'
- '[[SQL Injection]]'
commands:
- '[[Character Encoding]]'
---

# SQL Injection Entry Point Detection

## Summary

SQL Injection Entry Point Detection is a technique used by attackers to exploit vulnerabilities in web applications that use SQL databases. Attackers can use special characters, encoded data, merged characters, SQL injection logic testing, and Unicode character transformation to bypass security mea

## Description

# Description

SQL Injection Entry Point Detection is a technique used by attackers to exploit vulnerabilities in web applications that use SQL databases. Attackers can use special characters, encoded data, merged characters, SQL injection logic testing, and Unicode character transformation to bypass security measures and execute malicious code in the database. This technique can be used to steal sensitive data, modify or delete data, or even take control of the entire web application. To prevent SQL Injection attacks, it is important to detect and block entry points where attackers can inject malicious code.

## Requirements

1. Access to web application vulnerable to SQL Injection attacks

1. Knowledge of SQL Injection techniques

1. Tools for detecting and blocking SQL Injection attacks

## Defense

1. Use parameterized queries or prepared statements to prevent SQL Injection attacks

1. Implement input validation and sanitization to block malicious code

1. Regularly update web application and database software to patch vulnerabilities

## Objectives

1. Detect entry points in web applications vulnerable to SQL Injection attacks

1. Prevent attackers from injecting malicious code into the database

1. Protect sensitive data stored in the database

# Instructions

1. To use special characters in SQL queries, you can escape them with a backslash (\) or use single quotes for string literals. For example, to search for a string containing an apostrophe, you can use the following syntax: SELECT * FROM table WHERE column LIKE '%\'%';

**Code**: [['
%27
"
%22
#
%23
;
%3B
)
Wildcard (*)
&apos;  # r]]

> Special characters can be used in SQL queries to perform various operations such as concatenation, comparison, and wildcard searches. However, it is important to be aware of the potential security risks associated with using special characters in SQL queries, as they can be used to exploit vulnerabilities such as SQL injection attacks. To avoid these risks, it is recommended to use parameterized queries or prepared statements instead of building SQL queries dynamically with user input.

**Command** ([[Character Encoding]]):

```bash
'
%27
"
%22
#
%23
;
%3B
)
Wildcard (*)
&apos;  # required for XML content
```

2. To decode the data, use a combination of decoding functions such as URL decode and HTML decode.

**Code**: [[%%2727
%25%27]]

> This command is used to demonstrate the concept of multiple encoding. The provided data has been encoded twice, using URL encoding and then HTML encoding. The command can be used to show how to decode such data by using a combination of decoding functions.

3. Use the following SQL command to merge characters: CONCAT(string1, string2, ...)

**Code**: [[`+HERP
'||'DERP
'+'herp
' 'DERP
'%20'HERP
'%2B'HER]]

> The CONCAT function is used to merge two or more strings together. The arguments passed to the CONCAT function can be strings, numbers, or any other data type that can be implicitly converted to a string. In this example, the strings 'HERP', 'DERP', 'herp', 'DERP', 'HERP', and 'HERP' are being merged together using the concatenation operator '||' and the URL encoded characters '%20' and '%2B'.

4. The SQL injection logic testing command can be used to determine if a web application is vulnerable to SQL injection attacks. The command sends multiple requests to the web application with different SQL injection payloads to test for vulnerabilities.

**Code**: [[page.asp?id=1 or 1=1 -- true
page.asp?id=1' or 1=1]]

> The 'data' field contains the different payloads that are sent in the requests. The payloads test for SQL injection vulnerabilities by attempting to modify the SQL query that is executed by the web application. If the web application is vulnerable, the query will be modified and the response will be 'true'. If the web application is not vulnerable, the query will not be modified and the response will be 'false'. The 'lang' field indicates that the payloads are written in SQL. The 'text' field provides a brief description of the command. The 'instruction' field provides more detailed instructions for using the command.

5. Use this command to transform Unicode characters into their corresponding ASCII characters.

**Code**: [[Unicode character U+02BA MODIFIER LETTER DOUBLE PR]]

> This command takes a string of text as input and replaces any Unicode characters with their corresponding ASCII characters. The output is the transformed string with all Unicode characters replaced. The command is useful when working with text that contains non-ASCII characters and needs to be transformed for further processing.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Character Encoding]]

## Tags

- [[Entry point detection]]
- [[SQL Injection]]
