---
id: 366d2204-e1e5-42cd-984e-927b0e174492
name: 'Linux Networking, Routing & Communications:'
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:35.547224+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Linux Networking, Routing & Communications:



**Command** ([[List all network interfaces]]):

```bash
/sbin/ifconfig -a
cat /etc/network/interfaces

```







**Command** ([[Display ARP communications]]):

```bash
arp -a

```







**Command** ([[Display route information]]):

```bash
route

```







**Command** ([[Show configured DNS sever addresses]]):

```bash
cat /etc/resolv.conf

```







**Command** ([[List all TCP sockets and related PIDs (-p Privileged command)]]):

```bash
netstat -antp

```







**Command** ([[List all UDP sockets and related PIDs (-p Privileged command)]]):

```bash
netstat -anup

```







**Command** ([[List rules – Privileged command]]):

```bash
iptables -L

```







**Command** ([[View port numbers/services mappings]]):

```bash
cat /etc/services

```






