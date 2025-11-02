---
id: 859b352a-5601-473d-88d2-5a8febe2595e
name: wmic Query System for Unquoted Service Paths
type: command
executor: command_prompt
data: wmic.exe service get name,displayname,pathname,startmode |findstr /i "auto"
  |findstr /i /v "c:\windows\\" |findstr /i /v """
output: 'C:\>wmic.exe service get name,displayname,pathname,startmode |findstr /i
  "auto" |findstr /i /v "c:\windows\\" |findstr /i /v """

  Skype Service    Skype C:\Program Files (x86)\Microsoft\Skype.exe --service    Auto'
created_at: '2020-01-27T20:41:03.448594+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[wmic]]'
---

# wmic Query System for Unquoted Service Paths

```command_prompt
wmic.exe service get name,displayname,pathname,startmode |findstr /i "auto" |findstr /i /v "c:\windows\\" |findstr /i /v """
```

## Expected Output

```
C:\>wmic.exe service get name,displayname,pathname,startmode |findstr /i "auto" |findstr /i /v "c:\windows\\" |findstr /i /v """
Skype Service    Skype C:\Program Files (x86)\Microsoft\Skype.exe --service    Auto
```


