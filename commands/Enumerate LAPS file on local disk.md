---
id: 183a59a2-dfc0-46a1-86ba-8382b315a455
name: Enumerate LAPS file on local disk
type: command
executor: command_prompt
data: 'dir "C:\Program Files\LAPS\CSE\Admpwd.dll"

  '
output: '    Directory: C:\Program Files\LAPS\CSE

  Mode                 LastWriteTime         Length Name

  ----                 -------------         ------ ----

  -a----        2022-05-06  10:20 PM         244898 Admpwd.dll'
created_at: '2023-01-12T19:12:06.789118+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Enumerate LAPS file on local disk

```command_prompt
dir "C:\Program Files\LAPS\CSE\Admpwd.dll"

```

## Expected Output

```
    Directory: C:\Program Files\LAPS\CSE

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        2022-05-06  10:20 PM         244898 Admpwd.dll
```
