---
id: 16eb2450-2419-4205-b08c-b5afe1163caf
name: Scrape-GitHub-Repositories-for-Subdomains
type: procedure
verified: true
submitted: false
created_at: '2020-07-24T17:11:23.477563+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Domain Properties]]'
sub_techniques: []
tags:
  - reconnaissance
  - subdomain-enumeration
  - github
  - passive-recon
commands:
  - '[[commands/github-subdomains-enumerate-domain]]'
platforms:
  - Linux
tools:
  - '[[tools/GitHub-Subdomains]]'
validated: true
---

# Scrape-GitHub-Repositories-for-Subdomains

## Summary

This procedure uses the github-subdomains.py script to passively enumerate subdomains associated with a target domain by searching public GitHub repositories for hardcoded subdomain references, such as in configuration files, code snippets, or documentation. It is useful during reconnaissance phases to expand the attack surface without direct interaction with the target infrastructure.

## Description

GitHub repositories often contain leaked or hardcoded subdomains in public code, making them a valuable source for passive reconnaissance. The github-subdomains.py script from the github-search toolset queries GitHub's search API to find repositories mentioning the target domain and extracts potential subdomains from the results. This technique leverages public data to discover hidden subdomains that might not be found through active DNS enumeration. It requires a GitHub personal access token for higher rate limits and is most effective against organizations with active open-source presence. Expected outcomes include a list of unique subdomains that can be validated further with tools like httpx or dnsx.

## Requirements

1. Python 3 installed on a Linux system (e.g., Kali Linux).
2. GitHub personal access token (PAT) with 'repo' and 'search' scopes for authenticated queries.
3. Network access to GitHub API (no proxy restrictions).
4. The github-search tool installed, specifically the github-subdomains.py script.

## Defense

Defensive measures and detection strategies:

- Monitor GitHub repository activity for sensitive domain leaks and implement repository scanning tools like GitHub's secret scanning.
- Use GitHub Advanced Security to detect and alert on hardcoded credentials or domains in commits.
- Rate-limit API access and monitor for unusual search patterns targeting organization repos.
- Implement domain shadowing prevention by regularly auditing public repos for subdomain exposures.

## Objectives

1. Identify subdomains hardcoded in public GitHub repositories associated with the target domain.
2. Compile a list of potential subdomains for further validation and enumeration.
3. Expand the target's attack surface through passive intelligence gathering.

## Instructions

### Step 1: Install the GitHub-Subdomains Tool

**Context**: Download and set up the github-search tool, which includes the github-subdomains.py script, to prepare for subdomain scraping. This ensures you have the latest version and dependencies.

**Command** ([[commands/github-clone-and-install-github-search]]):
```bash
git clone https://github.com/gwen001/github-search.git && cd github-search && pip3 install -r requirements.txt
```

> This clones the repository and installs Python dependencies like requests and beautifulsoup4. Expected output includes successful clone messages and pip installation logs without errors.

### Step 2: Prepare GitHub Personal Access Token

**Context**: Obtain a GitHub PAT to authenticate API requests, avoiding rate limits (unauthenticated searches are capped at 10 per minute). This step is crucial for comprehensive searches.

**Instructions**: Log in to GitHub, navigate to Settings > Developer settings > Personal access tokens > Tokens (classic), generate a new token with 'repo' and 'search' scopes, and set it as an environment variable: `export GITHUB_TOKEN=your_token_here`. If the token is invalid or missing, the script will fall back to unauthenticated mode but with reduced results.

> Expected output: No direct output, but verify by running `echo $GITHUB_TOKEN` (should show the token masked). Success if token is set without syntax errors.

### Step 3: Enumerate Subdomains Using the Script

**Context**: Run the github-subdomains.py script against the target domain to search public repos and extract subdomain mentions. This performs the core reconnaissance.

**Command** ([[commands/github-subdomains-enumerate-domain]]):
```bash
python3 github-subdomains.py -d example.com -t
```

> Replace `example.com` with the target domain. The `-d` flag specifies the domain, and `-t` enables token authentication. The script queries GitHub's code search for the domain and parses results for subdomain patterns (e.g., *.example.com). Expected output: A list of discovered subdomains printed to stdout, such as `sub1.example.com`, `api.example.com`, along with the number of repos searched. If no subdomains are found, it reports zero results. Save output to a file with `> subdomains.txt` for further use.

### Step 4: Validate and Deduplicate Results

**Context**: Review the output for validity and remove duplicates to create a clean list for subsequent enumeration tools.

**Instructions**: Pipe the output through sort and uniq: `python3 github-subdomains.py -d example.com -t | sort | uniq > unique_subdomains.txt`. If results include false positives (e.g., non-subdomain mentions), manually filter or use a tool like grep for patterns like `*.example.com`.

> Expected output: A deduplicated file with valid subdomains. Success if the file contains unique entries without duplicates or irrelevant noise.
