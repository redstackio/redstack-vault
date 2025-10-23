---
id: 1cb4d7f8-5adf-46dc-9a08-1af34b35e19d
name: Basic Jinja2 Server Side Template Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.561568+00:00'
updated_at: '2023-04-10T20:23:44.307099+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Cloud Instance Metadata API|T1522 - Cloud Instance Metadata API]]'
tags:
- '[[Jinja2]]'
- '[[Jinja2 - Basic injection]]'
- '[[Server Side Template Injection]]'
---

# Basic Jinja2 Server Side Template Injection

## Summary

Jinja2 is a popular templating engine used by many web applications. It allows developers to dynamically generate HTML pages by inserting data into templates. However, if not properly secured, it can be vulnerable to server-side template injection attacks. An attacker can exploit this vulnerability

## Description

# Description

Jinja2 is a popular templating engine used by many web applications. It allows developers to dynamically generate HTML pages by inserting data into templates. However, if not properly secured, it can be vulnerable to server-side template injection attacks. An attacker can exploit this vulnerability to execute arbitrary code on the server, leading to web shell creation, credential dumping, and system information discovery. Businesses need to be aware of this vulnerability and take steps to secure their web applications that use Jinja2 templates.

 

## Requirements

1. Access to a vulnerable web application that uses Jinja2 templates

1. Knowledge of Jinja2 syntax and injection techniques

 

## Defense

1. Ensure that all input is properly sanitized and validated before being passed to the Jinja2 engine

1. Use a web application firewall to detect and block malicious requests

1. Regularly update and patch the web application and its dependencies

 

## Objectives

1. Inject and execute arbitrary code on the server

1. Create web shells for persistent access

1. Dump credentials from the server

1. Discover system information

 

# Instructions

1. To use Jinja templates, you first need to install the Jinja package using pip. Once installed, you can create a template file with placeholders for dynamic content. You can then render the template with the desired data to generate the final output.

Example:

```
from jinja2 import Template

template = Template('Hello {{ name }}!')
output = template.render(name='John')
print(output) # Output: 'Hello John!'
```

 



**Code**: [[16[[5*5]]
7777777
[('name', 'Jinja'), ('version', ]]



> The `data` field provides several examples of using Jinja templating. The first example evaluates the expression `4*4` and renders the result `16`. The second example uses double square brackets to evaluate the expression `5*5` and render the result `25`. The third example evaluates the expression `7*'7'` and renders the string `7777777`. The last example uses the `config` object to get information about the Jinja environment, such as the version and installed packages.

The `lang` field specifies the programming language used in the examples, which is Python.

The `text` field provides a link to the official Jinja website.

The `instruction` field provides a brief overview of how to use Jinja templates.

The `explain` field provides a more detailed explanation of the examples in the `data` field and the information in the other fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Cloud Instance Metadata API|T1522 - Cloud Instance Metadata API]]

## Tags

- [[Jinja2]]
- [[Jinja2 - Basic injection]]
- [[Server Side Template Injection]]


