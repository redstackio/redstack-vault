---
id: 65fe9358-3049-41fb-9781-50a561dccaf6
name: Cloud Groups
type: sub-technique
mitre_id: T1069.003
mitre_url: null
created_at: '2023-04-06T00:31:25.612456+00:00'
updated_at: '2023-04-06T00:31:25.612456+00:00'
parent_technique: '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
---

# Cloud Groups

**MITRE ID**: T1069.003

**Parent Technique**: [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]

This is a sub-technique of T1069 - Permission Groups Discovery.

## Summary

Adversaries may attempt to find cloud groups and permission settings. The knowledge of cloud permission groups can help adversaries determine the particular roles of users and groups within an environment, as well as which users are associated with a particular group.

With authenticated access ther

## Description

Adversaries may attempt to find cloud groups and permission settings. The knowledge of cloud permission groups can help adversaries determine the particular roles of users and groups within an environment, as well as which users are associated with a particular group.

With authenticated access there are several tools that can be used to find permissions groups. The <code>Get-MsolRole</code> PowerShell cmdlet can be used to obtain roles and permissions groups for Exchange and Office 365 accounts (Citation: Microsoft Msolrole)(Citation: GitHub Raindance).

Azure CLI (AZ CLI) and the Google Cloud Identity Provider API also provide interfaces to obtain permissions groups. The command <code>az ad user get-member-groups</code> will list groups associated to a user account for Azure while the API endpoint <code>GET https://cloudidentity.googleapis.com/v1/groups</code> lists group resources available to a user for Google.(Citation: Microsoft AZ CLI)(Citation: Black Hills Red Teaming MS AD Azure, 2018)(Citation: Google Cloud Identity API Documentation)

Adversaries may attempt to list ACLs for objects to determine the owner and other accounts with access to the object, for example, via the AWS <code>GetBucketAcl</code> API (Citation: AWS Get Bucket ACL). Using this information an adversary can target accounts with permissions to a given object or leverage accounts they have already compromised to access the object.

## Tactics

This sub-technique is used in the following tactics:

- [[Discovery|TA0007 - Discovery]]
