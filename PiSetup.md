# Raspberry Pi Setup

## Hardware

- Raspberry Pi Zero W
- Rasbian Lite (headless)

## TODO

- [ ] caps/escape
- [ ] Fix keyboard

## Setup

### SD Card Setup

First, plug the SD card into another computer so you can access the `boot` folder.
Changing things in that folder affect Pi Setup.
Lots of docs here: https://www.raspberrypi.org/documentation/configuration/wireless/headless.md

1. touch `ssh` in `/boot` to enable SSH
2. copy `wpa_supplicant.conf` (contents below) into `/boot`

### Rasbian Setup

```bash
# Built-in config
# 1. Change localization here to en_US UTF8 !
# 2. Then change keyboard layout!
sudo raspi-config 


# swap caps and escape
sudo vim /etc/default/keyboard
# Set XKBOPTIONS=caps:swapescape
sudo reboot

# enable ssh
sudo systemctl enable ssh

# reset password
passwd
sudo reboot

# set up wifi, see file content below
sudo vi /etc/wpa_supplicant/wpa_supplicant.conf
sudo reboot

# Update system
sudo apt update -y
sudo apt upgrade -y
sudo apt dist-upgrade -y
sudo apt autoremove -y

# Install things
sudo apt install vim git ruby -y

echo "gem: --no-document" > ~/.gemrc
sudo gem install bundler
bundle install
```

### `wpa_supplicant.conf`

```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
   ssid="square"
   psk="PASSWORD"
}
```

## ePaper Setup

Homepage / documentation: https://github.com/PiSupply/PaPiRus

`curl -sSL https://pisupp.ly/papiruscode | sudo bash`

`sudo raspi-config` and enable **SPI** and **I2C** Interfaces.

## Cron Setup

Install a mailer `sudo apt install postfix -y`

Manual cron installation `crontab netatmo.cron`