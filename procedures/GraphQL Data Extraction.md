---
id: 7902e15b-408c-4c57-bf78-f24228753816
name: GraphQL Data Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.793832+00:00'
updated_at: '2023-04-10T20:22:22.174805+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Data from Information Repositories|T1213 - Data from Information Repositories]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Exploit]]'
- '[[Extract data]]'
- '[[GraphQL Injection]]'
---

# GraphQL Data Extraction

## Summary

GraphQL is a query language used for APIs. The injection of malicious code into GraphQL queries can lead to unauthorized access to sensitive data. Attackers can use this technique to extract data from the victim's system. This attack is usually carried out by exploiting vulnerabilities in the input

## Description

# Description

GraphQL is a query language used for APIs. The injection of malicious code into GraphQL queries can lead to unauthorized access to sensitive data. Attackers can use this technique to extract data from the victim's system. This attack is usually carried out by exploiting vulnerabilities in the input validation of the GraphQL queries. The attacker can use the extracted data for various purposes, such as identity theft, financial fraud, or corporate espionage. 

To exploit this vulnerability, the attacker sends a specially crafted GraphQL query to the victim's system. The query contains malicious code that extracts the desired data from the victim's system. The extracted data is then sent back to the attacker's system.

The business value of this attack is that it allows attackers to gain unauthorized access to sensitive data, which they can use for various malicious purposes.

## Requirements

1. Access to the GraphQL endpoint

1. Knowledge of the GraphQL query language

1. Ability to craft malicious GraphQL queries

## Defense

1. Implement input validation on GraphQL queries to prevent injection attacks

1. Monitor GraphQL queries for suspicious activity

1. Limit access to sensitive data through proper access controls

## Objectives

1. Extract sensitive data from the victim's system

1. Gain unauthorized access to sensitive data

1. Use the extracted data for malicious purposes

# Instructions

1. Craft a malicious GraphQL query containing the fields to extract

**Code**: [[example.com/graphql?query={TYPE_1{FIELD_1,FIELD_2}]]

> The 'query' parameter in the URL specifies the GraphQL query to execute. The query contains the fields that the attacker wants to extract from the victim's system. The attacker can modify the query to extract different fields or data types.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Data from Information Repositories|T1213 - Data from Information Repositories]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[Exploit]]
- [[Extract data]]
- [[GraphQL Injection]]
