# Mini tutorials for use cases

The **Slash** project on GitHub is a web application designed to scrape popular e-commerce websites, helping users find the best deals quickly and efficiently. Here’s a mini-tutorial series to demonstrate typical use cases with practical examples:

### Use Case 1: Setup and Installation

**Goal**: Install Slash locally and configure the environment.

---

### 1. Clone and Set Up Local Environment

1. **Clone the Repository**
First, ensure `git` is installed on your computer. Choose a desired location and run the following command to clone the GitHub repository:
    
    ```bash
    git clone <https://github.com/DFY-NCSU/slash-phase6.git>
    cd slash-phase6
    ```
    
2. **Set Up Python Environment and Install Dependencies**
This project uses Python 3. Make sure Python and `pip` are installed on your system. All required libraries are listed in the `requirements.txt` file, which can be installed with the following command:
    
    ```bash
    pip3 install -r requirements.txt
    ```
    
3. **Install PostgreSQL Database**
This project requires PostgreSQL for database support. If PostgreSQL is not installed, download and install the latest version from the [PostgreSQL official download page](https://www.postgresql.org/download/).

### 2. Configure Database Connection

After installing PostgreSQL, configure the database connection by following these steps:

1. Open the `database.py` file in the project directory.
2. Locate the section where the database connection settings are defined, usually at the top of the file, which may look like the following:
    
    ```python
    username = 'postgres'
    password = 'pass'
    ```
    
    Replace the `username` and `password` values with your PostgreSQL username and password.
    

### 3. Run the Project

1. **Navigate to the `src` Directory**
After installing all dependencies, move to the `src` folder:
    
    ```bash
    cd src
    
    ```
    
2. **Run the Main Program**
    - **For Mac**:
        
        ```bash
        python3 main.py
        
        ```
        
    - **For Windows**:
        
        ```bash
        python main.py
        
        ```
        
    
    While the main program is running, proceed with the steps below to start the Streamlit application.
    

### 4. Launch the Streamlit Interface

Open a new terminal window, go up one directory level (`cd ..`), and then run the following command to start the user interface:

- **For Mac**:
    
    ```bash
    python3 -m streamlit run slash_user_interface.py
    
    ```
    
- **For Windows**:
    
    ```bash
    streamlit run slash_user_interface.py
    
    ```
    

---

Following these steps should successfully set up and run the Slash application. If you have any questions or need further assistance, feel free to reach out.

---

### Use Case 2: Running a Search Query

**Goal**: Retrieve deals for a specific item.

1. Run the application, which will launch a Streamlit interface.
2. Enter the item name or brand in the search box (e.g., "laptop" or “dell”).
3. Slash will scrape supported e-commerce sites, presenting results in a JSON format.

---

### Use Case 3: Filtering and Sorting Results

**Goal**: Narrow down deals by price, brand, or rating.

1. Use the built-in filters provided in the Streamlit UI.
2. Results can be customized based on preferences like lowest price or highest rating.