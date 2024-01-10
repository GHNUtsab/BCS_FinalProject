import tkinter as tk
from tkinter import messagebox
import pickle

def predict_url():
    url = url_entry.get()
    try:
        prediction = loaded_model.predict([url])
        probability = loaded_model.predict_proba([url])
        
        # Displaying the prediction
        if prediction[0] == 'bad':
            messagebox.showinfo("Prediction", f"The URL is predicted to be BAD with a probability of {probability[0][0]*100:.2f}%")
        else:
            messagebox.showinfo("Prediction", f"The URL is predicted to be GOOD with a probability of {probability[0][1]*100:.2f}%")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Load the model
with open('phishing.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Create the main window
root = tk.Tk()
root.title("URL Classifier")

# Create a label, entry widget, and button
tk.Label(root, text="Enter URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()
predict_button = tk.Button(root, text="Predict", command=predict_url)
predict_button.pack()

# Run the application
root.mainloop()
