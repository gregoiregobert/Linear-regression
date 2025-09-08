# Linear Regression Project 🚗📈

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/) [![License](https://img.shields.io/badge/License-MIT-green)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/gregoiregobert/Linear-regression?style=social)](https://github.com/gregoiregobert/Linear-regression/stargazers)  

## 📖 Project Description
This project implements **linear regression from scratch** using a single feature: the **mileage of a car**.  
The goal is to predict a car's price based on its mileage.

The project consists of **two main programs**:

<details>
<summary>1️⃣ Predictor (predict.py)</summary>

    Prompts the user for a mileage and returns the estimated price.
    Formula used:
    estimatePrice(mileage) = θ0 + θ1 * mileage

</details>

<details>
<summary>2️⃣ Trainer (train.py)</summary>

    Reads a dataset containing mileage and price.
    Performs linear regression using gradient descent.
    Saves theta0 and theta1 for the predictor program.

</details>

---

## 🛠 Implementation Details

- Hypothesis function:

        estimatePrice(mileage) = θ0 + θ1 * mileage
  
- Gradient descent updates:

      tmpθ0 = learningRate * (1/m) * sum(estimatePrice(mileage[i]) - price[i])
      tmpθ1 = learningRate * (1/m) * sum((estimatePrice(mileage[i]) - price[i]) * mileage[i])
    Where m = number of data points.  
    theta0 and theta1 are updated simultaneously.
    
- Training procedure:  
      Initialize theta0 and theta1 to 0
      Loop over the dataset and update parameters using the formulas above
      Save the final theta0 and theta1
---

## 🎁 Bonus Features

<details>
<summary>Click to expand 🎨</summary>

    - Plot dataset points to visualize mileage vs. price
    - Plot the regression line on the same graph
    - Calculate the precision of the algorithm

</details>

---

## 🚀 How to Use

<details>
<summary>1️⃣ Train the model</summary>

    python train.py dataset.csv

    - Input: CSV file with mileage and price
    - Output: Saved theta0 and theta1

</details>

<details>
<summary>2️⃣ Predict a car price</summary>

    python predict.py

    - Enter mileage when prompted:
      Enter mileage: 15000
    - Output: Estimated price

</details>

<details>
<summary>3️⃣ (Optional) Visualize results</summary>

    python plot.py dataset.csv

    - Shows a graph with data points and regression line

</details>

---

## 📊 Demo

![Regression Demo](assets/line_reg.gif)   ![](assets/lin_reg_curve.png)
---

## ⚙ Requirements

    - Python 3.x
    - Optional for plotting:
      pip install matplotlib pandas

---

## 🖋 Author
**Grégoire Gobert**

---

## 📝 Notes

- Linear regression is implemented **from scratch** without any ML libraries
- Ideal for learning **gradient descent** and model training fundamentals
