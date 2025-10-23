---
id: dbe16a19-9b3c-4459-ac7d-09e73742ad3c
name: Jinja2 Filter Bypass for Server Side Template Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.906529+00:00'
updated_at: '2023-04-10T20:23:43.888391+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Jinja2]]'
- '[[Jinja2 - Filter bypass]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Join data]]'
---

# Jinja2 Filter Bypass for Server Side Template Injection

## Summary

Jinja2 is a popular templating engine for Python web applications. It allows developers to create dynamic content by embedding Python code in HTML templates. However, if user input is not properly sanitized, it can lead to server-side template injection vulnerabilities. Attackers can exploit these 

## Description

# Description

Jinja2 is a popular templating engine for Python web applications. It allows developers to create dynamic content by embedding Python code in HTML templates. However, if user input is not properly sanitized, it can lead to server-side template injection vulnerabilities. Attackers can exploit these vulnerabilities to execute arbitrary code on the server. This procedure outlines a technique for bypassing Jinja2 filters to achieve server-side template injection. By chaining multiple filters together, attackers can bypass filters that would normally prevent code execution.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of Jinja2 templating syntax

1. Python scripting skills

 

## Defense

1. Sanitize user input to prevent server-side template injection vulnerabilities

1. Implement strict input validation to prevent malicious input

1. Use a web application firewall to detect and block malicious requests

 

## Objectives

1. Inject arbitrary code into a server-side template

1. Execute arbitrary code on the server

 

# Instructions

1. To get the request class, use the following code:

 



**Code**: [[request.__class__
request["__class__"]]]



> This command will return the class of the request object. The request object is an instance of the class that is used to send HTTP requests. This command can be useful when debugging or when you need to know the exact class of the request object being used.

2. To bypass a system or process, use the following command:

 



**Code**: [[_]]



> This command allows the user to bypass a system or process by providing an alternate route. The user should specify the system or process they wish to bypass and provide any necessary arguments. It is important to note that bypassing certain systems or processes may have consequences and should only be done with proper authorization and understanding of the potential risks.

3. This command is used to exploit a vulnerability on the localhost. The command is written in Python and requires a web server running on the localhost. The command takes in arguments in the form of a URL query string. The 'exploit' parameter is used to specify the exploit to be executed. The 'class' parameter is used to specify the class to be targeted by the exploit. The 'usc' parameter is used to specify the underscore character ('_').

 



**Code**: [[http://localhost:5000/?exploit={{request|attr([req]]



> When executed, this command will send a request to the specified URL with the specified parameters. The exploit specified in the 'exploit' parameter will be executed on the targeted class specified in the 'class' parameter. The exploit takes advantage of a vulnerability in the way Python handles attribute lookups to execute arbitrary code. The underscores in the 'usc' parameter are used to construct the attribute name used in the exploit. The command should only be used for testing and educational purposes and not for malicious activities.

4. Use this command to bypass certain restrictions or security measures in order to access data that would otherwise be unavailable.

 



**Code**: [[[]]



> This command requires knowledge of the specific restrictions or security measures in place, as well as the methods used to bypass them. It should only be used by authorized personnel with a legitimate need for the data in question.

5. Use this command to concatenate multiple text values into a single string.

 



**Code**: [[]]]



> The ']' character is used to indicate the end of a text value, while the 'and' string is used to join multiple text values together. For example, the command 'Hello]world]!' would result in the output 'Hello world!'.

6. This command is used to exploit request arguments. It works by using the 'request.args' function and joining the attributes together to create a payload. The payload is then passed as a parameter to the 'exploit' function. The 'class' parameter is used to specify the class to exploit.

 



**Code**: [[http://localhost:5000/?exploit={{request|attr((req]]



> The 'request.args' function is used to get the arguments passed in the request. The 'attr' function is used to access the attributes of the 'request' object. The 'join' function is used to join the attributes together to create the payload. The 'usc' parameter is used to specify the underscore character. The 'class' parameter is used to specify the class to exploit. The 'getlist' function is used to get a list of values for a specific argument. The 'l' parameter is used to specify the argument to get the list of values for. The 'a' parameter is used to specify the values to pass as the payload.

7. The join command is used to concatenate multiple strings into a single string. The command takes one or more strings as arguments and joins them together using a delimiter if specified.

 



**Code**: [[|join]]



> In this particular example, the |join command is being used to concatenate multiple strings together. However, the exact strings being joined are not specified in the given data. The user would need to provide the strings to be joined as arguments to the command.



**Command** ([[Join data]]):

```bash
|join
```



8. This command is used to exploit a request. To use this command, you need to replace the 'request.args.f' field with the desired exploit code. The 'request.args.a' field should be replaced with the arguments required for the exploit code. The exploit code will be executed on the server and the results will be returned.

 



**Code**: [[http://localhost:5000/?exploit={{request|attr(requ]]



> The 'http://localhost:5000/?exploit=' part of the URL is the endpoint where the exploit request will be sent. The '{{request|attr()}}' part is used to access the request object and execute the exploit code. The 'format()' method is used to format the exploit code with the arguments provided in the 'request.args.a' field. The '%s%sclass%s%s' part is a placeholder for the exploit code and should be replaced with the actual exploit code. The 'a=_' part of the URL is a placeholder for the exploit arguments and should be replaced with the actual arguments required for the exploit code.

9. To execute an OS command using Python, follow these steps:
1. Import the 'os' module in your Python script.
2. Use the 'popen' method of the 'os' module to execute the command.
3. Pass the command to be executed as an argument to the 'popen' method.
4. Use the 'read' method to read the output of the command.

 



**Code**: [[{{request|attr('application')|attr('\x5f\x5fglobal]]



> The given JSON object demonstrates how to execute an OS command using Python. The 'os' module provides a way to execute OS commands using Python. The 'popen' method of the 'os' module is used to execute the command. The command to be executed is passed as an argument to the 'popen' method. The output of the command can be read using the 'read' method.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Join data]]

## Tags

- [[Jinja2]]
- [[Jinja2 - Filter bypass]]
- [[Server Side Template Injection]]


