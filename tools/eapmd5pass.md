---
id: 2b75b232-01b3-415d-ba59-13667c7ec87f
name: eapmd5pass
type: tool
verified: false
created_at: '2019-08-28T21:17:31.129720+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# eapmd5pass

## Overview

EAP-MD5 is a legacy authentication mechanism that does not provide sufficient protection for user authentication credentials. Users who authenticate using EAP-MD5 subject themselves to an offline dictionary attack vulnerability. This tool reads from a live network interface in monitor-mode, or from

## Description

EAP-MD5 is a legacy authentication mechanism that does not provide sufficient protection for user authentication credentials. Users who authenticate using EAP-MD5 subject themselves to an offline dictionary attack vulnerability. This tool reads from a live network interface in monitor-mode, or from a stored libpcap capture file, and extracts the portions of the EAP-MD5 authentication exchange. Once the challenge and response portions have been collected from this exchange, eapmd5pass will mount an offline dictionary attack against the user’s password.






