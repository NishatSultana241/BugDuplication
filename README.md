# SimBug(A similarity-driven approach to detect duplicate bug reports from multimodal bug reports)
**Built by the following authors**
1. Nishat Sultana
2. Jiacheng Shi
3. Jaidyn Vankrik

   ## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Pre-processed Data](#Data)
  ## Installation
Follow these steps to install and set up the project:

### Clone the repository:
```bash
git clone https://github.com/NishatSultana241/BugDuplication.git
```
### Navigate to the project directory:
```bash
cd BugDuplication
```
### Install dependencies:
```bash
pip install -r requirements.txt
```
### Usage:
To run an inference using Llava model with multiple images use the command below,
```
python llava-multi-images.py --model-path liuhaotian/llava-v1.6-vicuna-7b --images /scratch/projects/nishat/BugDuplication/LLaVA/data/Aegis/Aegis_issue_450_image_1.jpg /scratch/projects/nishat/BugDuplication/LLaVA/data/Aegis/Aegis_issue_772_image_1.png --load-4bit --dist-images 150 --concat-strategy grid --temperature 0.7 --max-new-tokens 1024
```
