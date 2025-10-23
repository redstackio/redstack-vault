---
id: daa4a37e-09cc-46d4-96df-2a7e927fd083
name: Tshark Extract Hex and ASCII Dump from a Pcap
type: command
executor: bash
data: tshark -r $_DUMP.pcap -x
output: "root@kali:~# tshark -r dump.pcap -x\nRunning as user \"root\" and group \"\
  root\". This could be dangerous.\ntshark: Lua: Error during loading:\n /usr/share/wireshark/init.lua:32:\
  \ dofile has been disabled due to running Wireshark as superuser. See https://wiki.wireshark.org/CaptureSetup/CapturePrivileges\
  \ for help in running Wireshark as an unprivileged user.\n\n\n0000  00 00 00 00\
  \ 00 00 00 00 00 00 00 00 08 00 45 00   ..............E.\n0010  00 8f 9b f9 40 00\
  \ 40 06 75 6e 0a 0a 0a 77 0a 0a   ....@.@.un...w..\n0020  0a 77 e8 0e 01 85 6f 65\
  \ 03 0c 5d 2e 65 b2 80 18   .w....oe..].e...\n0030  02 ab 29 83 00 00 01 01 08 0a\
  \ 00 04 98 fc 00 04   ..).............\n0040  98 fc 30 59 02 01 01 60 54 02 01 03\
  \ 04 2d 75 69   ..0Y...`T....-ui\n0050  64 3d 6c 64 61 70 75 73 65 72 32 2c 6f 75\
  \ 3d 50   d=username1,ou=P\n0060  65 6f 70 6c 65 2c 64 63 3d 6c 69 67 68 74 77 65\
  \   eople,dc=central\n0070  69 67 68 74 2c 64 63 3d 68 74 62 80 20 38 62 63   bank,dc=com.\
  \ 6et\n0080  38 32 35 31 33 33 32 61 62 65 31 64 37 66 31 30   5646ds64624ss880\n\
  0090  35 64 33 65 35 33 61 64 33 39 61 63 32            465823ad463f2"
created_at: '2019-10-09T21:17:13.470504+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Tshark Extract Hex and ASCII Dump from a Pcap

```bash
tshark -r $_DUMP.pcap -x
```

## Expected Output

```
root@kali:~# tshark -r dump.pcap -x
Running as user "root" and group "root". This could be dangerous.
tshark: Lua: Error during loading:
 /usr/share/wireshark/init.lua:32: dofile has been disabled due to running Wireshark as superuser. See https://wiki.wireshark.org/CaptureSetup/CapturePrivileges for help in running Wireshark as an unprivileged user.


0000  00 00 00 00 00 00 00 00 00 00 00 00 08 00 45 00   ..............E.
0010  00 8f 9b f9 40 00 40 06 75 6e 0a 0a 0a 77 0a 0a   ....@.@.un...w..
0020  0a 77 e8 0e 01 85 6f 65 03 0c 5d 2e 65 b2 80 18   .w....oe..].e...
0030  02 ab 29 83 00 00 01 01 08 0a 00 04 98 fc 00 04   ..).............
0040  98 fc 30 59 02 01 01 60 54 02 01 03 04 2d 75 69   ..0Y...`T....-ui
0050  64 3d 6c 64 61 70 75 73 65 72 32 2c 6f 75 3d 50   d=username1,ou=P
0060  65 6f 70 6c 65 2c 64 63 3d 6c 69 67 68 74 77 65   eople,dc=central
0070  69 67 68 74 2c 64 63 3d 68 74 62 80 20 38 62 63   bank,dc=com. 6et
0080  38 32 35 31 33 33 32 61 62 65 31 64 37 66 31 30   5646ds64624ss880
0090  35 64 33 65 35 33 61 64 33 39 61 63 32            465823ad463f2
```


