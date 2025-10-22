---
id: c18aaa5c-9f0c-4bc9-a4a8-b9fe9e710195
name: Transferring Files with Linux
type: cheatsheet
verified: true
created_at: '2019-10-29T22:25:12.897557+00:00'
updated_at: '2023-05-30T20:13:30.385782+00:00'
---

# Transferring Files with Linux

**Status**: ✓ Verified

## Description

Commands used for transferring files using on Linux systems.

## HTTP

**Command** ([[Launch a Python 3 Web Server]]):

```bash
python3 -m http.server $_PORT
```

**Command** ([[Python2 Web Server]]):

```bash
python2 -m SimpleHTTPServer $_PORT
```

## SMB

**Command** ([[smbserver.py Launch an SMB Server]]):

```bash
smbserver.py $_SHARE $_PATH
```

## Netcat Pipes

**Command** ([[Netcat Upload a File with a Listener]]):

```bash
nc -lvnp $_PORT < $_FILENAME
```

**Command** ([[Netcat Download a File with a Listener]]):

```bash
nc -lvnp $_PORT > $_FILENAME
```

**Command** ([[Netcat Upload a File to a Listener]]):

```bash
nc $_TARGET_IP $_TARGET_PORT < $_FILENAME
```

**Command** ([[Netcat Download a File to a Listener]]):

```bash
nc $_TARGET_IP $_TARGET_PORT > $_FILENAME
```

## Bash 4+ Pipes

**Command** ([[cat > /dev/tcp/$_TARGET_IP/$_TARGET_PORT < $_FILEN]]):

```bash
cat > /dev/tcp/$_TARGET_IP/$_TARGET_PORT < $_FILENAME
```

**Command** ([[Bash Download a File from a Listener]]):

```bash
cat > /dev/tcp/$_TARGET_IP/$_TARGET_PORT > $_FILENAME
```
