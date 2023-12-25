import tkinter as tk
import requests

def verify_license(license_code):
    api_url = "https://api.mayar.id/saas/v1/license/verify"
    # response = requests.get(api_url)

    data = {'licenseCode': license_code}
    headers = {
        'Authorization': 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIzNDhlMDgzZC0zMTVhLTRlNWMtOTZiMS01YTJhOThjNDg0MTMiLCJhY2NvdW50SWQiOiJiZTMwNWVhNC01ZmUxLTRiYjktYTVjOC02YmMxZDBiZmQyNzkiLCJjcmVhdGVkQXQiOiIxNzAzNTEyMTI1OTY3Iiwicm9sZSI6ImRldmVsb3BlciIsInN1YiI6ImFsZG9kd2llckBnbWFpbC5jb20iLCJuYW1lIjoiTWFsbyBHdXN0byIsImxpbmsiOiJtaWxpZ2lzdGkiLCJpc1NlbGZEb21haW4iOmZhbHNlLCJpYXQiOjE3MDM1MTIxMjV9.J-TTl7fq7N9D4BZUxh9wryCzF-mab6hQKv7-iZXGVBZD2vGfwj1x58CtB8-WaOYT3rgXWISO6mmqJ9DPvLY3ycMP4bfcWEjQzkFHEH4V9ROXViSyEBb_VcuKpbbeDDTQRZ8rWv7Zu6OWBeSFB3Uw5vSobx7GVaQ7IIndk3xFCSrZ6vLXMVMw1rPLjoCf7BaSV86YviZ3CF3EOTcDsPENVxxGqhwfoXcfVoLuRI_ije6yNFBoAE3ULvsSqS-jKVlLvKy1FSqCN_I5sCsShvj0weTJeWASPyXQnfGYQiA0NkuKeAyGLJLrTzMMj4f2qoijlpmWUO9emNv0-L0ADzA9bg'
    }

    response = requests.post(api_url, data=data, headers=headers)

    print(response.status_code)

    if response.status_code == 200:
        try:
            print(response.json())
            license_info = response.json().get("licenseCode")
            if license_info and license_info.get("status") == "ACTIVE":
                return True
        except ValueError:
            print("Response is not valid JSON.")
    return False

def open_application():
    license_code = entry.get()
    if verify_license(license_code):
        status_label.config(text="Application opened successfully!", fg="green")
    else:
        status_label.config(text="Invalid license code. Application cannot be opened.", fg="red")  

root = tk.Tk()
root.title("License Verification")
root.geometry("300x150")

label = tk.Label(root, text="Enter License Code:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Open Application", command=open_application)
button.pack()

status_label = tk.Label(root, text="", font=('Helvetica', 10))
status_label.pack()

root.mainloop()