
# Medical Overseer Control (MOC) Hospital Admin Script

This is a python script for hospital admin that is already registered on the MOC database. This script allows you to automatically send image to our ML Serving model and update our database every 10 minutes or you can configure it yourself in the script.

## Run Locally

Clone the project

```bash
  git clone https://github.com/Bangkit-2023-Capstone-C23-PC644/moc_hospital_script.git
```

Go to the project directory

```bash
  cd moc_hospital_script
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the script

```bash
  python main.py
```


## Appendix

Note that for capturing the image this script **requires** a IP Camera and it's RSTP link. And you should **DEFINITELY** change the API_url variable to your MOC main API, the url variable in the while bracket to your MOC main API ml endpoint, and the cv2.waitkey to your desired duration between updates

