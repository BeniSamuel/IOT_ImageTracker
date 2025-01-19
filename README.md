# Assignment 001

## Table of Contents
1. [Introduction](#introduction)
2. [How to Use the Repository](#how-to-use-the-repository)
   - [Cloning the Repository](#cloning-the-repository)
   - [Forking the Repository](#forking-the-repository)
3. [How the Code Works](#how-the-code-works)
4. [Made With Love](#made-with-love)

---

## Introduction
This repository contains a Python script designed to automate the following tasks:
- Monitor a folder where a camera regularly saves captured pictures.
- Automatically upload each picture to the internet using the `curl` command after a 30-second interval.
- Once a picture is successfully uploaded, move it to another folder named `uploaded` to prevent redundancy.

---

## How to Use the Repository

### Cloning the Repository
To clone this repository, you will need Git installed on your computer. Follow these steps:
1. Copy the repository URL from GitHub.
2. Open your terminal or command prompt and run the following command:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of this repository.
3. Navigate to the repository directory:
   ```bash
   cd <repository-folder>
   ```

### Forking the Repository
Forking a repository allows you to create your own copy of someone else’s repository. This is useful if you want to make changes or experiment without affecting the original project. Here's how to fork this repository:
1. Click the **Fork** button at the top right corner of the repository page on GitHub.
2. This will create a copy of the repository in your GitHub account.
3. You can clone your forked repository to your local machine using the cloning instructions above.

---

## How the Code Works
1. **Folder Setup**:
   - The script monitors a folder named `images`. This is where the camera stores captured images.
   - The script uses the `uploaded` folder to store images that have been successfully uploaded to avoid re-uploading them.

2. **Image Uploading**:
   - The script uses the `curl` command to upload images to a predefined URL. Each image is sent with the key attribute `imageFile`.

3. **Automation**:
   - Every 30 seconds, the script checks the `images` folder for new files.
   - If an image is found, it is uploaded using `curl`. Upon successful upload, the image is moved to the `uploaded` folder.

4. **Requirements**:
   - Ensure you have Python installed on your system.
   - The `curl` tool must be installed and accessible from the command line.

---

## Made With Love
This project was made with love by **Beni Samuel**. ❤️
