import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def load_model(filename="model.pkl"):
    """Load the trained model from a file"""
    model = joblib.load(filename)
    return model


def predict(model: LogisticRegression, input_data: dict):
    """Make predictions using the trained model"""
    iris = load_iris()
    target_names = iris.target_names

    input = [
        [
            input_data["sepal_length"],
            input_data["sepal_width"],
            input_data["petal_length"],
            input_data["petal_width"],
        ]
    ]
    prediction = model.predict(input)
    predicted_class = target_names[prediction][0]
    return predicted_class


# Example usage
if __name__ == "__main__":
    # Load the model
    model = load_model()

    # Example input data (replace with actual input)
    example_input = [[5.1, 3.5, 1.4, 0.2]]  # Example for Iris dataset

    # Make predictions
    predicted_class = predict(model, example_input)
    print(f"Predicted class: {predicted_class}")
