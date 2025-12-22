---
type: command
executor: bash
data: tshark -r $_PCAP_FILE -x
output: |-
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
platforms:
  - Linux
tags:
  - packet-analysis
  - hex-dump
verified: true
validated: true
---

# tshark-read-pcap-hex-ascii-dump

## Command

```bash
tshark -r $_PCAP_FILE -x
```

## Description

This command reads packets from a specified PCAP capture file and displays their contents in both hexadecimal and ASCII formats. It is particularly useful for manual inspection of raw packet data, such as extracting plaintext credentials from unencrypted protocols like LDAP binds or HTTP requests in offline analysis scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PCAP_FILE | Path to the input PCAP file (e.g., ldap_capture.pcap) | Yes |
| -r | Read packet data from the specified capture file | Built-in |
| -x | Include a hex and ASCII dump of each packet's payload bytes | Built-in |

## Examples

### Basic Usage

```bash
tshark -r ldap.pcap -x
```

### Advanced Usage

```bash
tshark -r ldap.pcap -x -Y "ldap" | head -20
```

> Filters the output to LDAP packets only using a display filter (-Y "ldap") and limits to the first 20 lines for quick review.

## Expected Output

Description of what output to expect when the command runs successfully. The output includes packet headers, protocol dissections (if applicable), and a detailed hex/ASCII dump of the packet bytes. Note that running as root may trigger a Lua loading warning, but it does not prevent execution. Sample output shows dissected LDAP traffic with visible credentials in ASCII.

## Related

- [[tools/TShark]]
- [[procedures/Sniff-Unencrypted-LDAP-Queries-via-Loopback]]
