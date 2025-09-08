import pickle
import numpy as np

def load_parameters():
    try:
        with open("model_parameters.pkl", "rb") as f:
            theta0, theta1, price_mean, price_std, mileage_mean, mileage_std = pickle.load(f)
    except:
        theta0, theta1 = 0 ,0
        price_mean, price_std = 0, 1
        mileage_mean, mileage_std = 0, 1
        print("Paramètres du model introuvable")
    return theta0, theta1, price_mean, price_std, mileage_mean, mileage_std

def estimate_price(mileage, theta0, theta1):
    """Calcule le price estimé en fonction du `kilométrage en utilisant la régression linéaire."""
    return theta0 + (theta1 * mileage)

def normalize(x, x_mean, x_std):
    return (x - x_mean) / x_std

def denormalized(x_norm, x_mean, x_std):
    return x_norm * x_std + x_mean

def main():
    """Demande le kilométrage à l'utilisateur et affiche le price estimé."""
    theta0, theta1, price_mean, price_std, mileage_mean, mileage_std = load_parameters()

    mileage = float(input("Veuillez entrer le kilométrage de la voiture : "))
    mileage_norm = normalize(mileage, mileage_mean, mileage_std)

    price_norm = estimate_price(mileage_norm, theta0, theta1)
    price_estime = denormalized(price_norm, price_mean, price_std)

    print(f"Le prix estimé pour un kilométrage de {mileage:.0f} km est : {price_estime:.2f} €")

if __name__ == "__main__":
    main()
