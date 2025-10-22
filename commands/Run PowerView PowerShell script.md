---
id: f8c86c33-b7b3-4399-960c-6affe066c0f8
name: Run PowerView PowerShell script
type: command
executor: bash
data: 'powershell -EncodedCommand $encodedCommand

  powershell -ep bypass ./PowerView.ps1'
output: null
created_at: '2023-04-06T03:56:23.962672+00:00'
updated_at: '2023-04-10T20:37:00.767168+00:00'
---

# Run PowerView PowerShell script

```bash
powershell -EncodedCommand $encodedCommand
powershell -ep bypass ./PowerView.ps1
```
