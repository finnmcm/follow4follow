# Compare Followers in Instagram

This script provides a simple way to compare followers and following lists in Instagram

## Getting Started:
Start by downloading a json of your followers/following info in instagram.

In your profile, click the three bars on the top right. Then,

Navigate to **Accounts Center** -> **Your information and permissions** -> **Download your information**

From here, select **Some of your information**, and scroll until you see ***Followers and Following*** under **Connections**

Choose to download the data to your device, modify the **Date Range** to include All Time, and change the format to **JSON**

## Compiling Data
Once your Instagram data finishes downloading, download this project to your desktop.

Unzip the instagram file, and drag and drop the **connections** folder into your project folder.

From here, click on the **connections** folder -> **followers_and_following**, and find these files: ***followers_1.json***, ***following.json***

Highlight these files and copy them using Command-C on Mac.

Exit out of the **connections** folder, and paste these two files in the project folder, alongside the ***followers.py*** file

## Running the Program

**If you have a Python IDE already installed (VSCode, PyCharm, Spyder), open up the file and click run.**

To run the program from the command line, open Terminal and navigate to the project folder. If the project folder is in your desktop, run these two commands:

`cd Desktop`

`cd follow4follow-main`

To run the program, enter:  
` python ./followers.py`

The printed list is the list of people you follow who do not follow you back. Enjoy!




