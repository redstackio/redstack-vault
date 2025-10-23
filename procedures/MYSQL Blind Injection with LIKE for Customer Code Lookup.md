---
id: 6ce07e60-dc7b-496a-8ed7-88ebefc526eb
name: MYSQL Blind Injection with LIKE for Customer Code Lookup
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.654213+00:00'
updated_at: '2023-04-10T20:22:50.881915+00:00'
tags:
- '[[MYSQL Blind]]'
- '[[MYSQL Blind with LIKE]]'
- '[[MYSQL Injection]]'
---

# MYSQL Blind Injection with LIKE for Customer Code Lookup

## Summary

This procedure involves exploiting an SQL injection vulnerability to perform a customer code lookup by name pattern. The attacker uses a MYSQL blind injection technique with LIKE to extract information from the database. MYSQL blind injection is a type of SQL injection where the attacker is unable 

## Description

# Description

This procedure involves exploiting an SQL injection vulnerability to perform a customer code lookup by name pattern. The attacker uses a MYSQL blind injection technique with LIKE to extract information from the database. MYSQL blind injection is a type of SQL injection where the attacker is unable to see the results of the injection in the application's response. The attacker uses the LIKE operator in the injection to extract information one character at a time. The attacker can then use this information to perform further attacks, such as privilege escalation or credential access. This attack can result in a complete compromise of the target system.

 

## Requirements

1. Access to the target system

1. Knowledge of MYSQL injection and blind injection techniques

1. Access to a tool for performing the injection

 

## Defense

1. Ensure that all user input is properly validated and sanitized to prevent injection attacks

1. Implement least privilege access controls to prevent privilege escalation

1. Use network segmentation and access controls to limit access to the target system

 

## Objectives

1. Extract customer codes from the database by name pattern

1. Perform privilege escalation or credential access

 

# Instructions

1. Use this command to look up customer codes based on a pattern in their name.

 



**Code**: [[SELECT cust_code FROM customer WHERE cust_name LIK]]



> The 'SELECT' keyword is used to retrieve data from the database. In this case, we are retrieving the 'cust_code' column from the 'customer' table. The 'WHERE' keyword is used to filter the results based on a condition. The 'cust_name' column is being checked for a pattern using the 'LIKE' operator. The pattern 'k__l' indicates that the customer name should start with 'k', followed by any two characters, and end with 'l'. This command can be modified to search for different patterns by changing the value of the pattern string. 

## Tags

- [[MYSQL Blind]]
- [[MYSQL Blind with LIKE]]
- [[MYSQL Injection]]


