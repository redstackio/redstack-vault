---
id: d02b5569-be00-45b0-adaf-6544e89e16e4
name: GraphQL Type Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.876432+00:00'
updated_at: '2023-04-10T20:22:21.824680+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[Enumerate the types'' definition]]'
- '[[Exploit]]'
- '[[GraphQL Injection]]'
commands:
- '[[GraphQL Type Query]]'
---

# GraphQL Type Enumeration

## Summary

GraphQL is a query language for APIs that allows clients to request only the data they need, and nothing more. However, it is vulnerable to injection attacks. In this procedure, we will use a GraphQL injection vulnerability to enumerate the definition of interesting types. This can help an attacker

## Description

# Description

GraphQL is a query language for APIs that allows clients to request only the data they need, and nothing more. However, it is vulnerable to injection attacks. In this procedure, we will use a GraphQL injection vulnerability to enumerate the definition of interesting types. This can help an attacker understand the structure of the application's data and potentially identify additional attack vectors.

The attacker can use the following GraphQL query to retrieve the fields and types of the chosen type: {__type (name: "User") {name fields{name type{name kind ofType{name kind}}}}}. The attacker can replace "User" with the name of the type they are interested in.

 

## Requirements

1. Access to a GraphQL endpoint

1. Knowledge of the GraphQL query language

 

## Defense

1. Implement input validation to prevent injection attacks.

1. Monitor GraphQL queries for suspicious activity.

1. Restrict access to the GraphQL endpoint to authorized users only.

 

## Objectives

1. Enumerate the definition of interesting types

1. Identify additional attack vectors

 

# Instructions

1. To enumerate the definition of a type, replace "User" with the name of the type you are interested in and execute the following GraphQL query: {__type (name: "User") {name fields{name type{name kind ofType{name kind}}}}}

 



**Code**: [[{__type (name: "User") {name fields{name type{name]]



> This command sends a GraphQL query to the endpoint, requesting the definition of the specified type. The query uses the __type field to retrieve the type's name, fields, and their respective types. The ofType field is used to retrieve the underlying type of a list or non-null type.



**Command** ([[GraphQL Type Query]]):

```bash
{__type (name: "User") {name fields{name type{name kind ofType{name kind}}}}}
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Commands Used

- [[GraphQL Type Query]]

## Tags

- [[Enumerate the types' definition]]
- [[Exploit]]
- [[GraphQL Injection]]


