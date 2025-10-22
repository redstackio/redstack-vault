---
id: f0f8c905-7c63-4d69-9086-b8d58912a6a0
name: mona Config Working Directory
type: command
executor: ''
data: '!mona config -set workingfolder c:\$_PATH\%p'
output: '[+] Command used:

  !mona config -set workingfolder C:\Logs\%p

  Writing value to configuration file

  [+] Creating config file, setting parameter workingfolder

  New value of parameter workingfolder =  C:\Logs\%p'
created_at: '2019-09-21T00:36:54.528548+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# mona Config Working Directory

```bash
!mona config -set workingfolder c:\$_PATH\%p
```

## Expected Output

```
[+] Command used:
!mona config -set workingfolder C:\Logs\%p
Writing value to configuration file
[+] Creating config file, setting parameter workingfolder
New value of parameter workingfolder =  C:\Logs\%p
```
