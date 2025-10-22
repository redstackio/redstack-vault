---
id: a0ac9593-993a-44c7-b47e-e2f74494d4fc
name: rtpbreak
type: tool
verified: false
created_at: '2019-08-28T21:17:33.205642+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# rtpbreak

## Overview

With rtpbreak you can detect, reconstruct and analyze any RTP session. It doesn’t require the presence of RTCP packets and works independently form the used signaling protocol (SIP, H.323, SCCP, …). The input is a sequence of packets, the output is a set of files you can use as input for other tool

## Description

With rtpbreak you can detect, reconstruct and analyze any RTP session. It doesn’t require the presence of RTCP packets and works independently form the used signaling protocol (SIP, H.323, SCCP, …). The input is a sequence of packets, the output is a set of files you can use as input for other tools (wireshark/tshark, sox, grep/awk/cut/ cat/sed, …). It supports also wireless (AP_DLT_IEEE802_11) networks.

reconstruct any RTP stream with an unknown or unsupported signaling protocol

reconstruct any RTP stream in wireless networks, while doing channel hopping (VoIP activity detector)

reconstruct and decode any RTP stream in batch mode (with sox, asterisk, …)

reconstruct any already existing RTP stream

reorder the packets of any RTP stream for later analysis (with tshark, wireshark, …)

build a tiny wireless VoIP tapping system in a single chip Linux unit

build a complete VoIP tapping system (rtpbreak would be just the RTP dissector module!)
