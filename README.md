# wake-up-light
Wake-up light app and scripts for Raspberry Pi

See instructions at the [blog post](https://rdrn.me/wake-up-light/).

## Installation
Install requirements:
```
sudo apt update
sudo apt upgrade
sudo apt install git
sudo apt install python3-setuptools
sudo apt install python3-flask python3-crontab python3-rpi.gpio
```

Clone this repo:
```
git clone https://github.com/carderne/wake-up-light.git
```

Install [pigpio](http://abyz.me.uk/rpi/pigpio/download.html):
```
wget abyz.me.uk/rpi/pigpio/pigpio.tar
tar xf pigpio.tar
cd PIGPIO
make
sudo make install
```

## Running
Run in development mode:
```
FLASK_DEBUG=1 FLASK_APP=app.py flask run
```

See the blog post (link at the top) for instructions on setting up systemd etc.
