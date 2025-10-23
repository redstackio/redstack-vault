---
id: 4ad1b30d-8a82-4f6f-9a03-edd449fe052e
name: wifite
type: tool
verified: false
created_at: '2019-08-28T21:17:40.462055+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# wifite

## Overview

To attack multiple WEP, WPA, and WPS encrypted networks in a row. This tool is customizable to be automated with only a few arguments. Wifite aims to be the “set it and forget it” wireless auditing tool.  Features: sorts targets by signal strength (in dB); cracks closest access points first automat

## Description

To attack multiple WEP, WPA, and WPS encrypted networks in a row. This tool is customizable to be automated with only a few arguments. Wifite aims to be the “set it and forget it” wireless auditing tool.  Features:



sorts targets by signal strength (in dB); cracks closest access points first



automatically de-authenticates clients of hidden networks to reveal SSIDs



numerous filters to specify exactly what to attack (wep/wpa/both, above certain signal strengths, channels, etc)



customizable settings (timeouts, packets/sec, etc)



“anonymous” feature; changes MAC to a random address before attacking, then changes back when attacks are complete



all captured WPA handshakes are backed up to wifite.py’s current directory



smart WPA de-authentication; cycles between all clients and broadcast deauths



stop any attack with Ctrl+C, with options to continue, move onto next target, skip to cracking, or exit



displays session summary at exit; shows any cracked keys



all passwords saved to cracked.txt










