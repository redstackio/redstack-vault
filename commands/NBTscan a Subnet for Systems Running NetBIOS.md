---
id: 798e0c1d-4390-4d07-8337-65ec36c2d7ab
name: NBTscan a Subnet for Systems Running NetBIOS
type: command
executor: bash
data: nbtscan $_TARGET_SUBNET/$_CIDR
output: "root@kali:~# nbtscan 10.10.10.0/24\nDoing NBT name scan for addresses from\
  \ 10.10.10.0/24\n\nIP address       NetBIOS Name     Server    User            \
  \ MAC address      \n------------------------------------------------------------------------------\n\
  10.10.10.0       Sendto failed: Permission denied\n10.10.10.10      BOB-PC    <server>\
  \  <unknown>        00:0c:29:72:eb:b4\n10.10.10.230     ALICE-PC  <server>  <unknown>\
  \        00:1a:20:66:ca:c2\n10.10.10.235     WIN95-PC            ADMINISTRATOR \
  \   00:0c:29:5d:0c:2f\n10.10.10.255     Sendto failed: Permission denied"
created_at: '2019-09-23T17:52:33.526788+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# NBTscan a Subnet for Systems Running NetBIOS

```bash
nbtscan $_TARGET_SUBNET/$_CIDR
```

## Expected Output

```
root@kali:~# nbtscan 10.10.10.0/24
Doing NBT name scan for addresses from 10.10.10.0/24

IP address       NetBIOS Name     Server    User             MAC address      
------------------------------------------------------------------------------
10.10.10.0       Sendto failed: Permission denied
10.10.10.10      BOB-PC    <server>  <unknown>        00:0c:29:72:eb:b4
10.10.10.230     ALICE-PC  <server>  <unknown>        00:1a:20:66:ca:c2
10.10.10.235     WIN95-PC            ADMINISTRATOR    00:0c:29:5d:0c:2f
10.10.10.255     Sendto failed: Permission denied
```


