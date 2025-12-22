---
type: command
executor: bash
data: RsaCtfTool.py --dumpkey --key $_PUBLIC_KEY
output: >-
  [*] n:
  28794995250247715125026902658508399167022642246754153962374085581490401761510536853891919256319844764809658298530895125149489182364275067161035447061269397464845583379731219792001107968871037119699720250018480415163607543285344974686394414632252605303434651948041240578698528072366449573700742853462017590619176926184666101769631865122073235509298433541986351174718136151881239833931653153829201243212310986820725865666547065589474534883747531130648735885921000566622174465185593122397235039492515760056930328159655643117088573165069724497221892618198046184862379035006966118331403614996335315316208493348576217531831

  [*] e: 65537
tags:
  - cryptography
  - key-extraction
platforms:
  - Linux
  - Windows
  - macOS
verified: true
validated: true
---

# rsa-ctf-tool-dump-parameters-from-public-key

## Command

```bash
RsaCtfTool.py --dumpkey --key $_PUBLIC_KEY
```

## Description

This command extracts and displays the key parameters (modulus n and public exponent e) from an RSA public key file. It is the first step in analyzing a public key for potential cryptographic weaknesses before applying specific attacks like Wiener's or Fermat's factorization. Use this when you have obtained a target public key (e.g., from SSH or a web server) and need to inspect its components.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--dumpkey` | Dumps the RSA parameters from the key file | Yes |
| `--key` | Path to the input public key file (PEM or OpenSSH format) | Yes |
| `$_PUBLIC_KEY` | Placeholder for the public key file path (e.g., id_rsa.pub) | Yes |

## Examples

### Basic Usage

```bash
RsaCtfTool.py --dumpkey --key id_rsa.pub
```

Extracts parameters from a local public key file.

### Advanced Usage

```bash
RsaCtfTool.py --dumpkey --key ./keys/target.pub -v
```

Includes verbose output for additional details during extraction.

## Expected Output

```
@kali:~# RsaCtfTool.py --dumpkey --key id_rsa.pub 
[*] n: 28794995250247715125026902658508399167022642246754153962374085581490401761510536853891919256319844764809658298530895125149489182364275067161035447061269397464845583379731219792001107968871037119699720250018480415163607543285344974686394414632252605303434651948041240578698528072366449573700742853462017590619176926184666101769631865122073235509298433541986351174718136151881239833931653153829201243212310986820725865666547065589474534883747531130648735885921000566622174465185593122397235039492515760056930328159655643117088573165069724497221892618198046184862379035006966118331403614996335315316208493348576217531831
[*] e: 65537
```

The output shows the large modulus n (product of primes p and q) and the public exponent e (commonly 65537). If the key is malformed, an error will be raised.

## Related

- [[Related Procedure: Analyze RSA Key for Wiener Attack]]
- [[tools/RsaCtfTool]] (parent tool)
- [[commands/rsa-ctf-tool-wiener-attack]] (follow-up command for attacking the dumped parameters)
