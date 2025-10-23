---
id: 1a1ff284-eb19-4c4a-b423-ae0a655141ae
name: Use a local package
type: command
executor: bash
data: 'wsl --set-default-version 2

  curl.exe --insecure -L -o debian.appx https://aka.ms/wsl-debian-gnulinux

  Add-AppxPackage .\debian.appx'
output: null
created_at: '2023-04-06T03:56:28.325841+00:00'
updated_at: '2023-04-10T20:37:23.969433+00:00'
---

# Use a local package

```bash
wsl --set-default-version 2
curl.exe --insecure -L -o debian.appx https://aka.ms/wsl-debian-gnulinux
Add-AppxPackage .\debian.appx
```


