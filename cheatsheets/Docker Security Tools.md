---
id: 8c712096-a77a-4ba1-bda7-8f51eb4dbcf2
name: Docker Security Tools
type: cheatsheet
verified: false
created_at: '2020-05-31T01:49:24.518076+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Docker Security Tools

# Description

Docker Containers with Security Tools setup

# Kali LInux

**Kali Linux** is a Debian-based **Linux** distribution aimed at advanced Penetration Testing and Security Auditing. **Kali** contains several hundred tools which are geared towards various information security tasks, such as Penetration Testing, Security research, Computer Forensics and Reverse Engineering

1. Run the following command to (download) run the Kali Linux Container with a few favorite tools we pre configured.

**Code**: [[docker run --rm -ti --network host -v $PWD/work/ro]]

# Parrot OS Security Tools

Parrot OS, the flagship product of Parrot Security is a GNU/Linux distribution based on Debian and designed with Security and Privacy in mind. It includes a full portable laboratory for all kinds of cyber security operations, from pentesting to digital forensics and reverse engineering, but it also includes everything needed to develop your own software or keep your data secure.

1. Run the following command to (download) run the Parrot OS Container with Security Tools pre-configured.

**Code**: [[docker run --rm -ti --network host -v $PWD/work:/w]]
