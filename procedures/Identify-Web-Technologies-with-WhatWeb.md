---
id: b5b8827f-98ad-4585-8705-dfee242943cb
name: Identify-Web-Technologies-with-WhatWeb
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T17:47:18.057705+00:00'
updated_at: '2023-05-26T01:30:35.330888+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques:
  - '[[Software]]'
tags:
  - '[[tags/owasp]]'
  - '[[tags/Web Applications]]'
  - reconnaissance
  - fingerprinting
commands:
  - '[[commands/whatweb-identify-technologies]]'
platforms:
  - Web
tools:
  - '[[tools/WhatWeb]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Identify-Web-Technologies-with-WhatWeb

## Summary

This procedure uses the WhatWeb tool to fingerprint a web application by identifying the technologies, frameworks, servers, and other components used in its development. It is a key reconnaissance step for understanding the attack surface of web targets, such as detecting outdated software versions that may be vulnerable to known exploits.

## Description

WhatWeb is a next-generation web scanner that identifies what websites are running by detecting over 1,800 plugins for various web technologies, including web servers (e.g., Apache, Nginx), programming languages (e.g., PHP, Ruby), JavaScript libraries (e.g., jQuery), and content management systems (e.g., WordPress, Drupal). In offensive security operations, this technique is used during the reconnaissance phase to gather information about the target's technology stack without direct interaction beyond HTTP requests. It helps attackers prioritize exploitation paths based on identified components. The procedure assumes basic network access to the target URL and focuses on passive-like scanning to minimize detection. Expected outcomes include a report of detected technologies with confidence levels, which can inform subsequent procedures like vulnerability scanning or targeted exploitation.

## Requirements

1. WhatWeb tool installed on the attacker's machine (see [[tools/WhatWeb]] for installation).
2. Network connectivity to the target web application (no authentication required for public-facing sites).
3. Target URL or IP address of the web application to scan.
4. Optional: Proxy configuration (e.g., via Burp Suite) for traffic interception and evasion.

## Defense

Defensive measures and detection strategies:

- Implement Web Application Firewalls (WAFs) like ModSecurity to detect and block unusual scanning patterns.
- Use server-side obfuscation or version hiding (e.g., remove server banners in Apache/Nginx configs) to reduce fingerprinting accuracy.
- Monitor access logs for repeated requests to the same endpoints from suspicious IPs, using tools like Fail2Ban or SIEM systems.
- Enable HTTPS with HSTS to limit information disclosure in headers.

## Objectives

1. Identify the web server, programming languages, and frameworks used by the target application.
2. Detect potential vulnerabilities based on version information of identified technologies.
3. Gather intelligence for chaining with other reconnaissance or exploitation procedures.
4. Validate the technology stack to confirm the target environment (e.g., e-commerce platform like vCart).

## Instructions

### Step 1: Prepare the Target and Run WhatWeb Scan

**Context**: Begin by ensuring you have the target URL ready. This step executes the WhatWeb scan to probe the target and retrieve technology details. The tool sends HTTP requests and analyzes responses for signatures of known technologies. Use this in early reconnaissance to map the attack surface without alerting the target.

**Command** ([[commands/whatweb-identify-technologies]]):
```bash
whatweb $_TARGET_URL
```

> This command scans the specified URL and outputs detected technologies. Replace $_TARGET_URL with the actual endpoint, such as http://192.168.1.11/vcart/login.php. The scan is non-intrusive and typically completes in seconds. If the target requires specific headers or follows redirects, add flags like --follow-redirects or --user-agent.

### Step 2: Analyze and Verify Output

**Context**: Review the scan results to confirm detected technologies and note any version information. This step involves manual verification, such as cross-checking with browser developer tools or additional tools like Nmap for service confirmation. Decision point: If no technologies are detected, try scanning multiple endpoints or using aggressive plugins (--aggression 3).

**Command** ([[commands/whatweb-identify-technologies]]):
```bash
whatweb --aggression 3 --plugins javascript,php $_TARGET_URL
```

> Run this enhanced scan if initial results are incomplete. The --aggression flag increases probe depth, and --plugins limits to specific categories for focused analysis. Expected: More detailed output including script versions or framework specifics.

### Step 3: Document Findings and Plan Next Steps

**Context**: Log the results for reference in attack chains or reports. This non-technical step ensures the intelligence is actionable, such as identifying if PHP 5.x is used (potentially vulnerable to CVE-2019-11043). If sensitive data like admin panels is revealed, proceed to procedures like [[procedures/Directory-Brute-Force-with-Gobuster]].

No command required for this step; use text editors or note-taking tools to record output.
