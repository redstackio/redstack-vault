---
type: code
language: text
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - mssql
  - hashcat
  - reference
validated: true
---

# mssql-hashcat-modes-reference

## Code

```text
131    MSSQL (2000)    0x01002702560500000000000000000000000000000000000000008db43dd9b1972a636ad0c7d4b8c515cb8ce46578
132    MSSQL (2005)    0x010018102152f8f28c8499d8ef263c53f8be369d799f931b2fbe
1731   MSSQL (2012, 2014)  0x02000102030434ea1b17802fd95ea6316bd61d2c94622ca3812793e8fb1672487b5c904a45a31b2ab4a78890d563d2fcf5663e46fe797d71550494be50cf4915d3f4d55ec375
```

## Description

Reference list of Hashcat modes and sample hashes for MSSQL versions, used to select the correct -m flag when cracking extracted hashes.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Static reference data | N/A |

## Usage

Consult this during cracking setup: Match your extracted hash prefix (e.g., 0x0100 for 2000) to select mode 131. Paste into notes or scripts for automation.

## Detection

N/A (reference only; detection applies to Hashcat usage).

## Related

- [[procedures/MSSQL-Server-Password-Hash-Extraction-and-Cracking]]
