---
id: 4fd339e9-d58a-4879-90e2-85c12cede31a
name: Out-Minidump Dump the Memory of a Process
type: command
executor: powershell
data: Get-Process -Name $_NAME | Out-Minidump -DumpFilePath $_PATH
output: "PS C:\\Users\\Bob> Get-Process -Name firefox | Out-Minidump -DumpFilePath\
  \ dump\n\n\n    Directory: C:\\Users\\Bob\\dump\n\n\nMode                LastWriteTime\
  \         Length Name\n----                -------------         ------ ----\n-a----\
  \         1/2/2020  11:38 AM      523874048 firefox_436.dmp\n-a----         1/2/2020\
  \  11:38 AM      278172737 firefox_4144.dmp\n-a----         1/2/2020  11:38 AM \
  \     354892209 firefox_4720.dmp\n-a----         1/2/2020  11:39 AM      300889171\
  \ firefox_5016.dmp\n-a----         1/2/2020  11:39 AM      551828008 firefox_8776.dmp"
created_at: '2020-01-02T19:41:41.009034+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Out-Minidump Dump the Memory of a Process

```powershell
Get-Process -Name $_NAME | Out-Minidump -DumpFilePath $_PATH
```

## Expected Output

```
PS C:\Users\Bob> Get-Process -Name firefox | Out-Minidump -DumpFilePath dump


    Directory: C:\Users\Bob\dump


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         1/2/2020  11:38 AM      523874048 firefox_436.dmp
-a----         1/2/2020  11:38 AM      278172737 firefox_4144.dmp
-a----         1/2/2020  11:38 AM      354892209 firefox_4720.dmp
-a----         1/2/2020  11:39 AM      300889171 firefox_5016.dmp
-a----         1/2/2020  11:39 AM      551828008 firefox_8776.dmp
```


