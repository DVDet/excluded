[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)
## Introduction
Have you ever wanted to turn off all your lights except for a couple?
Looking around, there have been a number of conversations on the matter

https://community.home-assistant.io/t/automation-turn-off-all-lights-except-x/370571

https://www.reddit.com/r/homeassistant/comments/1hf8vh5/turn_off_all_lights_except_those_with_label/

https://community.home-assistant.io/t/is-there-a-way-to-adress-all-except-to-turn-lights-off/497651

and it keeps going. Many share solutions if you like using templates. Which I'm fine using but it does add to the mantanence cost as you have to figure out what you were thinking when you made that automation a few months ago. Having it in an easaly readable UI makes it so much easier to change or remember in the future. So, I decided to make this my first contribution to Home Assistant. In building this component I realized why it's not in the core system

WARNING: using this component can have unexpected results. For example if you decide to open all curtains, well, garage doors are included in the cover group. If you don't exclude them specificly they will open as well. Which seem like a managable risk. However, if you setup an automation to use one of these actions and months later add a new device, it will now be included in that automation.
