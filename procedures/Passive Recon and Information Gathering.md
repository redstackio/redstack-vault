---
id: c059c71a-ee42-4feb-96c6-969c3854a563
name: Passive Recon and Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.747083+00:00'
updated_at: '2023-04-10T20:21:17.932033+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Active Scanning|T1595 - Active Scanning]]'
- '[[Search Open Websites/Domains|T1593 - Search Open Websites/Domains]]'
- '[[Search Victim-Owned Websites|T1594 - Search Victim-Owned Websites]]'
tags:
- '[[Bug Hunting Methodology and Enumeration]]'
- '[[Passive recon]]'
commands:
- '[[Gitrob Analyze]]'
- '[[Integrate shodan-hq with nmap]]'
- '[[Search for JS files and old links]]'
- '[[theHarvester all domain search]]'
---

# Passive Recon and Information Gathering

## Summary

Passive reconnaissance is the initial stage of information gathering where an attacker collects information about the target without directly interacting with it. This method is used to identify the target's assets, their functionality, and potential vulnerabilities. Passive reconnaissance is a cri

## Description

# Description

Passive reconnaissance is the initial stage of information gathering where an attacker collects information about the target without directly interacting with it. This method is used to identify the target's assets, their functionality, and potential vulnerabilities. Passive reconnaissance is a critical step in the attack chain and can provide valuable information to attackers. In this procedure, we will cover various techniques for passive reconnaissance and information gathering, including Shodan Similar App Detection, Detect Forgotten Endpoints with Wayback Machine, Harvesting Domain Information, and GitHub Private Information Analysis with GitRob. 

Shodan Similar App Detection is used to identify similar applications to the target, which can provide valuable information about the target's infrastructure. Wayback Machine is used to detect forgotten endpoints, which can reveal old and vulnerable pages that are no longer in use. Harvesting Domain Information is used to collect information about the target's domain, including subdomains, DNS records, and SSL certificates. Finally, GitHub Private Information Analysis with GitRob is used to identify sensitive information that has been accidentally committed to GitHub repositories, such as API keys or credentials. 

This procedure is critical for an attacker to gather information about the target and identify potential attack vectors. By using passive reconnaissance, attackers can minimize their footprint and avoid detection.

 

## Requirements

1. Access to the internet

1. Access to the tools used in this procedure

 

## Defense

1. Limit the amount of information that is publicly available about the target

1. Use strong authentication mechanisms to protect sensitive information

1. Regularly monitor and audit the target's infrastructure for potential vulnerabilities

 

## Objectives

1. To identify the target's assets and their functionality

1. To identify potential vulnerabilities in the target's infrastructure

1. To minimize the attacker's footprint and avoid detection

 

# Instructions

1. To use this command, you need to have a Shodan API key. You can get one by signing up for a Shodan account. Once you have the API key, replace <yourShodanAPIKey> with your actual API key and <hackme> with the IP address or hostname of the target you want to scan. This command can be integrated with nmap using the shodan-hq.nse script.

 



**Code**: [[can be integrated with nmap (https://github.com/gl]]



> This command uses Shodan, a search engine for internet-connected devices, to detect similar apps running on a target system. By scanning the target's IP address or hostname, Shodan can provide information on the open ports and services running on the system. The shodan-hq.nse script can be used with nmap to automate this process. The script takes two arguments: the Shodan API key and the target to scan. Once the scan is complete, the script will output any similar apps detected on the target system.



**Command** ([[Integrate shodan-hq with nmap]]):

```bash
nmap --script shodan-hq.nse --script-args 'apikey=<yourShodanAPIKey>,target=<hackme>'
```



2. To detect forgotten endpoints of a target domain using the Wayback Machine, run the following command:

 



**Code**: [[look for JS files, old links
curl -sX GET "http://]]



> This command will look for JS files and old links of the target domain using the Wayback Machine's CDX API. The -sX option is used to send a GET request to the API endpoint with the specified parameters. The <targetDomain.com> parameter should be replaced with the actual domain name you want to search for. The output will be in text format and will include the original URLs of the archived pages that match the specified URL prefix. The collapse parameter is set to urlkey to group the results by URL.



**Command** ([[Search for JS files and old links]]):

```bash
curl -sX GET "http://web.archive.org/cdx/search/cdx?url=<targetDomain.com>&output=text&fl=original&collapse=urlkey&matchType=prefix"
```



3. This command uses The Harvester tool to gather information about a specific domain. The '-b all' flag specifies to use all available sources to gather information, while the '-d' flag specifies the target domain. Replace 'domain.com' with the domain you wish to gather information on.

 



**Code**: [[python theHarvester.py -b all -d domain.com]]



> The Harvester is a tool used for gathering information about a specific domain. It can be used for reconnaissance purposes to gather information about a target before an attack. The '-b all' flag specifies to use all available sources to gather information, while the '-d' flag specifies the target domain. Replace 'domain.com' with the domain you wish to gather information on.



**Command** ([[theHarvester all domain search]]):

```bash
python theHarvester.py -b all -d domain.com
```



4. To use GitRob, run the following command in your terminal: gitrob analyze [username] --site=[GitHub Enterprise URL] --endpoint=[GitHub API URL] --access-tokens=[access tokens separated by comma]

 



**Code**: [[gitrob analyze johndoe --site=https://github.acme.]]



> This command analyzes the specified user's repositories on the provided GitHub Enterprise instance and searches for sensitive information such as private keys, passwords, and confidential documents. The `--site` flag specifies the URL of the GitHub Enterprise instance, `--endpoint` specifies the API URL of the instance, and `--access-tokens` specifies the access tokens to be used for authentication. The command will output a report of any sensitive information found in the user's repositories.



**Command** ([[Gitrob Analyze]]):

```bash
johndoe --site=https://github.acme.com --endpoint=https://github.acme.com/api/v3 --access-tokens=token1,token2
```



## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Active Scanning|T1595 - Active Scanning]]
- [[Search Open Websites/Domains|T1593 - Search Open Websites/Domains]]
- [[Search Victim-Owned Websites|T1594 - Search Victim-Owned Websites]]

## Commands Used

- [[Gitrob Analyze]]
- [[Integrate shodan-hq with nmap]]
- [[Search for JS files and old links]]
- [[theHarvester all domain search]]

## Tags

- [[Bug Hunting Methodology and Enumeration]]
- [[Passive recon]]


