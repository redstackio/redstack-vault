---
id: bd1ce063-6b86-41a4-aed4-0e6b7a889fd4
name: Copy file to folder
type: command
executor: ''
data: xcopy C:\$FILENAME t:\FILENAME
output: 'xcopy c:\file.exe t:\file.exe

  Does t:\file.exe specify a file name or directory name on the target

  (F = File, D = directory) ? F

  c:\file.exe

  1 File(s) copied'
created_at: '2023-01-12T22:19:00.383458+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Copy file to folder

```bash
xcopy C:\$FILENAME t:\FILENAME
```

## Expected Output

```
xcopy c:\file.exe t:\file.exe
Does t:\file.exe specify a file name or directory name on the target
(F = File, D = directory) ? F
c:\file.exe
1 File(s) copied
```


