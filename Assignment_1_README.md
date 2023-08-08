# GitHub Link
[GitHub Repository](https://github.com/your-username/git_assignment_HeroVired)

## Table of Contents
[Project Description](#project-description)

1. [Repository Creation](#1-repository-creation)
2. [Branch Creation and Code Addition](#2-branch-creation-and-code-addition)
3. [Merge 'dev' with 'main' and Release Version 1](#3-merge-dev-with-main-and-release-version-1)
4. [Add Collaborators](#4-add-collaborators)
5. [Feature Implementation on New Branch 'feature/sqrt'](#5-feature-implementation-on-new-branch-featuresqrt)
6. [Bug Fix in 'dev' Branch](#6-bug-fix-in-dev-branch)
7. [Pull Request and Code Review](#7-pull-request-and-code-review)
8. [Merge 'feature/sqrt' into 'dev'](#8-merge-featuresqrt-into-dev)
9. [Testing on 'dev' and 'main' Branches](#9-testing-on-dev-and-main-branches)
10. [Merge 'dev' into 'main' and Release Version 2](#10-merge-dev-into-main-and-release-version-2)

## Project Description
The program is a Python application called "CalculatorPlus" that provides basic arithmetic operations, such as addition, subtraction, multiplication, and division. The program also adds support for calculating the square root of a number.

## 1. Repository Creation
- Create a new repository named "git_assignment_HeroVired".

        git branch git_assignment_HeroVired

## 2. Branch Creation and Code Addition
- Create a new branch named "dev" and switch to it.

        git branch dev
- Add the provided Python code snippet for the Calculator class to the "dev" branch.

## 3. Merge 'dev' with 'main' and Release Version 1
- Merge the "dev" branch into the "main" branch to finalize version 1 of the CalculatorPlus app.
- Create a release for version 1 of the app.

## 4. Add Collaborators
- I have added Adarsh as a collaborator.

## 5. Feature Implementation on New Branch 'feature/sqrt'
- Create a new branch named "feature/sqrt" to work on the square root feature.

        git branch feature/sqrt
- Add the 'sqrt' code implementation to the "feature/sqrt" branch.

## 6. Bug Fix in 'dev' Branch
- While working on "feature/sqrt," I encountered a critical bug report related to the "divide" function in the "dev" branch.
- I switched back to the "dev" branch.

        git checkout dev
        
- I updated the "divide" function to include a conditional check for division by zero and raise an appropriate ValueError.
- I tested the fixed "divide" function to ensure the bug is resolved.

## 7. Pull Request and Code Review
- After completing the feature implementation and ensuring that the application works correctly, I created a pull request targeting the main branch.
- I requested Adarsh to review the code.

## 8. Merge 'feature/sqrt' into 'dev'
- Once the pull request is approved, I merged the "feature/sqrt" branch into the "dev" branch.

## 9. Testing on 'dev' and 'main' Branches
- I tested the entire application, including the new square root feature and the bug-fixed divide function, on the "dev" branch.
- Ensuring all functionalities are working correctly.

## 10. Merge 'dev' into 'main' and Release Version 2
- I merged the "dev" branch into the "main" branch to finalize version 2 of the CalculatorPlus app.
- Created a release for version 2 of the app.
