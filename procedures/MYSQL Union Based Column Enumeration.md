---
id: 17cb6090-edaa-41bc-8f7e-78139aefd3af
name: MYSQL Union Based Column Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.235644+00:00'
updated_at: '2023-04-10T20:22:49.030437+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Detect columns number]]'
- '[[MYSQL Injection]]'
- '[[MYSQL Union Based]]'
- '[[Using `order by` or `group by`]]'
---

# MYSQL Union Based Column Enumeration

## Summary

MYSQL Union Based Column Enumeration is a technique used by attackers to identify the number of columns in a database table. The attack is carried out by using a SQL injection vulnerability to inject a UNION statement into the original SQL query. The UNION statement is used to combine the result se

## Description

# Description

MYSQL Union Based Column Enumeration is a technique used by attackers to identify the number of columns in a database table. The attack is carried out by using a SQL injection vulnerability to inject a UNION statement into the original SQL query. The UNION statement is used to combine the result sets of two or more SELECT statements into a single result set. By injecting a UNION statement with a different number of columns than the original query, the attacker can determine the number of columns in the database table. This technique is commonly used during reconnaissance phase of an attack to identify the structure of the database and the data types of each column.

From a technical standpoint, the attacker uses the SQL Column Enumeration and SQL Group By Command to inject the UNION statement into the original SQL query. The SQL Column Enumeration command is used to determine the number of columns in the original query, while the SQL Group By Command is used to group the results by the number of columns in the UNION statement.

The business value of this technique is that it allows attackers to gain valuable information about the target database, such as the table structure and data types. This information can be used to launch further attacks, such as data exfiltration or privilege escalation.

## Requirements

1. Access to a vulnerable application with a SQL injection vulnerability

1. Knowledge of SQL injection techniques

1. Knowledge of the target database management system

## Defense

1. Input validation should be implemented to prevent SQL injection vulnerabilities

1. Database users should be granted the minimum permissions necessary to perform their tasks

1. Database activity should be monitored for suspicious behavior

## Objectives

1. Identify the number of columns in a database table

1. Determine the structure of the database table

1. Identify the data types of each column

# Instructions

1. To enumerate the number of columns in an SQL query, you can use the ORDER BY clause with sequential numbers and check for errors. If the query returns an error for a certain number, it means that the table has fewer columns than that number. If the query executes successfully for a certain number, it means that the table has at least that many columns.

**Code**: [[1' ORDER BY 1--+	#True
1' ORDER BY 2--+	#True
1' O]]

> In this example, the ORDER BY clause is used with sequential numbers to check the number of columns in the table. The query is executed with different numbers until an error is returned. The last successful query is used to confirm the number of columns. Additionally, the UNION SELECT statement can be used to add columns to the query and confirm the number of columns in the table.

2. The SQL GROUP BY command is used to group rows that have the same values into summary rows, like “find the number of customers in each country”. It is often used with aggregate functions such as COUNT, SUM, AVG, etc. In this example, the GROUP BY command is used to group the rows by the first, second, and third columns. The fourth query returns false because the query is only using 3 columns. The last query shows an example of how the GROUP BY command can be used in a UNION SELECT statement.

**Code**: [[1' GROUP BY 1--+	#True
1' GROUP BY 2--+	#True
1' G]]

> The arguments of the GROUP BY command are the columns that you want to group the rows by. For example, if you have a table of customer data with columns for name, country, and age, you could use the GROUP BY command to group the rows by country. The syntax for the GROUP BY command is as follows:

SELECT column1, column2, ..., columnN
FROM table_name
WHERE [conditions]
GROUP BY column1, column2, ..., columnN
ORDER BY column1, column2, ..., columnN;

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Detect columns number]]
- [[MYSQL Injection]]
- [[MYSQL Union Based]]
- [[Using `order by` or `group by`]]
