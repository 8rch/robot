*** Settings ***
Library RPA.Browser
Documentation Extract Marie Curie Birthday & Age From Web
*** Variables ***
${URL} https://en.wikipedia.org/w/index.php?title=Special%3ASearch&profile=default&search=%s
${SEARCH TERM} Marie Curie
*** Keywords ***
Open Wiki Page
Go To ${URL}=${SEARCH TERM}
Sleep 1 second
Get Info About Person
[Arguments] @{person}=Marie Curie
... @{birthday}=None
... @{death}=None
Set Suite Variable $person
Set Suite Variable $birthday
Set Suite Variable $death
Element Should Cont