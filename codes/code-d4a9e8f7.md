---
id: d4a9e8f7-fef3-4ccb-9540-e70fab591c85
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:18.413842+00:00'
updated_at: '2023-04-10T20:34:36.510716+00:00'
---

# Code Snippet d4a9e8f7

**Language**: Powershell

```powershell
wget "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh" -O linpeas.sh
curl "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh" -o linpeas.sh
./linpeas.sh -a #all checks - deeper system enumeration, but it takes longer to complete.
./linpeas.sh -s #superfast & stealth - This will bypass some time consuming checks. In stealth mode Nothing will be written to the disk.
./linpeas.sh -P #Password - Pass a password that will be used with sudo -l and bruteforcing other users
```


