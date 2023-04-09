# bloxlib
Python library to interact and modify the game called "Roblox"


# Project Structure
--> instance.py -> Instance class => base class to interact with game instances in memory
<br>
--> BoundedFunc.py / PropertyDescriptor.py / GetSetImpl.py -> Internal game structures to handle reflection
<br>
--> Camera.py -> simple class inherited from instance containing useful function
<br>
--> Memory.py -> Utility function
<br>
--> Exploit.py -> Base process class (encapsulates pymem)

# HOW TO USE ?
All modules are contained within bloxlib , so if you need Instance module just do `from bloxlib.instance import Instance` same applies for other like `from bloxlib.Memory import GetDataModel` etc...

### If you need examples head over to the examples repository here : https://github.com/ElCapor/bloxlib-examples


# Requirements
PyMem -> Mandatory just run `pip3 install pymem` to install it
<br>
PyQt5 -> Optional , used for gui applications, just run `pip3 install pyqt5` to install it

# Exploit class
### Exploit class is just a wrapper around pymem that allow's to easily get processes and operate on them
#### Members :
`ProgramName` : string , represents the name of the opened process
`Program` : pymem.Pymem , pymem structure that represents the process
#### Functions :
`Exploit(ProgramName)` takes as a an argument an integer or a string , creates a process based on a name or a string.

`Exploit.h2d(hex : string) -> int` converts the given string representation of a hexadecimal number into an int

`Exploit.d2h(decimal : int) -> str` converts the given integer into it's hexadecimal string representation , mostly used to print addresses

`AOBSCANALL(AOB_Sig,xreturn_multiple)` scans the whole process memory for a specific bytes pattern defined in AOB_Sig , an example can be found in Memory.py

`Exploit.gethxc(hex_string)`  Get Hex Count, counts the amount of Hex in the Hex String. returns the length of the hex instructions.

`Exploit.hex2le(hex_array)` converts hexadecimal values to little endian, for use with assembly shell code.

`Exploit.calcjmpop(des,cur)`  Calculates the Jump or Call using the two arguments. Mainly used for assembly instructions

`Exploit.DRP(address)` Reads a pointer in memory.

## Memory.py
### Simple file that holds memory tools
`GetDataModel()` returns the address of the datamodel ( = game root) by performing an array of bytes scan
`SetupOptimizations()` will allocate the functions that are required for get & set property , note that it is necessary to call it for now in order to be able to use that, meaning that you can't use multithreading for now
`FreeOptimizations()` will free the memory of the functions , you should call this at the end of your program to clean up the memory

## Instance class
### What is an Instance ?
#### Roblox Engineers made a base class named instance that represents every game object. Every object in game an instance that have properties and functions in common.

`Instance(Address : int)` Specifies an instance in memory, returns an instance with address set to 0 when called without arguments.
Arguments : Address representing the memory address of the instance

`Instance().new(className : str) -> Instance` Creates a new instance given a class name , returns an instance with address 0 when class doesnt exist
`Instance.getAddress() -> int` returns the address of the instance

`Instance.GetName() -> str` returns the name of the instance

`Instance.GetChildren() -> list` returns a list containing child instances of a specified instance

`Instance.GetChildren() -> list` returns a list containing descendants instances of a specified instance

`Instance.FindFirstChild(name : str) -> Instance ` returns the first found instance by a name

`Instance.GetClassDescriptor() ` -> returns the address of class descriptor for the given instance

`Instance.GetPropertyDescriptors()` -> returns a list containing all the property descriptors of a given instance check PropertyDescriptor part to learn more about it

`Instance.GetPropertyDescriptor(name : str) -> PropertyDescriptor` Returns the property descriptor for a given name

`Instance.GetBoundedFuncs() -> list` returns a list containing all bounded functions of an instance , check the BoundedFunction section to learn about it

`Instance.GetBoundedFunction() -> BoundedFunction` returns the boundefunction linked to that instance according to the name, check the BoundedFunction section to learn about it

`Instance.GetProperty(name)` get the property of instance given the name of that property , **SUPER INSTABLE**

`Instance.SetProperty(name, value)` set the property of an instance given the name of that property , **SUPER INSTABLE**


## PropertyDescriptor Class
### What is a property descriptor ?
#### In order to make it easier to use their c++ classes into lua , roblox engineers decided to build a class called PropertyDescriptor that holds all properties of an instance and allows them to be easily called and set
`PropertyDescriptor(Address)` defines a PropertyDescriptor at the specified address , when no argument is specified it sets it to 0

`PropertyDescriptor.GetAddress()` returns the address of the given property descriptor

`PropertyDescriptor.GetName()` returns the name of the given property descriptor

`PropertyDescriptor.GetSet()` returns a GetSet structure which holds get & set function for that property , check GetSet section to learn more about it


## GetSet Class
### What is GetSet ?
#### Basically roblox engineers build a simple class that's only 0x30 in size and it just holds the get and set function for a given property descriptor
`GetSetImpl(Address)` defines a GetSet structure at the specified address , when no argument is specified it sets it to 0

`GetSetImpl.GetAddress()` returns the address of the given property descriptor

`GetSetImpl.Get()` returns the address of the **Get** function for that property

`GetSetImpl.Set()` returns the address of the **Set** function for that property

## BoundedFunction class
### What is BoundedFunction ?
#### Roblox engineers built a simple class to allow them to call Instance methods in game using Lua. It is worth noting that this structure also holds the security for some functions and is the reasons for identity checks
`BoundedFunc(Address)` defines a BoundedFunction structure at the specified address , when no argument is specified it sets it to 0

`BoundedFunc.GetAddress()` returns the address of the given Bounded Function

`BoundedFunc.GetFunc()` returns the address of the function

`BoundedFunc.GetSecurity()` returns the security level of the function (integer)

`BoundedFunc.SetSecurity(new_security : int)` Sets the security level of the function report below for a table of security numbers

`BoundedFunc.GetSecurityName()` returns the security level of the function (string)

Security Table

| Security     | String     |
|--------------|------------|
| 0            |  None      |
| 1            |  Plugin    |
| 2            |LocalScript | 
| 3            |RobloxPlace | 
| 4            |RobloxScript| 
| 5            |CoreScript  | 
| 6            |  Roblox    | 
| 7            |  Roblox    | 
| 8            |WritePlayer | 


## AUTHOR :  ElCapor
### CONTRIBUTION FROM : Ficelloo & 01


# LICENCE
YOU ARE NOT ALLOWED TO USE THIS IN A COMMERCIAL PROJECT UNLESS YOU BUY THE RIGHTS FROM ME (ElCapor).
ANY CHANGE MADE TO THIS WORK MUST BE STATED

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.