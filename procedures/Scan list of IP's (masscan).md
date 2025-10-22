---
id: 5be83940-de36-4a10-849b-95d6e5ede9aa
name: Scan list of IP's (masscan)
type: procedure
verified: true
submitted: true
created_at: '2020-06-30T18:05:36.072614+00:00'
updated_at: '2023-05-26T00:49:55.141691+00:00'
commands:
- '[[masscan portscan list of ips]]'
---

# Scan list of IP's (masscan)

**Status**: ✓ Verified

## Summary

The heavyweight port scanner of the internet will scan a list of ip addresses very quickly. The ip input file has one ip address per line. the -p1-65535 are the ports that it will scan 

## Description

# Description

The heavyweight port scanner of the internet will scan a list of ip addresses very quickly.

The ip input file has one ip address per line. the -p1-65535 are the ports that it will scan

**Command** ([[masscan portscan list of ips]]):

```bash
masscan -iL $_IPS_FILE --rate $_RATE -p$_LOW_PORT-$_HIGH_PORT -oL $_OUTPUT_FILE
```

## Commands Used

- [[masscan portscan list of ips]]
