---
id: f98a740e-d770-4441-882e-5defe5f97904
name: Subdomain Enumeration with Knockpy and EyeWitness
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.378801+00:00'
updated_at: '2023-04-10T20:25:35.397118+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Active Scanning|T1595 - Active Scanning]]'
- '[[Password Policy Discovery|T1201 - Password Policy Discovery]]'
tags:
- '[[Enumerate all subdomains (only if the scope is *.domain.ext)]]'
- '[[Subdomains Enumeration]]'
- '[[Using KnockPy with Daniel Miessler’s SecLists for subdomain "/Discover/DNS"]]'
commands:
- '[[Clone danielmiessler/SecLists repository]]'
- '[[Clone EyeWitness from GitHub]]'
- '[[Clone guelfoweb/knock repository]]'
- '[[Run EyeWitness with filename and optional timeout]]'
- '[[Run EyeWitness with rdp.txt and --rdp option]]'
- '[[Run EyeWitness with urls.txt and --web option]]'
- '[[Run EyeWitness with urls.xml, timeout of 8 seconds, and --headless option]]'
- '[[Run knockpy to enumerate subdomains]]'
- '[[Run setup script]]'
---

# Subdomain Enumeration with Knockpy and EyeWitness

## Summary

Subdomain enumeration is the process of finding all the subdomains of a given domain. This procedure uses KnockPy, a python tool that uses a list of subdomains from Daniel Miessler’s SecLists to find subdomains. EyeWitness and Nmap scans are then used to gather more information about the subdomains

## Description

# Description

Subdomain enumeration is the process of finding all the subdomains of a given domain. This procedure uses KnockPy, a python tool that uses a list of subdomains from Daniel Miessler’s SecLists to find subdomains. EyeWitness and Nmap scans are then used to gather more information about the subdomains. This procedure is useful for discovering potential attack vectors and identifying assets that may be vulnerable to attack.

From a technical perspective, the procedure works by sending DNS requests to a domain and its subdomains to discover additional subdomains. EyeWitness and Nmap scans are then used to gather information about the discovered subdomains, such as open ports and running services. This information can be used to identify potential vulnerabilities and attack vectors.

The business value of this procedure is that it allows organizations to identify potential attack vectors and vulnerable assets. By identifying these assets, organizations can take steps to secure them and reduce the risk of a successful attack.

## Requirements

1. Access to the domain being enumerated

1. KnockPy tool installed

1. EyeWitness and Nmap tools installed

## Defense

1. Ensure that only authorized individuals have access to the domain being enumerated

1. Regularly monitor for unauthorized subdomains

1. Implement DNSSEC to protect against DNS spoofing attacks

## Objectives

1. Identify all subdomains of a given domain

1. Gather information about the discovered subdomains

1. Identify potential attack vectors and vulnerable assets

# Instructions

1. To use this command, follow these steps:
1. Clone the knock and SecLists repositories using the following commands:
   git clone https://github.com/guelfoweb/knock
   git clone https://github.com/danielmiessler/SecLists.git
2. Navigate to the knock directory using the command:
   cd knock
3. Run the knockpy command with the target domain and wordlist file as arguments, as shown below:
   knockpy domain.com -w subdomains-top1mil-110000.txt

Note: The wordlist file used in this example is subdomains-top1mil-110000.txt. You can use a different wordlist file if you prefer.

**Code**: [[git clone https://github.com/guelfoweb/knock
git c]]

> This command is used to perform subdomain enumeration on a specified domain using the knockpy tool. The command first clones the knock and SecLists repositories to the local machine. Then, it navigates to the knock directory and runs the knockpy command with the specified domain and wordlist file as arguments. The wordlist file used in this example is subdomains-top1mil-110000.txt, which contains a list of the top 1 million subdomains. This command can be useful for reconnaissance and vulnerability assessment purposes.

**Command** ([[Clone guelfoweb/knock repository]]):

```bash
git clone https://github.com/guelfoweb/knock
```

**Command** ([[Clone danielmiessler/SecLists repository]]):

```bash
git clone https://github.com/danielmiessler/SecLists.git
```

**Command** ([[Run knockpy to enumerate subdomains]]):

```bash
knockpy domain.com -w subdomains-top1mil-110000.txt
```

2. To use EyeWitness and Nmap scans, follow the below steps:
1. Clone the EyeWitness repository using the command: git clone https://github.com/ChrisTruncer/EyeWitness.git
2. Run the setup script using the command: ./setup/setup.sh
3. Run EyeWitness using any of the following commands:
   a. ./EyeWitness.py -f filename -t optionaltimeout --open (Optional)
   b. ./EyeWitness -f urls.txt --web
   c. ./EyeWitness -x urls.xml -t 8 --headless
   d. ./EyeWitness -f rdp.txt --rdp

**Code**: [[git clone https://github.com/ChrisTruncer/EyeWitne]]

> The above commands allow you to use EyeWitness and Nmap scans to gather information about your target. The 'git clone' command is used to clone the EyeWitness repository from Github. The 'setup.sh' script is used to install any required dependencies. The 'EyeWitness.py' and 'EyeWitness' commands are used to run EyeWitness with different options. The '-f' option is used to specify the input file containing target URLs or IP addresses. The '-t' option is used to specify the timeout for each request. The '--open' option is used to open the generated report in a web browser. The '--web' option is used to run EyeWitness with default options for web application scanning. The '-x' option is used to specify the input file in XML format. The '--headless' option is used to run EyeWitness in headless mode. The '--rdp' option is used to scan for RDP services.

**Command** ([[Clone EyeWitness from GitHub]]):

```bash
git clone https://github.com/ChrisTruncer/EyeWitness.git
```

**Command** ([[Run setup script]]):

```bash
./setup/setup.sh
```

**Command** ([[Run EyeWitness with filename and optional timeout]]):

```bash
./EyeWitness.py -f filename -t optionaltimeout --open (Optional)
```

**Command** ([[Run EyeWitness with urls.txt and --web option]]):

```bash
./EyeWitness -f urls.txt --web
```

**Command** ([[Run EyeWitness with urls.xml, timeout of 8 seconds, and --headless option]]):

```bash
./EyeWitness -x urls.xml -t 8 --headless
```

**Command** ([[Run EyeWitness with rdp.txt and --rdp option]]):

```bash
./EyeWitness -f rdp.txt --rdp
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Active Scanning|T1595 - Active Scanning]]
- [[Password Policy Discovery|T1201 - Password Policy Discovery]]

## Commands Used

- [[Clone danielmiessler/SecLists repository]]
- [[Clone EyeWitness from GitHub]]
- [[Clone guelfoweb/knock repository]]
- [[Run EyeWitness with filename and optional timeout]]
- [[Run EyeWitness with rdp.txt and --rdp option]]
- [[Run EyeWitness with urls.txt and --web option]]
- [[Run EyeWitness with urls.xml, timeout of 8 seconds, and --headless option]]
- [[Run knockpy to enumerate subdomains]]
- [[Run setup script]]

## Tags

- [[Enumerate all subdomains (only if the scope is *.domain.ext)]]
- [[Subdomains Enumeration]]
- [[Using KnockPy with Daniel Miessler’s SecLists for subdomain "/Discover/DNS"]]
