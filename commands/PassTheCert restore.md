---
id: 29361b2d-9662-4380-8954-ebcb445a7fa0
name: PassTheCert restore
type: command
executor: bash
data: ./PassTheCert.exe --server dc.domain.local --cert-path C:\cert.pfx --elevate
  --target "DC=domain,DC=local" --restore restoration_file.txt
output: null
created_at: '2023-04-06T03:56:06.176594+00:00'
updated_at: '2023-04-10T20:26:17.485526+00:00'
---

# PassTheCert restore

```bash
./PassTheCert.exe --server dc.domain.local --cert-path C:\cert.pfx --elevate --target "DC=domain,DC=local" --restore restoration_file.txt
```
