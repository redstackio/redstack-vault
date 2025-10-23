---
id: ab9ff659-b9ad-4918-88ac-19b6d3629c31
name: Exclude a Folder from Windows Defender
type: command
executor: command_prompt
data: REG ADD "HKLM\SOFTWARE\Microsoft\Microsoft Antimalware\Exclusions\Paths" /v
  "$_PATH" /t REG_DWORD /d 0 /f
output: 'C:\>REG ADD "HKLM\SOFTWARE\Microsoft\Microsoft Antimalware\Exclusions\Paths"
  /v "C:\Windows\Temp" /t REG_DWORD /d 0 /f

  The operation completed successfully.'
created_at: '2020-05-28T01:04:47.842273+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Exclude a Folder from Windows Defender

```command_prompt
REG ADD "HKLM\SOFTWARE\Microsoft\Microsoft Antimalware\Exclusions\Paths" /v "$_PATH" /t REG_DWORD /d 0 /f
```

## Expected Output

```
C:\>REG ADD "HKLM\SOFTWARE\Microsoft\Microsoft Antimalware\Exclusions\Paths" /v "C:\Windows\Temp" /t REG_DWORD /d 0 /f
The operation completed successfully.
```


