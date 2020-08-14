# UPDATE OR CREATE JUPYTER-GUI

1 - From PhysiCell=Jupyter-GUI
python setup_new_proj.py C:\Users\hlimadar\Documents\GitHub\Hypoxia_simulator C:\Users\hlimadar\Documents\GitHub\AMIGOS-hypoxia\HypoxiaCode Hypoxia_simulator

2 - From Hypoxia_simulator
python make_my_tool.py Hypoxia_simulator

3 - Build your PhysiCell project in your /src directory and copy the resulting ```myproj``` executable to ../bin:
~/git/ise_proj1$ cd src
~/git/ise_proj1/src$ make
...
~/git/ise_proj1/src$ cp myproj ../bin      # will be "myproj.exe" on Windows
~/git/ise_proj1$ cd ..

# CREATE NANOHUB 
1 - On https://nanohub.org/tools/create, fill out the basic information for creating your nanoHUB tool. Tool Name should be 3-15 alphanumeric characters, including at least one non numeric character (e.g., ```iu399sp19p099```). Although not required, it’s probably wise to also use only lowercase characters. Provide the URL to your newly created GitHub repo (e.g., ```https://github.com/...```) and also select the bullet to ```Publish as a Jupyter notebook```. When you finally click the ```Register Tool``` button, you will be told if that tool name has already been taken, however, it may take a few seconds for that to appear. Also, don't worry if you forget to provide some info on this initial form, you can always edit it later.

<!--
* In another tab of your browser, go to your newly created repository and edit the ```middleware/invoke``` script *in-place*. You want the name of the .ipynb to be your newly created notebook (=repo) name and the name following the ```-t``` to be the name of your nanoHUB tool. For example:
```
/usr/bin/invoke_app "$@" -C "start_jupyter -A -T @tool ise_proj1.ipynb" -t iu399sp19p099 \
```
If you happened to create your repo to be the same name as your nanoHUB tool, then it would be:
```
/usr/bin/invoke_app "$@" -C "start_jupyter -A -T @tool iu399sp19p099.ipynb" -t iu399sp19p099 \
```
The reason we edit this file in-place is to retain its executable mode. It should be indicated as follows:
-->

Before you request to have your tool installed on nanoHUB, you need to make sure the ```invoke``` file in the ```middleware``` subdirectory is executable:

![alt ensure executable](https://github.com/rheiland/tool4nanobio/blob/master/doc/invoke_file_exec_mode.png)

If you are using Windows, this file seems to lose its "executable" permission when you commit it. You will need to ```cd``` into the ```middleware``` folder of your newly created project and, using ```git``` from the command line:
```
$ git update-index --chmod=+x invoke
$ git commit -m "Changing file permissions"
$ git push
```
then view/refresh the ```invoke``` file from your browser and verify "Executable File" appears in the upper-left as in the screenshot above.