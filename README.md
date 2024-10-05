# pywaveshare - Waveshare GSM/GPRS/GNSS HAT Controller for Raspberry Pi

With pywaveshare, you can easily use the functionality of the [Waveshare GSM/GPRS/GNSS HAT for Raspberry Pi](https://www.waveshare.com/gsm-gprs-gnss-hat.htm). On this module a SIM868 Controller is doing the job to connect your Raspberry Pi with the world just by using a sim card.

## Changelog
[See this document.](CHANGELOG.md)

## Overview
pywaveshare was written for Python 3. It provides the following features

- Non-blocking receiving and sending SMS in background
- Non-blocking calling
- Non-blocking refreshing of actual GPS position
- Non-blocking URL Call and receiving of response

## Quickstart

In the following paragraphs, I am going to describe how you can get and use pywaveshare for your own projects.

### Download

To download pywaveshare, either fork this github repo or simply use pypi via pip.

```sh
$ python3 -m pip install -U pywaveshare
```

### Setup

* Install your sim card in your module, connect the GSM and the GPS antennas and mount the module on the pin headers of your Raspberry Pi. Make sure, that you **do not** need to enter Pin Code to use your card. Pin Codes are not supported yet.

* Enable the UART Interface in your Raspberry Pi

    - Start raspi-config: `sudo raspi-config`.
    - Select option 5 - interfacing options.
    - Select option P6 - serial.
    - At the prompt `Would you like a login shell to be accessible over serial?` answer 'No'
    - At the prompt `Would you like the serial port hardware to be enabled?` answer 'Yes'
    - Exit raspi-config and reboot the Pi for changes to take effect.

### Usage

1. Import gsmHat to your project

```python
from pywaveshare.boards.sim868 import GSMHat, SMS, GPS
```

2. Create an instance

```python
gsm = GSMHat('/dev/ttyS0', 115200)
```

3. Check, if new SMS are available in your main loop

```python
# Check, if new SMS is available
if gsm.SMS_available() > 0:
    # Get new SMS
    newSMS = gsm.SMS_read()
    # Do something with it
```

4. Do something with your newly received SMS

```python
# Get new SMS
newSMS = gsm.SMS_read()

print('Got new SMS from number %s' % newSMS.Sender)
print('It was received at %s' % newSMS.Date)
print('The message is: %s' % newSMS.Message)
```

5. You can also write SMS

```python
Number = '+491601234567'
Message = 'Hello mobile world'

# Send SMS
gsm.SMS_write(Number, Message)
```

6. Or you can call a number

```python
Number = '+491601234567'
gsm.Call(Number)        # This call hangs up automatically after 15 seconds
time.sleep(10)          # Wait 10 seconds ...
gsm.HangUp()            # Or you can HangUp by yourself earlier
gsm.Call(Number, 60)    # Or lets change the timeout to 60 seconds. This call hangs up automatically after 60 seconds
```

7. Lets see, where your Raspberry Pi (in a car or on a motocycle or on a cat?) is positioned on earth

```python
# Get actual GPS position
GPSObj = gsm.GetActualGPS()

# Lets print some values
print('GNSS_status: %s' % str(GPSObj.GNSS_status))
print('Fix_status: %s' % str(GPSObj.Fix_status))
print('UTC: %s' % str(GPSObj.UTC))
print('Latitude: %s' % str(GPSObj.Latitude))
print('Longitude: %s' % str(GPSObj.Longitude))
print('Altitude: %s' % str(GPSObj.Altitude))
print('Speed: %s' % str(GPSObj.Speed))
print('Course: %s' % str(GPSObj.Course))
print('HDOP: %s' % str(GPSObj.HDOP))
print('PDOP: %s' % str(GPSObj.PDOP))
print('VDOP: %s' % str(GPSObj.VDOP))
print('GPS_satellites: %s' % str(GPSObj.GPS_satellites))
print('GNSS_satellites: %s' % str(GPSObj.GNSS_satellites))
print('Signal: %s' % str(GPSObj.Signal))
```

8. Calculate the distance between two Points on Earth

```python
GPSObj1 = GPS()                 # You can also use gsm.GetActualGPS() to get an GPS object
GPSObj1.Latitude = 52.266949    # Location of Braunschweig, Germany
GPSObj1.Longitude = 10.524822

GPSObj2 = GPS()
GPSObj2.Latitude = 36.720005    # Location of Manavgat, Turkey
GPSObj2.Longitude = 31.546094

print('Distance from Braunschweig to Manavgat in metres:')
print(GPS.CalculateDeltaP(GPSObj1, GPSObj2))        # this will print 2384660.7 metres
```

9. Call URL to send some data

```python
# Init gsmHat
gsm = GSMHat('/dev/ttyS0', 115200)

# Set the APN Connection data. You will get this from your provider
# e.g. German Provider 'Congstar'
gsm.SetGPRSconnection('internet.telekom', 'congstar', 'cs')

# Get actual GPS position
GPSObj = gsm.GetActualGPS()

# Build url string with data
url = 'www.someserver.de/myscript.php'
url += '?time='+str(int(GPSObj.UTC.timestamp()))
url += '&lat='+str(GPSObj.Latitude)
url += '&lon='+str(GPSObj.Longitude)
url += '&alt='+str(GPSObj.Altitude)

gsm.CallUrl(url)    # Send actual position to a webserver
```

10. Get the Response from a previous URL call

```python
# Check, if new Response Data is available
if gsm.UrlResponse_available() > 0:
    # Read the Response
    newResponse = gsm.UrlResponse_read()
    # Do something with it
```

## What will come in the future?
- More options to configure the module (e.g. using sim cards with pin code)

## On which platform was pywaveshare developed and tested?

### Hardware:
- [Raspberry Pi 4, Model B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
- [GSM/GPRS/GNSS/Bluetooth HAT for Raspberry Pi](https://www.waveshare.com/gsm-gprs-gnss-hat.htm), **later version that allows to power on/off the module by controlling GPIO 4**

### Software:
* Raspbian (Codename: buster, Release: 10)
* Kernel: Linux 5.4.51-v7l+
* Python: 3.12


## License
[See this document.](LICENSE)
