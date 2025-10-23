---
id: 994b0ba0-cc1f-4bce-b580-50ecf1879550
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:21:27.746033+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 994b0ba0

**Language**: Bash

```bash

echo open 10.1.2.3> C:\script.txt
echo user myftpuser>> C:\script.txt
echo pass myftppass>> C:\script.txt
echo put E:\backups\database.dbf>> C:\script.txt
echo bye>> C:\script.txt
ftp -s:script.txt

```


