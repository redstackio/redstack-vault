---
id: 48c5c5e1-956b-4f3a-827a-2d9648dd9e8e
name: Web Enumeration and Backup File Discovery
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.819302+00:00'
updated_at: '2023-04-10T20:21:17.610664+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
tags:
- '[[Active recon]]'
- '[[Bug Hunting Methodology and Enumeration]]'
- '[[Web discovery]]'
commands:
- '[[bfac scan on http://example.com/test.php]]'
- '[[bfac scan on testing_list.txt]]'
- '[[Directory Enumeration with Gobuster]]'
---

# Web Enumeration and Backup File Discovery

## Summary

Web Enumeration and Backup File Discovery is a technique used to discover hidden directories and files on a web server. This technique is used by attackers to gather information about the target to identify vulnerabilities that can be exploited. The technique involves using tools like Gobuster and 

## Description

# Description

Web Enumeration and Backup File Discovery is a technique used to discover hidden directories and files on a web server. This technique is used by attackers to gather information about the target to identify vulnerabilities that can be exploited. The technique involves using tools like Gobuster and BFAC Backup File Finder to enumerate directories and files. Gobuster is a tool that bruteforces directories and files on a web server while BFAC Backup File Finder is a tool that searches for backup files on a web server.

Technical Explanation: The technique involves sending requests to the web server using a wordlist to discover hidden directories and files. These directories and files may contain sensitive information that can be used to exploit vulnerabilities on the target system. The technique can also be used to discover backup files that may contain sensitive information such as passwords and configuration files.

Business Value: This technique can be used by organizations to identify vulnerabilities on their web servers before attackers can exploit them. By discovering hidden directories and files, organizations can take steps to secure their web servers and prevent data breaches.

## Requirements

1. Access to the target web server

1. Tools like Gobuster and BFAC Backup File Finder

## Defense

1. Disable directory listing on the web server to prevent attackers from discovering hidden directories and files

1. Implement access controls to prevent unauthorized access to sensitive directories and files

1. Regularly scan web servers for hidden directories and files to identify potential vulnerabilities

## Objectives

1. Identify hidden directories and files on a web server

1. Discover backup files that may contain sensitive information

# Instructions

1. Use gobuster or ffuf to enumerate subdirectories and files on a target website. The `-w` flag specifies the wordlist to be used for the enumeration, `-u` specifies the target URL, and `-t` specifies the number of threads to be used for the enumeration.

**Code**: [[# gobuster -w wordlist -u URL -t threads
./gobuste]]

> -w: Specifies the wordlist to be used for the enumeration.
-u: Specifies the target URL.
-t: Specifies the number of threads to be used for the enumeration.

**Command** ([[Directory Enumeration with Gobuster]]):

```bash
# gobuster -w wordlist -u URL -t threads
./gobuster -u http://example.com/ -w words.txt -t 10
```

2. BFAC is a tool that helps in finding backup files and directories that are inadvertently exposed. The tool can be used to find sensitive files that may be exposed on a website or a web application. The command line tool can be used to scan a website or a list of websites to find backup files. The tool can be run with the following commands:
1. `bfac --url <url> --level <level>`: This command is used to scan a website for backup files. The `--url` option specifies the URL of the website to scan. The `--level` option specifies the depth of the scan. The higher the value of level, the deeper the scan.
2. `bfac --list <file>`: This command is used to scan a list of websites for backup files. The `--list` option specifies the location of the file containing the list of websites to scan.

**Code**: [[bfac --url http://example.com/test.php --level 4
b]]

> The `bfac` tool is used to find backup files that are inadvertently exposed on a website or a web application. The tool can be used to scan a website or a list of websites to find backup files. The `--url` option specifies the URL of the website to scan. The `--level` option specifies the depth of the scan. The higher the value of level, the deeper the scan. The `--list` option specifies the location of the file containing the list of websites to scan. The tool can be used to find sensitive files that may be exposed on a website or a web application.

**Command** ([[bfac scan on http://example.com/test.php]]):

```bash
bfac --url http://example.com/test.php --level 4
```

**Command** ([[bfac scan on testing_list.txt]]):

```bash
bfac --list testing_list.txt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]
- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

## Commands Used

- [[bfac scan on http://example.com/test.php]]
- [[bfac scan on testing_list.txt]]
- [[Directory Enumeration with Gobuster]]

## Tags

- [[Active recon]]
- [[Bug Hunting Methodology and Enumeration]]
- [[Web discovery]]
