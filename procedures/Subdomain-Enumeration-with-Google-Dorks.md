---
id: 65d8e640-5bc6-405b-9780-fdce7cc05e44
name: Subdomain-Enumeration-with-Google-Dorks
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.435775+00:00'
updated_at: '2023-04-10T20:25:37.737810+00:00'
tactics:
  - '[[tactics/Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
  - >-
    [[techniques/Search Open Technical Databases|T1596 - Search Open Technical
    Databases]]
sub_techniques:
  - '[[sub-techniques/Digital Certificates|T1596.003 - Digital Certificates]]'
tags:
  - '[[tags/Enumerate all subdomains (only if the scope is *.domain.ext)]]'
  - '[[tags/Subdomains Enumeration]]'
  - '[[tags/Using Google Dorks and Google Transparency Report]]'
commands:
  - '[[commands/google-dorks-search-files-by-extension]]'
  - '[[commands/google-dorks-search-admin-login-urls]]'
  - '[[commands/google-dorks-search-pdf-files]]'
  - '[[commands/google-dorks-enumerate-subdomains]]'
  - '[[commands/google-dorks-enumerate-multi-level-subdomains]]'
  - '[[commands/google-dorks-search-urls-with-ampersand]]'
platforms:
  - Web
tools: []
validated: true
---

# Subdomain-Enumeration-with-Google-Dorks

## Summary

This procedure uses Google Dorks (advanced search operators) to enumerate subdomains of a target domain during reconnaissance. It identifies indexed subdomains, multi-level subdomains, and related assets like PDF files, URLs with potential vulnerabilities (e.g., ampersands or admin paths), and files with specific extensions. Additionally, it incorporates the Google Transparency Report to discover subdomains via recent certificate additions, helping to map the attack surface without direct network access.

## Description

Subdomain enumeration reveals hidden or forgotten subdomains that may host vulnerable applications, expose sensitive data, or provide entry points for further attacks. Google Dorks leverage search engine indexing to find subdomains like 'site:*.target.com', excluding common ones like 'www' to focus on unique assets. For deeper discovery, multi-level queries like 'site:*.*.target.com' uncover nested subdomains. Complementary searches target files (e.g., PDFs for leaked info) and URLs indicating admin interfaces or injection points (e.g., ampersands for parameter tampering). The Google Transparency Report supplements this by listing domains in recent certificates, revealing unindexed subdomains tied to the target's infrastructure. This passive technique maps the target's digital footprint, aiding in identifying takeover opportunities or misconfigurations. It applies to web-based reconnaissance against any domain with Google-indexed content.

## Requirements

1. Internet access to Google Search and the Google Transparency Report (transparencyreport.google.com/safe-browsing/search).
2. Basic knowledge of Google Dork operators (site:, inurl:, filetype:, ext:).
3. A target domain (e.g., example.com) in scope for reconnaissance.
4. Optionally, a browser extension or proxy like Burp Suite for capturing and automating searches, though manual entry suffices.

## Defense

- Implement proper access control mechanisms to prevent unauthorized access to sensitive information or systems.
- Regularly monitor and review domain certificates to identify any unauthorized subdomains.
- Implement network segmentation to limit the impact of a potential subdomain takeover.
- Use robots.txt and meta tags to discourage search engine indexing of sensitive subdomains.
- Monitor certificate transparency logs (e.g., via tools like crt.sh) to detect unexpected subdomain registrations.

## Objectives

1. Identify all subdomains of a target domain, including multi-level ones.
2. Discover potential entry points like admin URLs or files with sensitive extensions.
3. Uncover non-indexed subdomains via certificate transparency for a complete attack surface map.
4. Gather intelligence on file types and URL patterns that may indicate vulnerabilities.

## Instructions

### Step 1: Enumerate Basic Subdomains

**Context**: Start with a broad search to find first-level subdomains indexed by Google, excluding the main 'www' subdomain to focus on unique assets. This reveals the primary attack surface.

**Command** ([[commands/google-dorks-enumerate-subdomains]]):
```bash
site:*.domain.com -www
```

> Paste this query into the Google search bar. It returns pages from subdomains like 'mail.domain.com' or 'api.domain.com'. Review results for unique subdomains, noting any that appear frequently. Expected: A list of URLs grouped by subdomain.

### Step 2: Enumerate Multi-Level Subdomains

**Context**: Extend the search to nested subdomains (e.g., 'dev.api.domain.com') which may host development or staging environments prone to misconfigurations.

**Command** ([[commands/google-dorks-enumerate-multi-level-subdomains]]):
```bash
site:*.*.domain.com
```

> Enter this in Google Search. It captures deeper hierarchy subdomains not caught by basic queries. Manually extract and deduplicate subdomain names from results. Expected: URLs showing complex subdomain structures.

### Step 3: Search for PDF Files

**Context**: PDFs often contain sensitive information like internal docs or credentials; this step identifies them for potential data leakage.

**Command** ([[commands/google-dorks-search-pdf-files]]):
```bash
site:domain.com filetype:pdf
```

> Use this query to filter for PDF results across the domain and subdomains. Download and scan files for intel. Expected: Links to downloadable PDFs with metadata or content previews.

### Step 4: Search for URLs with Ampersands

**Context**: URLs with '&' may indicate query parameters vulnerable to injection or manipulation; this helps spot potential XSS or parameter pollution sites.

**Command** ([[commands/google-dorks-search-urls-with-ampersand]]):
```bash
site:domain.com inurl:'&'
```

> Query Google for URLs containing ampersands. Inspect for multi-parameter endpoints. Expected: List of dynamic URLs suitable for further testing.

### Step 5: Search for Admin and Login URLs

**Context**: Locate authentication or admin interfaces that could be brute-forced or exploited for unauthorized access.

**Command** ([[commands/google-dorks-search-admin-login-urls]]):
```bash
site:domain.com inurl:login,register,upload,logout,redirect,redir,goto,admin
```

> This comma-separated inurl query finds pages with common auth-related paths. Prioritize unique findings. Expected: URLs to login portals or admin panels.

### Step 6: Search for Files with Specific Extensions

**Context**: Target script and config files (e.g., .php, .txt) that might expose source code, backups, or configs.

**Command** ([[commands/google-dorks-search-files-by-extension]]):
```bash
site:domain.com ext:php,asp,aspx,jsp,jspa,txt,swf
```

> Use ext: to filter for web-script extensions. Attempt to access and view source if public. Expected: Direct links to files with previews or downloads.

### Step 7: Check Google Transparency Report for Certificate-Based Subdomains

**Context**: For subdomains not indexed by Google, query the Transparency Report to find recent certificate inclusions, revealing infrastructure changes.

**Instructions**: Navigate to transparencyreport.google.com/safe-browsing/search, enter the target domain, and review the 'Search results' for certificate-related domains. Cross-reference with enumerated subdomains.

> No specific command; manual browser interaction. Expected: List of domains/subdomains in recent certificates. If none, fall back to tools like crt.sh for similar intel.

**Code** ([[codes/google-dorks-subdomain-enumeration-queries]]):

> For batch execution or scripting, refer to the consolidated query list in the linked code snippet.
