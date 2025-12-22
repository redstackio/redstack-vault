---
id: f48ea886-17c6-4ebf-9029-439e17612ca9
type: command
executor: powershell
data: >-
  powershell -nop -c "Import-Module AppLocker; Get-AppLockerPolicy -Effective
  -Xml"
output: >-
  PS C:\users> powershell -nop -c "Import-Module AppLocker; Get-AppLockerPolicy
  -Effective -Xml"

  <AppLockerPolicy Version="1"><RuleCollection Type="Appx"
  EnforcementMode="NotConfigured" /><RuleCollection Type="Dll"
  EnforcementMode="NotConfigured" /><RuleCollection Type="Exe"
  EnforcementMode="Enabled"><FilePathRule
  Id="921cc481-6e17-4653-8f75-050b80acca20" 
created_at: '2019-11-14T23:38:41.540665+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - applocker
  - discovery
  - enumeration
verified: true
validated: true
---

# powershell-get-applocker-policy-xml

## Command

```powershell
powershell -nop -c "Import-Module AppLocker; Get-AppLockerPolicy -Effective -Xml"
```

## Description

This command imports the AppLocker PowerShell module and exports the effective AppLocker policy in XML format, revealing all configured rules for application control across file types like executables, scripts, and DLLs. Use it during discovery to assess security restrictions on a target Windows system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -nop | Non-interactive mode; skips loading user profile for faster, stealthier execution | Yes |
| -c | Command execution string | Yes |
| Import-Module AppLocker | Loads the AppLocker module (built-in on supported Windows editions) | Built-in |
| Get-AppLockerPolicy -Effective -Xml | Retrieves the merged effective policy in XML; -Effective combines local/group policy rules | Built-in |

## Examples

### Basic Usage

```powershell
powershell -nop -c "Import-Module AppLocker; Get-AppLockerPolicy -Effective -Xml"
```

### Save to File

```powershell
powershell -nop -c "Import-Module AppLocker; Get-AppLockerPolicy -Effective -Xml" | Out-File -Encoding UTF8 applocker.xml
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
PS C:\users> powershell -nop -c "Import-Module AppLocker; Get-AppLockerPolicy -Effective -Xml"
<AppLockerPolicy Version="1"><RuleCollection Type="Appx" EnforcementMode="NotConfigured" /><RuleCollection Type="Dll" EnforcementMode="NotConfigured" /><RuleCollection Type="Exe" EnforcementMode="Enabled"><FilePathRule Id="921cc481-6e17-4653-8f75-050b80acca20" Name="(Default Rule) All files located in the Program Files folder" Description="Allows members of the Everyone group to run applications that are located in the Program Files folder." UserOrGroupSid="S-1-1-0" Action="Allow"><Conditions>
```

The output is raw XML showing policy version, rule collections by type (Appx, Dll, Exe, etc.), enforcement modes, and individual rules with IDs, names, descriptions, SIDs, actions, and conditions.

## Related

- [[procedures/Enumerate-AppLocker-Rules]]
- [[techniques/Security Software Discovery|T1063]]
