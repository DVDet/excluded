[![Project Maintenance][maintenance-shield]][user_profile]
[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]
[![GitHub Activity][commits-shield]][commits]
[![Downloads][download-latest-shield]]()
[![HACS Installs][hacs-installs-shield]]()
## Introduction
Have you ever wanted to turn off all your lights except for a couple?
Looking around, there have been a number of conversations on the matter

https://community.home-assistant.io/t/automation-turn-off-all-lights-except-x/370571

https://www.reddit.com/r/homeassistant/comments/1hf8vh5/turn_off_all_lights_except_those_with_label/

https://community.home-assistant.io/t/is-there-a-way-to-adress-all-except-to-turn-lights-off/497651

and it keeps going. Many share solutions if you like using templates. Which I'm fine using but it does add to the maintenance cost as you have to figure out what you were thinking when you made that automation a few months ago. Having it in an easily readable UI makes it so much easier to change or remember in the future. So, I decided to make this my first contribution to Home Assistant. In building this component I realized why it's not in the core system

$${\color{red}WARNING}$$: using this component can have unexpected results. For example if you decide to open all curtains, well, garage doors are included in the cover group. If you don't exclude them specifically they will open as well. Which seems like a manageable risk if you add them to the exclusions. However, if you setup an automation to use one of these actions and months later add a new device, it will now be included in that automation.

### Current status
I don't anticipate much change to the core logic as I believe it to be straight forward and robust. Unless someone points out something better or a nice feature (unlikely on the feature as it should stay simple) I will leave it alone. I do plan to complete all the base domains....eventually. Please let me know of a domain you would like added. The process is somewhat tedious, so it may take a bit before I get around to it. see list below of currently supported domains.

#### Currently supported domains
- Fan
- Light

## Installation

### Step 1: Download files

#### Option 1: Via HACS

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=dvdet&repository=excluded&category=integration)

Make sure you have HACS installed. If you don't, run `wget -O - https://get.hacs.xyz | bash -` in HA.  
Choose Integrations under HACS. Click the '+' button on the bottom of the page, search for "scheduler component", choose it, and click install in HACS.

#### Option 2: Manual
Clone this repository or download the source code as a zip file and add/merge the `custom_components/` folder with its contents in your configuration directory.


### Step 2: Restart HA
In order for the newly added integration to be loaded, HA needs to be restarted.

### Step 3: Add integration to HA 
In HA, go to Configuration > Integrations.
In the bottom right corner, click on the big button with a '+'.

If the component is properly installed, you should be able to find 'Excluded' in the list. You might need to clear you browser cache for the integration to show up.

## Usage

Once the integration is installed you can test it out by going to developer tools -> actions and type in "excluded". You should see all the actions currently available. 
<img width="1473" height="919" alt="image" src="https://github.com/user-attachments/assets/bd2bc819-3dce-46f6-befc-9ee268540aba" />

### Turn off all Lights except for the Bed light

1. In the input box for actions search for "excluded.turn_off_lights"
2. for targets, select "bed light"
3. click perform ation
<img width="1437" height="521" alt="image" src="https://github.com/user-attachments/assets/092e0820-a09b-4aca-8a32-d2c3e9d399f4" />


