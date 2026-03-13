import pickle

with open("vector_store/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

print("Total chunks:", len(metadata))

for i in range(10):
    print(metadata[i])