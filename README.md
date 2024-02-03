# How to Run ?

### STEPS:

Clone the Repository

```bash
git clone https://github.com/SuchindraKumar/Text-Summarizer-Project.git
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

### 2.search about the EC2

### 3.you need to config the UBUNTU Machine

### 4.launch the instance

### 5.update the machine and  Run the Following Commmands:

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
git clone "Your-repository"
```
```
sudo apt install python3-pip
```
```
pip3 install -r requirements.txt
```
```
python3 -m streamlit run StreamlitAPP.py
```

### If You want to Add OpenAI API Key:

1. create .env file in your server touch .env
2. vi .env #press insert #copy your api key and paste it there #press and then :wq and hit enter
3. go with security and add the inbound rule add the port 8501
