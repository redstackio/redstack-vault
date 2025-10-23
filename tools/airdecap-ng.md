---
id: 489b7109-f2f3-4e0a-9267-0310387927f6
name: airdecap-ng
type: tool
verified: false
created_at: '2019-08-28T21:17:28.370387+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# airdecap-ng

## Overview

Airdecap-ng can decrypt WEP/WPA/WPA2 capture files and it can also be used to strip the wireless headers from an unencrypted wireless capture. It outputs a new file ending with -dec.cap, which is the decrypted/stripped version of the input file.Airdecloak-ng removes WEP cloaking from a pcap file. I

## Description

Airdecap-ng can decrypt WEP/WPA/WPA2 capture files and it can also be used to strip the wireless headers from an unencrypted wireless capture.



It outputs a new file ending with -dec.cap, which is the decrypted/stripped version of the input file.Airdecloak-ng removes WEP cloaking from a pcap file. It works by reading the input file and selecting packets from a specific network. Each selected packet is put into a list and classified (default status is “unknown”). Filters are then applied (in the order specified by the user) on this list. They will change the status of the packets (unknown, uncloaked, potentially cloaked or cloaked). The order of the filters is important as each filter will base its analysis amongst other things on the status of the packets and different orders will give different results.






