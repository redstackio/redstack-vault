---
id: 34a353fa-c241-448c-91cc-38d990537d00
name: User Enumeration Via Subtly Different Response(Burp Intruder)
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T15:28:11.573734+00:00'
updated_at: '2023-05-26T18:09:38.131345+00:00'
tags:
- '[[Enumeration]]'
- '[[Web Applications]]'
---

# User Enumeration Via Subtly Different Response(Burp Intruder)

**Status**: ✓ Verified

## Summary

Descritpion Some times brute forcing doesnt give the desired results. A detailed analysis of the responses of the brute force attack is needed to identify the subtle differences in the resposne. Instructions 1. Login to the account using random username and password 

## Description

# Descritpion

Some times brute forcing doesnt give the desired results. A detailed analysis of the responses of the brute force attack is needed to identify the subtle differences in the resposne.



# Instructions





1. Login to the account using random username and password







![ae575dbf-fd4a-4515-9ce3-766d8ca398f3.png](_assets/images/Mash/ae575dbf-fd4a-4515-9ce3-766d8ca398f3.png)







2. From the proxy tab, under HTTP History , identify the login request and send the request to the intruder tab.





![590aa793-14a2-40d9-97b0-a818fce34b4e.png](_assets/images/Mash/590aa793-14a2-40d9-97b0-a818fce34b4e.png)





3.From the positions tab, slect attack type to sniper







![1b08fe9c-26b8-4281-8100-d8b5d93c7f78.png](_assets/images/Mash/1b08fe9c-26b8-4281-8100-d8b5d93c7f78.png)





4. Select the username from the *positions *tab and click on *add *to the username parameter value to the payload position







![ee50eb48-a11f-4cfb-9280-34ead7c0e94a.png](_assets/images/Mash/ee50eb48-a11f-4cfb-9280-34ead7c0e94a.png)





5.Use the provided the list of usernames provided or use any username paylaods from [*https://github.com/danielmiessler/SecLists/tree/master/Usernames/Name](https://github.com/danielmiessler/SecLists/tree/master/Usernames/Names)s and pate them in the paylaod tab*





![0a6457ca-c1f5-467f-bff1-08293fc3efdc.png](_assets/images/Mash/0a6457ca-c1f5-467f-bff1-08293fc3efdc.png)





6.Click on *options *tab ,under *grep-extract* , click *add *. Scroll down in the response.







![40917a7d-57d5-46ca-84e8-4c765b6c8be3.png](_assets/images/Mash/40917a7d-57d5-46ca-84e8-4c765b6c8be3.png)





7. Identify the *invalid username or password*. Highlight the text .



![790c017d-cb83-4761-8213-cc3b2d78b6ea.png](_assets/images/Mash/790c017d-cb83-4761-8213-cc3b2d78b6ea.png)





8.Click on ok to start the attack.





![5ae4e35b-9076-4ff4-bc89-73eeffc3bff8.png](_assets/images/Mash/5ae4e35b-9076-4ff4-bc89-73eeffc3bff8.png)





9. When the attack finishes , notice the additional column which shows the error message.On closer analysis of error messages , the hihlighted response contains a typo error meesage. It doent have the full stop at the end of the error message invalid username or password Make a note of the username *accounting*





![da56b66b-fcd4-402f-a766-257e9abed1dc.png](_assets/images/Mash/da56b66b-fcd4-402f-a766-257e9abed1dc.png)





10.Repeat the same steps 3 to 9 for the password filed . 





![c610570d-2bd5-4329-b4ba-c31cf771cafc.png](_assets/images/Mash/c610570d-2bd5-4329-b4ba-c31cf771cafc.png)





11. Use the username  and passwords identified from steps 9 and 10 to login.





![c5165dfa-ad37-4bf6-9cba-5f0ac1eebacf.png](_assets/images/Mash/c5165dfa-ad37-4bf6-9cba-5f0ac1eebacf.png)





12. Observe that the login is successful





![964685df-aee9-4276-ad6f-10198f7e5773.png](_assets/images/Mash/964685df-aee9-4276-ad6f-10198f7e5773.png)



## Tags

- [[Enumeration]]
- [[Web Applications]]


