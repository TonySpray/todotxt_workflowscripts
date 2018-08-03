# Todo.txt Workflow Scripts

*A collection of little scripts I threw together to capture my todos quickly into todo.txt.*

----
To see the scripts in action [here](https://youtu.be/rPVh0itaMgo)


**/Python-Simple-File-Sync/** contains a python simple sync script and an example crontab entry to run the script once a minute.
- Put the script in a bin folder. (I have a .bin in my home folder.)
- Complete the paths in the crontad.example and add it to your crontab with: `crontab -e`


**/Pythonista-Scripts/** contains my scripts to create the MySorter App.
Pythonista is an iPhone app that gives you the ability to create iOS apps and extentions in python. [Pythonista Site](http://omz-software.com/pythonista/)
To create a the MySorter app:
- Download the xcode project from [https://github.com/omz/PythonistaAppTemplate](https://github.com/omz/PythonistaAppTemplate)
- Follow the instructions in the project's README regarding Changing the App's Name, Icon, and Launch Screen, etc.
- Copy the contents of the Pythonista-Scripts folder into the project's Script folder.
- Build with xCode. (If your iOS deviece is connected to your computer it nhould show as a. build target)
