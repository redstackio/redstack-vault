---
id: 59eb354f-efde-41f1-b574-ba71bbf47b76
name: Server Side Template Injection - Java Basic Injection using Java ClassLoader
  and Resource Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.306709+00:00'
updated_at: '2023-04-10T20:23:29.222543+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Java]]'
- '[[Java - Basic injection]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Print Class Loader Information]]'
- '[[Print HTML Content]]'
- '[[Print Resource Path]]'
- '[[Print Two Numbers]]'
---

# Server Side Template Injection - Java Basic Injection using Java ClassLoader and Resource Retrieval

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a server-side template. In Java, one of the ways to perform SSTI is by using Java ClassLoader and Resource Retrieval. This technique allows the attacker to load and execute arbitrary Java 

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a server-side template. In Java, one of the ways to perform SSTI is by using Java ClassLoader and Resource Retrieval. This technique allows the attacker to load and execute arbitrary Java classes on the server. This can lead to remote code execution (RCE) and compromise the entire system.

To perform this attack, the attacker needs to identify a vulnerable application that uses server-side templates. They then need to inject malicious code that loads and executes the attacker's Java class. Once the class is executed, the attacker can perform any action they want on the server.

This attack can be used to steal sensitive data, modify or delete files, and even take over the entire server. It can have severe consequences for the business, leading to data loss, downtime, and reputational damage.

 

## Requirements

1. Access to a vulnerable application that uses server-side templates

1. Knowledge of Java ClassLoader and Resource Retrieval

 

## Defense

1. Ensure that all server-side templates are properly sanitized and validated to prevent injection attacks

1. Implement input validation and output encoding to prevent injection attacks

1. Monitor the server for suspicious activity, such as loading and executing unknown Java classes

 

## Objectives

1. Load and execute arbitrary Java classes on the server

1. Perform remote code execution (RCE)

1. Steal sensitive data, modify or delete files, and take over the server

 

# Instructions

1. To use the Java ClassLoader and retrieve resources, follow these steps:
1. Create a ClassLoader object
2. Use the getResource() method to retrieve the resource
3. Use the getContent() method to access the content of the resource

 



**Code**: [[49
49
jdk.internal.loader.ClassLoaders$AppClassLoa]]



> The 'data' field in this JSON object contains sample code that demonstrates the usage of the Java ClassLoader and resource retrieval. The first two lines of the 'data' field perform a simple calculation and output the result. The next two lines demonstrate how to get the ClassLoader object and retrieve the path of the resource. The last line retrieves the content of a resource file named 'index.htm' located in a directory that is five levels up from the current directory. The 'instruction' field provides a high-level overview of the steps required to use the ClassLoader and retrieve resources, while the 'explain' field provides additional details for each step.



**Command** ([[Print Two Numbers]]):

```bash
49
49
```





**Command** ([[Print Class Loader Information]]):

```bash
jdk.internal.loader.ClassLoaders$AppClassLoader@3fee733d
```





**Command** ([[Print Resource Path]]):

```bash
/Users/username/project/src/main/resources/
```





**Command** ([[Print HTML Content]]):

```bash
<!DOCTYPE html>
<html>
<head>
<title>Index</title>
</head>
<body>
<h1>Welcome to the Index page</h1>
</body>
</html>

```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Print Class Loader Information]]
- [[Print HTML Content]]
- [[Print Resource Path]]
- [[Print Two Numbers]]

## Tags

- [[Java]]
- [[Java - Basic injection]]
- [[Server Side Template Injection]]


