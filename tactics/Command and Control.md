---
id: 5b9f6fbc-12b5-4eb8-9238-b233c8d5c17d
name: Command and Control
type: tactic
mitre_id: TA0011
mitre_url: null
created_at: '2019-08-28T21:17:44.558586+00:00'
updated_at: '2023-05-29T16:48:53.579491+00:00'
techniques:
- '[[Commonly Used Port|T1043 - Commonly Used Port]]'
- '[[Communication Through Removable Media|T1092 - Communication Through Removable
  Media]]'
- '[[Connection Proxy|T1090 - Connection Proxy]]'
- '[[Custom Command and Control Protocol|T1094 - Custom Command and Control Protocol]]'
- '[[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]'
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Data Obfuscation|T1001 - Data Obfuscation]]'
- '[[Domain Fronting|T1172 - Domain Fronting]]'
- '[[Domain Generation Algorithms|T1483 - Domain Generation Algorithms]]'
- '[[Dynamic Resolution|T1568 - Dynamic Resolution]]'
- '[[Encrypted Channel|T1573 - Encrypted Channel]]'
- '[[Fallback Channels|T1008 - Fallback Channels]]'
- '[[Multiband Communication|T1026 - Multiband Communication]]'
- '[[Multi-hop Proxy|T1188 - Multi-hop Proxy]]'
- '[[Multilayer Encryption|T1079 - Multilayer Encryption]]'
- '[[Multi-Stage Channels|T1104 - Multi-Stage Channels]]'
- '[[Non-Standard Port|T1571 - Non-Standard Port]]'
- '[[Port Knocking|T1205 - Port Knocking]]'
- '[[Protocol Tunneling|T1572 - Protocol Tunneling]]'
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
- '[[Remote File Copy|T1105 - Remote File Copy]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
- '[[Standard Cryptographic Protocol|T1032 - Standard Cryptographic Protocol]]'
- '[[Standard Non-Application Layer Protocol|T1095 - Standard Non-Application Layer
  Protocol]]'
- '[[Uncommonly Used Port|T1065 - Uncommonly Used Port]]'
- '[[Web Service|T1102 - Web Service]]'
procedures:
- '[[Abusing Active Directory ACLs/ACEs to Retrieve LAPS Passwords]]'
- '[[AdminCount-Abuse]]'
- '[[Awk-Interactive-Reverse-Shell]]'
- '[[Retrieve-AWS-IAM-Policy-Version]]'
- '[[AWS-Secrets-Manager-Credential-Exfiltration]]'
- '[[Azure-AD-Administrative-Unit-Management]]'
- '[[Install-Azure-AD-Connect-PTA-Backdoor-and-Retrieve-Logs]]'
- '[[Azure-Reconnaissance]]'
- '[[Exploit-Azure-SSRF-to-Access-VM-Metadata-Service]]'
- '[[Create-Backdoored-Docker-Image]]'
- '[[Establish-Bash-UDP-Reverse-Shell]]'
- '[[Basic-Directory-Traversal-Exploitation]]'
- '[[BITSAdmin-Download-and-Execute-Payload]]'
- '[[Browse-FTP-Site-with-Interactive-Session]]'
- '[[Bypass-SSRF-Filters-Using-Bash-Variables-and-Curl-Verbose]]'
- '[[chisel-port-forwarding-and-socks-proxy-network-pivoting]]'
- '[[Cobalt-Strike-Lateral-Movement-via-Beacon-Remote-Exploits-and-Executes]]'
- '[[Validate-Cobalt-Strike-Malleable-C2-Profile-Using-c2lint]]'
- '[[Cobalt-Strike-Team-Server-Installation-and-Execution]]'
- '[[Establish-VPN-Like-Connection-and-Pivot-Using-Cobalt-Strike]]'
- '[[Copy-File-to-Remote-Windows-Host-Using-WinRS-and-BitsAdmin]]'
- '[[Copy-File-to-Remote-Windows-Machine-via-Xcopy]]'
- '[[Creating-Files-with-Zero-Width-Spaces]]'
- '[[CRLF-Filter-Bypass-with-UTF-8-Encoding]]'
- '[[CRLF-Filter-Bypass-with-UTF-8-Encoding]]'
- '[[CRLF-Filter-Bypass-with-UTF-8-Encoding]]'
- '[[Perform-Cross-Site-WebSocket-Hijacking]]'
- '[[DB2-SQL-Injection-Select-Nth-Character-Extraction]]'
- '[[DB2-Time-Based-Blind-SQL-Injection]]'
- '[[configure-dns-for-cobalt-strike-dns-beacon]]'
- '[[Test-Service-for-DNS-Rebinding-Vulnerability]]'
- '[[DNS-Rebinding-Protection-Bypass-via-CNAME]]'
- '[[Exploit-Directory-Traversal-with-Double-URL-Encoding]]'
- '[[dynamic-port-forwarding-with-ssh-socks-proxy]]'
- '[[Embed-File-in-Image-Using-Steghide]]'
- '[[Bypass-SSRF-Filters-Using-Enclosed-Alphanumerics]]'
- '[[XSS-Dot-Filter-Bypass-Using-Exotic-Payloads]]'
- '[[Bypass-Email-Filters-with-Exotic-XSS-Payloads]]'
- '[[Exotic-Payloads-for-Bypassing-Filters-in-JavaScript]]'
- '[[extract-hidden-file-from-image-with-steghide]]'
- '[[XSS-Filter-Bypass-via-Alternate-Redirect-Methods]]'
- '[[Filter-Bypass-Using-Katakana-Library-for-XSS]]'
- '[[Git-Index-File-Recovery]]'
- '[[Recover-Git-Repository-from-Exposed-Dot-Git-Directory]]'
- '[[Exploit-Insecure-Git-Repository-with-GitTools]]'
- '[[Establish-Golang-Reverse-Shell]]'
- '[[Golden-Certificate-Domain-Persistence]]'
- '[[Establish-Groovy-Java-Reverse-Shell]]'
- '[[Image-Based-htaccess-Upload-Bypass]]'
- '[[Insecure-File-Upload-Exploit-via-Picture-Compression]]'
- '[[Extract-Source-Code-from-Bazaar-Repository-using-rip-bzr]]'
- '[[Establish-Java-Reverse-Shell]]'
- '[[Generate-Java-Reverse-Shell-WAR-Payload]]'
- '[[JavaScript-Alert-WAF-Bypass]]'
- '[[Jetty RCE via Insecure XML File Upload]]'
- '[[Setup-Lan-Turtle-for-AutoSSH-Reverse-Connection]]'
- '[[LFI-to-RCE-via-Apache-and-Nginx-Log-Files]]'
- '[[Execute-Queries-via-Linked-SQL-Servers]]'
- '[[Establish-Persistence-via-Linux-APT-Backdoor]]'
- '[[Linux-Crontab-Reverse-Shell-Persistence]]'
- '[[Linux-Privilege-Escalation-via-SSH-Key]]'
- '[[Linux-Privilege-Escalation-via-Writable-Files]]'
- '[[Linux-Staged-Reverse-TCP-Meterpreter-Shell]]'
- '[[Implement-Lua-Reverse-Shell]]'
- '[[Exploit-FFmpeg-HLS-Vulnerability-via-Malicious-AVI-for-Arbitrary-File-Read]]'
- '[[Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]'
- '[[Setup-Metasploit-Reverse-Shell-Handler]]'
- '[[Metasploit-Scripting-with-Meterpreter-Reverse-HTTPS-Payload]]'
- '[[Setup-Meterpreter-SOCKS-Proxy]]'
- '[[Mshta-Remote-HTA-Execution]]'
- '[[mssql-out-of-band-dns-exfiltration]]'
- '[[MSSQL-Time-Based-SQL-Injection]]'
- '[[generate-multi-platform-reverse-shell-payloads]]'
- '[[MYSQL Dumpfile PHP Shell Creation]]'
- '[[MySQL-Error-Based-Data-Extraction-Using-UpdateXML]]'
- '[[MySQL-Injection-Out-of-Band-Data-Exfiltration]]'
- '[[MySQL-SQL-Injection-for-Out-of-Band-DNS-Exfiltration]]'
- '[[MySQL-Union-Based-Injection-to-Extract-Users-Table-Data]]'
- '[[Establish-Reverse-Shell-with-Ncat]]'
- '[[Create-Bind-Shell-with-Netcat-OpenBSD]]'
- '[[Establish-Reverse-Shell-with-Netcat]]'
- '[[Netcat-Traditional-Bind-Shell]]'
- '[[Network-Pivoting-with-Proxychains]]'
- '[[network-pivoting-with-sshuttle]]'
- '[[Setup-Ngrok-Port-Forwarding-Tunnel]]'
- '[[Octal-IP-Format-SSRF-Bypass]]'
- '[[openssl-reverse-shell]]'
- '[[Open-URL-Redirection-Exploitation]]'
- '[[Oracle-SQL-Injection-Time-Based-Attack]]'
- '[[Out-of-Band-XPath-Injection]]'
- '[[pass-the-golden-ticket-attack-using-meterpreter]]'
- '[[Establish-Reverse-Shell-Using-Perl]]'
- '[[Establish-PHP-Bind-Shell]]'
- '[[Exploit-PHP-Deserialization-with-POP-Chain]]'
- '[[Demonstrate-PHP-Type-Juggling-with-Empty-Array-Hashing]]'
- '[[Establish-PHP-Reverse-Shell]]'
- '[[Polyglot-Command-Injection-for-DNS-Data-Exfiltration]]'
- '[[PostgreSQL-Time-Based-Blind-SQL-Injection-for-Table-Dump]]'
- '[[Establish-PowerShell-Reverse-Shell]]'
- '[[PrintNightmare-WebDAV-Attack]]'
---

# Command and Control

**MITRE ID**: TA0011

## Description

The command and control tactic represents how adversaries communicate with systems under their control within a target network. There are many ways an adversary can establish command and control with various levels of covertness, depending on system configuration and network topology. Due to the wide degree of variation available to the adversary at the network level, only the most common factors were used to describe the differences in command and control. There are still a great many specific techniques within the documented methods, largely due to how easy it is to define new protocols and use existing, legitimate protocols and network services for communication. The resulting breakdown should help convey the concept that detecting intrusion through command and control protocols without prior knowledge is a difficult proposition over the long term. Adversaries' main constraints in network-level defense avoidance are testing and deployment of tools to rapidly change their protocols, awareness of existing defensive technologies, and access to legitimate Web services that, when used appropriately, make their tools difficult to distinguish from benign traffic.



## Techniques

This tactic includes 26 techniques:

- [[Commonly Used Port|T1043 - Commonly Used Port]]
- [[Communication Through Removable Media|T1092 - Communication Through Removable Media]]
- [[Connection Proxy|T1090 - Connection Proxy]]
- [[Custom Command and Control Protocol|T1094 - Custom Command and Control Protocol]]
- [[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]
- [[Data Encoding|T1132 - Data Encoding]]
- [[Data Obfuscation|T1001 - Data Obfuscation]]
- [[Domain Fronting|T1172 - Domain Fronting]]
- [[Domain Generation Algorithms|T1483 - Domain Generation Algorithms]]
- [[Dynamic Resolution|T1568 - Dynamic Resolution]]
- [[Encrypted Channel|T1573 - Encrypted Channel]]
- [[Fallback Channels|T1008 - Fallback Channels]]
- [[Multiband Communication|T1026 - Multiband Communication]]
- [[Multi-hop Proxy|T1188 - Multi-hop Proxy]]
- [[Multilayer Encryption|T1079 - Multilayer Encryption]]
- [[Multi-Stage Channels|T1104 - Multi-Stage Channels]]
- [[Non-Standard Port|T1571 - Non-Standard Port]]
- [[Port Knocking|T1205 - Port Knocking]]
- [[Protocol Tunneling|T1572 - Protocol Tunneling]]
- [[Remote Access Tools|T1219 - Remote Access Tools]]
- [[Remote File Copy|T1105 - Remote File Copy]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]
- [[Standard Cryptographic Protocol|T1032 - Standard Cryptographic Protocol]]
- [[Standard Non-Application Layer Protocol|T1095 - Standard Non-Application Layer Protocol]]
- [[Uncommonly Used Port|T1065 - Uncommonly Used Port]]
- [[Web Service|T1102 - Web Service]]

## Related Procedures

There are 100 procedures implementing this tactic:

- [[Abusing Active Directory ACLs/ACEs to Retrieve LAPS Passwords]]
- [[AdminCount-Abuse]]
- [[Awk-Interactive-Reverse-Shell]]
- [[Retrieve-AWS-IAM-Policy-Version]]
- [[AWS-Secrets-Manager-Credential-Exfiltration]]
- [[Azure-AD-Administrative-Unit-Management]]
- [[Install-Azure-AD-Connect-PTA-Backdoor-and-Retrieve-Logs]]
- [[Azure-Reconnaissance]]
- [[Exploit-Azure-SSRF-to-Access-VM-Metadata-Service]]
- [[Create-Backdoored-Docker-Image]]
- [[Establish-Bash-UDP-Reverse-Shell]]
- [[Basic-Directory-Traversal-Exploitation]]
- [[BITSAdmin-Download-and-Execute-Payload]]
- [[Browse-FTP-Site-with-Interactive-Session]]
- [[Bypass-SSRF-Filters-Using-Bash-Variables-and-Curl-Verbose]]
- [[chisel-port-forwarding-and-socks-proxy-network-pivoting]]
- [[Cobalt-Strike-Lateral-Movement-via-Beacon-Remote-Exploits-and-Executes]]
- [[Validate-Cobalt-Strike-Malleable-C2-Profile-Using-c2lint]]
- [[Cobalt-Strike-Team-Server-Installation-and-Execution]]
- [[Establish-VPN-Like-Connection-and-Pivot-Using-Cobalt-Strike]]

*...and 80 more*


