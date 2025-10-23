---
id: 17892c55-8d44-4952-bb1f-73adbe6d1a39
name: braa
type: tool
verified: false
created_at: '2019-08-28T21:17:22.925210+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# braa

## Overview

Braa is a mass snmp scanner. The intended usage of such a tool is of course making SNMP queries – but unlike snmpget or snmpwalk from net-snmp, it is able to query dozens or hundreds of hosts simultaneously, and in a single process. Thus, it consumes very few system resources and does the scanning 

## Description

Braa is a mass snmp scanner. The intended usage of such a tool is of course making SNMP queries – but unlike snmpget or snmpwalk from net-snmp, it is able to query dozens or hundreds of hosts simultaneously, and in a single process. Thus, it consumes very few system resources and does the scanning VERY fast.Braa implements its OWN snmp stack, so it does NOT need any SNMP libraries like net-snmp. The implementation is very dirty, supports only several data types, and in any case cannot be stated ‘standard-conforming’! It was designed to be fast, and it is fast. For this reason (well, and also because of my laziness ;), there is no ASN.1 parser in braa – you HAVE to know the numerical values of OID’s (for instance .1.3.6.1.2.1.1.5.0 instead of system.sysName.0).braa Homepage | Kali braa Repo






