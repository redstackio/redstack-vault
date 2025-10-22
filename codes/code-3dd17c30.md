---
id: 3dd17c30-604b-4860-b248-c863496d5293
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:17.905700+00:00'
updated_at: '2023-04-10T20:34:13.316249+00:00'
---

# Code Snippet 3dd17c30

**Language**: Powershell

```powershell
sudo useradd -ou 0 -g 0 john
sudo passwd john
echo "linuxpassword" | passwd --stdin john
```
