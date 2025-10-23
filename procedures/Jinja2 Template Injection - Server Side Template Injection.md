---
id: 431b004f-a3c0-41fb-b676-e6e98c8d7836
name: Jinja2 Template Injection - Server Side Template Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.582731+00:00'
updated_at: '2023-04-10T20:23:31.365261+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Jinja2]]'
- '[[Jinja2 - Template format]]'
- '[[Server Side Template Injection]]'
---

# Jinja2 Template Injection - Server Side Template Injection

## Summary

Jinja2 is a popular templating engine used for web applications. It allows developers to inject dynamic content into web pages by using templates. However, if the input is not properly sanitized, it can lead to Server Side Template Injection (SSTI) vulnerabilities. Attackers can exploit this vulner

## Description

# Description

Jinja2 is a popular templating engine used for web applications. It allows developers to inject dynamic content into web pages by using templates. However, if the input is not properly sanitized, it can lead to Server Side Template Injection (SSTI) vulnerabilities. Attackers can exploit this vulnerability to execute arbitrary code on the server, leading to full compromise of the application and potentially the underlying system. This attack can be carried out remotely if the application is exposed to the internet.

From a technical perspective, an attacker can inject malicious code into the template engine, which is executed on the server-side. This can allow the attacker to execute arbitrary code on the server, read or modify sensitive data, and even gain access to the underlying system. From a business perspective, this attack can lead to loss of sensitive data, financial loss, and damage to the reputation of the organization.



 

## Requirements

1. Access to the web application

1. Knowledge of the templating engine used by the application

1. Knowledge of the input fields that are vulnerable to SSTI

 

## Defense

1. Ensure that all input is properly sanitized and validated before being passed to the templating engine

1. Implement a Content Security Policy (CSP) to prevent the execution of untrusted code

1. Regularly monitor the application for any suspicious activity or unexpected behavior.

 

## Objectives

1. To execute arbitrary code on the server

1. To gain access to sensitive data

1. To gain access to the underlying system

 

# Instructions

1. To perform a Jinja2 template injection, an attacker can manipulate the input parameters of a Flask application that uses Jinja2 templates. By injecting malicious code into the input parameters, an attacker can execute arbitrary code on the server.

 



**Code**: [[{% extends "layout.html" %}
{% block body %}
  <ul]]



> Jinja2 is a powerful templating engine for Python web frameworks such as Flask or Django. It allows developers to create dynamic web pages by rendering templates with variables and control structures. However, if user input is not properly sanitized and validated, it can lead to a Jinja2 template injection vulnerability. An attacker can inject malicious code into the input parameters, which can be executed on the server-side, leading to data theft, server compromise, or other malicious activities.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Tags

- [[Jinja2]]
- [[Jinja2 - Template format]]
- [[Server Side Template Injection]]


