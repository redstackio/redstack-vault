---
id: 1cc9186d-3b66-4a65-bc03-abe748d83789
name: Find Subdomains (amass)
type: procedure
verified: true
submitted: true
created_at: '2020-06-29T16:22:08.379970+00:00'
updated_at: '2023-05-26T00:41:17.136514+00:00'
commands:
- '[[amass dns enumerate subdomains]]'
- '[[amass dns enum subdomains with validated dns servers list]]'
- '[[sort amass results into domain file]]'
- '[[sort amass results into ip file]]'
---

# Find Subdomains (amass)

**Status**: ✓ Verified

## Summary

Amass uses a GraphDB that can store details of every scan which can then later be visualized, or differentiated. This can be done by specifying an output directory to amass. This will also retain a log of the scan attempts. Identifying the targets subdomains is important to: Know what servers are a

## Description

## Description

Amass uses a GraphDB that can store details of every scan which can then later be visualized, or differentiated. This can be done by specifying an output directory to amass. This will also retain a log of the scan attempts.

Identifying the targets subdomains is important to:

- Know what servers are available to the public and some times private.

- Discover services, location and more through the subdomain naming.

- Provide more options to enumerate the target.

Use the 'amass' tool to automate the process of enumerating subdomains on a target.

**Command** ([[amass dns enumerate subdomains]]):

```bash
amass enum -ip -d $_TARGET_DOMAIN
```

## Note

This is just a little bit of linux magic for you to organize and sort the results of the amass dns enumeration into a domains and ips document.

You can cut the results file and extract just the domains into a new file.

**Command** ([[sort amass results into domain file]]):

```bash
cat $_RESULTS_FILE | cut -d']' -f2 | awk '{print $1}' | sort -u > $_OUTPUT_FILE
```

You can cut the results file and extract the IPv4 addresses into a new file.

**Command** ([[sort amass results into ip file]]):

```bash
cat $_RESULTS_FILE | cut -d']' -f2 | awk '{print $2}' | sort -u > $_OUTPUT_FILE
```

# Advanced

You can use the server list built by dnsvalidator with amass, and special arguments to obtain an accurate list of responses. The max dns queries will limit the amount of queries and help to speed up the results. Careful if you use too many validated dns servers in the resolvers.txt list, try between 25-100.

**Command** ([[amass dns enum subdomains with validated dns servers list]]):

```bash
amass enum -rf $_RESOLVERS_FILE -src -ip -d $_TARGET_DOMAIN -max-dns-queries $_MAX_QUERIES_NUM
```

## Commands Used

- [[amass dns enumerate subdomains]]
- [[amass dns enum subdomains with validated dns servers list]]
- [[sort amass results into domain file]]
- [[sort amass results into ip file]]
