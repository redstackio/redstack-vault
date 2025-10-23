---
id: f48ea886-17c6-4ebf-9029-439e17612ca9
name: Export AppLocker Rules in XML
type: command
executor: powershell
data: powershell -nop -c "Import-Module AppLocker; Get-AppLockerPolicy -Effective
  -Xml"
output: 'PS C:\users> powershell -nop -c "Import-Module AppLocker; Get-AppLockerPolicy
  -Effective -Xml"

  <AppLockerPolicy Version="1"><RuleCollection Type="Appx" EnforcementMode="NotConfigured"
  /><RuleCollection Type="Dll" EnforcementMode="NotConfigured" /><RuleCollection Type="Exe"
  EnforcementMode="Enabled"><FilePathRule Id="921cc481-6e17-4653-8f75-050b80acca20" '
created_at: '2019-11-14T23:38:41.540665+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Export AppLocker Rules in XML

```powershell
powershell -nop -c "Import-Module AppLocker; Get-AppLockerPolicy -Effective -Xml"
```

## Expected Output

```
PS C:\users> powershell -nop -c "Import-Module AppLocker; Get-AppLockerPolicy -Effective -Xml"
<AppLockerPolicy Version="1"><RuleCollection Type="Appx" EnforcementMode="NotConfigured" /><RuleCollection Type="Dll" EnforcementMode="NotConfigured" /><RuleCollection Type="Exe" EnforcementMode="Enabled"><FilePathRule Id="921cc481-6e17-4653-8f75-050b80acca20" 
```


