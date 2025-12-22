---
id: 0936a276-80e7-4e3a-953b-716593b6601f
name: strings-extract-jsp-name-from-war
type: command
executor: bash
data: strings reverse.war | grep jsp
output: null
created_at: '2023-04-06T03:56:24.622871+00:00'
updated_at: '2023-04-10T20:25:27.396541+00:00'
platforms:
  - Linux
tags:
  - payload
  - java
  - extraction
verified: true
validated: true
---

# strings-extract-jsp-name-from-war

## Command

```bash
strings reverse.war | grep jsp
```

## Description

This command extracts human-readable strings from a WAR file and filters for JSP-related text to identify the embedded servlet filename in a Metasploit-generated payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| reverse.war | Path to the input WAR file | Yes |
| grep jsp | Filters output to lines containing 'jsp' | Yes |

## Examples

### Basic Usage

```bash
strings shell.war | grep jsp
```

### Advanced Usage

```bash
strings reverse.war | grep -i jsp | head -1
```

## Expected Output

A line showing the JSP filename, e.g.:

shell.jsp

or a generated name like abc123.jsp. If no output, the file may not contain a standard JSP payload.

## Related

- [[procedures/Generate-Java-Reverse-Shell-WAR-Payload]]
- [[commands/msfvenom-java-jsp-reverse-tcp-war]]
