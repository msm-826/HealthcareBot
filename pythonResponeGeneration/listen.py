import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import sys
from main import Main

mn = Main()

# Fetch the service account key JSON file contents
cred = credentials.Certificate('google-services.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://healthcarebot-901fa-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('entries')
ref_child = ref.child('query')



def stream_handler(event):
    resToShow = mn.main(event.data)
    # print(resToShow)
    ref.update({'reply': resToShow})
    if(resToShow[:10] == "contactxyz"):
        time.sleep(1)
        ref.update({ 'reply' : "" })
    # print(event.data)

event_stream = ref_child.listen(stream_handler)

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        event_stream.close()
        sys.exit()