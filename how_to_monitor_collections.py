	cv = client.get_collection_view(
		"<your notion db link>"
	)

	def my_callback(record, difference):
		print("The record's title is now:", record.title)
		print("Here's what was changed:")
		print(difference)

	for block_row in cv.collection.get_rows():
		print("Adding callback for:", block_row.title)
		block_row.add_callback(my_callback)