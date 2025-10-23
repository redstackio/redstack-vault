---
id: a00dfda4-f08a-4543-b0ca-164f841730f8
name: Launch an Interactive FTP Session
type: command
executor: bash
data: ftp $_TARGET_IP
output: 'root@kali:~# ftp 10.10.10.10

  Connected to 10.10.10.10.

  220 Microsoft FTP Service

  Name (10.10.10.10:root): anonymous

  331 Anonymous access allowed, send identity (e-mail name) as password.

  Password:

  230 User logged in.

  Remote system type is Windows_NT.

  ftp>'
created_at: '2019-09-11T22:47:55.931243+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Launch an Interactive FTP Session

```bash
ftp $_TARGET_IP
```

## Expected Output

```
root@kali:~# ftp 10.10.10.10
Connected to 10.10.10.10.
220 Microsoft FTP Service
Name (10.10.10.10:root): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password:
230 User logged in.
Remote system type is Windows_NT.
ftp>
```


