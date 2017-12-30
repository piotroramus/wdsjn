from preprocessing import load_preprocessed_documents

input_file = 'resources/pap.txt'

# preprocess_documents(input_file)
docs = load_preprocessed_documents()
print(docs[0])
