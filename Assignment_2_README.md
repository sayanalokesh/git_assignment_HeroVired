# Graded Assignment on Git and GitHub – Assignment 2

# [GitHub Link](https://github.com/sayanalokesh/git_assignment_HeroVired)

# Project description

Git LFS (Large File Storage) is a Git extension that allows you to store large binary files, such as images, videos, and audio files, in a separate repository. This can help to improve the performance of your Git repository, as large files can take up a lot of space and time to track.

## Step by step process
1. [Initialize Git LFS in the repository](#initialize-git-lfs-in-the-repository)
2. [Checking out to branch](#checking-out-to-branch)
3. [Install Git LFS](#install-git-lfs)
4. [Placing the 200MB file to local repo](#placing-the-200mb-file-to-local-repo)
5. [Tracking the 200MB.bin file](#tracking-the-200mbbin-file)
6. [Adding and committing to Git](#adding-and-committing-to-git)
7. [Pushing the file to Remote Repo](#pushing-the-file-to-remote-repo)
8. [Clone the repository on another machine to verify that the binary files are downloaded correctly](#clone-the-repository-on-another-machine-to-verify-that-the-binary-files-are-downloaded-correctly)

## Initialize Git LFS in the repository
Create a new branch with the name lfs.

      git branch lfs

## Checking out to branch
Checkout to lfs.
      
      git checkout lfs

## Install Git LFS
Install Git LFS by running the following command after checking out to the `lfs` branch.
      
      git lfs install

## Placing the 200MB file to local repo
Place your large binary file (larger than 200 MB) in the repository folder. Let's say the file is named 200MB PDF File-lfs.pdf

## Tracking the 200MB.bin file
Once the file is added, we need to track whether it is visible or not. For that we need to use the below command.

      git lfs track "200MB PDF File-lfs.pdf

## Adding and committing to Git
Since we have added the file to the assignment folder, we need to commit the changes by adding it to Git.

      git add 200MB PDF File-lfs.pdf
      git commit -m “ADD: Add large binary file using Git LFS

## Pushing the file to Remote Repo
Now we push the file to GitHub
      
      git push origin lfs
Now the large binary file 200MB PDF File-lfs.pdf should be tracked by Git LFS and uploaded to the remote repository as we named the branch with lfs.

## Clone the repository on another machine to verify that the binary files are downloaded correctly
Now we need to clone the repo on other machine and to verify that the binary files are downloaded correctly

      git clone git@github.com:sayanalokesh/git_assignment_HeroVired.git

Switch to the 'lfs' branch on the new machine

      cd git_assignment_HeroVired
      git checkout lfs
Check if the 200MB PDF File-lfs.pdf is available in the repository and has been downloaded correctly using Git LFS.

If we want to check that the LFS files are fully downloaded, we can use the following command to pull the LFS files

      git lfs pull

After that we need to track the file.

      git lfs track "200MB PDF File-lfs.pdf "