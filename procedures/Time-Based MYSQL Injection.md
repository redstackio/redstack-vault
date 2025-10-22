---
id: 925e6746-a0b0-42d4-a0bb-83668bcada9b
name: Time-Based MYSQL Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.672511+00:00'
updated_at: '2023-04-10T20:22:55.537590+00:00'
tags:
- '[[MYSQL Injection]]'
- '[[MYSQL Time Based]]'
---

# Time-Based MYSQL Injection

## Summary

Time-based MYSQL injection is a technique used by attackers to exploit vulnerabilities in web applications that use MYSQL databases. The attacker injects malicious SQL code into the application, causing the database to delay its response. By measuring the time it takes for the database to respond, 

## Description

# Description

Time-based MYSQL injection is a technique used by attackers to exploit vulnerabilities in web applications that use MYSQL databases. The attacker injects malicious SQL code into the application, causing the database to delay its response. By measuring the time it takes for the database to respond, the attacker can determine if the injection was successful and extract sensitive data such as usernames and passwords. This technique is often used when other injection methods fail, and can be difficult to detect and prevent.

Technical Explanation: Time-based MYSQL injection is a type of SQL injection that is based on the delay of the database's response. By injecting a sleep command into the SQL statement, the attacker can force the database to delay its response for a specified period of time. The attacker can then measure the time it takes for the database to respond, allowing them to determine if the injection was successful. This technique can be used to extract sensitive data from the database, such as usernames and passwords.

Business Value: Time-based MYSQL injection can be used by attackers to steal sensitive data from web applications. This can lead to financial losses, damage to reputation, and legal consequences.

## Requirements

1. Access to a vulnerable web application that uses a MYSQL database

1. Knowledge of SQL injection techniques

1. Access to a tool that can automate the injection process

## Defense

1. Use parameterized queries or prepared statements to prevent SQL injection attacks

1. Regularly scan web applications for vulnerabilities and patch them promptly

1. Monitor database activity for suspicious behavior, such as delays in response time

## Objectives

1. To successfully inject malicious SQL code into the web application's database

1. To extract sensitive data such as usernames and passwords from the database

# Instructions

1. This command is used to test the performance of MySQL database by delaying the output. The command uses the BENCHMARK function to execute a given number of iterations of a specific function. The SLEEP function is used to introduce a delay in the execution of the command. The RANDNUM and RANDSTR are placeholders for randomly generated numbers and strings respectively. The ELT function is used to return the Nth element of a given list, in this case, it is used to introduce a delay.

**Code**: [[+BENCHMARK(40000000,SHA1(1337))+
'%2Bbenchmark(320]]

> The BENCHMARK function is used to execute a function multiple times to test the performance of MySQL. The function is executed a specified number of times, in this case, 40,000,000 times for the first BENCHMARK function and 3,200 times for the second BENCHMARK function. The SHA1 function is used to generate a hash value for the input value. The SLEEP function is used to introduce a delay in the execution of the command, the delay time is determined by the value of [SLEEPTIME]. The MD5 function is used to generate a hash value for the input value. The RLIKE function is used to match a regular expression pattern against a string. The ELT function is used to return the Nth element of a given list, in this case, it is used to introduce a delay.

## Tags

- [[MYSQL Injection]]
- [[MYSQL Time Based]]
