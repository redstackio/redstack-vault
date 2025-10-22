---
id: a1c0aea9-9475-485f-96da-469c8667da7e
name: Basic Expression Language EL Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.953322+00:00'
updated_at: '2023-04-10T20:23:41.617125+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Expression Language EL]]'
- '[[Expression Language EL - Basic injection]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Print property value and evaluate expression]]'
---

# Basic Expression Language EL Injection

## Summary

Basic Expression Language (EL) injection is a type of Server Side Template Injection attack that targets web applications using Java. EL is a scripting language used in Java-based web applications to dynamically generate web pages. Attackers can exploit vulnerabilities in the application by injecti

## Description

# Description

Basic Expression Language (EL) injection is a type of Server Side Template Injection attack that targets web applications using Java. EL is a scripting language used in Java-based web applications to dynamically generate web pages. Attackers can exploit vulnerabilities in the application by injecting malicious code into the EL expressions to execute arbitrary code on the server. This attack can be used to steal sensitive data, escalate privileges, or take control of the server.

Technical Explanation: The attacker identifies a vulnerable web application that uses Java EL expressions. They then inject malicious code into the EL expression to execute arbitrary code on the server. The attacker can use this access to steal sensitive data, escalate privileges, or take control of the server.

Business Value: Basic EL injection can be used by attackers to gain access to sensitive data, escalate privileges, or take control of the server. This can result in loss of business, damage to reputation, and regulatory fines.

## Requirements

1. Access to a vulnerable web application that uses Java EL expressions

1. Knowledge of EL syntax and injection techniques

## Defense

1. Implement input validation and sanitization to prevent injection attacks

1. Use a web application firewall to detect and block malicious requests

1. Keep software up to date with the latest security patches

## Objectives

1. Execute arbitrary code on the server

1. Steal sensitive data

1. Escalate privileges

# Instructions

1. The Java Expression Language (EL) is used to access data in JavaServer Pages (JSP) and JavaServer Faces (JSF). The EL can be used to access data in JavaBeans components, session, request, and application scopes, and implicit objects such as pageContext, request, response, and session. The EL also includes operators and functions that can be used to manipulate data. The Template Text commands are used to generate dynamic content in JSP pages. The commands include ${<property>} to access data using the EL, #{<expression string>} for deferred evaluation of expressions, and T(<javaclass>) to access static methods and fields of a Java class.

**Code**: [[${<property>}
${1+1}

#{<expression string>}
#{1+1]]

> The ${<property>} command is used to access data using the EL. The <property> can be a variable, a bean property, a map key, or an array index. For example, ${person.name} accesses the name property of the person object. The ${1+1} command evaluates the expression and returns the result. In this case, it returns 2.

The #{<expression string>} command is used for deferred evaluation of expressions. The <expression string> can be any valid EL expression. For example, #{person.name} is evaluated when the value is needed, not when the page is rendered. This can improve performance by reducing the number of evaluations.

The T(<javaclass>) command is used to access static methods and fields of a Java class. The <javaclass> is the fully qualified name of the class. For example, T(java.lang.Math).max(2,3) returns the maximum of 2 and 3.

**Command** ([[Print property value and evaluate expression]]):

```bash
"${<property>}\n${1+1}\n\n#{<expression string>}\n#{1+1}\n\nT(<javaclass>)"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Commands Used

- [[Print property value and evaluate expression]]

## Tags

- [[Expression Language EL]]
- [[Expression Language EL - Basic injection]]
- [[Server Side Template Injection]]
