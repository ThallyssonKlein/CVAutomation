class MyDescriptionMonitor:
    def __init__(self, data, client):
        self.privateEnglishCVDescriptionBlockId = data.get_item('privateEnglishCVDescriptionBlockId')
        self.privatePortugueseCVDescriptionBlockId = data.get_item('privatePortugueseDescription')
        self.publicEnglishCVDescriptionBlockId = data.get_item('publicEnglishCVDescriptionBlockId')
        self.publicPortugueseCVDescriptionBlockId = data.get_item('publicPortugueseDescription')

        self.block1 = client.get_block(self.privateEnglishCVDescriptionBlockId)
        self.block1.add_callback(self.callback1)
        self.block2 = client.get_block(self.privatePortugueseCVDescriptionBlockId)
        self.add_callback(self.callback2)
        self.block3 = client.get_block(self.publicEnglishCVDescriptionBlockId)
        self.block3.add_callback(self.callback3)
        self.block4 = client.get_block(self.publicPortugueseCVDescriptionBlockId)
        self.block4.add_callback(self.callback4)
    
    def callback1(record, difference):
		print("The record's title is now:", record.title)
		print("Here's what was changed:")
		print(difference)

    def callback2(record, difference):
		print("The record's title is now:", record.title)
		print("Here's what was changed:")
		print(difference)
    
    def callback3(record, difference):
		print("The record's title is now:", record.title)
		print("Here's what was changed:")
		print(difference)
    
    def callback4(record, difference):
		print("The record's title is now:", record.title)
		print("Here's what was changed:")
		print(difference)