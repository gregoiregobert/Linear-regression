import pickle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def normalize(x):
    return (x - np.mean(x)) / np.std(x)

def loadData(fichier):
    """Charge le fichier de données contenant les kilométrages et les price."""
    data = np.loadtxt(fichier, delimiter=',', skiprows=1)
    mileage = data[:, 0]
    kilometrage_norm = normalize(mileage)
    price = data[:, 1]
    prix_norm = normalize(price)
    return kilometrage_norm, mileage, prix_norm, price

def compute_cost(mileage, price, theta0, theta1):
    m = len(mileage)
    prediction = theta0 + theta1 * mileage
    return (1 / (2 * m)) * np.sum((prediction - price) ** 2)

def trainModel(mileage, price, learning_rate, iterations):
    """Effectue la régression linéaire pour ajuster theta0 et theta1."""
    m = len(mileage)
    theta0 = 0
    theta1 = 0
    history = []
    theta_history = []

    for _ in range(iterations):
        prediction = theta0 + theta1 * mileage
        erreur = prediction - price
        tmp_theta0 = theta0 - learning_rate * (1 / m) * np.sum(erreur)
        tmp_theta1 = theta1 - learning_rate * (1 / m) * np.sum(erreur * mileage)
       
        theta0, theta1 = tmp_theta0, tmp_theta1 # Update parameters

        cost = compute_cost(mileage, price, theta0, theta1)
        history.append(cost)
        theta_history.append((theta0, theta1))
    
    return theta0, theta1, history, theta_history

def saveModel(theta0, theta1, prix_mean, prix_std, kilometrage_mean, kilometrage_std):
    """Sauvegarde les paramètres theta0 et theta1 dans un fichier."""
    with open("model_parameters.pkl", "wb") as f:
        pickle.dump((theta0, theta1, prix_mean, prix_std, kilometrage_mean, kilometrage_std), f)

def std_mean(price):
    x_mean = np.mean(price)
    x_std = np.std(price)
    return x_mean, x_std

def show_cost_function(history):
    """Affiche simplement la courbe statique de l'évolution du coût (MSE)."""
    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(len(history)), history, color='blue', lw=2)
    plt.title("Évolution de la fonction de coût")
    plt.xlabel("Itérations")
    plt.ylabel("Coût (MSE)")
    plt.grid(True)
    plt.show()


# Fonction d'animation du model
def animate_model(mileage, price, theta_history):
    fig, ax = plt.subplots()
    ax.scatter(mileage, price, color='blue', label='Données')
    line, = ax.plot([], [], color='red', lw=2, label='Modèle')
    ax.set_xlim(min(mileage), max(mileage))
    ax.set_ylim(min(price), max(price))
    ax.set_title("Apprentissage du modèle")
    ax.set_xlabel("Kilométrage (normalisé)")
    ax.set_ylabel("Prix (normalisé)")
    ax.legend()
    ax.grid(True)

    x_vals = np.linspace(min(mileage), max(mileage), 100)

    def update(frame):
        theta0, theta1 = theta_history[frame]
        y_vals = theta0 + theta1 * x_vals
        line.set_data(x_vals, y_vals)
        return line,

    ani = FuncAnimation(fig, update, frames=len(theta_history), interval=200, blit=True)
    plt.show()

def main():
    kilometrage_norm, mileage, prix_norm, price = loadData("data.csv")
    learning_rate = 0.3
    iterations = 15

    theta0, theta1, history, theta_history = trainModel(kilometrage_norm, prix_norm, learning_rate, iterations)
    prix_mean, prix_std = std_mean(price)
    kilometrage_mean, kilometrage_std = std_mean(mileage)
    saveModel(theta0, theta1, prix_mean, prix_std, kilometrage_mean, kilometrage_std)
    print(f"Entraînement terminé : theta0 = {theta0}, theta1 = {theta1}")
    show_cost_function(history)
    animate_model(kilometrage_norm, prix_norm, theta_history)

if __name__ == "__main__":
    main()
