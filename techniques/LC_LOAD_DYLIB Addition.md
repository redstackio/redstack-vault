---
id: ee08afa1-4517-4fef-9316-6dfc159b7394
name: LC_LOAD_DYLIB Addition
type: technique
mitre_id: T1161
mitre_url: null
created_at: '2019-08-28T21:17:32.641682+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# LC_LOAD_DYLIB Addition

**MITRE ID**: T1161

## Description

Mach-O binaries have a series of headers that are used to perform certain operations when a binary is loaded. The LC_LOAD_DYLIB header in a Mach-O binary tells macOS and OS X which dynamic libraries (dylibs) to load during execution time. These can be added ad-hoc to the compiled binary as long adjustments are made to the rest of the fields and dependencies [1]. There are tools available to perform these changes. Any changes will invalidate digital signatures on binaries because the binary is being modified. Adversaries can remediate this issue by simply removing the LC_CODE_SIGNATURE command from the binary so that the signature isn’t checked at load time [2].

# Detection

Monitor processes for those that may be used to modify binary headers. Monitor file systems for changes to application binaries and invalid checksums/signatures. Changes to binaries that do not line up with application updates or patches are also extremely suspicious.

# Mitigation

Enforce that all binaries be signed by the correct Apple Developer IDs, and whitelist applications via known hashes. Binaries can also be baselined for what dynamic libraries they require, and if an app requires a new dynamic library that wasn’t included as part of an update, it should be investigated.

# Footnotes

[1] Patrick Wardle. (2015). Writing Bad @$$ Malware for OS X. Retrieved July 10, 2017.

[2] Patrick Wardle. (2015). Malware Persistence on OS X Yosemite. Retrieved July 10, 2017.

## Defense

Enforce that all binaries be signed by the correct Apple Developer IDs, and whitelist applications via known hashes. Binaries can also be baselined for what dynamic libraries they require, and if an app requires a new dynamic library that wasn’t included 

## Tactics

- [[Persistence|TA0003 - Persistence]]
