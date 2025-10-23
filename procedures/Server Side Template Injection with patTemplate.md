---
id: 36949c4d-0c8a-4c53-896a-6a4f788be744
name: Server Side Template Injection with patTemplate
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.418774+00:00'
updated_at: '2023-04-10T20:23:33.717533+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[patTemplate]]'
- '[[Server Side Template Injection]]'
---

# Server Side Template Injection with patTemplate

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a server-side template, which is then executed by the server. patTemplate is a PHP library used for server-side templating. By exploiting patTemplate's Page Template command, an attacker c

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a server-side template, which is then executed by the server. patTemplate is a PHP library used for server-side templating. By exploiting patTemplate's Page Template command, an attacker can inject malicious code into the server-side template, leading to SSTI. This technique can be used to execute arbitrary code, steal sensitive data, or take control of the server.

From a technical standpoint, patTemplate's Page Template command allows for the creation of dynamic web pages by defining placeholders in a template that are replaced with dynamic content at runtime. However, if user input is not properly sanitized, an attacker can inject malicious code into the template, leading to SSTI. From a business perspective, this vulnerability can lead to data theft, server compromise, and reputational damage.


 

## Requirements

1. Access to the target web application

1. Knowledge of patTemplate's Page Template command

1. Ability to inject malicious code into the template

 

## Defense

1. Ensure that all user input is properly sanitized before being used in server-side templates

1. Implement content security policies (CSPs) to restrict the types of content that can be included in templates

1. Regularly scan web applications for vulnerabilities and apply patches as needed

 

## Objectives

1. Inject malicious code into the server-side template

1. Execute arbitrary code on the server

1. Steal sensitive data

1. Take control of the server

 

# Instructions

1. The PatTemplate Page Template is a template that contains multiple other templates. It is used to create complex pages with reusable components. The <patTemplate:tmpl> tag is used to define a new template within the page template. The 'name' attribute is used to give the template a unique name that can be referenced later. The {NAME} placeholder is used to insert dynamic content into the template.

 



**Code**: [[<patTemplate:tmpl name="page">
  This is the main ]]



> Arguments:
- name: The name of the template. Must be unique within the page template.
- data: The content of the template, including other templates defined within it.
- lang: The language used to define the template. In this case, it is XML.
- text: Not used.
- instruction: A description of the template and its purpose.
- explain: A description of the arguments used in the template.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[patTemplate]]
- [[Server Side Template Injection]]


