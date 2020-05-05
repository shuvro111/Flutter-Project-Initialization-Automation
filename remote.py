import os
import sys
from github import Github

#Folder create
foldername = input("Please Enter Folder Name: \n")
foldername = foldername.lower()
path = os.environ['mp']
_dir = path + '/' + foldername

os.mkdir(_dir)
os.chdir(_dir)

print("Folder Created Successfully\n")


#github
token = os.environ['gt']
g = Github(token)
user = g.get_user()
login = user.login


response = input("Do You Want To Create Repository With Same Name As Folder?\n")

while(response != 'Y' or response != 'y' or response != 'N' or response != 'n'):

  print("Please Enter A Valid Response\n")
  
  response = input("Do You Want To Create Repository With Same Name As Folder?\n")

  if (response == 'Y' or response == 'y'): 
    repo = user.create_repo(foldername, private=True)

    commands = [f'echo "# {repo.name}" >> README.md',
              'git init',
              f'git remote add origin https://github.com/{login}/{foldername}.git',
              'git add .',
              'git commit -m "Initial commit"',
              'git push -u origin master']

    for c in commands:
      os.system(c)
    break

  elif (response == 'N' or response == 'n'):
    reponame = input("Please Enter Repository name: \n")
    repo = user.create_repo(reponame, private=True)

    commands = [f'echo "# {repo.name}" >> README.md',
              'git init',
                f'git remote add origin https://github.com/{login}/{reponame}.git',
              'git add .',
              'git commit -m "Initial commit"',
              'git push -u origin master']

    for c in commands:
      os.system(c)

    break




print("Repository Created Successfully!")

#Flutter Project

flutterResponse = input("Do You Want To Create Flutter Project With Same Name As Folder?\n")


while(flutterResponse != 'Y' or flutterResponse != 'y' or flutterResponse != 'N' or flutterResponse != 'n'):
  
  print("Please Enter A Valid Response\n")
  
  flutterResponse = input("Do You Want To Create Flutter Project With Same Name As Folder?\n")
  
  if (flutterResponse == 'Y' or flutterResponse == 'y'):

    createProjectCmd = 'flutter create' + " " + foldername.lower()
    
    os.system(createProjectCmd)
    os.chdir(foldername)
    os.system('code .')
    break

  elif (flutterResponse == 'N' or flutterResponse == 'n'):
    projectName = input("Please Enter Project name: \n")
    createProjectCmd = 'flutter create' + " " + projectName;

    os.system(createProjectCmd)
    os.chdir(projectName)
    os.system('code .')
    break
    


















