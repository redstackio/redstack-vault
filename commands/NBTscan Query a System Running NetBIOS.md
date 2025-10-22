---
id: f0fbb8c9-cc96-4ccd-aa1a-60838dd84c1d
name: NBTscan Query a System Running NetBIOS
type: command
executor: ''
data: nbtscan _$TARGET_IP
output: "root@kali:~# nbtscan 10.10.10.10\nDoing NBT name scan for addresses from\
  \ 10.10.10.10\n\nIP address       NetBIOS Name     Server    User             MAC\
  \ address      \n------------------------------------------------------------------------------\n\
  10.10.10.10      BOB-PC           <server>  <unknown>        00:0c:29:72:eb:b4\n"
created_at: '2019-09-23T17:52:33.520354+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# NBTscan Query a System Running NetBIOS

```bash
nbtscan _$TARGET_IP
```

## Expected Output

```
root@kali:~# nbtscan 10.10.10.10
Doing NBT name scan for addresses from 10.10.10.10

IP address       NetBIOS Name     Server    User             MAC address      
------------------------------------------------------------------------------
10.10.10.10      BOB-PC           <server>  <unknown>        00:0c:29:72:eb:b4

```
