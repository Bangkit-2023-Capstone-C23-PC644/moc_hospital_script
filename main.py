import requests
import json
import cv2


def main():
    api_url = "YOUR_MAIN_API_URL"

    hospitalID = "YOUR_7_DIGIT_HOSPITAL_ID"
    password = "YOUR PASSWORD"
    todo = {"hospitalID": hospitalID, "password": password}
    headers =  {"Content-Type":"application/json"}
    response = requests.post(api_url, data=json.dumps(todo), headers=headers)
    if(response.status_code != 200):
        print("wrong credentials")
        return
    
    data = response.json()
    token = data['token']
    streamlink = "YOUR_RSTP_LINK"

    cap = cv2.VideoCapture(streamlink)

    while True:
        # Read a frame from the stream
        ret, frame = cap.read()

        # Save the frame as a screenshot
        cv2.imwrite('screenshot.png', frame)

        # Send request to REST API
        url = 'YOUR_ML_ENDPOINT_IN_THE_MAIN_API'
        files = {'file': open('screenshot.png', 'rb')}
        headers1 = {"authorization": token}
        response = requests.post(url, files=files, headers=headers1)

        # Print response
        print(response.text)

       
        cv2.waitKey(600000)  # 600,000 milliseconds = 10 minutes
        
main()