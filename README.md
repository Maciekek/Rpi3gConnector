
# Rraspberry Pi 3g connector

Simply tool to automatically connect and reconnect with 3g network.



### Modem
Huawei  E1750

## How to run it?
Clone repo (or download) this repo to `Rpi3gConnector` dir in `/home/pi`.

```
	/home/pi/Rpi3gConnector
```


Start:

```sh
    sudo python connect3g.py
```

## Description
Program is written in Python. Program checks if connection is active by ping some www page. If response of the request is succesfully, program will sleep for a some time. After specific time, program will check again if connection is active. If response of the request is NOT succesfully, program will try to reconnect, and so on. 


There is also automatically login to hamachi network. Remember to configure hamachi on your own on your machine. Commands like: `hamachi` and `hamachi login` must be available. 



## Autostart after reboot 
Program can start automatically after system start.


> ** Do this steps:**
> - Copy content of the folder ```CopyToinit.d``` to `/etc/init.d`

    Command: cp CopyToinit.d/connect3g /etc/init.d

> - Add script to `update-rc`
    
    Command: sudo update-rc.d connect3g defaults

> - To remove it from autostart

    Command: sudo update-rc.d connect3g remove




### How I test it 

>- Connection succesfully 
>- Eject sim card
>- Eject modem 
>- Insert sim cart
>- Insert 3g modem to Rpi
>- Wait until reconnect


