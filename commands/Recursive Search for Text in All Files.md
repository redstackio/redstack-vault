---
id: 66f3436b-89bb-4658-9145-2c07bf33881f
name: Recursive Search for Text in All Files
type: command
executor: bash
data: grep -R $_STRING $_PATH/*
output: 'bob@a7ffb5e7e757:/$ grep -R passw /etc/* 2>/dev/null

  /etc/adduser.conf:# Please note that system software, such as the users allocated
  by the base-passwd

  /etc/bindresvport.blacklist:774 # rpasswd

  /etc/cron.daily/passwd:for FILE in passwd group shadow gshadow; do

  /etc/debconf.conf:# World-readable, and accepts everything but passwords.

  /etc/debconf.conf:Reject-Type: password

  /etc/debconf.conf:# Not world readable (the default), and accepts only passwords.

  /etc/debconf.conf:Name: passwords'
created_at: '2020-03-10T07:20:54.637311+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Recursive Search for Text in All Files

```bash
grep -R $_STRING $_PATH/*
```

## Expected Output

```
bob@a7ffb5e7e757:/$ grep -R passw /etc/* 2>/dev/null
/etc/adduser.conf:# Please note that system software, such as the users allocated by the base-passwd
/etc/bindresvport.blacklist:774 # rpasswd
/etc/cron.daily/passwd:for FILE in passwd group shadow gshadow; do
/etc/debconf.conf:# World-readable, and accepts everything but passwords.
/etc/debconf.conf:Reject-Type: password
/etc/debconf.conf:# Not world readable (the default), and accepts only passwords.
/etc/debconf.conf:Name: passwords
```
