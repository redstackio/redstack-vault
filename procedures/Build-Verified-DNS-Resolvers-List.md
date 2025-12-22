---
id: b72460ae-da99-459e-a5e2-48753a8a8e80
type: procedure
verified: true
submitted: true
created_at: '2020-06-30T02:51:19.652319+00:00'
updated_at: '2023-03-13T19:52:35.078857+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Scanning IP Blocks]]'
sub_techniques: []
tags:
  - dns
  - reconnaissance
  - osint
platforms:
  - Linux
commands:
  - '[[commands/dnsvalidator-fetch-and-validate-resolvers]]'
  - '[[commands/dnsvalidator-docker-fetch-and-validate-resolvers]]'
  - '[[commands/sort-and-limit-resolvers-list]]'
tools:
  - '[[tools/dnsvalidator]]'
validated: true
---

# Build-Verified-DNS-Resolvers-List

## Summary

This procedure uses Dnsvalidator to fetch, test, and validate a list of public DNS resolvers from a reliable source, creating a customized file of responsive servers. This enhances the reliability of DNS-based enumeration tools by avoiding flaky default resolvers, particularly useful in reconnaissance phases where query accuracy is critical.

## Description

Public DNS resolvers can vary in response time and accuracy, leading to incomplete or erroneous results in tools like Amass or MassDNS. By pre-validating a large list (e.g., from public-dns.info), this procedure builds a tailored resolvers.txt file. Run it once before engagements with 20-200 threads to balance speed and thoroughness; the process may take 10-30 minutes depending on thread count.

## Requirements

- Internet access to fetch the nameservers list
- Dnsvalidator installed (or Docker image)
- Sufficient CPU cores for threading (4+ recommended)
- Output directory with write permissions

## Defense

- Monitor for unusual DNS query volumes from reconnaissance tools
- Use DNS firewalls to block known malicious resolver fetches
- Log and alert on high-threaded DNS validation patterns

## Objectives

- Obtain 25-100 validated DNS server IPs
- Ensure resolvers respond quickly to A record queries
- Prepare for integration with enumeration tools

## Instructions

### Step 1: Fetch and Validate Resolvers

**Context**: Download and test the public DNS list against baseline resolutions to verify uptime and speed.

**Command** ([[commands/dnsvalidator-fetch-and-validate-resolvers]]):

```bash
dnsvalidator -tL https://public-dns.info/nameservers.txt -threads $_THREADS -o $_OUTPUT_FILE
```

This command pulls the list, tests each server with threaded queries, and outputs validated IPs to the file. Use $_THREADS=50 for moderate speed.

### Step 2: Alternative Docker Execution

**Context**: If native installation is unavailable, use the Docker container to run validation, mounting the output directory.

**Command** ([[commands/dnsvalidator-docker-fetch-and-validate-resolvers]]):

```bash
docker run -v $(pwd):$_OUTPUT_DIRECTORY -t dnsvalidator -tL https://public-dns.info/nameservers.txt -threads $_THREADS -o $_OUTPUT_DIRECTORY/$_OUTPUT_RESULTS
```

Mounts current directory for output; results saved as resolvers.txt in the specified path.

### Step 3: Sort and Limit Results

**Context**: Sort the validated list alphabetically and trim to a usable size (e.g., top 25 fastest/most reliable) to optimize tool performance.

**Command** ([[commands/sort-and-limit-resolvers-list]]):

```bash
cat $_FILE | sort | tail -n 25 > $_LIMITED_FILE
```

This extracts the last 25 after sorting, assuming the tool orders by reliability; adjust -n for more resolvers.
