---
id: 8b6b574f-330e-440e-ba1b-eaf446808c95
name: dirb-directory-brute-force
type: command
executor: bash
data: 'dirb http://$_TARGET_IP $_WORDLIST -r'
output: >
  root@kali:~# dirb http://10.10.10.10 common.txt -r


  -----------------

  DIRB v2.22    

  By The Dark Raver

  -----------------


  START_TIME: Fri Sep 13 21:43:08 2019

  URL_BASE: http://10.10.10.10/

  WORDLIST_FILES: common.txt

  OPTION: Not Recursive


  -----------------


  GENERATED WORDS:
  4593                                                          


  ---- Scanning URL: http://10.10.10.10/ ----

  ==> DIRECTORY:
  http://10.10.10.10/api/                                                                                                               

  ==> DIRECTORY:
  http://10.10.10.10/backups/                                                                                                           

  ==> DIRECTORY:
  http://10.10.10.10/dev/                                                                                                               

  + http://10.10.10.10/index.html
  (CODE:200|SIZE:10918)                                                                                                

  + http://10.10.10.10/server-status
  (CODE:403|SIZE:276)                                                                                               

  ==> DIRECTORY:
  http://10.10.10.10/var/                                                                                                               
                                                                                                                                                       
  -----------------

  END_TIME: Fri Sep 13 21:43:09 2019

  DOWNLOADED: 4593 - FOUND: 2
created_at: '2019-09-14T01:56:14.220988+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Web
tags:
  - directory-enumeration
  - web-reconnaissance
verified: true
validated: true
---

# dirb-directory-brute-force

## Command

```bash
dirb http://$_TARGET_IP $_WORDLIST -r
```

## Description

This command uses DIRB to perform a non-recursive brute-force scan for directories and files on a target web server using a specified wordlist. It sends HTTP requests for each wordlist entry, reporting discovered content based on response codes (e.g., 200 for found, 403 for forbidden) and sizes. Ideal for initial web reconnaissance to uncover hidden endpoints without recursing into subdirectories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | The IP address or hostname of the target web server (e.g., 10.10.10.10 or target.com) | Yes |
| $_WORDLIST | Path to the wordlist file containing potential directory/file names (e.g., /usr/share/wordlists/dirb/common.txt) | Yes |
| -r | Enables non-recursive mode; prevents scanning within discovered directories to keep the scan focused and faster | No (recommended for broad initial scans) |

## Examples

### Basic Usage

Scan a target IP with the common DIRB wordlist in non-recursive mode.

```bash
dirb http://10.10.10.10 /usr/share/wordlists/dirb/common.txt -r
```

### Advanced Usage

Scan an HTTPS target with a larger wordlist, specific extensions, and increased threads.

```bash
dirb https://target.com /usr/share/wordlists/dirb/big.txt -r -X .php,.html -t 150
```

## Expected Output

The output includes scan metadata, progress through the wordlist, and discoveries marked with '==>' for directories or '+' for files, followed by a summary.

```
root@kali:~# dirb http://10.10.10.10 common.txt -r

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Fri Sep 13 21:43:08 2019
URL_BASE: http://10.10.10.10/
WORDLIST_FILES: common.txt
OPTION: Not Recursive

-----------------

GENERATED WORDS: 4593                                                          

---- Scanning URL: http://10.10.10.10/ ----
==> DIRECTORY: http://10.10.10.10/api/                                                                                                               
==> DIRECTORY: http://10.10.10.10/backups/                                                                                                           
==> DIRECTORY: http://10.10.10.10/dev/                                                                                                               
+ http://10.10.10.10/index.html (CODE:200|SIZE:10918)                                                                                                
+ http://10.10.10.10/server-status (CODE:403|SIZE:276)                                                                                               
==> DIRECTORY: http://10.10.10.10/var/                                                                                                               
                                                                                                                                                     
-----------------
END_TIME: Fri Sep 13 21:43:09 2019
DOWNLOADED: 4593 - FOUND: 2

```

Look for '==>' lines indicating directories and '+' for accessible files. The summary shows total words processed and items found.

## Related

- [[tools/dirb]]
