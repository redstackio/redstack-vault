---
id: a9554478-5911-459d-a9ed-5f9d4829a81f
name: Subdomain Enumeration with Aquatone
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.591355+00:00'
updated_at: '2023-04-10T20:25:37.020269+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
tags:
- '[[Enumerate all subdomains (only if the scope is *.domain.ext)]]'
- '[[Subdomains Enumeration]]'
- '[[Using Aquatone - old version (Ruby)]]'
commands:
- '[[Active scans with Aquatone]]'
- '[[Discover subdomains with Aquatone]]'
- '[[Gather final results with Aquatone]]'
- '[[Install Aquatone]]'
- '[[Pull Aquatone Docker image]]'
- '[[Run Aquatone Docker image with target domain]]'
---

# Subdomain Enumeration with Aquatone

## Summary

Subdomain enumeration is a reconnaissance technique used to discover additional targets within a target organization's domain. Aquatone is a subdomain and URL scanner that can be used to discover subdomains and URLs of a target domain. Aquatone can be used to generate reports of identified subdomai

## Description

# Description

Subdomain enumeration is a reconnaissance technique used to discover additional targets within a target organization's domain. Aquatone is a subdomain and URL scanner that can be used to discover subdomains and URLs of a target domain. Aquatone can be used to generate reports of identified subdomains and URLs, which can be used to identify potential attack surfaces. The tool is written in Ruby and is available as a Docker image. The tool can be used to identify subdomains that may be used in phishing attacks or other malicious activities.

## Requirements

1. Access to the target domain

1. Aquatone Subdomain and URL Scanner or Aquatone Docker Image

## Defense

1. Implement proper access controls to prevent unauthorized access to the target domain

1. Implement network segmentation to limit the scope of potential attacks

1. Monitor network traffic for suspicious activity and indicators of compromise

## Objectives

1. Discover subdomains of a target domain

1. Identify potential attack surfaces

1. Gather information for reconnaissance

# Instructions

1. To use Aquatone, first install it using the command 'gem install aquatone'.

To discover subdomains, use the command 'aquatone-discover --domain example.com'. This will generate a file named 'hosts.txt' in the directory '~/aquatone/example.com/'. You can provide additional arguments like '--threads' to specify the number of threads to use or '--sleep' and '--jitter' to add a delay between requests.

To perform active scans on the discovered subdomains, use the command 'aquatone-scan --domain example.com'. This will generate a file named 'urls.txt' in the directory '~/aquatone/example.com/'. You can provide additional arguments like '--ports' to specify the ports to scan or '--threads' to specify the number of threads to use.

Finally, to gather all the results, use the command 'aquatone-gather --domain example.com'.

**Code**: [[gem install aquatone

Discover subdomains : result]]

> The Aquatone tool is used for subdomain discovery and URL scanning. The 'aquatone-discover' command is used to discover subdomains for a given domain. The 'aquatone-scan' command is used to actively scan the discovered subdomains for open ports. The 'aquatone-gather' command is used to gather all the results. The user can provide additional arguments to these commands to customize the behavior of the tool.

**Command** ([[Install Aquatone]]):

```bash
gem install aquatone
```

**Command** ([[Discover subdomains with Aquatone]]):

```bash
aquatone-discover --domain example.com
aquatone-discover --domain example.com --threads 25
aquatone-discover --domain example.com --sleep 5 --jitter 30
aquatone-discover --set-key shodan o1hyw8pv59vSVjrZU3Qaz6ZQqgM91ihQ
```

**Command** ([[Active scans with Aquatone]]):

```bash
aquatone-scan --domain example.com
aquatone-scan --domain example.com --ports 80,443,3000,8080
aquatone-scan --domain example.com --ports large
aquatone-scan --domain example.com --threads 25
```

**Command** ([[Gather final results with Aquatone]]):

```bash
aquatone-gather --domain example.com
```

2. Follow the steps below to use the Aquatone Docker image:

**Code**: [[https://hub.docker.com/r/txt3rob/aquatone-docker/
]]

> The Aquatone Docker image allows you to run Aquatone in a Docker container. This provides an isolated environment for running Aquatone and ensures that all dependencies are met. The Docker image is provided by txt3rob and can be pulled from the Docker Hub registry. Once you have pulled the Docker image, you can run Aquatone with the target domain as an argument.

**Command** ([[Pull Aquatone Docker image]]):

```bash
docker pull txt3rob/aquatone-docker
```

**Command** ([[Run Aquatone Docker image with target domain]]):

```bash
docker run -it txt3rob/aquatone-docker aq example.com
```

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

## Commands Used

- [[Active scans with Aquatone]]
- [[Discover subdomains with Aquatone]]
- [[Gather final results with Aquatone]]
- [[Install Aquatone]]
- [[Pull Aquatone Docker image]]
- [[Run Aquatone Docker image with target domain]]

## Tags

- [[Enumerate all subdomains (only if the scope is *.domain.ext)]]
- [[Subdomains Enumeration]]
- [[Using Aquatone - old version (Ruby)]]
