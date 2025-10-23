---
id: 9f07f4b3-a211-4856-86be-714da33f021b
name: Password Bruteforce Via Password Change
type: procedure
verified: true
submitted: true
created_at: '2020-09-02T13:43:58.812507+00:00'
updated_at: '2023-05-26T18:08:02.085621+00:00'
platforms:
- Web
tags:
- '[[broken authentication]]'
- '[[Web Applications]]'
---

# Password Bruteforce Via Password Change

**Status**: ✓ Verified

## Summary

Password change functioanlity can be used by an attacker to bruteforce and identify the password if there are no sufficient protections inplace. 

## Description

# Description

Password change functioanlity can be used by an attacker to bruteforce and identify the password if there are no sufficient protections inplace.



# Instructions





1. Login to the application with Weiner credentials. Open the burpsuite and configure the browser to intercept the requests.





![f58d3dff-6c93-4300-9b59-fa843906137c.png](_assets/images/Mash/f58d3dff-6c93-4300-9b59-fa843906137c.png)





2.Access my account and observe that there is a change password functionality where a current password , new password and confirm new password fields are required to change the password. Intercept the *changepassword *request.





![f881cc31-9c55-445e-92e0-627ab524d3e8.png](_assets/images/Mash/f881cc31-9c55-445e-92e0-627ab524d3e8.png)





3.Back to login page and try to login with incorrect credentials twice and observe the error pages.





![f8db4bef-64a1-4248-bbef-393abfc3c87a.png](_assets/images/Mash/f8db4bef-64a1-4248-bbef-393abfc3c87a.png)





4.Enter the incorrect password and observe the response from the server. It says *Current password is incorrect*.





![005003d0-288b-4c49-98a6-40562a28d652.png](_assets/images/Mash/005003d0-288b-4c49-98a6-40562a28d652.png)





5.Now enter the current password and in new password fileds enter two different password. Response says *New passwords do not match*.





![75859ddf-3269-4c66-a369-3305796519ce.png](_assets/images/Mash/75859ddf-3269-4c66-a369-3305796519ce.png)





6.Identify the change password request from HTTP History and send the request to intruder tab.Make sure that the new password parameters are different.





![6e2b3d68-4041-48d9-9a3a-5ba974ae10d3.png](_assets/images/Mash/6e2b3d68-4041-48d9-9a3a-5ba974ae10d3.png)





7.Two password parameters are different *new-password-1=hacker888&new-password-2=hacker999*





![17b90e0b-6ecc-420c-ba88-11eb27dfa41d.png](_assets/images/Mash/17b90e0b-6ecc-420c-ba88-11eb27dfa41d.png)





8.From the positions tab in the intruder window , highlight the current password and click on add to the *current password* parameter to the payload position.





![5ff1f55a-eae4-49e9-821c-fba78cbaa869.png](_assets/images/Mash/5ff1f55a-eae4-49e9-821c-fba78cbaa869.png)





9.Navigate to payloads tab and select* simple list* for payload type. Paste the list of passwords in the tab.



Password list can be obtained from:[*https://github.com/1N3/IntruderPayload](https://github.com/1N3/IntruderPayloads)s*





![fe6f18ba-6194-404e-a374-e62fb63692e1.png](_assets/images/Mash/fe6f18ba-6194-404e-a374-e62fb63692e1.png)





10. Go to options tab from the intruder window and add a grep match rule to flag responses containing *New passwords do not match*. Click on *start attack *





![1ae77dca-1fd5-47c5-af0a-6eefec33ec60.png](_assets/images/Mash/1ae77dca-1fd5-47c5-af0a-6eefec33ec60.png)





![85c13d00-49c3-439d-8d12-a88f14924906.png](_assets/images/Mash/85c13d00-49c3-439d-8d12-a88f14924906.png)





12.observe that one response contains* `New passwords do not match*` message, Make a note of the password for this request





![bb3ebd4e-44c5-4a38-a17b-3ac50cace400.png](_assets/images/Mash/bb3ebd4e-44c5-4a38-a17b-3ac50cace400.png)





13.Login with the identified password from the above step





![9ada88d5-ed77-4a51-9345-12e713705af1.png](_assets/images/Mash/9ada88d5-ed77-4a51-9345-12e713705af1.png)



## Platforms

- Web

## Tags

- [[broken authentication]]
- [[Web Applications]]


