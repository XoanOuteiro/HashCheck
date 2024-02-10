# HashCheck

 This is a super simple CLI-Based file integrity verifier using Python and hashlib
 via MD5 hashing

 ## Installation

 Clone this repository:
 
 ``` shell
 git clone https://github.com/XoanOuteiro/HashCheck
 ```

 Then move into the repository folder and run:
 
 ``` shell
 pip install -r requirements.txt
 ```

 ### Usage

 Open a CLI in the src folder, the program can the be used via

 ``` shell
python HashCheck.py
 ```

or

``` shell
python3 HashCheck.py
```

and by adding the following flags:
| Command | Description |
| --- | --- |
| -h / --help | Displays a brief description of the usage of the app |
| -v / --version | Displays the current build version |
| -pF / --parseFile | Returns a single MD5 hash as a summary of all the contents of the specified file (requires a filepath) |
| -f / --File | Specifies a file to be checked against another file (-tF) or a hash (-tH) (requires a filepath) |
| -tF / --toFile | Specifies a file to be checked against the -f file (requires a filepath)  |
| -tH / --toHash | Specifies the hash against which the file hash will be checked (requires a hash) |


