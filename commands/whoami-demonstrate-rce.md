---
data: whoami
tags:
  - rce
  - demonstration
type: command
output: 'Output of the current user on the target system (e.g., ''tomcat'' or ''www-data'')'
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:31.159Z'
id: 20604a87-4511-4afb-ad16-5de9319464bc
verified: false
validated: true
submitted: true
---
---

# whoami-demonstrate-rce

## Command

```bash
whoami
```

## Description

This command displays the effective username of the current user executing the process, used here as a benign payload to demonstrate successful remote code execution in the PrimeFaces RCE exploit. It verifies server access without causing harm.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; prints current user | No |

## Examples

### Basic Usage

```bash
whoami
```

### Advanced Usage

N/A - This is a simple, parameterless command.

## Expected Output

The username of the current user, such as 'tomcat' for a Java web server process or 'www-data' for Apache, indicating the context in which the RCE payload executed.

## Related

- [[Related Procedure: Exploit-PrimeFaces-RCE-via-EL-Injection]]
