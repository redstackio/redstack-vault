---
id: 3d8c2f91-4a7e-42b1-9c5d-7f1a3e6b8d2c
name: Network Service Discovery and Enumeration (Nmap)
type: procedure
verified: true
submitted: true
created_at: '2023-12-09T00:00:00.000000+00:00'
updated_at: '2025-11-30T21:55:00.000000+00:00'
platforms:
- Linux
- Windows
- Network
tags:
- reconnaissance
- scanning
- nmap
- service enumeration
- network discovery
- metasploitable2
mitre_tactics:
- TA0043  # Reconnaissance
mitre_techniques:
- T1046   # Network Service Discovery
skill_level: beginner
impact_level: low
detection_risk: medium
commands:
- '[[nmap service version scan with ping disabled]]'
tools:
- '[[nmap]]'
---

# Network Service Discovery and Enumeration (Nmap)

**Status**: ✓ Verified

## Summary

Perform comprehensive network service discovery using Nmap to identify all open ports, running services, and service versions on a target system. This reconnaissance technique is essential for understanding the attack surface and identifying potentially vulnerable services.

## Description

# Description 

Network service discovery is the first critical step in penetration testing and vulnerability assessment. Using Nmap's service version detection (-sV flag) combined with disabled ping checks (-Pn flag), this procedure identifies:

- All open TCP/UDP ports on the target
- Service names and versions running on each port
- Operating system fingerprinting data
- Banner information from services

For Metasploitable2 targets, this scan typically reveals multiple vulnerable services including vsftpd 2.3.4 (Port 21), Telnet (Port 23), VNC (Port 5900), PostgreSQL (Port 5432), and Apache Tomcat (Port 8180).

## MITRE ATT&CK Mapping

**Tactics:**
- TA0043 - Reconnaissance

**Techniques:**
- T1046 - Network Service Discovery

**Sub-Techniques:**
- Active Scanning
- Port Scanning
- Service Enumeration

## Instructions

### Step 1: Identify Target IP Address

First, determine the IP address of your target system. For Metasploitable2, this can be found by logging in with default credentials (msfadmin:msfadmin) and running:

```bash
ifconfig
```

Note the target IP address (e.g., 192.168.137.128 or 192.168.1.167).

### Step 2: Execute Nmap Service Version Scan

From your attacking machine (e.g., Kali Linux), run the following Nmap command:

**Command:** [[nmap service version scan with ping disabled]]

```bash
sudo nmap -sV -Pn <target_ip>
```

**Parameters Explained:**
- `-sV`: Probe open ports to determine service/version info
- `-Pn`: Treat all hosts as online -- skip host discovery
- `sudo`: Required for certain scan types

**Example:**
```bash
sudo nmap -sV -Pn 192.168.137.128
```

### Step 3: Analyze Scan Results

Review the Nmap output to identify:

1. **Open Ports**: Services accepting connections
2. **Service Versions**: Specific software versions (check for known vulnerabilities)
3. **Unusual Ports**: Non-standard port assignments
4. **Vulnerable Services**: Known exploitable services

**Expected Output Example:**
```
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
22/tcp   open  ssh         OpenSSH 4.7p1
23/tcp   open  telnet      Linux telnetd
25/tcp   open  smtp        Postfix smtpd
80/tcp   open  http        Apache httpd 2.2.8
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X
5432/tcp open  postgresql  PostgreSQL DB 8.3.0 - 8.3.7
5900/tcp open  vnc         VNC (protocol 3.3)
8180/tcp open  http        Apache Tomcat/Coyote JSP engine 1.1
```

### Step 4: Document Findings

Create a list of potentially vulnerable services:

**High Priority Targets:**
- vsftpd 2.3.4 (Port 21) - Known backdoor vulnerability
- Apache Tomcat (Port 8180) - Potential manager upload vulnerability
- PostgreSQL (Port 5432) - Payload execution vulnerability
- VNC (Port 5900) - Weak authentication

**Medium Priority:**
- Telnet (Port 23) - Unencrypted, may have default credentials
- Samba/SMB (Ports 139, 445) - Various exploit possibilities

### Step 5: Cross-Reference with Vulnerability Databases

For each identified service version, check:
- ExploitDB (searchsploit)
- Metasploit Framework modules
- CVE databases
- Vendor security advisories

## Platforms

- Linux
- Windows
- Network

## Tags

- reconnaissance
- scanning
- nmap
- service enumeration
- network discovery
- metasploitable2

## Expected Outcomes

**Success Indicators:**
✅ Complete port scan results obtained
✅ Service versions identified for all open ports
✅ Vulnerable services documented
✅ Attack surface mapped

**Output Artifacts:**
- Nmap scan results (text file)
- List of open ports and services
- Prioritized target list
- Vulnerability assessment notes

## Detection & Evasion

**Detection Risk:** 🟡 Medium

**Detection Methods:**
- Network IDS/IPS signatures for Nmap scans
- Firewall logs showing port scanning activity
- High volume of connection attempts
- SYN packet patterns

**Evasion Techniques:**
- Use timing templates: `-T2` (polite) or `-T1` (sneaky)
- Scan from multiple sources
- Use fragmented packets: `-f`
- Randomize scan order: `--randomize-hosts`

## Troubleshooting

**Issue:** No ports showing as open
- Solution: Verify network connectivity, check firewall rules, try different scan types

**Issue:** Permission denied errors
- Solution: Run with `sudo` privileges

**Issue:** Scan takes too long
- Solution: Reduce port range or use faster timing templates (`-T4`)

## Related Procedures

- [[Basic Port Scan with Aggressive Service Enumeration]]
- [[Scan list of IP's (masscan)]]
- [[Find Subdomains (amass)]]

## References

- [Nmap Official Documentation](https://nmap.org/book/man.html)
- [MITRE ATT&CK T1046](https://attack.mitre.org/techniques/T1046/)
- Metasploitable2 Exploitation Walkthrough - Rajesh Kumar
