*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  seppo  seppo123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  antti  antti123
    Output Should Contain  User with username antti already exists

Register With Too Short Username And Valid Password
    Input Credentials  aa  antti123
    Output Should Contain  Username must be at least 3 characters in length, and can contain only letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  antti  antti12
    Output Should Contain  Password must be at least 8 in length, and cannot contain only letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  antti  anttiantti
    Output Should Contain  Password must be at least 8 in length, and cannot contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  antti  antti123
    Input New Command