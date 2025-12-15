---
id: cmd-goldsrc-precache-generic
data: precache_generic "maps/cs_assault_detail.txt"
tags:
  - file-delivery
  - server-precache
type: command
output: >-
  File added to precache list; clients prompted to download if missing (requires
  sv_downloadurl workaround for bugs).
executor: amxx_script
platforms:
  - Windows
  - Game (GoldSrc Engine)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.581Z'
verified: false
validated: true
submitted: true
---
# precache-generic-maps-cs-assault-detail-txt

## Command

```bash
precache_generic "maps/cs_assault_detail.txt"
```

## Description

AMX Mod X plugin command to preload a generic file into the server's resource list, ensuring connected clients download it automatically, used here to deliver the malicious detail texture file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"maps/cs_assault_detail.txt"` | Path to the file to precache and send to clients | Yes |

## Examples

### Basic Usage

```bash
precache_generic "maps/cs_assault_detail.txt"
```

### With Workaround

Set sv_downloadurl first, then execute to fix precache bug.

```bash
sv_downloadurl "http://server.com/cstrike/"
precache_generic "maps/other_file.txt"
```

## Expected Output

Server logs confirm precache; clients receive file download prompt or auto-download during connection.

## Related

- [[commands/client-cmd-r-detailtextures-1]]
