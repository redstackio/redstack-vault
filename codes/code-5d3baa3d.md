---
id: 5d3baa3d-36ce-4e45-9c88-bc57ad6d08c8
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:28.325702+00:00'
updated_at: '2023-04-10T20:37:23.971306+00:00'
---

# Code Snippet 5d3baa3d

**Language**: ps1

```ps1
# List and install online packages
wsl --list --online
wsl --install -d kali-linux

# Use a local package
wsl --set-default-version 2
curl.exe --insecure -L -o debian.appx https://aka.ms/wsl-debian-gnulinux
Add-AppxPackage .\debian.appx

# Run the machine as root
wsl kali-linux --user root
```


