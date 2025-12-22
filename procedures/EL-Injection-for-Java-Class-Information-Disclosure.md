---
id: edf1425c-4ba1-448d-b22b-2de67475201b
name: EL-Injection-for-Java-Class-Information-Disclosure
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:38.974271+00:00'
updated_at: '2023-04-10T20:23:39.619654+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Software Discovery|T1518 - Software Discovery]]'
sub_techniques: []
tags:
  - expression-language-el
  - expression-language-el-properties
  - server-side-template-injection
commands: []
platforms:
  - Web
  - Java
tools: []
validated: true
---

# EL-Injection-for-Java-Class-Information-Disclosure

## Summary

This procedure demonstrates how to exploit Server-Side Template Injection (SSTI) vulnerabilities using Expression Language (EL) to disclose information about Java classes on the server. By injecting EL expressions into vulnerable templates, attackers can access class properties, methods, and system details, aiding in reconnaissance and further exploitation.

## Description

Server-Side Template Injection (SSTI) occurs when user input is unsafely embedded into server-side templates, allowing execution of arbitrary code. In Java-based applications using Expression Language (EL), such as JSP or other templating engines, attackers can inject EL syntax to interact with Java objects. This procedure focuses on disclosing Java class information, such as class names, methods, and runtime details, which reveals server configuration, installed software, and potential attack vectors. The technique is particularly effective against web applications that process user-supplied data in templates without proper sanitization. Expected outcomes include enumeration of sensitive system properties, which can inform subsequent attacks like remote code execution.

## Requirements

1. Access to a web application with a vulnerable server-side template (e.g., JSP page accepting user input).
2. Ability to inject and submit EL expressions via HTTP requests (e.g., using a browser, curl, or proxy like Burp Suite).
3. Basic knowledge of Java classes, EL syntax, and the target application's input points.
4. Network access to the target server.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for all user inputs in templates, using whitelisting for allowed characters and rejecting EL syntax like ${...}.
- Disable or restrict EL evaluation in templating engines where possible, or use secure alternatives like parameterized queries.
- Employ Web Application Firewalls (WAFs) to detect and block injection patterns, including EL expressions.
- Monitor application logs for anomalous template executions and enable detailed logging of template processing.
- Regularly update Java and templating libraries to patch known SSTI vulnerabilities.

## Objectives

1. Identify and disclose Java class names and properties to map the server's software environment.
2. Enumerate methods and runtime details to uncover potential escalation paths.
3. Gather reconnaissance data for further exploitation, such as identifying vulnerable classes for RCE.

## Instructions

### Step 1: Identify Injection Point and Test Basic EL Execution

**Context**: Locate a user input field or parameter in the web application that is rendered in a server-side template (e.g., a search box or profile field). Test for SSTI by injecting a simple EL expression to confirm execution.

Inject the following EL expression into the vulnerable input:

Use [[codes/EL-Expressions-for-Class-Information-Disclosure]] for the payload.

```el
${7*7}
```

> This basic test evaluates to 49 if EL is executable. If the output shows 49 instead of the literal string, SSTI is confirmed. This step verifies the vulnerability without disclosing sensitive data.

### Step 2: Disclose Object Class Name

**Context**: Once SSTI is confirmed, use EL to query the class of an input object (e.g., the second parameter in a template context, often accessible as ${2}). This reveals the type of objects processed by the template.

Inject the following EL expression:

Use [[codes/EL-Expressions-for-Class-Information-Disclosure]] for the payload.

```el
${2.class}
```

> Expected output is the fully qualified class name of the object, such as "java.lang.String". This helps identify the context and available objects for further queries. If no output or an error occurs, try alternative indices like ${0} or ${1}.

### Step 3: Query Specific Class by Name

**Context**: Load and inspect a known Java class to gather its details, confirming access to the Java runtime environment.

Inject the following EL expression:

Use [[codes/EL-Expressions-for-Class-Information-Disclosure]] for the payload.

```el
${2.class.forName("java.lang.String")}
```

> Expected output is the class object for java.lang.String, such as "class java.lang.String". This validates the ability to dynamically load classes, a precursor to more advanced discovery.

### Step 4: Enumerate Class Methods

**Context**: Access method details of a critical class like java.lang.Runtime to understand available functions for potential exploitation.

Inject the following EL expression:

Use [[codes/EL-Expressions-for-Class-Information-Disclosure]] for the payload.

```el
${''.getClass().forName('java.lang.Runtime').getMethods()[6].toString()}
```

> Expected output details the getRuntime() method, such as "public static java.lang.Runtime java.lang.Runtime.getRuntime()". The index [6] targets the getRuntime method; adjust based on method order if needed. This reveals executable methods for RCE paths.

### Step 5: Analyze and Escalate Findings

**Context**: Review disclosed information for actionable intelligence, such as vulnerable methods or system properties.

Manually inspect the outputs from previous steps. Cross-reference with known Java vulnerabilities (e.g., via CVE databases). If runtime access is confirmed, proceed to advanced EL injections for command execution.

> Success is indicated by consistent class/method disclosures without errors. Document findings for chaining into other procedures like EL-based RCE.
