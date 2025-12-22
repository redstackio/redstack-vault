---
id: 920b73aa-c17e-4592-9230-231795f7aaa4
name: smtp-user-enum-enumerate-users-rcpt-mode
type: command
executor: bash
data: smtp-user-enum -M RCPT -U $_USERNAME_LIST -t $_TARGET_IP
output: |
  root@kali:~# smtp-user-enum -M RCPT -U users -t 10.10.10.10
  Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

   ----------------------------------------------------------
  |                   Scan Information                       |
   ----------------------------------------------------------

  Mode ..................... RCPT
  Worker Processes ......... 5
  Usernames file ........... users
  Target count ............. 1
  Username count ........... 7
  Target TCP port .......... 25
  Query timeout ............ 5 secs
  Target domain ............ 

  ######## Scan started at Tue Sep 24 15:28:45 2019 #########
  10.10.10.10: alice exists
  10.10.10.10: root exists
  10.10.10.10: mail exists
  ######## Scan completed at Tue Sep 24 15:28:45 2019 #########
  3 results.

  7 queries in 1 seconds (7.0 queries / sec)
created_at: '2019-09-24T19:45:11.088198+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - smtp
  - user-discovery
verified: true
validated: true
---

# smtp-user-enum-enumerate-users-rcpt-mode

## Command

```bash
smtp-user-enum -M RCPT -U $_USERNAME_LIST -t $_TARGET_IP
```

## Description

This command uses smtp-user-enum in RCPT mode to enumerate valid OS-level user accounts on a target SMTP server by sending RCPT TO commands and analyzing the responses for existence indicators.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -M RCPT | Specifies the enumeration mode using RCPT TO SMTP command | Yes |
| -U $_USERNAME_LIST | Path to a file containing a list of usernames to test | Yes |
| -t $_TARGET_IP | IP address or hostname of the target SMTP server | Yes |
| -p | TCP port for SMTP (default: 25) | No |
| -T | Target domain to append to usernames (if not in file) | No |
| -w | Number of worker processes (default: 5) | No |
| -t | Query timeout in seconds (default: 5) | No |

## Examples

### Basic Usage

```bash
smtp-user-enum -M RCPT -U /path/to/users.txt -t 192.168.1.100
```

### Advanced Usage

```bash
smtp-user-enum -M RCPT -U /path/to/users.txt -t mail.example.com -p 587 -w 10 -T example.com
```

## Expected Output

```
root@kali:~# smtp-user-enum -M RCPT -U users -t 10.10.10.10
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

 ---------------------------------------------------------
|                   Scan Information                       |
 ---------------------------------------------------------

Mode ..................... RCPT
Worker Processes ......... 5
Usernames file ........... users
Target count ............. 1
Username count ........... 7
Target TCP port .......... 25
Query timeout ............ 5 secs
Target domain ............ 

######## Scan started at Tue Sep 24 15:28:45 2019 #########
10.10.10.10: alice exists
10.10.10.10: root exists
10.10.10.10: mail exists
######## Scan completed at Tue Sep 24 15:28:45 2019 #########
3 results.

7 queries in 1 seconds (7.0 queries / sec)
```

## Related

- [[tools/smtp-user-enum]]
- [[procedures/smtp-user-enumeration]]
