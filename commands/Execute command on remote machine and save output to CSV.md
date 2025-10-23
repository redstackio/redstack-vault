---
id: f65a79af-6207-47cd-adc3-a523fa78c288
name: Execute command on remote machine and save output to CSV
type: command
executor: bash
data: psexec.exe \\remote_machine cmd.exe /c dir > output.csv
output: null
created_at: '2023-04-06T03:56:30.905077+00:00'
updated_at: '2023-04-10T20:37:58.731576+00:00'
---

# Execute command on remote machine and save output to CSV

```bash
psexec.exe \\remote_machine cmd.exe /c dir > output.csv
```


