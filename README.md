# python.beginner
A beginner's guide to python and its concepts tried for 3.6.2

Before you begin this guide to python, It is highly advisable to read this file before starting with this repository. This file will help you to understand the setup and environment configurations and will save a lot of time and headache before you start learning python.

• Version
This repository and all the examples and the code that it contains was prepared with version 3.6.2 and should be valid and relevant for versions >=3.6.2. However if you are just starting out with python, then this should not be a worry for you unless you want to go for Python 2.x. This repository is primarily prepared for learning python with versions 3.x.


• Pre-requisite: Knowledge/Technical Debt
There are very less pre-requisites on the knowledge front before you begin your python journey. A general overview of Object oriented world because of python being an objected oriented programming language some programming basics is enough to get you started on the journey.
	
• Pre-requisite: Getting Python
Before you start to code in python make sure you have python installed in your system. To get that, go to python's official website https://www.python.org/downloads/ and download the relevant version you require. At the time of creation of this repository, the  version was 3.6.2, you can download the latest version if you want for the OS that you have on your machine and it should not be a   problem until its 3.x as mentioned above.
	
• Pre-requisite: Installing Python
After the download is complete, just run the executable file (in case of windows) with the default settings and it will install python. For my system it was installed on C:\Users\<UserName>\AppData\Local\Programs\Python\Python36-32 (my OS is Windows 7).
	
Editor: 
You are free to use any editor you like, I used Visual Studio Code and if you are using the same, certain configurations with it will help you and will save you a lot of headache before you begin.
	
Extension:
If you are using visual studio code, then 'Python' extension by Don Jayamanne will help you a lot in your learning journey. You may wish to find relevant extensions depending on the editor you choose.
		
Pylint:
Once you start coding and write your first program in Visual Studio Code, you might find an annoying message by the editor that pylint is not installed on a path, you can install it by going to the path where python is installed and then opening the cmd terminal (for windows) and running the command pip install -m pylint.
		
Environment:
		
    launch.json:  
			
			'configuration': [
			{
				"name": "Python",
				"type": "python",
				"request": "launch",
				"stopOnEntry": false,
				"pythonPath": "${config:python.pythonPath}",
				"program": "${file}",
				"cwd": "${workspaceRoot}",
				"env": {},
				"envFile": "${workspaceRoot}/.env",
				"debugOptions": [
				"WaitOnAbnormalExit",
				"WaitOnNormalExit",
				"RedirectOutput"
				],
				"args": [
				"Some Argument"
				]
			}
			]
			
		This configuration is suitable with the settings.json that is given below. 
			
		settings.json:
			
			{
			"python.linting.pylintEnabled": true,
			"python.linting.pylintPath": "C:\\Users\\<UserName>\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\pylint.exe",
			"python.pythonPath": "C:\\Users\\<UserName>\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe",
			"python.autoComplete.extraPaths": [
			"C:/Program Files (x86)/Google/google_appengine",
			"C:/Program Files (x86)/Google/google_appengine/lib"
			]
			}
			
		Note: 
				1) Give the pylint path where your pylint is installed when you ran the command to install pylint.
				2) Give the python path where your python is installed.
		
• Running your code: 
After you have finished coding for a file and wish to run the file and see its output, you can do so in your Editor itself
		
	i. Open up the terminal by pressing ctrl + ` (for Windows, for MAC press cmd + `) and make sure the terminal is cmd.exe which you can verify looking at the top right corner of the terminal.
	ii. Suppose the name of your file is hello.py, so to run it just type hello.py and press enter (Windows, for MAC, it should be the return key)
	
		 
	
	
