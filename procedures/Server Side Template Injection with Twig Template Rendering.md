---
id: 1d1d9e9b-b540-4ea2-931a-50c782c36aaf
name: Server Side Template Injection with Twig Template Rendering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.313372+00:00'
updated_at: '2023-04-10T20:23:51.929900+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[DCShadow|T1207 - DCShadow]]'
tags:
- '[[Server Side Template Injection]]'
- '[[Twig]]'
- '[[Twig - Template format]]'
commands:
- '[[Render Twig Template with Custom Greeting]]'
- '[[Render Twig Template with First Name]]'
---

# Server Side Template Injection with Twig Template Rendering

## Summary

Server Side Template Injection (SSTI) is a vulnerability that occurs when user input is embedded in a template in an unsafe manner. In the case of Twig, a popular templating engine, SSTI can occur when user input is not properly sanitized. An attacker can exploit this vulnerability by injecting mal

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that occurs when user input is embedded in a template in an unsafe manner. In the case of Twig, a popular templating engine, SSTI can occur when user input is not properly sanitized. An attacker can exploit this vulnerability by injecting malicious code into the template, which is then executed on the server-side. This can lead to a variety of attacks such as remote code execution, information disclosure, and denial of service.

From a technical perspective, SSTI with Twig Template Rendering occurs when an attacker is able to inject Twig code into a template. This code is then executed on the server-side, allowing the attacker to execute arbitrary code or access sensitive information.

The business value of understanding and mitigating SSTI with Twig Template Rendering is significant. By understanding the vulnerability, organizations can prevent attackers from accessing sensitive information, executing arbitrary code, and disrupting critical business operations.

 

## Requirements

1. Access to a system running Twig Template Rendering

1. Knowledge of Twig syntax and SSTI vulnerabilities

 

## Defense

1. Ensure that all user input is properly sanitized before being used in a template

1. Run Twig in a sandboxed environment to prevent unauthorized code execution

1. Implement content security policies to prevent malicious code injection

 

## Objectives

1. Identify potential SSTI vulnerabilities in Twig templates

1. Exploit SSTI vulnerabilities to execute arbitrary code or access sensitive information

1. Mitigate SSTI vulnerabilities to prevent exploitation

 

# Instructions

1. This command is used to render a Twig template with dynamic data. The data is passed to the template in the form of an array. The first argument is the path to the template file and the second argument is the data array.

 



**Code**: [[$output = $twig->render(
  'Dear' . $_GET['custom_]]



> In the given code, the Twig template is being rendered with a custom greeting and the user's first name. The first argument in the render function is the string 'Dear' concatenated with the value of the custom_greeting parameter from the GET request. The second argument is an array with the key 'first_name' and the value of the user's first name. The second render function is similar, but uses a string with a placeholder for the first name instead. The rendered output is stored in the $output variable.



**Command** ([[Render Twig Template with Custom Greeting]]):

```bash
$output = $twig->render(
  'Dear' . $_GET['custom_greeting'],
  array("first_name" => $user.first_name)
);

```





**Command** ([[Render Twig Template with First Name]]):

```bash
$output = $twig->render(
  "Dear {first_name}",
  array("first_name" => $user.first_name)
);
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[DCShadow|T1207 - DCShadow]]

## Commands Used

- [[Render Twig Template with Custom Greeting]]
- [[Render Twig Template with First Name]]

## Tags

- [[Server Side Template Injection]]
- [[Twig]]
- [[Twig - Template format]]


