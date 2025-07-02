import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# CSV file read karo
df = pd.read_csv("traffic_dataset.csv")

# ⚠️ Manually label karo (0 = Normal, 1 = Suspicious)
# Filhal ke liye dummy labels add kar rahe hain
df["Label"] = [0, 1] * (len(df) // 2)  # Alternate normal/suspicious

# Features & labels split karo
X = df[["Protocol"]]
y = df["Label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model train karo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Model save karo
with open("firewall_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as firewall_model.pkl")
