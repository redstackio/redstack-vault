---
id: 9236cb6e-c76f-49f1-9396-f747ca069b47
name: Testing for Expression Language Injection
type: procedure
verified: true
submitted: true
created_at: '2020-07-25T13:21:48.498222+00:00'
updated_at: '2023-05-26T18:36:58.311747+00:00'
platforms:
- Web
tags:
- '[[Expression Langugae Injection]]'
- '[[injection]]'
- '[[Web Applications]]'
---

# Testing for Expression Language Injection

**Status**: ✓ Verified

## Summary

An attacker can leverage the user controlled fields such as search fields, session variables, request parameters etc... to parse the data by EL(expression Language ) interpreter and executes the mailicious JSP (Java Server Pages) tags . 

## Description

# Description

An attacker can leverage the user controlled fields such as search fields, session variables, request parameters etc... to parse the data by EL(expression Language ) interpreter and executes the mailicious JSP (Java Server Pages) tags .

# Instructions 

1. Place the payload in the search field as shown below.

*Payload: $(99999+1)*

2. Payload is being parsed by the EL interpreter and gets executed . The result can be observed in the search results .

## Platforms

- Web

## Tags

- [[Expression Langugae Injection]]
- [[injection]]
- [[Web Applications]]
