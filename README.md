# CSV to QIF Converter

This program helps you easily convert `.csv` files into `.qif` files for financial applications. It provides a simple interface to load a `.csv` file, select the relevant columns, and save the result as a `.qif` file.

---

## How to Access and Use the App

### Step 1: Install Docker

1. **Download Docker Desktop**:
   - Visit the [Docker website](https://www.docker.com/products/docker-desktop/) and download Docker Desktop for Mac.
2. **Install Docker**:
   - Follow the instructions on the website to install Docker on your Mac.
   - Once installed, open Docker Desktop and make sure it is running. You should see the Docker icon in your menu bar.

---

### Step 2: Get the App

1. **Go to the App Repository**:
   - Visit the [Releases](https://github.com/perpetuallyuncertain/qif_converter/pkgs/container/mumma_converter) page of the GitHub repository.
2. **Copy the App Command**:
   - In the latest release, find the container URL under **Usage**. It will look like this:
     ```
     docker run -p 8501:8501 ghcr.io/prepetuallyuncertain/mumma_converter:latest
     ```

---

### Step 3: Run the App

1. **Open the Terminal**:
   - On your Mac, open the Terminal app (you can find it by searching for "Terminal" in Spotlight or under Applications > Utilities).
2. **Run the Command**:
   - Paste the following command into the terminal and press Enter:
     ```
     docker run -p 8501:8501 ghcr.io/prepetuallyuncertain/mumma_converter:latest
     ```
3. **Access the App**:
   - After a few seconds, the app will start running. Open your web browser and go to:
     ```
     http://localhost:8501
     ```
   - You will see the app interface.

---

### Step 4: Convert a CSV File

1. **Load Your File**:
   - In the app, click **Choose a CSV File** and select your `.csv` file.
   - The table contents will appear for review.
2. **Select Columns**:
   - Choose the columns for **Date**, **Amount**, **Payee**, and (optional) **Memo**.
   - If you have separate **Debit** and **Credit** columns, check the box and specify them.
3. **Convert to QIF**:
   - Click **Convert to QIF**.
   - A button will appear to download the `.qif` file.

---

### Step 5: Save and Use the QIF File

- Save the downloaded `.qif` file to your desired location.
- Import the `.qif` file into your financial software.

---

## Notes

- If you encounter any issues, contact me, and I’ll help you fix it.
- Make sure your `.csv` file has clear column headers for smooth conversion.

---
