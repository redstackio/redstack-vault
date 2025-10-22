---
id: 9658e9f6-7e90-4d6e-aa5b-0715413f1c4f
name: bulk_extractor
type: tool
verified: false
created_at: '2019-08-28T21:17:24.800530+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# bulk_extractor

## Overview

bulk_extractor is a program that extracts features such as email addresses, credit card numbers, URLs, and other types of information from digital evidence files. It is a useful forensic investigation tool for many tasks such as malware and intrusion investigations, identity investigations and cybe

## Description

bulk_extractor is a program that extracts features such as email addresses, credit card numbers, URLs, and other types of information from digital evidence files. It is a useful forensic investigation tool for many tasks such as malware and intrusion investigations, identity investigations and cyber investigations, as well as analyzing imagery and pass-word cracking. The program provides several unusual capabilities including:

It finds email addresses, URLs and credit card numbers that other tools miss because it can process compressed data (like ZIP, PDF and GZIP ﬁles) and incomplete or partially corrupted data. It can carve JPEGs, office documents and other kinds of files out of fragments of compressed data. It will detect and carve encrypted RAR files.

It builds word lists based on all of the words found within the data, even those in compressed files that are in unallocated space. Those word lists can be useful for password cracking.

It is multi-threaded; running bulk_extractor on a computer with twice the number of cores typically makes it complete a run in half the time.

It creates histograms showing the most common email addresses, URLs, domains, search terms and other kinds of information on the drive.

bulk_extractor operates on disk images, files or a directory of files and extracts useful information without parsing the ﬁle system or ﬁle system structures. The input is split into pages and processed by one or more scanners. The results are stored in feature files that can be easily inspected, parsed, or processed with other automated tools.

bulk_extractor also creates histograms of features that it finds. This is useful because features such as email addresses and internet search terms that are more common tend to be important.

In addition to the capabilities described above, bulk_extractor also includes:

A graphical user interface, Bulk Extractor Viewer, for browsing features stored in feature ﬁles and for launching bulk_extractor scans

A small number of python programs for performing additional analysis on feature ﬁles
