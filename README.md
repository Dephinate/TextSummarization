Text Summarizer  
1) Template creation
Use python to create the folder structure and directories. 
Python code for template creation: template.py

2) Setup and Requirements installation
3) Logging, Utils and Exception Module
4) Project Workflows
5) Training Pipeline
6) Prediciton Pipeline
7) User App creation
8) Final CI/CD Deployment on AWS


Step 1) Create template file. See comments in template.py for more information
Step 2) Create Virtual env. Set requirements.txt. For pytorch please do it separately in order to avoid version issues. I am using pytorch 2.1.2 with cuda 11.4 on my system
Step 3) Create logger in src/TextSummarizer/logging/__init__.py 
Step 4) Create unitilities
Update config.yaml
Update params.yaml
Update entity
Update the configuration manager in src
Update the components
Update the pipeline
Update the main.py
Update the app.py