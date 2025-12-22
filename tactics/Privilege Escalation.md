---
id: 63698000-924e-41b7-ad9c-da382fc5cc3f
name: Privilege Escalation
type: tactic
mitre_id: TA0004
mitre_url: null
created_at: '2019-08-28T21:17:39.724450+00:00'
updated_at: '2023-05-29T16:48:53.579491+00:00'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Accessibility Features|T1015 - Accessibility Features]]'
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[AppCert DLLs|T1182 - AppCert DLLs]]'
- '[[AppInit DLLs|T1103 - AppInit DLLs]]'
- '[[Application Shimming|T1138 - Application Shimming]]'
- '[[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]'
- '[[Bypass User Account Control|T1088 - Bypass User Account Control]]'
- '[[Create or Modify System Process|T1543 - Create or Modify System Process]]'
- '[[DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]'
- '[[Dylib Hijacking|T1157 - Dylib Hijacking]]'
- '[[Elevated Execution with Prompt|T1514 - Elevated Execution with Prompt]]'
- '[[Emond|T1519 - Emond]]'
- '[[create-nginx-container-via-socket|T1611 - Escape to Host]]'
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
- '[[Extra Window Memory Injection|T1181 - Extra Window Memory Injection]]'
- '[[File System Permissions Weakness|T1044 - File System Permissions Weakness]]'
- '[[Group Policy Modification|T1484 - Group Policy Modification]]'
- '[[Hijack Execution Flow|T1574 - Hijack Execution Flow]]'
- '[[Hooking|T1179 - Hooking]]'
- '[[Image File Execution Options Injection|T1183 - Image File Execution Options Injection]]'
- '[[Launch Daemon|T1160 - Launch Daemon]]'
- '[[Logon Scripts|T1037 - Logon Scripts]]'
- '[[New Service|T1050 - New Service]]'
- '[[Parent PID Spoofing|T1502 - Parent PID Spoofing]]'
- '[[Path Interception|T1034 - Path Interception]]'
- '[[Plist Modification|T1150 - Plist Modification]]'
- '[[Port Monitors|T1013 - Port Monitors]]'
- '[[PowerShell Profile|T1504 - PowerShell Profile]]'
- '[[Process Injection|T1055 - Process Injection]]'
- '[[Scheduled Task|T1053 - Scheduled Task]]'
- '[[Service Registry Permissions Weakness|T1058 - Service Registry Permissions Weakness]]'
- '[[Setuid and Setgid|T1166 - Setuid and Setgid]]'
- '[[SID-History Injection|T1178 - SID-History Injection]]'
- '[[Startup Items|T1165 - Startup Items]]'
- '[[Sudo|T1169 - Sudo]]'
- '[[Sudo Caching|T1206 - Sudo Caching]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
- '[[Web Shell|T1100 - Web Shell]]'
procedures:
- '[[Abuse-GPO-with-PowerView-to-Push-Empire-Stager]]'
- '[[Abuse-Group-Policy-Objects-with-pyGPOAbuse]]'
- '[[Abusing Active Directory ACLs/ACEs - GenericWrite and Remote Connection Manager]]'
- '[[Abusing-Backup-Operators-Group-for-Sensitive-File-Access]]'
- '[[Abuse-DNSAdmins-for-DLL-Hijacking-Privilege-Escalation]]'
- '[[Abusing-Golden-Privileges-with-Juicy-Potato]]'
- '[[Abusing Group Policy Objects with StandIn to Manage Local Administrators and
  User Rights]]'
- '[[Abuse-Linux-Cgroup-v1-with-CAP-SYS-ADMIN-for-Host-Privilege-Escalation]]'
- '[[Abusing-Shadow-Copies-for-Privilege-Escalation]]'
- '[[Active Directory ACLs/ACEs Password Reset]]'
- '[[Active-Directory-Certificate-Services-Access-Control-Vulnerabilities]]'
- '[[Active-Directory-Certificate-Services-ESC9-Attack]]'
- '[[Active-Directory-Object-Owner-Hijacking]]'
- '[[Add-and-Execute-PHP-Code-on-Authenticated-WordPress-Site]]'
- '[[AdminCount-Abuse]]'
- '[[Request-Alternative-Name-Certificate-via-AD-CS]]'
- '[[Enumerate-Installed-Antivirus-Products-Windows]]'
- '[[Apache-Karaf-XXE-Out-of-Band-Data-Exfiltration]]'
- '[[Application-Escape-and-Breakout-via-Unassociated-Protocols-in-Firefox]]'
- '[[AWS-API-Gateway-Stage-Enumeration]]'
- '[[configure-aws-cli-profile-for-persistence]]'
- '[[AWS-Console-Access-via-API-Keys]]'
- '[[Push-SSH-Key-to-EC2-Instance-via-AWS-Instance-Connect]]'
- '[[Exploit-AWS-EC2-Metadata-SSRF-for-Credential-Extraction]]'
- '[[aws-iam-create-access-key-for-user]]'
- '[[AWS-IAM-Attach-Inline-Policy-to-User]]'
- '[[AWS-Lambda-Function-Invocation-for-Privilege-Escalation]]'
- '[[aws-lambda-function-policy-enumeration]]'
- '[[AWS-Lambda-Function-Privilege-Escalation-via-IAM-Policy-Attachment]]'
- '[[aws-lambda-role-privilege-escalation]]'
- '[[Enumerate-AWS-Managed-Policies-for-IAM-User]]'
- '[[Assume-AWS-Role-for-Persistence]]'
- '[[AWS-Shadow-Admin-Access]]'
- '[[aws-ssh-key-persistence]]'
- '[[aws-ssh-persistence-via-authorized-keys]]'
- '[[Add-Azure-AD-App-Secret-for-Service-Principal-Authentication]]'
- '[[Azure-Automation-Account-Runbook-Persistence]]'
- '[[azure-pass-the-certificate-ad-cert-request-and-rce]]'
- '[[Exploit-Azure-SSRF-to-Access-VM-Metadata-Service]]'
- '[[Backdoor-Git-User-Configurations-for-Persistence]]'
- '[[Implement-Sudo-Backdoor-via-Bashrc-Alias]]'
- '[[Perform-Blind-XPath-Injection-for-Data-Extraction]]'
- '[[Change Password in a Writable /etc/passwd]]'
- '[[Cloudflare-XSS-Bypass-via-SVG-Onload-Alert]]'
- '[[CLR Assembly Creation and Execution]]'
- '[[Elevate-Privileges-Using-Cobalt-Strike-Beacon-Runasadmin]]'
- '[[Establish-Persistence-Using-SharPersist-in-Cobalt-Strike]]'
- '[[Compromise of Personal Access Token for Gitlab Source Code Management and CI/CD]]'
- '[[connect-to-ssh-server-with-private-key]]'
- '[[CORS Misconfiguration Exploitation - Expanding the Origin / Regex Issues]]'
- '[[CORS Misconfiguration Exploitation - Expanding the Origin / Regex Issues]]'
- '[[CORS Misconfiguration Exploitation - Expanding the Origin / Regex Issues]]'
- '[[CORS Misconfiguration Exploitation - Expanding the Origin / Regex Issues]]'
- '[[CORS-Misconfiguration-Exploitation-Origin-Reflection]]'
- '[[CORS-Misconfiguration-Exploitation-Origin-Reflection]]'
- '[[CORS-Misconfiguration-Exploitation-Origin-Reflection]]'
- '[[CORS-Misconfiguration-Exploitation-Origin-Reflection]]'
- '[[Create-and-Run-Windows-Service-as-SYSTEM-Administrator]]'
- '[[Create-Windows-Scheduled-Task-for-Persistence]]'
- '[[create-windows-pscredential-object]]'
- '[[Creating-and-Importing-CLR-Assembly-for-OS-Command-Execution-in-MSSQL]]'
- '[[Credential-Harvesting-from-Task-Scheduler-using-Mimikatz]]'
- '[[Dart-Reverse-PowerShell-Shell]]'
- '[[Enumerate-DB2-User-Privileges]]'
- '[[DCOM-Shell-Command-Execution-via-MMC-Application-Class]]'
- '[[Exploit-ZeroLogon-and-PrinterBug-for-DC-System-Access]]'
- '[[DirtyPipe-Kernel-Exploit-for-Privilege-Escalation]]'
- '[[Exploit-Open-Docker-API-for-Container-Management]]'
- '[[Enumerate-and-Analyze-SSL-TLS-Certificate]]'
- '[[Domain-Takeover-via-Certifried-CVE-2022-26923]]'
- '[[Set-Secondary-Email-for-Azure-AD-User]]'
- '[[efs-potato-privilege-escalation]]'
- '[[Elevating-Privileges-via-RottenPotato-and-Token-Impersonation]]'
- '[[enumerate-linux-privilege-escalation-paths-with-linenum]]'
- '[[Enumerate-Linux-Privilege-Escalation-Paths-linPEAS]]'
- '[[Enumerate-MSSQL-Server-Permissions]]'
- '[[enumerate-windows-missing-patches-hotfixes-sherlock]]'
- '[[Enumerate-Windows-for-Privilege-Escalation-JAWS]]'
- '[[Enumerate-Windows-for-Privilege-Escalation-Using-PowerUp]]'
- '[[Enumerate-Windows-for-Privilege-Escalation-Using-SharpUp]]'
- '[[Enumerate-Windows-for-Privilege-Escalation-with-winPEAS]]'
- '[[Escalate-Privileges-Using-Juicy-Potato]]'
- '[[EternalBlue-SMB-Exploitation]]'
- '[[execute-powershell-commands-as-another-user-using-pssession]]'
- '[[Bypass-Space-Filter-in-XSS-with-Exotic-Payloads]]'
- '[[Exploit-Group-Policy-Objects-with-Write-Access]]'
- '[[Exploit-PrintNightmare-for-SYSTEM-Shell-on-Domain-Controller]]'
- '[[exploit-clientcopyimage-vulnerability-ms15-051]]'
- '[[Exploit-Dirty-Cow-Vulnerability]]'
- '[[Find-Linux-Files-with-Elevated-Privileges]]'
- '[[Forge-Internal-Forest-Trust-Ticket-and-Escalate-to-Parent-DA-via-SIDHistory]]'
- '[[GitHack-Exploiting-Insecure-Source-Code-Management]]'
- '[[Git-Hook-Persistence]]'
- '[[Golden-Certificate-Domain-Persistence]]'
- '[[GPO-Abuse-with-PowerGPOAbuse]]'
- '[[HiveNightmare-SAM-Dump-via-Shadow-Copies]]'
- '[[HQL-Error-Based-Column-Enumeration]]'
- '[[HTAccess-and-PHP-Shell-Upload]]'
- '[[IAM-Authentication-for-RDS-MySQL-Database]]'
- '[[IIS-Raid-Backdoor-Persistence]]'
---

# Privilege Escalation

**MITRE ID**: TA0004

## Description

Privilege escalation is the result of actions that allows an adversary to obtain a higher level of permissions on a system or network. Certain tools or actions require a higher level of privilege to work and are likely necessary at many points throughout an operation. Adversaries can enter a system with unprivileged access and must take advantage of a system weakness to obtain local administrator or SYSTEM/root level privileges. A user account with administrator-like access can also be used. User accounts with permissions to access specific systems or perform specific functions necessary for adversaries to achieve their objective may also be considered an escalation of privilege.



## Techniques

This tactic includes 40 techniques:

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Accessibility Features|T1015 - Accessibility Features]]
- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[AppCert DLLs|T1182 - AppCert DLLs]]
- [[AppInit DLLs|T1103 - AppInit DLLs]]
- [[Application Shimming|T1138 - Application Shimming]]
- [[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]
- [[Bypass User Account Control|T1088 - Bypass User Account Control]]
- [[Create or Modify System Process|T1543 - Create or Modify System Process]]
- [[DLL Search Order Hijacking|T1038 - DLL Search Order Hijacking]]
- [[Dylib Hijacking|T1157 - Dylib Hijacking]]
- [[Elevated Execution with Prompt|T1514 - Elevated Execution with Prompt]]
- [[Emond|T1519 - Emond]]
- [[create-nginx-container-via-socket|T1611 - Escape to Host]]
- [[Event Triggered Execution|T1546 - Event Triggered Execution]]
- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]
- [[Extra Window Memory Injection|T1181 - Extra Window Memory Injection]]
- [[File System Permissions Weakness|T1044 - File System Permissions Weakness]]
- [[Group Policy Modification|T1484 - Group Policy Modification]]
- [[Hijack Execution Flow|T1574 - Hijack Execution Flow]]
- [[Hooking|T1179 - Hooking]]
- [[Image File Execution Options Injection|T1183 - Image File Execution Options Injection]]
- [[Launch Daemon|T1160 - Launch Daemon]]
- [[Logon Scripts|T1037 - Logon Scripts]]
- [[New Service|T1050 - New Service]]
- [[Parent PID Spoofing|T1502 - Parent PID Spoofing]]
- [[Path Interception|T1034 - Path Interception]]
- [[Plist Modification|T1150 - Plist Modification]]
- [[Port Monitors|T1013 - Port Monitors]]
- [[PowerShell Profile|T1504 - PowerShell Profile]]
- [[Process Injection|T1055 - Process Injection]]
- [[Scheduled Task|T1053 - Scheduled Task]]
- [[Service Registry Permissions Weakness|T1058 - Service Registry Permissions Weakness]]
- [[Setuid and Setgid|T1166 - Setuid and Setgid]]
- [[SID-History Injection|T1178 - SID-History Injection]]
- [[Startup Items|T1165 - Startup Items]]
- [[Sudo|T1169 - Sudo]]
- [[Sudo Caching|T1206 - Sudo Caching]]
- [[Valid Accounts|T1078 - Valid Accounts]]
- [[Web Shell|T1100 - Web Shell]]

## Related Procedures

There are 100 procedures implementing this tactic:

- [[Abuse-GPO-with-PowerView-to-Push-Empire-Stager]]
- [[Abuse-Group-Policy-Objects-with-pyGPOAbuse]]
- [[Abusing Active Directory ACLs/ACEs - GenericWrite and Remote Connection Manager]]
- [[Abusing-Backup-Operators-Group-for-Sensitive-File-Access]]
- [[Abuse-DNSAdmins-for-DLL-Hijacking-Privilege-Escalation]]
- [[Abusing-Golden-Privileges-with-Juicy-Potato]]
- [[Abusing-Group-Policy-Objects-with-StandIn-to-Manage-Local-Administrators-and-User-Rights]]
- [[Abuse-Linux-Cgroup-v1-with-CAP-SYS-ADMIN-for-Host-Privilege-Escalation]]
- [[Abusing-Shadow-Copies-for-Privilege-Escalation]]
- [[Active Directory ACLs/ACEs Password Reset]]
- [[Active-Directory-Certificate-Services-Access-Control-Vulnerabilities]]
- [[Active-Directory-Certificate-Services-ESC9-Attack]]
- [[Active-Directory-Object-Owner-Hijacking]]
- [[Add-and-Execute-PHP-Code-on-Authenticated-WordPress-Site]]
- [[AdminCount-Abuse]]
- [[Request-Alternative-Name-Certificate-via-AD-CS]]
- [[Enumerate-Installed-Antivirus-Products-Windows]]
- [[Apache-Karaf-XXE-Out-of-Band-Data-Exfiltration]]
- [[Application-Escape-and-Breakout-via-Unassociated-Protocols-in-Firefox]]
- [[AWS-API-Gateway-Stage-Enumeration]]

*...and 80 more*


