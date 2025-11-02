---
id: da2d00e4-9966-403e-8ab0-10c2c7ba14b8
name: Nmap UDP Scan with Service Enumeration
type: command
executor: bash
data: nmap -sU -sV $_TARGET_IP -oN $_OUTPUT
output: 'root@kali:~# nmap -sU -sV 10.10.10.10 -oN udpports

  Starting Nmap 7.70 ( https://nmap.org ) at 2019-10-11 15:08 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.00038s latency).

  Not shown: 992 closed ports

  PORT     STATE         SERVICE      VERSION

  137/udp  open          netbios-ns   Microsoft Windows netbios-ns (workgroup: WORKGROUP)

  138/udp  open|filtered netbios-dgm

  161/udp  open          snmp         SNMPv1 server (public)

  500/udp  open|filtered isakmp

  1900/udp open|filtered upnp

  3702/udp open|filtered ws-discovery

  4500/udp open|filtered nat-t-ike

  5355/udp open|filtered llmnr

  MAC Address: 08:00:27:02:B4:38 (Oracle VirtualBox virtual NIC)

  Service Info: Host: VICTIM-PC; OS: Windows; CPE: cpe:/o:microsoft:windows


  Service detection performed. Please report any incorrect results at https://nmap.org/submit/
  .

  Nmap done: 1 IP address (1 host up) scanned in 852.73 seconds'
created_at: '2019-10-11T19:37:17.022538+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
- '[[host]]'
---

# Nmap UDP Scan with Service Enumeration

```bash
nmap -sU -sV $_TARGET_IP -oN $_OUTPUT
```

## Expected Output

```
root@kali:~# nmap -sU -sV 10.10.10.10 -oN udpports
Starting Nmap 7.70 ( https://nmap.org ) at 2019-10-11 15:08 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00038s latency).
Not shown: 992 closed ports
PORT     STATE         SERVICE      VERSION
137/udp  open          netbios-ns   Microsoft Windows netbios-ns (workgroup: WORKGROUP)
138/udp  open|filtered netbios-dgm
161/udp  open          snmp         SNMPv1 server (public)
500/udp  open|filtered isakmp
1900/udp open|filtered upnp
3702/udp open|filtered ws-discovery
4500/udp open|filtered nat-t-ike
5355/udp open|filtered llmnr
MAC Address: 08:00:27:02:B4:38 (Oracle VirtualBox virtual NIC)
Service Info: Host: VICTIM-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 852.73 seconds
```


