from src.quantum.q_algorithm import run_quantum_model
from src.utils.data_processing import preprocess_data

# Load and preprocess data
raw_data = "data/raw/seismic_data.csv"
data = preprocess_data(raw_data)

# Run quantum model
results = run_quantum_model(data)

# Output results
print("Prediction Results:", results)
