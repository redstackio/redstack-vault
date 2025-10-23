---
id: 1e77f444-4e90-4509-a393-ab5ebbc5aa47
name: GraphQL Projection Data Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.849465+00:00'
updated_at: '2023-04-10T20:22:22.527955+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[Exploit]]'
- '[[Extract data using projections]]'
- '[[GraphQL Injection]]'
commands:
- '[[Retrieve doctor''s information]]'
---

# GraphQL Projection Data Extraction

## Summary

GraphQL Projection Data Extraction is a technique used to extract sensitive data from a GraphQL endpoint by manipulating the projection fields. This technique is often used by attackers to extract data such as personal identifiable information (PII) and credentials. To perform this attack, an attac

## Description

# Description

GraphQL Projection Data Extraction is a technique used to extract sensitive data from a GraphQL endpoint by manipulating the projection fields. This technique is often used by attackers to extract data such as personal identifiable information (PII) and credentials. To perform this attack, an attacker first identifies a GraphQL endpoint and then injects a malicious payload into the projection fields. The payload is designed to extract data from the GraphQL endpoint and return it to the attacker. This technique is effective because it allows the attacker to bypass GraphQL query restrictions and extract data that they are not authorized to access.

 

## Requirements

1. Access to a vulnerable GraphQL endpoint

 

## Defense

1. Implement input validation to prevent malicious payloads from being injected into the projection fields

1. Implement access controls to restrict unauthorized access to sensitive data

1. Monitor GraphQL endpoint for suspicious activity

 

## Objectives

1. Extract sensitive data from a GraphQL endpoint

1. Bypass GraphQL query restrictions

 

# Instructions

1. To perform a GraphQL Projection Data Extraction attack, an attacker can use the following payload:

 



**Code**: [[{doctors(options: "{\"patients.ssn\" :1}"){firstNa]]



> The payload is injected into the projection fields and is designed to extract sensitive data from the GraphQL endpoint. In this example, the payload is extracting the first name, last name, and social security number (SSN) of all the doctors' patients.



**Command** ([[Retrieve doctor's information]]):

```bash
{doctors(options: "{\"patients.ssn\" :1}"){firstName lastName id patients{ssn}}}
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]
- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Commands Used

- [[Retrieve doctor's information]]

## Tags

- [[Exploit]]
- [[Extract data using projections]]
- [[GraphQL Injection]]


