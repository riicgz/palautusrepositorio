*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  tommi
    Set Password  tommi123
    Set Password Confirmation  tommi123
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  yo
    Set Password  yoyoyo123
    Set Password Confirmation  yoyoyo123
    Click  button >> text=Register
    Register Should Fail

Register With Valid Username And Too Short Password
    Set Username  kimmo
    Set Password  kimmo89
    Set Password Confirmation  kimmo89
    Click  button >> text=Register
    Register Should Fail

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  123kalle
    Set Password Confirmation  123kalle
    Click  button >> text=Register
    Register Should Fail

*** Keywords ***
Register Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Register Should Fail
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
