---
id: a7dc5a6a-8998-44c2-97fd-5c66ff696787
name: Identifying Time-Based SQL Injection
type: procedure
verified: true
submitted: true
created_at: '2020-07-21T14:54:46.274454+00:00'
updated_at: '2023-05-26T01:33:01.563707+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SQL]]'
- '[[sqli]]'
- '[[Web Applications]]'
---

# Identifying Time-Based SQL Injection

**Status**: ✓ Verified

## Summary

An attacker will inject SQL queries through user input fields or parameters in the URL to execute them on the database and extract sensitive information. In Time-Based SQL injection, attacker will use a conditional query along with a time statement to predict the information in the database. Follow

## Description

# Description

An attacker will inject SQL queries through user input fields or parameters in the URL to execute them on the database and extract sensitive information. In Time-Based SQL injection, attacker will use a conditional query along with a time statement to predict the information in the database. Following similar payload can be used to perform Time-Based SQL injection.

' or sleep(5) #

`' waitfor delay '00:00:10'--`

`BENCHMARK(5000000,ENCODE('MSG','by 5 seconds'))`

# `Instructions`

`1. Inject the payload *' or` sleep(5) #* through user input field

2. After the search button is clicked, the application loads with a delay of 5 seconds as specified in the payload

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sqli]]
- [[Web Applications]]
