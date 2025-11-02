---
id: b13e8ebe-2e60-4a4c-a8da-d12363dd8bfb
name: Nmap Service Scan of UDP ports
type: command
executor: bash
data: nmap -sU -sV $_TARGET_IP
output: 'root@kali:~# nmap -sU -sV 10.10.10.10

  Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 17:31 EDT

  Nmap scan report for 10.10.10.10

  Host is up (0.00071s latency).

  Not shown: 946 closed ports, 49 open|filtered ports

  PORT      STATE SERVICE    VERSION

  53/udp    open  domain     ISC BIND 9.4.2

  111/udp   open  rpcbind    2 (RPC #100000)

  137/udp   open  netbios-ns Samba nmbd netbios-ns (workgroup: WORKGROUP)

  2049/udp  open  nfs        2-4 (RPC #100003)

  35794/udp open  nlockmgr   1-4 (RPC #100021)

  MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)

  Service Info: Host: HOST


  Service detection performed. Please report any incorrect results at https://nmap.org/submit/
  .

  Nmap done: 1 IP address (1 host up) scanned in 1236.35 seconds'
created_at: '2019-09-13T22:29:10.914972+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Nmap]]'
- '[[host]]'
---

# Nmap Service Scan of UDP ports

```bash
nmap -sU -sV $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmap -sU -sV 10.10.10.10
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 17:31 EDT
Nmap scan report for 10.10.10.10
Host is up (0.00071s latency).
Not shown: 946 closed ports, 49 open|filtered ports
PORT      STATE SERVICE    VERSION
53/udp    open  domain     ISC BIND 9.4.2
111/udp   open  rpcbind    2 (RPC #100000)
137/udp   open  netbios-ns Samba nmbd netbios-ns (workgroup: WORKGROUP)
2049/udp  open  nfs        2-4 (RPC #100003)
35794/udp open  nlockmgr   1-4 (RPC #100021)
MAC Address: 08:00:27:31:27:7A (Oracle VirtualBox virtual NIC)
Service Info: Host: HOST

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1236.35 seconds
```


