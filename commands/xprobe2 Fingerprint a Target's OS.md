---
id: b295bff0-542c-49d6-90a9-8dc37165d14a
name: xprobe2 Fingerprint a Target's OS
type: command
executor: bash
data: xprobe2 $_TARGET_IP
output: 'root@kali:~# xprobe2 10.10.10.10


  Xprobe2 v.0.3 Copyright (c) 2002-2005 fyodor@o0o.nu, ofir@sys-security.com, meder@o0o.nu


  [+] Target is 10.10.10.10

  [+] Loading modules.

  [+] Following modules are loaded:

  [x] [1] ping:icmp_ping  -  ICMP echo discovery module

  [x] [2] ping:tcp_ping  -  TCP-based ping discovery module

  [x] [3] ping:udp_ping  -  UDP-based ping discovery module

  [x] [4] infogather:ttl_calc  -  TCP and UDP based TTL distance calculation

  [x] [5] infogather:portscan  -  TCP and UDP PortScanner

  [x] [6] fingerprint:icmp_echo  -  ICMP Echo request fingerprinting module

  [x] [7] fingerprint:icmp_tstamp  -  ICMP Timestamp request fingerprinting module

  [x] [8] fingerprint:icmp_amask  -  ICMP Address mask request fingerprinting module

  [x] [9] fingerprint:icmp_port_unreach  -  ICMP port unreachable fingerprinting module

  [x] [10] fingerprint:tcp_hshake  -  TCP Handshake fingerprinting module

  [x] [11] fingerprint:tcp_rst  -  TCP RST fingerprinting module

  [x] [12] fingerprint:smb  -  SMB fingerprinting module

  [x] [13] fingerprint:snmp  -  SNMPv2c fingerprinting module

  [+] 13 modules registered

  [+] Initializing scan engine

  [+] Running scan engine

  [-] ping:tcp_ping module: no closed/open TCP ports known on 10.10.10.10. Module
  test failed

  [-] ping:udp_ping module: no closed/open UDP ports known on 10.10.10.10. Module
  test failed

  [-] No distance calculation. 10.10.10.10 appears to be dead or no ports known

  [+] Host: 10.10.10.10 is up (Guess probability: 50%)

  [+] Target: 10.10.10.10 is alive. Round-Trip Time: 0.51510 sec

  [+] Selected safe Round-Trip Time value is: 1.03021 sec

  [-] fingerprint:tcp_hshake Module execution aborted (no open TCP ports known)

  [-] fingerprint:smb need either TCP port 139 or 445 to run

  [-] fingerprint:snmp: need UDP port 161 open

  [+] Primary guess:

  [+] Host 10.10.10.10 Running OS: Pͺ4�U (Guess probability: 93%)

  [+] Cleaning up scan engine

  [+] Modules deinitialized

  [+] Execution completed.'
created_at: '2019-09-13T22:29:10.947332+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[host]]'
- '[[xprobe2]]'
---

# xprobe2 Fingerprint a Target's OS

```bash
xprobe2 $_TARGET_IP
```

## Expected Output

```
root@kali:~# xprobe2 10.10.10.10

Xprobe2 v.0.3 Copyright (c) 2002-2005 fyodor@o0o.nu, ofir@sys-security.com, meder@o0o.nu

[+] Target is 10.10.10.10
[+] Loading modules.
[+] Following modules are loaded:
[x] [1] ping:icmp_ping  -  ICMP echo discovery module
[x] [2] ping:tcp_ping  -  TCP-based ping discovery module
[x] [3] ping:udp_ping  -  UDP-based ping discovery module
[x] [4] infogather:ttl_calc  -  TCP and UDP based TTL distance calculation
[x] [5] infogather:portscan  -  TCP and UDP PortScanner
[x] [6] fingerprint:icmp_echo  -  ICMP Echo request fingerprinting module
[x] [7] fingerprint:icmp_tstamp  -  ICMP Timestamp request fingerprinting module
[x] [8] fingerprint:icmp_amask  -  ICMP Address mask request fingerprinting module
[x] [9] fingerprint:icmp_port_unreach  -  ICMP port unreachable fingerprinting module
[x] [10] fingerprint:tcp_hshake  -  TCP Handshake fingerprinting module
[x] [11] fingerprint:tcp_rst  -  TCP RST fingerprinting module
[x] [12] fingerprint:smb  -  SMB fingerprinting module
[x] [13] fingerprint:snmp  -  SNMPv2c fingerprinting module
[+] 13 modules registered
[+] Initializing scan engine
[+] Running scan engine
[-] ping:tcp_ping module: no closed/open TCP ports known on 10.10.10.10. Module test failed
[-] ping:udp_ping module: no closed/open UDP ports known on 10.10.10.10. Module test failed
[-] No distance calculation. 10.10.10.10 appears to be dead or no ports known
[+] Host: 10.10.10.10 is up (Guess probability: 50%)
[+] Target: 10.10.10.10 is alive. Round-Trip Time: 0.51510 sec
[+] Selected safe Round-Trip Time value is: 1.03021 sec
[-] fingerprint:tcp_hshake Module execution aborted (no open TCP ports known)
[-] fingerprint:smb need either TCP port 139 or 445 to run
[-] fingerprint:snmp: need UDP port 161 open
[+] Primary guess:
[+] Host 10.10.10.10 Running OS: Pͺ4�U (Guess probability: 93%)
[+] Cleaning up scan engine
[+] Modules deinitialized
[+] Execution completed.
```


