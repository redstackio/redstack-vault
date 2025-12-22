---
id: 36d036cd-b768-4c85-94ea-58cab5014cde
name: Brute-Force-Directories-and-Files-on-Subdomains-Using-Dirsearch
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:30.232193+00:00'
updated_at: '2023-05-26T00:43:10.546889+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - reconnaissance
  - web-fuzzing
  - directory-enumeration
  - file-discovery
commands:
  - '[[commands/dirsearch-brute-force-subdomains-with-custom-wordlist]]'
platforms:
  - Web
tools:
  - '[[tools/Dirsearch]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Brute-Force-Directories-and-Files-on-Subdomains-Using-Dirsearch

## Summary

This procedure uses the Dirsearch tool to perform brute-force enumeration of directories and files across a list of subdomains, leveraging a custom wordlist to identify hidden or sensitive endpoints such as admin panels, API documentation, and configuration files. It is primarily used during the reconnaissance phase to map the attack surface of web applications by discovering unprotected resources that could reveal information or serve as entry points.

## Description

Directory and file brute-forcing is a common reconnaissance technique to uncover hidden web resources that are not linked from the main site. By providing a list of subdomains (e.g., from prior enumeration tools like subfinder or Amass) and a tailored wordlist focusing on common paths like API endpoints and admin interfaces, Dirsearch sends HTTP requests to test for the existence of these paths. This helps identify potential vulnerabilities such as exposed documentation (e.g., Swagger UI), backup files, or misconfigured directories. The procedure assumes the attacker has a list of subdomains and runs on a system with Python and Dirsearch installed. It maps to MITRE ATT&CK technique T1083 (File and Directory Discovery) under the Discovery tactic, as it systematically probes for filesystem elements via web interfaces. Success reveals the structure of the web application, aiding further targeted attacks like information disclosure or exploitation.

## Requirements

1. A list of target subdomains saved in a text file (one per line, e.g., sub-domains.txt), obtained from prior subdomain enumeration.
2. Dirsearch tool installed ([[tools/Dirsearch]]).
3. A custom wordlist file (e.g., paths.txt) containing potential directory and file paths; use the provided wordlist [[codes/Common-Web-Directories-and-Files-Wordlist]].
4. Network access to the target subdomains (no authentication required for basic probing).
5. Sufficient system resources for multi-threaded requests (e.g., 50 threads on a standard attacking machine).

## Defense

Defensive measures include web application firewalls (WAFs) that rate-limit or block brute-force patterns, server-side logging of anomalous HTTP requests, and directory listing disabled via web server configurations (e.g., Apache's Options -Indexes). Detection can involve monitoring for high volumes of 404/403 responses from a single IP or using tools like Fail2Ban to ban suspicious scanners.

## Objectives

1. Identify hidden directories and files on multiple subdomains to expand the attack surface.
2. Discover sensitive endpoints like API docs or admin panels for further reconnaissance or exploitation.
3. Generate a report of discovered resources for analysis in subsequent attack phases.

## Instructions

### Step 1: Prepare the Custom Wordlist

**Context**: Create or verify the paths.txt wordlist with common targets for web fuzzing. This ensures the brute-force targets relevant paths like API and admin locations, increasing the likelihood of useful discoveries without excessive noise.

Use the following content to build paths.txt, based on [[codes/Common-Web-Directories-and-Files-Wordlist]]:

```bash
/phpinfo.php
/info.php
/admin.php
/api/apidocs
/apidocs
/api
/api/v2
/api/v1
/v2
/package.json
/security.txt
/application.wadl
/api/apidocs
/swagger
/swagger-ui
/swagger-ui.html
/swagger/swagger-ui.html
/api/swagger-ui.html
/v1.x/swagger-ui.html
/swagger/index.html
/graphql
/graphiql
```

> Save this to paths.txt. This step customizes the scan to focus on high-value paths, explaining the choice: these are common in modern web apps for documentation and management interfaces.

### Step 2: Execute the Brute-Force Scan

**Context**: Run Dirsearch against the subdomain list using the custom wordlist. This step performs the actual probing, sending requests for each path on each subdomain and logging responses to identify existing resources (e.g., 200 OK for found items, 404 for not found).

**Command** ([[commands/dirsearch-brute-force-subdomains-with-custom-wordlist]]):
```bash
python3 dirsearch.py -L sub-domains.txt -e .* -w paths.txt --simple-report=output.txt -t 50
```

> This command loads subdomains from sub-domains.txt (-L), tests all extensions (-e .*), uses paths.txt as the wordlist (-w), outputs a simple report to output.txt (--simple-report), and runs 50 threads (-t) for efficiency. Adjust threads based on system resources to avoid overwhelming the network or triggering defenses. The scan will output progress to the console and save detailed results (status codes, paths) to the report file.

### Step 3: Review and Verify Results

**Context**: Analyze the output report to confirm discoveries and manually verify promising finds. This validates the procedure's success and identifies actionable intelligence, such as accessible API docs.

Open output.txt and look for 200/403 status codes indicating potential hits.

**Expected Output**: A text report like:

```
Target: api.example.com

[Status: 200, Size: 1234, Path: /api/apidocs]
[Status: 403, Size: 0, Path: /admin.php]

Target: app.example.com

[Status: 200, Size: 5678, Path: /swagger-ui.html]
```

> Manually browse hits (e.g., via browser or curl) to confirm content. If no hits, expand the wordlist or reduce threads to evade detection.

## Expected Output

Console progress showing scanned targets and paths, plus a simple report file (output.txt) listing discovered resources with HTTP status codes, response sizes, and paths. Success is indicated by entries with 200 OK or other non-404 responses, revealing hidden web elements.
