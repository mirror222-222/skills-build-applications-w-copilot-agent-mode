from pymongo import MongoClient

def test_mongo_connection():
    try:
        client = MongoClient('localhost', 27017)
        print("Connected to MongoDB successfully.")
        db = client['octofit_db']

        # Test inserting a document
        test_collection = db['test_collection']
        test_document = {"name": "Test User", "email": "test@example.com"}
        result = test_collection.insert_one(test_document)
        print("Document inserted with ID:", result.inserted_id)

        # Verify the document was inserted
        inserted_document = test_collection.find_one({"_id": result.inserted_id})
        print("Inserted Document:", inserted_document)

        # Clean up
        test_collection.delete_one({"_id": result.inserted_id})
        print("Test document deleted successfully.")
    except Exception as e:
        print("An error occurred:", e)

test_mongo_connection()
