import http.client
import json
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

conn = http.client.HTTPSConnection("api.elevateai.com")
payload = json.dumps({
  "type": "audio",
  "languageTag": "en-us",
  "vertical": "default",
  "audioTranscriptionMode": "highAccuracy",
  "originalFileName": "audio.wav",
  "includeAiResults": True,
})
headers = {
  'Content-Type': 'application/json',
  'X-API-Token': ''
}
conn.request("POST", "/v1/interactions", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))