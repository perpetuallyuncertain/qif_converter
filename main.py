import streamlit as st
import pandas as pd
from io import StringIO

def convert_to_qif(df, selected_columns, debit_credit_columns=None):
    # Ensure debit_credit_columns is valid or None
    if debit_credit_columns and len(debit_credit_columns) != 2:
        raise ValueError("debit_credit_columns must contain exactly two column names or be None.")

    # Creating a QIF format based on selected columns and names
    qif_lines = ["!Type:Bank"]
    for _, row in df.iterrows():
        # Date
        try:
            qif_lines.append("D" + str(row[selected_columns[0]]))
        except KeyError as e:
            raise KeyError(f"Date column not found: {e}")

        # Initialize amount with default column
        try:
            amount = pd.to_numeric(row[selected_columns[1]], errors='coerce')
        except (KeyError, ValueError) as e:
            raise ValueError(f"Error parsing Amount column ({selected_columns[1]}): {e}")
        
        # Override amount if debit/credit columns are provided
        if debit_credit_columns:
            try:
                debit = pd.to_numeric(row[debit_credit_columns[0]], errors='coerce')
                credit = pd.to_numeric(row[debit_credit_columns[1]], errors='coerce')
                if pd.notna(debit):
                    amount = debit * -1
                elif pd.notna(credit):
                    amount = credit
            except KeyError as e:
                raise KeyError(f"Debit/Credit column not found: {e}")
            except ValueError as e:
                raise ValueError(f"Error parsing Debit/Credit columns: {e}")

        # Add amount to QIF lines
        qif_lines.append("T" + str(amount))

        # Payee
        try:
            qif_lines.append("P" + str(row[selected_columns[2]]))
        except KeyError as e:
            raise KeyError(f"Payee column not found: {e}")

        # Memo (optional)
        if len(selected_columns) > 3:
            try:
                qif_lines.append("M" + str(row[selected_columns[3]]))
            except KeyError as e:
                raise KeyError(f"Memo column not found: {e}")
        
        # End of QIF entry
        qif_lines.append("^")

    return "\n".join(qif_lines)



# Streamlit Interface
st.title('CSV to QIF Converter')

# File Upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    df = pd.read_csv(stringio)

    # Show the data
    st.write("### CSV File Contents:")
    st.dataframe(df)

    use_debit_credit = st.checkbox("Use separate Debit and Credit columns?")

    # Allow user to select columns for QIF conversion
    st.write("### Select Columns for QIF Conversion:")
    selected_columns = st.multiselect(
        "Select columns to convert (in order: Date, Amount, Payee, Memo)",
        options=df.columns
    )

    # Allow user to select debit and credit columns if applicable
    debit_credit_columns = None
    if use_debit_credit:
        debit_credit_columns = st.multiselect(
            "Select Debit and Credit columns (in order: Debit, Credit)",
            options=df.columns
        )
        if len(debit_credit_columns) != 2:
            st.warning("Please select both Debit and Credit columns.")
            debit_credit_columns = None

    # Ensure at least Date, Amount, and Payee are selected
    if len(selected_columns) >= 3:
        # Convert to QIF and provide download link
        if st.button("Convert to QIF"):
            qif_content = convert_to_qif(df, selected_columns, debit_credit_columns)
            st.download_button(
                label="Download QIF File",
                data=qif_content,
                file_name="converted.qif",
                mime="text/plain"
            )
    else:
        st.warning("Please select at least Date, Amount, and Payee columns.")
