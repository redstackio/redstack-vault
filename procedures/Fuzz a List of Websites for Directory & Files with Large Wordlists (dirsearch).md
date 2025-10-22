---
id: 08ed4825-3b5c-4a16-97ba-da726689042a
name: Fuzz a List of Websites for Directory & Files with Large Wordlists (dirsearch)
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:34.325749+00:00'
updated_at: '2023-05-26T00:50:24.344291+00:00'
commands:
- '[[dirsearch brute force directories and files from sub-domain list with custom
  paths wordlists]]'
---

# Fuzz a List of Websites for Directory & Files with Large Wordlists (dirsearch)

**Status**: ✓ Verified

## Summary

Use this tool to find directories and files in a list of sub-domains using a SecList wordlist containing the Top 1000 Robots.txt entries, use this if the basic paths.txt list doesn't find much. dirsearch Top-1000 Robots.txt is part of SecLists wordlist. top-1000-robots.txt wordlist If you are havin

## Description

# Description

Use this tool to find directories and files in a list of sub-domains using a SecList wordlist containing

the Top 1000 Robots.txt entries, use this if the basic paths.txt list doesn't find much.

[dirsearch](https://github.com/maurosoria/dirsearch)

Top-1000 Robots.txt is part of SecLists wordlist.

[top-1000-robots.txt wordlist](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/RobotsDisallowed-Top1000.txt)

If you are having trouble obtaining results with the Top 1000 wordlist, try these others:

raft-large-dictionaries.txt is a massive wordlist you can try

[raft directories](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/raft-large-directories.txt)

raft-large-files.txt is a massive wordlist of possible files you can try

[raft files](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/raft-large-files.txt)

##  Instructions

1. Pass in a list of sub-domains, the Top-1000-Robots.txt from SecLists, and your # of threads.

**Command** ([[dirsearch brute force directories and files from sub-domain list with custom paths wordlists]]):

```bash
python3 dirsearch.py -L sub-domaints.txt -e .* -w RobotsDisallowed-Top1000.txt --simple-report=output.txt -t 50

```

## Commands Used

- [[dirsearch brute force directories and files from sub-domain list with custom paths wordlists]]
