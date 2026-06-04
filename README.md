# 🎓 CSE422: Artificial Intelligence - Ultimate Student Survival Guide 🚀

Welcome to the **CSE422 (Artificial Intelligence)** open-source repository! This repository has been structured as a comprehensive, interactive student survival guide to help you navigate through the concepts, mathematical formulas, and coding requirements of the CSE422 course at BRAC University.

Whether you're struggling to understand the difference between **Greedy Best-First Search** and **A\* Search**, scratching your head over **Genetic Algorithm** chromosome encodings, or trying to calculate a **Logistic Regression** update rule by hand—this guide has got your back!

---

## 🗺️ Course Overview: What are we building?
Artificial Intelligence in CSE422 is split into two major halves: **Classical AI** (search algorithms and game theory) and **Modern AI** (machine learning and neural networks). 

Here is the step-by-step roadmap to conquering the syllabus, complete with the exact video resources that saved my life.

---

### 🧗 Phase 1: Classical AI & Search Algorithms
Before machines could learn, they had to search! This phase is all about finding the optimal path from Point A to Point B.

![Searching Path GIF](https://media.giphy.com/media/L02M3FJhkF19S/giphy.gif)

*   **Step 1: Agents & Environments.** Understand what a rational agent is and whether your environment is deterministic, stochastic, episodic, or sequential.
*   **Step 2: Uninformed vs. Informed Search.** 
    *   *Uninformed:* BFS, DFS, UCS (Searching blindly).
    *   *Informed:* A* Search and Greedy Best-First Search (Using a "heuristic" or estimated distance to the goal).
*   **Step 3: Local Search.** What if you don't care about the path, just the final optimal state? Learn **Hill Climbing**, **Simulated Annealing** (using temperature to escape local maxima), and **Genetic Algorithms** (crossover and mutation!).
*   **Step 4: Adversarial Search (Games).** How to beat your opponent in Tic-Tac-Toe or Chess using **Minimax** and optimizing it with **Alpha-Beta Pruning**.

📺 **Phase 1 Video Resources:**
*   ▶️ [CSE422 | L1 Introduction to AI | TRZ Class Recording](https://www.youtube.com/watch?v=RlNQLWaM6Pk)
*   ▶️ [Greedy Best-First Search Explained | Protorials By Saif](https://www.youtube.com/watch?v=RlNQLWaM6Pk)
*   ▶️ [CSE422 Mid Review Class (Solving Alpha-Beta Pruning & Local Search)](https://www.youtube.com/watch?v=WZ3qYEozQWA)

---

### 🎲 Phase 2: Probability & Bayes Theorem
To transition into Machine Learning, you must understand probability. Machines handle uncertainty using math.

![Math Confused GIF](https://media.giphy.com/media/ne3xrYlWtQFtC/giphy.gif)

*   **Step 5: Joint Probability Distributions.** Learn to read a probability table and calculate Marginal, Joint, and Conditional probabilities.
*   **Step 6: Naive Bayes Classification.** Using Bayes' Theorem with the "naive" assumption that all features are independent to predict things like Spam Emails or Disease Diagnosis.

📺 **Phase 2 Video Resources:**
*   ▶️ [Fundamentals of Probability and Joint Distribution Tables](https://www.youtube.com/watch?v=O2L2Uv9pdDA)

---

### 📉 Phase 3: Modern AI & Machine Learning
Welcome to the realm of Data, Gradients, and Neural Networks! 

![Neural Network GIF](https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif)

*   **Step 7: Decision Trees.** Splitting data using *Entropy* and *Information Gain* to build a tree of yes/no questions.
*   **Step 8: Linear Regression & Gradient Descent.** Fitting a straight line ($y = mx + c$) to continuous data (like housing prices) and optimizing the error using Gradient Descent (taking small steps down the error hill).
*   **Step 9: Logistic Regression.** When you need to predict discrete categories (Yes/No, 0/1). You apply a **Sigmoid Curve** to your linear equation and use *Binary Cross-Entropy* to calculate the loss.
*   **Step 10: Neural Networks & Perceptrons.** Combining multiple logistic regression models (neurons) into layers (Input, Hidden, Output) to capture complex, non-linear trends. You must learn *Forward Propagation* (making a prediction) and *Backpropagation* (updating weights based on the error).

📺 **Phase 3 Video Resources (The Golden Playlist):**
*   ▶️ [CSE422/ CSE427 Logistic Regression and Neural Network Perceptrons - SWG](https://www.youtube.com/watch?v=y4gaxD7WZDhxCqvmjPK-r3ix7xAd-WPT)
*   ▶️ [Gradient Descent, Step-by-Step | StatQuest](https://youtu.be/sDv4f4s2SB8)
*   ▶️ [Linear Regression using Gradient Descent | Emerging Tech Innovator](https://youtu.be/sDv4f4s2SB8)
*   ▶️ [Perceptron Learning Algorithm Explained | Protorials By Saif](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
*   ▶️ [But what is a neural network? | 3Blue1Brown](https://www.youtube.com/watch?v=airhfXvrT6m4)
*   ▶️ [How Forward Propagation in Neural Networks works | Mısra Turp](https://www.youtube.com/watch?v=LmEsNuem8P8)
*   ▶️ [Are You Counting Neural Network Parameters the Right Way | Deep knowledge](https://www.youtube.com/watch?v=E1KshUWoC3I)

---

## 🛠️ Step-by-Step Practical Student Guide

### 📍 Step 1: Setting Up the Skeletons
To pass the lab evaluations and midterm, you must be able to code three core skeletons from scratch (no templates are provided in exams!):
1.  **A\* Search:** Maintain a priority queue that pops the node with the lowest $f(n) = g(n) + h(n)$ and updates neighbors.
2.  **Genetic Algorithm:** Write a custom `fitness(chromosome)` function (e.g., adding penalties for violating constraints) and a `mutate(chromosome)` step that safely flips genes. (Check out the clean, modular Python implementation in [/Practice_Problems/genetic_algorithm.py](file:///C:/Users/Abedi/Downloads/CSE422/Practice_Problems/genetic_algorithm.py) to see how to properly initialize and decode chromosomes without infinite recursion bugs).
3.  **Alpha-Beta Pruning:** Implement a recursive minimax tree traversal with `if alpha >= beta: break` pruning blocks.

### 📍 Step 2: Master File Input/Output (I/O)
Most students panic because they struggle to parse text files (e.g., `input.txt` representing grids, coordinates, or graphs). Practice parsing strings into dictionaries or lists without using "fancy" built-in functions like `map()` if your TAs prefer traditional loops:
```python
# Safest manual parsing:
with open('input.txt', 'r') as f:
    lines = f.readlines()
    
# Manual extraction of row/col size
rows_cols = lines[0].split()
num_rows = int(rows_cols[0])
num_cols = int(rows_cols[1])
```

### 📍 Step 3: Solve Machine Learning Math by Hand
Do not just import libraries. Practice calculating:
*   **Posterior Probabilities** for Naive Bayes tables.
*   **Gradient Descent Updates** for simple univariate coordinates ($m_{\text{new}} = m_{\text{old}} - \alpha \times \frac{\partial L}{\partial w}$).
*   **Sigmoid outputs** ($\sigma(Z) = \frac{1}{1 + e^{-Z}}$).

### 🧮 Mathematical Formula Cheat Sheet
Do not walk into the final exam without these memorized:
* **Binary Cross-Entropy (BCE) Loss:** $Loss = - \left[ y \ln(A) + (1 - y) \ln(1 - A) \right]$
* **Sigmoid Derivative (Often asked as a conceptual question!):** $\sigma'(x) = A \times (1 - A)$
* **Gradient Descent for Linear Regression (MSE):** $m_{\text{new}} = m_{\text{old}} - \alpha \times \left( \frac{2}{n} \sum (\hat{y} - y) \times x \right)$
* **Gradient Descent for Logistic Regression (BCE Shortcut):** $w_{\text{new}} = w_{\text{old}} - \alpha \times \left( (A - y) \times x \right)$
* **Neural Network Parameter Counting:** $(\text{Inputs} \times \text{Neurons}) + \text{Biases}$

---

## 📚 Curated Resources & Official Course Links

Use these official playlists, slides, and files to prepare for exams:

### 📺 Study Playlists & Video References
| Resource Topic | Type | Link | Description |
| :--- | :--- | :--- | :--- |
| **A\* Search** | YouTube | [Abdul Bari's A\* Algorithm Tutorial](https://www.youtube.com/watch?v=RlNQLWaM6Pk) | Quick 15-minute whiteboard breakdown of path costs. |
| **Regression Analysis** | YouTube | [StatQuest's Gradient Descent](https://youtu.be/sDv4f4s2SB8) | Linear/Logistic regression slides are based on this video. |
| **Neural Networks** | YouTube | [3Blue1Brown's Neural Networks Series](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | Gold standard for visual understanding of weights and biases. |
| **Probability & Bayes** | YouTube | [StatQuest's Naive Bayes](https://youtu.be/O2L2Uv9pdDA) | Clear step-by-step conditional probability walkthroughs. |

### 📂 Official Class Recordings & Materials (Tanzim Reza Sir - Theory)
*   **Logistic Regression Class Video:** [Drive File Link](https://drive.google.com/file/d/1y4gaxD7WZDhxCqvmjPK-r3ix7xAd-WPT/view?usp=sharing)
*   **Probability Theory & Naive Bayes Lectures:** [Drive Folder Link](https://drive.google.com/drive/u/0/folders/1GuMupferfCW2eLs7W5M4cUvmhY-mNjCn)
*   **Midterm Marks Folder:** [Drive Folder Link](https://drive.google.com/drive/folders/1txWHiPb-B6fZhnhRK1mSHWfN4yunZhHB?usp=sharing)
*   **Final Marks Tracker (Excluding Finals):** [Drive Folder Link](https://drive.google.com/drive/folders/1-Deccl9qLcF74vs8oIsVKgGLnUsLW_M0?usp=sharing)
*   **Theory Grades Spreadsheet:** [Google Docs Link](https://docs.google.com/spreadsheets/d/1Gizou792BYSl64h3VfLPVaurBvkMisvO/edit?usp=sharing&ouid=107280348520227181657&rtpof=true&sd=true)
*   **Theory Final Practice Problems:** [Google Docs Link](https://docs.google.com/document/d/1QfM6zQ_EITaZuSSxoLg-Yg8wqCMNkmQbP1OAwa6HEcs/edit?usp=sharing)

### 📝 Essential Practice Problem Sets (IBU Ma'am)
* **Problem Set 4:** [Probability and Naive Bayes](file:///C:/Users/Abedi/Downloads/CSE422/11_Naive-Bayes.pdf)
* **Problem Set 6:** [Logistic Regression & Gradient Descent Datasets](file:///C:/Users/Abedi/Downloads/CSE422/Problem%20Set%206%20Logistic%20Regression.pdf)
* **Problem Set 7:** [Decision Trees & Entropy Calculations](file:///C:/Users/Abedi/Downloads/CSE422/Problem%20Set%207%20Learning%20and%20Decision%20Tree.pdf)

### 💻 Lab Materials & Colabs (Asif Hasan & Rafeed Rahman - Lab)
*   **Lab Midterm Practice (A\*):** [Drive Link](https://drive.google.com/drive/folders/1V7ZT6e_kprbPVpYAGk2H4p4M1yD86JA3)
*   **Lab Midterm Practice (GA):** [Google Docs Link](https://docs.google.com/document/d/1Il3gRVe7lRK6X6s_oqWAmC1AyYb6-Kvoo_wPy1kFiZ0/edit?tab=t.0#heading=h.mybrk29sdv5d)
*   **Lab Midterm Practice (ABP):** [Google Docs Link](https://docs.google.com/document/d/1M8GNijaRmbrEgLEJ8Sgi__-DYyj20kpJ/edit#heading=h.jceabxqthilo)
*   **Lab Google Colabs:**
    *   [Model Evaluation Colab](https://colab.research.google.com/drive/17BkE0YBP4YEWAnWcdVV4-p2aqsC8S4YW)
    *   [K-fold Cross Validation Colab](https://colab.research.google.com/drive/1KuVmSq5cKXD_IM2ly3JHjn4Kcd0sjTxr?usp=sharing)
    *   [Exploratory Data Analysis (EDA) Folder](https://drive.google.com/drive/folders/14Kb3UsdEsw2IYvjYq8FVkm7i_r0QDXUk)
*   **Model Evaluation Slides:** [Google Slides Link](https://docs.google.com/presentation/d/1FtF9imoDXCk7afkFePyTuC1TDBmOSwMMwOcgq94k2_Q/edit?slide=id.g3799a2fbcca_0_293#slide=id.g3799a2fbcca_0_293)
*   **Project Group Registration & Datasets:** [Google Docs Link](https://docs.google.com/spreadsheets/d/1ldrvL5cX5mVHsenggUfFfzQo75CSl9XqqP4Z-LZOKHs/edit?usp=sharing)
*   **Project Guidelines:** [Drive PDF Link](https://drive.google.com/file/d/1fSKAeSpT4y3CrSp77fEUU2rmZCRj0m8k/view)
*   **Project Submission Form:** [Google Forms Link](https://forms.gle/SwnPDNLGbe1NAtDG8)

---

## 💻 My Lab & Project Files
In this repository, you will find my Python implementations using `scikit-learn` and `Google Colab`:
*   [Minimax_Alpha_Beta_Pruning.ipynb](file:///C:/Users/Abedi/Downloads/CSE422/Minimax_Alpha_Beta_Pruning.ipynb) — Minimax algorithm with Alpha-Beta Pruning.
*   [Genetics_Evaluations.ipynb](file:///C:/Users/Abedi/Downloads/CSE422/Genetics_Evaluations.ipynb) — Genetic Algorithm evaluation simulations.
*   [Model_Evaluation.ipynb](file:///C:/Users/Abedi/Downloads/CSE422/Model_Evaluation.ipynb) — Model metrics, scaling, and hyperparameter checks.
*   [K_Fold_Cross_Validation (1).ipynb](file:///C:/Users/Abedi/Downloads/CSE422/K_Fold_Cross_Validation%20(1).ipynb) — K-Fold validation splitting.
*   [EDA_CSE422_Lab (1).ipynb](file:///C:/Users/Abedi/Downloads/CSE422/EDA_CSE422_Lab%20(1).ipynb) — Exploratory Data Analysis & plots.
*   [CSE422_Lab_Project (1).ipynb](file:///C:/Users/Abedi/Downloads/CSE422/CSE422_Lab_Project%20(1).ipynb) — Final classification models comparison.
*   [cse422_lab_project.py](file:///C:/Users/Abedi/Downloads/CSE422/cse422_lab_project.py) — Standalone project Python script.

![Coding Hacker GIF](https://media.giphy.com/media/YQitE4YNQBroM/giphy.gif)

---

### 💡 Professor's Pro-Tip for Surviving:
As outlined in the course overview: *"If you want to do well in this course, you must practice the algorithms before class... and everything must be practiced practically using Python libraries like scikit-learn in Google Colab."*

---

## 🏆 Key Takeaways & Exam Tips
> 💡 **Pro-Tip for Local Search:** In Simulated Annealing, remember that at high temperatures, the system is highly random and accepts downhill/suboptimal moves. As the temperature cools down to 0, it behaves like normal Hill Climbing. Do not reverse this in exams!
>
> 💡 **Pro-Tip for A\* Graph Search:** A\* is only optimal on graphs if the heuristic is consistent (monotonic). An admissible heuristic is not enough for graph search because it can finalize nodes prematurely via sub-optimal paths.
>
> 💡 **Pro-Tip for Decoding Final Exam Questions:**
> * If a question asks to "update the weight of a single perceptron using Binary Cross Entropy," it is just **Logistic Regression** in disguise. Use the simple gradient shortcut: $(A - Y) \times X$.
> * In probability word problems, watch out for the phrase *"conditionally independent."* It changes your entire joint probability path equation.
> * If a dataset table has continuous numeric targets (e.g., predicting a house price of 1500), it's Linear Regression. If the target is strictly 0 or 1, it's Logistic Regression.

Good luck surviving CSE422! 🎓

![Code working victory](https://media.giphy.com/media/HteV6g0VWqWUU/giphy.gif)
