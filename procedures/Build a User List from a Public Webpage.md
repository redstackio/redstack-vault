---
id: fa6098c3-25f1-437b-8c52-2310e3416a59
name: Build a User List from a Public Webpage
type: procedure
verified: true
submitted: true
created_at: '2020-03-16T04:10:19.986818+00:00'
updated_at: '2023-05-25T19:58:31.804768+00:00'
tactics:
- '[[Organizational Information Gathering|TA0017 - Organizational Information Gathering]]'
techniques:
- '[[Acquire OSINT data sets and information|T1277 - Acquire OSINT data sets and information]]'
platforms:
- Web
tags:
- '[[Enumeration]]'
---

# Build a User List from a Public Webpage

**Status**: ✓ Verified

## Summary

Administrators will often create user names following predictable patterns, making it possible for attackers to guess at valid names. This procedure will go over popular naming schemes for building potential user lists from a public website, which can be then used to brute force logins. 

## Description

# Description

Administrators will often create user names following predictable patterns, making it possible for attackers to guess at valid names. This procedure will go over popular naming schemes for building potential user lists from a public website, which can be then used to brute force logins. 



# Instructions

User name policies vary from company to company, but a large portion tend to use combinations of a person's the first and last name. The following is a basic list of common user name schemes:

- <first name>

- <last name>

- <nickname>

- <first name><last name>

- <first name initial><last name>

- <last name initial><first name>

1. Enumerate a website with a browser and look for employee names on both the actual pages, and in the source. 
2. After assembling all employee names, create user names based on the aformentioned schemes.

For example, if a site discloses "Mary Washington", potential user names may be:





**Code**: [[mary
Mary
Washington
washington
marywashington
Mar]]



Valid users can often be enumerated with "Forgotten Password" links on web pages, certain services which disclose user names (some mail clients), etc. Once a single valid user name is identified, administrator's naming scheme usually becomes obvious.



## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Organizational Information Gathering|TA0017 - Organizational Information Gathering]]

### Techniques

- [[Acquire OSINT data sets and information|T1277 - Acquire OSINT data sets and information]]

## Tags

- [[Enumeration]]


