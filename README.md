### MESSAGING TO +12017628866 WILL BE AVAILABLE UNTIL THE HECATRON IS OVER, FEEL FREE TO TEST IT
![example input/output](https://github.com/mirkan1/covid19_sms_info/blob/master/example.PNG?raw=true)

# PROJECT DESCRIPTION
You can get a country's fight against COVID-19; how many confirmed number of cases, recovered patients, deaths, etc. by sending a message:
example input
```
    to: +12017628866
    message: "USA" 
```
example output
```
    In Italy confirmed number of cases are 159516.
        Recovered people are more than 35435.
        3260 people are still in critical condition and 20465 deaths
```
And/Or you can get a news article about COVID-19 by sending message:
example input
```
    to: +12017628866
    message: "news" 
```
example output
```
    *India coronavirus: World's largest postal service turns lifesaver*
    India has the largest postal service in the world - and now it is stepping in to help deliver lifesaving medicines during a countrywide lockdown aimed at tackling the coronavirus pandemic. The BBC's Ayeshea Perera in Delhi reports. Red postal vans are a familiar sight in India. They make thousands of journeys every day, criss-crossing the ...
    from: YAHOO!,
    published on 13-4-2020
    https://news.yahoo.com/india-coronavirus-worlds-largest-postal-230159614.html
```



# USED APIs
    - twilioAPI (twilio.com)
        for SMS messaging
    - rapidAPI (rapidapi.com)
        for information gathering

# INSTALLATION
## 1. open yourself a Twilio account, have your ACCOUNT_SID, AUTH_TOKEN, and PHONE_NUMBER ready, page to find it is 
https://www.twilio.com/console/ 

## 2. if you don't have python3 and/or node.js installed to your computer download and install it. 

Python: 
```
https://www.python.org/downloads/release/python-370/
```

Node.js:
```
https://nodejs.org/en/download/
```

## 3. Install Twilio to your computer:

### WINDOWS
Before we can install, we need to make sure you have Node.js installed (version 10 or above). To see if you have node installed, try running this command:

```
node -v
```
If your system reports v10.0.0 or above, you can skip the next step.

Installing Node.js on Windows
Using the Windows Installer (.msi) is the recommended way to install Node.js on Windows. You can download the installer from the Node.js download page.

Installing Twilio CLI
The CLI is installed with npm (Node Package Manager), which comes with Node.js. To install the CLI run the following command:

```
npm install twilio-cli -g
```
Note the -g option is what installs the command globally so you can run it from anywhere in your system.

Updating
If you already installed the CLI with npm and want to upgrade to the latest version, run:

```
npm install twilio-cli@latest -g
```

### MAX OS X
One of the easiest ways to install the CLI on Mac OS X is to use Homebrew. If you don't already have it installed, visit the Homebrew site for installation instructions and then return here.

Once Homebrew is installed, simply run the following command to install the CLI:

```
brew tap twilio/brew && brew install twilio
```
Updating
If you already installed the CLI with brew and want to upgrade to the latest version, run:

brew upgrade twilio
Warning for Node.js developers
If you have installed Node.js version 10 or higher on your Mac, you can avoid potential Node.js version conflicts by installing the CLI using npm:

```
npm install twilio-cli -g
```
### LINUX
Before we can install, we need to make sure you have Node.js installed (version 10 or above). Even if you already installed Node yourself, the CLI works best when you install it using nvm. Here's how to get nvm installed on most Linux systems:

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
```
Please visit the nvm installation instructions for additional options and troubleshooting steps. Once you have nvm installed, run the following to install and use the most recent LTS release of Node.js:

```
nvm install --lts
```
nvm use <insert version reported from above>
Installing other Twilio CLI prerequisites for Linux
Depending on your distribution, you will need to run one of the following commands:

Debian/Ubuntu: ```sudo apt-get install libsecret-1-dev```
Red Hat-based: sudo yum install libsecret-devel
Arch Linux: sudo pacman -S libsecret
Installing Twilio CLI
The CLI is installed with npm (Node Package Manager), which comes with Node.js. To install the CLI run the following command:

```
npm install twilio-cli -g
```
Note the -g option is what installs the command globally so you can run it from anywhere in your system.

Updating
If you already installed the CLI with npm and want to upgrade to the latest version, run:

```
npm install twilio-cli@latest -g
```

## 4. Clone this repisitory:

on terminal/cmd
```
git clone https://github.com/mirkan1/covid_sms_info.git
```

## 5. Install required python packages on requirements.txt file:

on terminal/cmd
```
pip install -r requirements.txt
```
or
```
pip3 install -r requirements.txt
```

## 6. make adjustment on settings.py:
in order to do this you need to replace ACCOUNT_SID, AUTH_TOKEN, and PHONE_NUMBER on settings.py:
```
ACCOUNT_SID = 'YOUR_ACCOUNT_SID' 
AUTH_TOKEN = 'YOUR_ACCOUNT_TOKEN' 
PHONE_NUMBER = "+YOUR_TWILIO_PHONE_NUMBER"
PORT = "5000"
HOSTNAME = "localhost"
```
after we are done with this we are ready to lunch

## 7. run main.py:

on terminal/cmd
```
python3 .\main.py
```