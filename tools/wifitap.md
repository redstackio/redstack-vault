---
id: 71c8932f-ab6b-418c-af27-876035f1d069
name: wifitap
type: tool
verified: false
created_at: '2019-08-28T21:17:26.952722+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# wifitap

## Overview

Wifitap is a proof of concept for communication over WiFi networks using traffic injection.Wifitap allows any application do send and receive IP packets using 802.11 traffic capture and injection over a WiFi network simply configuring wj0, which means : setting an IP address consistent with target 

## Description

Wifitap is a proof of concept for communication over WiFi networks using traffic injection.Wifitap allows any application do send and receive IP packets using 802.11 traffic capture and injection over a WiFi network simply configuring wj0, which means :



setting an IP address consistent with target network address range



routing desired traffic through it



In particular, it’s a cheap method for arbitrary packets injection in 802.11 frames without specific library.In addition, it will allow one to get rid of any limitation set at access point level, such as bypassing inter-client communications prevention systems (e.g. Cisco PSPF) or reaching multiple SSID handled by the same access point.






