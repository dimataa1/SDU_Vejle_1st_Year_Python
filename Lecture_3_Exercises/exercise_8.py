"""
Create a new Python file called:

student_report.py
Write a program that stores:
a student's name;
two assignment scores.
Use functions to:

calculate the average score;
display a short student report.
Your output should look similar to:

Student: Sara
Assignment 1: 75
Assignment 2: 85
Average: 80.0
Use meaningful variable names and include at least one useful comment.
When your program works correctly, continue with the Git and GitLab part below.

Part 1 — Make Sure VS Code Is Open in the Correct Folder
Your Python file should be inside the folder that you have opened in VS Code.

In VS Code, open:

Terminal → New Terminal

The terminal should open at the bottom of VS Code.

Check which folder you are currently working in:

pwd
Then check which files are inside the folder:
dir
Make sure you can see:
student_report.py
If you cannot see the file, you are probably working in the wrong folder.
Open the correct folder in VS Code using:

File → Open Folder

Then open the terminal again.

Part 2 — Initialize Git
In the VS Code terminal, initialize the folder as a Git repository:

git init
You only need to do this once for a new local repository.
Now check the Git status:

git status
You should see student_report.py listed as an untracked file.
Part 3 — Add the File to Git
Add your Python file:

git add student_report.py
Then check the status again:
git status
Notice what changed.
Your file should now be ready to commit.

Part 4 — Create Your First Commit
Create a commit with a meaningful message:

git commit -m "Add student report program"
Check the repository again:
git status
You can also view your commit history:
git log
Find the commit you just created.
Part 5 — Connect to SDU GitLab
Create or use your repository on:

gitlab.sdu.dk
Copy the repository URL from SDU GitLab.
Then connect your local repository to the GitLab repository.

For example:

git remote add origin YOUR_REPOSITORY_URL
You can check the remote connection with:
git remote -v
Make sure the URL points to SDU GitLab.
Part 6 — Push Your Program
Push your commit to GitLab.

Depending on your branch setup, the first push may look like:

git push -u origin main
After the first successful push, you will usually only need:
git push
Open your repository on SDU GitLab and check that:
student_report.py is visible;
your commit is visible;
the code on GitLab matches the code in VS Code.
Part 7 — Modify the Program
Extend your program so that it also calculates and displays the difference between the two assignment scores.

For example:

Student: Sara
Assignment 1: 75
Assignment 2: 85
Average: 80.0
Score difference: 10
Run the program again in VS Code and make sure it works correctly.
Part 8 — Save the New Version with Git
Check what has changed:

git status
Add the modified file:
git add student_report.py
Create a second commit:
git commit -m "Add score difference"
Push the new commit:
git push
Open SDU GitLab again and confirm that you can now see both commits.
If You Get an Error
If you see:

fatal: not a git repository
you are either in the wrong folder or Git has not been initialized there.
Check:

pwd
dir
Then, if it is the correct folder:
git init
If you see:
fatal: pathspec 'student_report.py' did not match any files
Git cannot find that file in the current folder.
Check:

dir
Make sure the file is saved and that you are working in the correct VS Code folder.
"""

def calculate_average(score_1, score_2):
    # Average of the two assignment scores
    average = (score_1 + score_2) / 2
    return average


def show_student_report(name, score_1, score_2):
    average = calculate_average(score_1, score_2)
    print("Student:", name)
    print("Assignment 1:", score_1)
    print("Assignment 2:", score_2)
    print("Average:", average)


student_name = "Sara"
assignment_1 = 75
assignment_2 = 85

show_student_report(student_name, assignment_1, assignment_2)