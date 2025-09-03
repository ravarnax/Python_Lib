import numpy as np
import matplotlib.pyplot as plt

# Create Data
np.random.seed(42)
data = np.random.randint(40, 100, size=(10,5)) # 10 students, 5 students

print("Student Marks (10 students x 5 subjects):")
print(data)

# Define functions
def show_statistics(choice):
    if choice == '1':
        print("\n Subject-wise mean: ", np.mean(data, axis=0))
    elif choice == '2':
        print("\n Subject-wise median: ", np.median(data, axis=0))
    elif choice == '3':
        print("\n Subject-wise variance: ", np.var(data, axis=0))
    elif choice == '4':
        print("\n Subject-wise Std Deviation: ", np.std(data, axis=0))
    elif choice == '5':
        p25, p50, p75 = np.percentile(data, [25,50,75])
        print(f'\n Percentiles of ALl marks -> 25th: {p25}, 50th: {p50}, 75th: {p75}')
    elif choice == '6':
        print("\n Correlation Matrix (Subjects vs Subjects):")
    elif choice == '7':
        plot_data()
    else:
        print("Invalid choice, try again")
        
def plot_data():
    plt.figure(figsize=(8,5))
    plt.boxplot(data,labels=[f"Sub {i+1}" for i in range(data.shape[1])])
    plt.title("Distribution of Marks by Subject")
    plt.ylabel("Marks")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()
    
# User Menu
while True:
    print("\n===== 📊 Statistics Dashboard =====")
    print("1. Mean")
    print("2. Median")
    print("3. Variance")
    print("4. Standard Deviation")
    print("5. Percentiles (25, 50, 75)")
    print("6. Correlation Matrix")
    print("7. Plot Marks (Boxplot)")
    print("0. Exit")

    choice = input("👉 Enter your choice: ")
    if choice == "0":
        print("👋 Exiting Dashboard. Goodbye!")
        break
    else:
        show_statistics(choice)
