# The thorough explanation of the operations conducted in Question 3.
[GitHub Link](https://github.com/herovired/git-assignments/tree/main/Question-3)

## Table of Contents
[GitHub Link](https://github.com/sayanalokesh/git_assignment_HeroVired)

[Project description](#project-description)
1. [Creating a branch](#1-creating-a-branch)
2. [Creating 2 branches to work on 2 features](#10-merging-the-2-branches-to-dev)
3. [Checking out to feature/circle-area](#3-checking-out-to-featurecircle-area)
4. [Checking out to feature/rectangle-area](#4-checking-out-to-featurerectangle-area)
5. [Checking out to feature/circle-area](#5-checking-out-to-featurecircle-area)
6. [Adding the feature to the branch feature/circle-area](#6-adding-the-feature-to-the-branch-featurecircle-area)
7. [Checking out to feature/rectangle-area](#7-checking-out-to-featurerectangle-area)
8. [Adding the feature to the branch feature/rectangle-area](#8-adding-the-feature-to-the-branch-featurerectangle-area)
9. [Merging the 2 branches to dev](#9-merging-the-2-branches-to-dev)
10. [Merging the 2 branches to dev](#10-merging-the-2-branches-to-dev)

## Project description
In this project, we will create a new branch called `geometry-calculator` in our GitHub repository. We will work on a simple Python program that calculates the area of a circle and the area of a rectangle. We will use Git stash to switch between working on multiple features (calculating circle area and calculating rectangle area) without committing incomplete changes.

## 1.	Creating a branch

    Git branch geometry-calculator

This command creates a new branch named `geometry-calculator`.

## 2.	Creating 2 branches to work on 2 features

    Git branch feature/circle-area
This command creates a new branch named `feature/circle-area`. This branch will be used to track the development of the code for calculating the area of a circle.

    Git branch feature/rectangle-area
This command creates a new branch named `feature/rectangle-area`. This branch will be used to track the development of the code for calculating the area of a rectangle.

## 3.	Checking out to feature/circle-area

    Git checkout feature/circle-area
This command is used to go to the branch `feature/circle-area`.

Create a python file with the name Trigircle.py
This command creates a new Python file named `Trigircle.py`. This file will contain the code for calculating the area of a circle.

    Git stash save -u area.py
This command stashes the current working state of the repository. This means that the changes that we have made to the files will be saved, but this will not be committed to the repository. This is useful if we want to work on a different feature without affecting the current state of the repository.
Git stash list

This command lists all the files in the stash.

## 4.	Checking out to feature/rectangle-area

    Git checkout feature/rectangle-area
This command switches to the `feature/rectangle-area` branch.

Create another python file with the name area.py
This comment indicates that the code for calculating the area of a rectangle was created, but it was not yet added to the Git repository.

    Git stash save -u area.py
This command stashes the current working state of the repository again. This is necessary because we have made changes to the files since the last time, we stashed them.

## 5.	Checking out to feature/circle-area

    Git checkout feature/circle-area
This command switches back to the `feature/circle-area` branch.

    Git stash pop 0
Since we have already developed the feature, we will get the feature from stash. This command pops the most recent stash from the stack. The <pop-number> parameter is optional. If we do not specify a pop number, the most recent stash will be popped.

## 6.	Adding the feature to the branch feature/circle-area

    Git add area.py.
This command adds all of the changed files to the staging area. The staging area is a temporary area where we can collect changes before you commit them to the repository.

    Git commit -m “Area of a circle”
This command commits the changes in the staging area to the repository. The -m parameter specifies a commit message.

## 7.	Checking out to feature/rectangle-area

    Git checkout feature/rectangle-area
This command switches back to the `feature/rectangle-area` branch.

    Git stash pop <pop-number-related-to-rectangle>
This command pops the stash that was created for the `feature/rectangle-area` branch

## 8.	Adding the feature to the branch feature/rectangle-area

    Git add area.py.
This command adds all of the changed files to the staging area.

    Git commit -m “Area of a rectangle”
This command commits the changes in the staging area to the repository.

## 9.	Merging the 2 branches to dev
After pushing the code to respective branches, it is time to merge both of them to the dev branch. I’ve added Adarsh as a reviewer and he merged the area after approving the code.

## 10.   Merging the code to main
Since the reviewer has already approved the code, The code has been successufully merged to the main branch.