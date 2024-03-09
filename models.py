import pickle
def revertlabel(x: int) -> str:
    if x:
        return "Not Spam"
    return "Spam"

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)
    
with open('models/vectorizer.pkl', 'rb') as F:
    countVector = pickle.load(F)

def get_model_output(sms: str) -> str:
    return revertlabel(model.predict(countVector.transform([sms])))

def main():
    print(get_model_output("Win 1000 dollars today for free"))

if __name__ == "__main__":
    main()