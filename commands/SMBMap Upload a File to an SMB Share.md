---
id: c213fcb3-65e2-4d03-ac4d-8ed69b073236
name: SMBMap Upload a File to an SMB Share
type: command
executor: ''
data: smbmap -u $_USERNAME -p $_PASSWORD --upload $_FILENAME $_SHARE_NAME/$_FILENAME
  -H $_TARGET_IP
output: 'root@kali:~# smbmap -u bob -p secretpass --upload shelly.sh stuff/shelly.sh
  -H 10.10.10.10

  [+] Finding open SMB ports....

  [+] User SMB session establishd on 10.10.10.10...

  [+] Starting upload: shelly.sh (8 bytes)

  [+] Upload complete'
created_at: '2019-09-18T01:44:02.137716+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SMBMap Upload a File to an SMB Share

```bash
smbmap -u $_USERNAME -p $_PASSWORD --upload $_FILENAME $_SHARE_NAME/$_FILENAME -H $_TARGET_IP
```

## Expected Output

```
root@kali:~# smbmap -u bob -p secretpass --upload shelly.sh stuff/shelly.sh -H 10.10.10.10
[+] Finding open SMB ports....
[+] User SMB session establishd on 10.10.10.10...
[+] Starting upload: shelly.sh (8 bytes)
[+] Upload complete
```


