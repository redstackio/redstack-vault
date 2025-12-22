---
id: dd5a3824-1ab8-4330-a01c-56c725b02755
name: Basic-EL-Expression-Syntax-Examples
type: code
language: java
verified: true
created_at: '2023-04-06T03:56:38.948972+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - Java
tags:
  - el-injection
  - ssti
  - syntax
validated: true
---

# Basic-EL-Expression-Syntax-Examples

## Code

```java
${<property>}
${1+1}

#{<expression string>}
#{1+1}

T(<javaclass>)
```

## Description

This code snippet illustrates fundamental EL syntax for injection testing in Java web applications. It shows immediate evaluation with ${} for property access and arithmetic, deferred evaluation with #{} for runtime expressions, and T() for static Java class references. Use these patterns as building blocks for SSTI payloads to probe and exploit EL vulnerabilities.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $<property> | Property, bean, or implicit object to access | pageContext.request.method |
| $<expression string> | Valid EL expression for deferred evaluation | system['os.name'] |
| $<javaclass> | Fully qualified Java class name | java.lang.System |

## Usage

Embed these snippets directly into vulnerable input fields (e.g., via Burp Repeater or curl) in JSP/JSF applications. Start with simple tests like ${1+1} to confirm evaluation, then escalate to T(java.lang.Runtime).getRuntime().exec('id') for RCE. This is typically used in web pentesting to validate EL injection points before crafting advanced payloads.

## Detection

- Web logs showing EL evaluation errors or unusual property accesses (e.g., ${ or #{} in request parameters).
- Application server logs (e.g., Tomcat) with exceptions from invalid EL contexts or static method invocations.
- WAF alerts for SSTI signatures matching EL patterns.
- Anomalous server-side executions, such as unexpected process spawns from Runtime.exec().

## Related

- [[procedures/Basic-EL-Injection-in-Java-Web-Applications]]
