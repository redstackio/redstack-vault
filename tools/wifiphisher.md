---
id: 7a9b5083-7d47-41de-b024-c64e30c3f176
name: wifiphisher
type: tool
verified: false
created_at: '2019-08-28T21:17:34.757082+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# wifiphisher

## Overview

Wifiphisher is a security tool that mounts automated phishing attacks against Wi-Fi networks in order to obtain credentials or infect the victims with ‘malware’. It is a social engineering attack that can be used to obtain WPA/WPA2 secret passphrases and unlike other methods, it does not require an

## Description

Wifiphisher is a security tool that mounts automated phishing attacks against Wi-Fi networks in order to obtain credentials or infect the victims with ‘malware’. It is a social engineering attack that can be used to obtain WPA/WPA2 secret passphrases and unlike other methods, it does not require any brute forcing.

After achieving a man-in-the-middle position using the Evil Twin attack, Wifiphisher redirects all HTTP requests to an attacker-controlled phishing page.From the victim’s perspective, the attack takes place in three phases:

Victim is deauthenticated from their access point.

Victim joins a rogue access point. Wifiphisher sniffs the area and copies the target access point settings.

Victim is served a realistic specially-customized phishing page.
