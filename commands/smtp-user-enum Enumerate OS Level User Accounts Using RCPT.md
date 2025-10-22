---
id: 920b73aa-c17e-4592-9230-231795f7aaa4
name: smtp-user-enum Enumerate OS Level User Accounts Using RCPT
type: command
executor: bash
data: smtp-user-enum -M RCPT -U $_USERNAME_LIST -t $_TARGET_IP
output: "root@kali:~# smtp-user-enum -M RCPT -U users -t 10.10.10.10\nStarting smtp-user-enum\
  \ v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )\n\n ----------------------------------------------------------\n\
  |                   Scan Information                       |\n ----------------------------------------------------------\n\
  \nMode ..................... RCPT\nWorker Processes ......... 5\nUsernames file\
  \ ........... users\nTarget count ............. 1\nUsername count ........... 7\n\
  Target TCP port .......... 25\nQuery timeout ............ 5 secs\nTarget domain\
  \ ............ \n\n######## Scan started at Tue Sep 24 15:28:45 2019 #########\n\
  10.10.10.10: alice exists\n10.10.10.10: root exists\n10.10.10.10: mail exists\n\
  ######## Scan completed at Tue Sep 24 15:28:45 2019 #########\n3 results.\n\n7 queries\
  \ in 1 seconds (7.0 queries / sec)\n"
created_at: '2019-09-24T19:45:11.088198+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# smtp-user-enum Enumerate OS Level User Accounts Using RCPT

```bash
smtp-user-enum -M RCPT -U $_USERNAME_LIST -t $_TARGET_IP
```

## Expected Output

```
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

```
