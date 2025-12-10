import requests


class IRCTC:
    def __init__(self):
        
        user=input('''
Welcome to IRCTC WEBSITE ! Hou would you like to praceed ?
              1. Enter 1 to check live tarin status.
              2. Enter 2 to check PNR status.
              3. Enter 3 to check train schedule.
            ''')
        if user=='1':
            print('live train status')
        elif user=='2':
            print('PNR status')
        else:
            self.train_Schedule()    
    def train_Schedule(self):
        train_No=input('Enter the train no')   
        self.fetch_data(train_No)     

    def fetch_data(self,train_No) :
        data=requests.get('https://indianrailapi.com/api/v2/TrainSchedule/apikey/yourapikey/TrainNumber/{}'.format(train_No))   
        data=data.json()
        print(data)

obj=IRCTC()        
