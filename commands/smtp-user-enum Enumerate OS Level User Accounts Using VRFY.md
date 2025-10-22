---
id: 3f157e9f-56c4-4d8a-be36-31b03bb260e6
name: smtp-user-enum Enumerate OS Level User Accounts Using VRFY
type: command
executor: null
data: smtp-user-enum -M VRFY -U $_USERNAME_LIST -t $_TARGET_IP
output: "root@kali:~# smtp-user-enum -M VRFY -U users -t 10.10.10.10\nStarting smtp-user-enum\
  \ v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )\n\n ----------------------------------------------------------\n\
  |                   Scan Information                       |\n ----------------------------------------------------------\n\
  \nMode ..................... VRFY\nWorker Processes ......... 5\nUsernames file\
  \ ........... users\nTarget count ............. 1\nUsername count ........... 7\n\
  Target TCP port .......... 25\nQuery timeout ............ 5 secs\nTarget domain\
  \ ............ \n\n######## Scan started at Tue Sep 24 15:22:08 2019 #########\n\
  10.10.10.10: root exists\n10.10.10.10: mail exists\n10.10.10.10: alice exists\n\
  ######## Scan completed at Tue Sep 24 15:22:08 2019 #########\n3 results.\n\n7 queries\
  \ in 1 seconds (7.0 queries / sec)"
created_at: '2019-09-24T19:45:11.092424+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# smtp-user-enum Enumerate OS Level User Accounts Using VRFY

```bash
smtp-user-enum -M VRFY -U $_USERNAME_LIST -t $_TARGET_IP
```

## Expected Output

```
root@kali:~# smtp-user-enum -M VRFY -U users -t 10.10.10.10
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------

Mode ..................... VRFY
Worker Processes ......... 5
Usernames file ........... users
Target count ............. 1
Username count ........... 7
Target TCP port .......... 25
Query timeout ............ 5 secs
Target domain ............ 

######## Scan started at Tue Sep 24 15:22:08 2019 #########
10.10.10.10: root exists
10.10.10.10: mail exists
10.10.10.10: alice exists
######## Scan completed at Tue Sep 24 15:22:08 2019 #########
3 results.

7 queries in 1 seconds (7.0 queries / sec)
```
