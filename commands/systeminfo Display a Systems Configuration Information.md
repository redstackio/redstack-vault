---
id: 05cd0db7-d0ad-48b5-ae31-ee9a9a07ede4
name: systeminfo Display a Systems Configuration Information
type: command
executor: command_prompt
data: systeminfo
output: "C:\\>systeminfo\n\nHost Name:                 Bob-PC\nOS Name:          \
  \         Microsoft Windows 10 Pro\nOS Version:                10.0.18362 N/A Build\
  \ 18362\nOS Manufacturer:           Microsoft Corporation\nOS Configuration:   \
  \       Standalone Workstation\nOS Build Type:             Multiprocessor Free\n\
  Registered Owner:          Bob\nRegistered Organization:\nProduct ID:          \
  \      00330-80000-00000-AA332\nOriginal Install Date:     10/4/2019, 4:02:38 PM\n\
  System Boot Time:          1/24/2020, 10:45:03 AM\nSystem Manufacturer:       innotek\
  \ GmbH\nSystem Model:              VirtualBox\nSystem Type:               x64-based\
  \ PC\nProcessor(s):              1 Processor(s) Installed.\n                   \
  \        [01]: Intel64 Family 6 Model 158 Stepping 13 GenuineIntel ~3600 Mhz\nBIOS\
  \ Version:              innotek GmbH VirtualBox, 12/1/2006\nWindows Directory: \
  \        C:\\Windows\nSystem Directory:          C:\\Windows\\system32\nBoot Device:\
  \               \\Device\\HarddiskVolume1\nSystem Locale:             en-us;English\
  \ (United States)\nInput Locale:              en-us;English (United States)\nTime\
  \ Zone:                 (UTC-08:00) Pacific Time (US & Canada)\nTotal Physical Memory:\
  \     4,096 MB\nAvailable Physical Memory: 2,358 MB\nVirtual Memory: Max Size: \
  \ 4,800 MB\nVirtual Memory: Available: 2,998 MB\nVirtual Memory: In Use:    1,802\
  \ MB\nPage File Location(s):     C:\\pagefile.sys\nDomain:                    WORKGROUP\n\
  Logon Server:              \\\\Bob-PC\nHotfix(s):                 9 Hotfix(s) Installed.\n\
  \                           [01]: KB4515871\n                           [02]: KB4503308\n\
  \                           [03]: KB4506472\n                           [04]: KB4509096\n\
  \                           [05]: KB4515383\n                           [06]: KB4516115\n\
  \                           [07]: KB4520390\n                           [08]: KB4521863\n\
  \                           [09]: KB4517389\nNetwork Card(s):           4 NIC(s)\
  \ Installed.\n                           [01]: Intel(R) PRO/1000 MT Desktop Adapter\n\
  \                                 Connection Name: Ethernet\n                  \
  \               DHCP Enabled:    Yes\n                                 DHCP Server:\
  \     192.168.1.1\n                                 IP address(es)\n           \
  \                      [01]: 192.168.1.158\n                                 [02]:\
  \ fe80::fd84:316:b9f4:d7a7\n                           [02]: Hyper-V Virtual Ethernet\
  \ Adapter\n                                 Connection Name: vEthernet (Default\
  \ Switch)\n                                 DHCP Enabled:    No\n              \
  \                   IP address(es)\n                                 [01]: 172.18.74.241\n\
  \                                 [02]: fe80::11e5:a888:e30d:40bc\n            \
  \               [03]: Microsoft KM-TEST Loopback Adapter\n                     \
  \            Connection Name: Npcap Loopback Adapter\n                         \
  \        DHCP Enabled:    Yes\n                                 DHCP Server:   \
  \  255.255.255.255\n                                 IP address(es)\n          \
  \                       [01]: 169.254.234.189\n                                \
  \ [02]: fe80::cd04:9faa:dd51:eabd\n                           [04]: TAP-Windows\
  \ Adapter V9\n                                 Connection Name: Ethernet 2\n   \
  \                              Status:          Media disconnected\nHyper-V Requirements:\
  \      A hypervisor has been detected. Features required for Hyper-V will not be\
  \ displayed."
created_at: '2020-01-24T21:45:44.860174+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# systeminfo Display a Systems Configuration Information

```command_prompt
systeminfo
```

## Expected Output

```
C:\>systeminfo

Host Name:                 Bob-PC
OS Name:                   Microsoft Windows 10 Pro
OS Version:                10.0.18362 N/A Build 18362
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Workstation
OS Build Type:             Multiprocessor Free
Registered Owner:          Bob
Registered Organization:
Product ID:                00330-80000-00000-AA332
Original Install Date:     10/4/2019, 4:02:38 PM
System Boot Time:          1/24/2020, 10:45:03 AM
System Manufacturer:       innotek GmbH
System Model:              VirtualBox
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: Intel64 Family 6 Model 158 Stepping 13 GenuineIntel ~3600 Mhz
BIOS Version:              innotek GmbH VirtualBox, 12/1/2006
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-us;English (United States)
Input Locale:              en-us;English (United States)
Time Zone:                 (UTC-08:00) Pacific Time (US & Canada)
Total Physical Memory:     4,096 MB
Available Physical Memory: 2,358 MB
Virtual Memory: Max Size:  4,800 MB
Virtual Memory: Available: 2,998 MB
Virtual Memory: In Use:    1,802 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              \\Bob-PC
Hotfix(s):                 9 Hotfix(s) Installed.
                           [01]: KB4515871
                           [02]: KB4503308
                           [03]: KB4506472
                           [04]: KB4509096
                           [05]: KB4515383
                           [06]: KB4516115
                           [07]: KB4520390
                           [08]: KB4521863
                           [09]: KB4517389
Network Card(s):           4 NIC(s) Installed.
                           [01]: Intel(R) PRO/1000 MT Desktop Adapter
                                 Connection Name: Ethernet
                                 DHCP Enabled:    Yes
                                 DHCP Server:     192.168.1.1
                                 IP address(es)
                                 [01]: 192.168.1.158
                                 [02]: fe80::fd84:316:b9f4:d7a7
                           [02]: Hyper-V Virtual Ethernet Adapter
                                 Connection Name: vEthernet (Default Switch)
                                 DHCP Enabled:    No
                                 IP address(es)
                                 [01]: 172.18.74.241
                                 [02]: fe80::11e5:a888:e30d:40bc
                           [03]: Microsoft KM-TEST Loopback Adapter
                                 Connection Name: Npcap Loopback Adapter
                                 DHCP Enabled:    Yes
                                 DHCP Server:     255.255.255.255
                                 IP address(es)
                                 [01]: 169.254.234.189
                                 [02]: fe80::cd04:9faa:dd51:eabd
                           [04]: TAP-Windows Adapter V9
                                 Connection Name: Ethernet 2
                                 Status:          Media disconnected
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.
```


