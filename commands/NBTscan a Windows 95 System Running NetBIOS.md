---
id: 480e15da-dbbe-4f00-976f-344880fbdca1
name: NBTscan a Windows 95 System Running NetBIOS
type: command
executor: ''
data: nbtscan -r $_TARGET_IP
output: "root@kali:~# nbtscan -r 10.10.10.10\nDoing NBT name scan for addresses from\
  \ 10.10.10.10\n\nIP address       NetBIOS Name     Server    User             MAC\
  \ address      \n------------------------------------------------------------------------------\n\
  10.10.10.10      BOB-PC           <server>  <unknown>        00:0c:29:97:74:7b"
created_at: '2019-09-23T17:52:33.521404+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# NBTscan a Windows 95 System Running NetBIOS

```bash
nbtscan -r $_TARGET_IP
```

## Expected Output

```
root@kali:~# nbtscan -r 10.10.10.10
Doing NBT name scan for addresses from 10.10.10.10

IP address       NetBIOS Name     Server    User             MAC address      
------------------------------------------------------------------------------
10.10.10.10      BOB-PC           <server>  <unknown>        00:0c:29:97:74:7b
```


