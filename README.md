# Wildkard test automation framework

## Features
- Basic framework that makes it easier to create new tests and support existing ones
- Running on iOS real device
- Using Appium's XCUITest Driver for iOS, which leverages Apple's XCUITest libraries under the hood to facilitate automation the app

## Limitation
- Due to complicated setup of working multiple users and intercepting notifications from several 3rd party apps, tests are configured to be run for only one user with the real phone number
- In the current UI of the app, the option for selecting a league and navigating to `organizing`,
can not be reached by a locator (Xpath or accessibility id) and temporarily, until it is fixed on the Frontend side,
it is implemented with typing by coordinates, that is not a good practice and it depends on device's screen resolution.
Please change the coordinates of this element by inspecting it via Appium inspector:
![](https://i.ibb.co/G3y47g8/Appium-2020-04-18-16-42-40.png)
It should be done after execution of `Environment Setup` topic located below.
Put coordinates into the file `src->features->landing.py-> func click__league_menu`. 
 
## Next steps
- Add script for automatic cleanup the system before each test run (now tests for signing up, teams creating will be skipped if its test data already taken in the system)
- Add support to work with multiple users, intercepting notifications from several apps (iOS Messages and textPlus)
- Add logging of all test steps
- Add HTML report to illustrate tests result and statistics (now it is viewed from console)
- Extend tests coverage (now the coverage is about 40 % of Core scenarios)
- Add API level with actions, which is required for performing preconditions

## Requirements

- A phone device with iOS 9.3 or higher (for tests development iOS 13.4 was used)
- A Mac computer with macOS 10.11 or higher (for tests development macOS Catalina 10.15.4 was used)

## Environment Setup

- Ensure that you have [Homebrew](https://brew.sh) for installing system dependencies
- Ensure that you have Node.js & NPM installed and configured
- Ensure that you have the latest Xcode installed
- Install the Carthage dependency manager: `brew install carthage`

### Install Appium Desktop
- Download and install he latest [appium-desktop](https://github.com/appium/appium-desktop)

### Install Appium Console
- Install via NPM `npm install -g appium`

### Real Device Setup

Find out where your Appium installation is: `which appium`
Ideally Appium installed using npm will be at this location `/usr/local/bin/appium`

Open a terminal and go to
`cd /usr/local/lib/node_modules/appium/node_modules/appium-webdriveragent/`
run the following in order to set the project up
```
mkdir -p Resources/WebDriverAgent.bundle
./Scripts/bootstrap.sh -d
```
The log should look something like this
![](https://miro.medium.com/max/1400/1*iLp7y7um4J24PFfZCrYQbg.png)

In terminal type the following to open the WebDriverAgent folder
`open /usr/local/lib/node_modules/appium/node_modules/appium-webdriveragent/`
![](https://miro.medium.com/max/952/1*11PEgk4uh9s0gzfd7FM2iQ.png)

Open `WebDriverAgent.xcodeproj` in Xcode.
Make sure to add your apple developer account id in the accounts section. You can tap on the ‘+’ button to add your apple id just in case (Xcode Preferences - Accounts).

Now we have to code sign the `WebDriverAgentLib` and `WebDriverAgentRunner`.
Select `WebDriverAgentLib` target and at the signing section check Automatically manage signing. Xcode will be able to create a provisioning profile for the `WebDriverAgentLib` target most of the time.
![](https://miro.medium.com/max/2000/1*iwK8HzxV1ASs-Cx_bO9G3w.png)

Select `WebDriverAgentRunner` target and at the signing section check Automatically manage signing. Xcode will fail to create a provisioning profile for the `WebDriverAgentRunner` target.
![](https://miro.medium.com/max/2000/1*stYodCe35WbFxx2uzwvMlg.png)

We have to manually change the bundle id for the target. To do that go to the “Build Settings” tab, and change the “Product Bundle Identifier” from com.facebook.WebDriverAgentRunner to something that Xcode will accept. Change com.facebook.WebDriverAgentRunner to com.<SomeUniqueName>.WebDriverAgentRunner.
![](https://miro.medium.com/max/2000/1*av0uM_kYGuB1UsUHsFDc3w.png)
For example
![](https://miro.medium.com/max/1400/1*ipajhbbyZXZXi02GqTAvHw.png)

Now go back to the “General” tab you should see that the Xcode created a provisioning profile for the `WebDriverAgentRunner` target.
![](https://miro.medium.com/max/1400/1*yYLXI4t2ASpCAChkCS7OmA.png)

Now we need to build the project to verify that everything works.Connect your iPhone using a USB cable. Copy the device identifier from Xcode. 
Steps: check the screenshot.
![](https://miro.medium.com/max/2000/1*m1axAbEtb1av7-OrLzCX2g.png)

Run
`xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -allowProvisioningUpdates -destination ‘id=<udid>’ test`

Right now you are probably going to see the test getting failed and If you look at your phone you will see the WebDriverAgentRunner app installed. If that the case we are almost there.
![](https://miro.medium.com/max/1220/1*AtXRDnv0sdHOUeLlSAEOpw.png)
Test Failed!
![](https://miro.medium.com/max/1400/1*oBCkwwuQD1OAxJAokpZOUA.png)
WebDriverAgentRunner app

We need to trust the configuration profile on your phone.
Go to Settings > General > Profiles and Device Management > Trust the configuration.
![](https://miro.medium.com/max/1400/1*h8FSAHbSX_GrGYSzkuW5eQ.png)

Build it again. If you see something like this you are good.
![](https://miro.medium.com/max/1400/1*82mW9RKIrna-0ny2mQGxRA.png)
At this point, you may suspend the test by pressing ‘control + Z’

During the xcodebuild, If you get “unable to communicate with the device” error, please disconnect, reboot and reconnect the device and try once again.

Make sure to note your xcodeOrgId
![](https://miro.medium.com/max/1400/1*4cbSy07-nbfU7g4xQwN3GA.png)

The section above (Environment Setup) was filled on the basic of tutorials:
- [http://appium.io/docs/en/drivers/ios-xcuitest](http://appium.io/docs/en/drivers/ios-xcuitest/)
- [http://appium.io/docs/en/drivers/ios-xcuitest-real-devices](http://appium.io/docs/en/drivers/ios-xcuitest-real-devices/)
- [https://medium.com](https://medium.com/@yash3x/appium-xcuitest-on-real-ios-devices-bd1ebe0dea55)


## Test framework setup

Ensure that you have the latest version of this repository downloaded and you are in the directory `wildkard-mobile-automation`

### Install dependencies

- Ensure that you have `Python3` with `pip` installed
- Install `pipenv` packaging manager: `pip3 install pipenv`
- Install the required packages: `pipenv update`

### Fill the config

Open the config file `config.json` in your favourite editor and replace the fields with your values.

### Run tests

`pipenv run pytest vvs`

See results in the console.
