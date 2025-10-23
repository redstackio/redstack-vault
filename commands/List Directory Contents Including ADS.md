---
id: 3e17ab5e-7693-41d6-bc5c-65631261059f
name: List Directory Contents Including ADS
type: command
executor: command_prompt
data: dir /R
output: "C:\\temp>dir /R\n Volume in drive C has no label.\n Volume Serial Number\
  \ is E03E-1CF0\n\n Directory of C:\\temp\n\n11/22/2019  09:44 AM    <DIR>      \
  \    .\n11/22/2019  09:44 AM    <DIR>          ..\n11/22/2019  09:44 AM        \
  \     1,032 id_rsa\n11/22/2019  09:45 AM                24 normal.txt\n        \
  \                         1,032 normal.txt:secret:$DATA\n               2 File(s)\
  \          1,056 bytes\n               2 Dir(s)  26,816,774,144 bytes free"
created_at: '2019-11-22T18:04:45.283994+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List Directory Contents Including ADS

```command_prompt
dir /R
```

## Expected Output

```
C:\temp>dir /R
 Volume in drive C has no label.
 Volume Serial Number is E03E-1CF0

 Directory of C:\temp

11/22/2019  09:44 AM    <DIR>          .
11/22/2019  09:44 AM    <DIR>          ..
11/22/2019  09:44 AM             1,032 id_rsa
11/22/2019  09:45 AM                24 normal.txt
                                 1,032 normal.txt:secret:$DATA
               2 File(s)          1,056 bytes
               2 Dir(s)  26,816,774,144 bytes free
```


