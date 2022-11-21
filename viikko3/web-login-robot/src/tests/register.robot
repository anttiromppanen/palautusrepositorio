*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  antti
    Set Password  antti123
    Set Password Again  antti123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  an
    Set Password  antti123
    Set Password Again  antti123
    Submit Register Credentials
    Register Should Fail With Message  Username must be at least 3 characters in length, and can contain only letters a-z

Register With Valid Username And Too Short Password
    Set Username  antti
    Set Password  antti12
    Set Password Again  antti12
    Submit Register Credentials
    Register Should Fail With Message  Password must be at least 8 in length, and cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  antti
    Set Password  antti123
    Set Password Again  antti1234
    Submit Register Credentials
    Register Should Fail With Message  Passwords must match

Login After Successful Registration
    Set Username  antti69
    Set Password  antti123
    Set Password Again  antti123
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  antti69
    Set Password  antti123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  antti
    Set Password  antti
    Set Password Again  antti
    Submit Register Credentials
    Register Should Fail With Message  Password must be at least 8 in length, and cannot contain only letters
    Go To Login Page
    Login Page Should Be Open
    Set Username  antti
    Set Password  antti
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Again
    [Arguments]  ${password_again}
    Input Password  password_confirmation  ${password_again}

Create User And Go To Register Page
    Go To Register Page
    Register Page Should Be Open