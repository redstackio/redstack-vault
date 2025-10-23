---
id: c41bbd74-1591-49a2-b27a-36296def37be
name: Server Side Template Injection using Plates
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.473555+00:00'
updated_at: '2023-04-10T20:23:37.819949+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Plates]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Render a template using Plates]]'
---

# Server Side Template Injection using Plates

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server by injecting their own template code into a server-side template engine. This can lead to complete compromise of the server and sensitive data. Plates is a PHP templating engine 

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server by injecting their own template code into a server-side template engine. This can lead to complete compromise of the server and sensitive data. Plates is a PHP templating engine that is vulnerable to SSTI attacks. By exploiting this vulnerability, an attacker can execute arbitrary code on the server and gain access to sensitive data. This can be used to steal credentials, modify data, or launch further attacks. Business value is that by identifying and mitigating SSTI vulnerabilities, organizations can prevent data breaches and protect sensitive data.

 

## Requirements

1. Access to the target server

1. Knowledge of the Plates templating engine

 

## Defense

1. Regularly update and patch the server and all software

1. Implement input validation and sanitization to prevent injection attacks

1. Use secure coding practices to prevent vulnerabilities

 

## Objectives

1. Exploit SSTI vulnerability in Plates templating engine

1. Execute arbitrary code on the server

1. Gain access to sensitive data

 

# Instructions

1. To render a template using Plates, follow these steps:
1. Create a new Plates instance by passing the path to your templates directory as a parameter to the `Engine` constructor.
2. Call the `render` method on your `Engine` instance and pass the name of the template you want to render as the first argument and an array of variables to be used in the template as the second argument.
3. Output the result of the `render` method to display the rendered template.

 



**Code**: [[// Create new Plates instance
$templates = new Lea]]



> The `render` method takes two arguments:
1. The name of the template to render. This should be the filename of the template without the file extension.
2. An array of variables to be used in the template. The keys of the array should correspond to the variable names used in the template, and the values should be the values to be assigned to those variables.



**Command** ([[Render a template using Plates]]):

```bash
// Create new Plates instance
$templates = new League\Plates\Engine('/path/to/templates');

// Render a template
echo $templates->render('profile', ['name' => 'Jonathan']);
```



2. This command creates a page template for displaying user profiles.

 



**Code**: [[<?php $this->layout('template', ['title' => 'User ]]



> The 'name' variable in the template is used to display the user's name. This template can be used with a PHP framework like Laravel or Symfony to display user profiles. The 'layout' method is used to specify the main layout file for the template, and the 'e' method is used to escape any special characters in the user's name.

3. Use this template to create a consistent layout for your web pages.

 



**Code**: [[<html>
  <head>
    <title><?=$this->e($title)?></]]



> This PHP layout template contains a basic HTML structure with placeholders for dynamic content. The '<?=$this->e($title)?>' code will output the title of the page, while '<?=$this->section('content')?>' will output the main content of the page. You can use this template as a starting point and customize it to fit your specific needs.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Render a template using Plates]]

## Tags

- [[Plates]]
- [[Server Side Template Injection]]


