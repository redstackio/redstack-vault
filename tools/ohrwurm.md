---
id: 380a0e0a-fec1-42ae-98a4-53dd62f96ed6
name: ohrwurm
type: tool
verified: false
created_at: '2019-08-28T21:17:42.576638+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# ohrwurm

## Overview

ohrwurm is a small and simple RTP fuzzer that has been successfully tested on a small number of SIP phones. Features: reads SIP messages to get information of the RTP port numbers reading SIP can be omitted by providing the RTP port numbers, sothat any RTP traffic can be fuzzed RTCP traffic can be 

## Description

ohrwurm is a small and simple RTP fuzzer that has been successfully tested on a small number of SIP phones. Features:



reads SIP messages to get information of the RTP port numbers



reading SIP can be omitted by providing the RTP port numbers, sothat any RTP traffic can be fuzzed



RTCP traffic can be suppressed to avoid that codecs



learn about the “noisy line”



special care is taken to break RTP handling itself



the RTP payload is fuzzed with a constant BER



the BER is configurable



requires arpspoof from dsniff to do the MITM attack



requires both phones to be in a switched LAN (GW operation only works partially)










