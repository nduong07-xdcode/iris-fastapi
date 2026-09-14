from sklearn import datasets
from sklearn.svm import SVC
import joblib

iris = datasets.load_iris()
X = iris.data
y = iris.target

model = SVC(kernel="linear")
model.fit(X, y)
joblib.dump(model, "svm_model.pkl")
print("Model saved!")

