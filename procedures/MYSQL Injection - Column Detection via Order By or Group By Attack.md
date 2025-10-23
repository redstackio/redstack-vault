---
id: e98960c3-c4e4-4c2c-aff1-a93cccbe76ba
name: MYSQL Injection - Column Detection via Order By or Group By Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.268884+00:00'
updated_at: '2023-04-10T20:22:54.543285+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Detect columns number]]'
- '[[MYSQL Injection]]'
- '[[MYSQL Union Based]]'
- '[[Using `order by` or `group by`]]'
- '[[Using `order by` or `group by` Error Based]]'
commands:
- '[[Group by columns 1-100]]'
- '[[SQL Injection Detected]]'
---

# MYSQL Injection - Column Detection via Order By or Group By Attack

## Summary

This procedure involves an attacker exploiting a vulnerability in a MYSQL database to detect the number of columns present in a database table. The attacker can use the `order by` or `group by` commands to manipulate the database and retrieve information about the table structure. The attacker can 

## Description

# Description

This procedure involves an attacker exploiting a vulnerability in a MYSQL database to detect the number of columns present in a database table. The attacker can use the `order by` or `group by` commands to manipulate the database and retrieve information about the table structure. The attacker can then use this information to launch further attacks on the database, such as data exfiltration or privilege escalation. The technical explanation involves the attacker injecting malicious SQL code into a vulnerable web application, which is then executed by the backend database. This allows the attacker to manipulate the database and retrieve sensitive information. The business value of this attack is that it can allow an attacker to gain unauthorized access to sensitive data, resulting in financial losses, reputational damage, and legal liabilities.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of SQL injection techniques

1. Ability to inject malicious SQL code into the web application

 

## Defense

1. Implement input validation and sanitization techniques to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Limit access to the database to authorized users only

 

## Objectives

1. Detect the number of columns present in a database table

1. Retrieve sensitive information from the database

1. Launch further attacks on the database, such as data exfiltration or privilege escalation

 

# Instructions

1. To perform an order by attack in SQL injection, append 'ORDER BY' clause with a list of numbers to the end of the input. The number of columns can be determined by checking the error message returned by the server. Use the UNION SELECT statement to inject the malicious code and retrieve the desired data.

 



**Code**: [[1' ORDER BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]



> The 'ORDER BY' clause is used to sort the result set in ascending or descending order. In SQL injection, this clause can be used to determine the number of columns in the database table. By appending a list of numbers to the end of the input, the attacker can determine the number of columns required to execute the query. The error message returned by the server can be used to determine the exact number of columns. Once the number of columns is determined, the UNION SELECT statement can be used to inject the malicious code and retrieve the desired data.

2. This is an SQL Injection attack where the attacker attempts to modify the query by injecting a GROUP BY clause. The GROUP BY clause is used to group the data based on one or more columns. By manipulating the GROUP BY clause, an attacker can retrieve sensitive information from the database.


 



**Code**: [[1' GROUP BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]



> The attacker modifies the query by injecting a GROUP BY clause with a list of columns. In this case, the attacker injected a GROUP BY clause with a list of 100 columns. The error message 'Unknown column '4' in 'group statement'' indicates that the attacker tried to group the data by a non-existent column. The error message '# This error means query uses 3 column' indicates that the original query used only 3 columns. The attacker then attempted to perform a UNION SELECT operation to retrieve data from another table. The 'True' at the end of the query is used to comment out the rest of the original query.



**Command** ([[Group by columns 1-100]]):

```bash
1' GROUP BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100--+\n\n
```





**Command** ([[SQL Injection Detected]]):

```bash
1' UNION SELECT 1,2,3--+\t
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Group by columns 1-100]]
- [[SQL Injection Detected]]

## Tags

- [[Detect columns number]]
- [[MYSQL Injection]]
- [[MYSQL Union Based]]
- [[Using `order by` or `group by`]]
- [[Using `order by` or `group by` Error Based]]


