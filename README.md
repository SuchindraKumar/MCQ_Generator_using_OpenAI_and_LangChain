# How to Run ?

### STEPS:

Clone the Repository

```bash
git clone https://github.com/SuchindraKumar/MCQ_Generator_using_OpenAI_and_LangChain.git
```
### STEP 01- Create a Conda Environment after Opening the Repository

```bash
conda create -p env python=3.8 -y
```

```bash
source activate env

```


### STEP 02- Install the Requirements
```bash
pip install -r requirements.txt
```



# Finally Run the following Command
```bash

streamlit run StreamlitAPP.py
```

# Now,

```bash
Open Up Your local-host and Port
```

# For AWS Deployment Follow the Steps

### 1.first login to the AWS: https://aws.amazon.com/console/

### 2.Search about the EC2

### 3.You need to config the UBUNTU Machine

### 4.Launch the instance

### 5.Update the machine Run the Following Commmands:

```
sudo apt update
```
```
sudo apt-get update
```
```
sudo apt upgrade -y
```
```
sudo apt install git curl unzip tar make sudo vim wget -y
```
```
git clone "Your-Repository"
```
```
sudo apt install python3-pip

```
For Checking All the File Present In Our Machine
```
ls
```
Enter In Your Project Directory(MCQ_Generator_using_OpenAI_and_LangChain):
```
cd MCQ_Generator_using_OpenAI_and_LangChain
```

```
pip3 install -r requirements.txt
```


### If You want to Add OpenAI API Key:

1. create .env file in your server
 ```
   touch .env
   ```
2.For Opening .env File:
```
 vi .env
```
3. Press insert :
```
 Copy your OpenAI API key and paste it there
```

5. Press ***Esc*** and then ***:wq*** and Hit Enter

6. Go with Security and Add the Inbound Rule:
 ```  
 Add the port 8501
```
For Run The App:
 ```
python3 -m streamlit run StreamlitAPP.py
```
