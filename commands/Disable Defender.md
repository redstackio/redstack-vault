---
id: 4a892d0c-821a-4ad9-b511-b3a1920c7dd3
name: Disable Defender
type: command
executor: powershell
data: Set-MpPReference -DisableRealtimeMonitoring $true -Verbose
output: Set-MpPReference -DisableRealtimeMonitoring $true -Verbose
created_at: '2023-01-10T04:46:44.806628+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[SET]]'
- '[[Set-MpPreference]]'
---

# Disable Defender

```powershell
Set-MpPReference -DisableRealtimeMonitoring $true -Verbose
```

## Expected Output

```
Set-MpPReference -DisableRealtimeMonitoring $true -Verbose
```


