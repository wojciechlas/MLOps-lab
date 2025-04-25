from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib


def load_data():
    """Load the Iris dataset"""
    data = load_iris(as_frame=True)
    return data


def train_model(data):
    """Train a simple classification model"""
    # Split the data into training and testing sets
    X = data.data
    y = data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train a Logistic Regression model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    return model


def save_model(model, filename="model.pkl"):
    """Save the trained model to a file"""
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")


# Train the model and save it
if __name__ == "__main__":
    data = load_data()
    model = train_model(data)
    save_model(model)
