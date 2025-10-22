---
id: 33f2fea4-4ffa-483a-a863-24006a38b7a9
name: sipp
type: tool
verified: false
created_at: '2019-08-28T21:17:27.543929+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# sipp

## Overview

SIPp is a free Open Source test tool / traffic generator for the SIP protocol. It includes a few basic SipStone user agent scenarios (UAC and UAS) and establishes and releases multiple calls with the INVITE and BYE methods. It can also reads custom XML scenario files describing from very simple to 

## Description

SIPp is a free Open Source test tool / traffic generator for the SIP protocol. It includes a few basic SipStone user agent scenarios (UAC and UAS) and establishes and releases multiple calls with the INVITE and BYE methods. It can also reads custom XML scenario files describing from very simple to complex call flows. It features the dynamic display of statistics about running tests (call rate, round trip delay, and message statistics), periodic CSV statistics dumps, TCP and UDP over multiple sockets or multiplexed with retransmission management and dynamically adjustable call rates.Other advanced features include support of IPv6, TLS, SCTP, SIP authentication, conditional scenarios, UDP retransmissions, error robustness (call timeout, protocol defense), call specific variable, Posix regular expression to extract and re-inject any protocol fields, custom actions (log, system command exec, call stop) on message receive, field injection from external CSV file to emulate live users.SIPp can also send media (RTP) traffic through RTP echo and RTP / pcap replay. Media can be audio or video.While optimized for traffic, stress and performance testing, SIPp can be used to run one single call and exit, providing a passed/failed verdict.Last, but not least, SIPp has a comprehensive documentation available both in HTML and PDF format.SIPp can be used to test various real SIP equipment like SIP proxies, B2BUAs, SIP media servers, SIP/x gateways, SIP PBX, … It is also very useful to emulate thousands of user agents calling your SIP system.
