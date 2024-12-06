import streamlit as st
import pandas as pd
import os
from io import StringIO

def convert_to_qif(df, selected_columns, column_names, debit_credit_columns=None):
    # Creating a QIF format based on selected columns and names
    qif_lines = ["!Type:Bank"]
    for _, row in df.iterrows():
        qif_lines.append("D" + str(row[selected_columns[0]]))  # Date
        
        # Handle debit and credit columns if provided
        if debit_credit_columns:
            debit = pd.to_numeric(row[debit_credit_columns[0]], errors='coerce')
            credit = pd.to_numeric(row[debit_credit_columns[1]], errors='coerce')

            # Debit as negative, credit as positive
            if pd.notna(debit):
                amount = debit * -1
            else:
                amount = credit

        
        qif_lines.append("T" + str(amount))  # Amount
        qif_lines.append("P" + str(row[selected_columns[2]]))  # Payee
        if len(selected_columns) > 3:
            qif_lines.append("M" + str(row[selected_columns[3]]))  # Memo (Optional)
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

    # Allow user to select columns for QIF conversion
    st.write("### Select Columns for QIF Conversion:")
    selected_columns = st.multiselect(
        "Select columns to convert (in order: Date, Amount, Payee, Memo)",
        options=df.columns,
        default=df.columns[:3]  # Default to the first 3 columns
    )

    # Allow user to select debit and credit columns if applicable
    use_debit_credit = st.checkbox("Use separate Debit and Credit columns?")
    debit_credit_columns = None
    if use_debit_credit:
        debit_credit_columns = st.multiselect(
            "Select Debit and Credit columns (in order: Debit, Credit)",
            options=df.columns,
            default=df.columns[:2]  # Default to the first 2 columns
        )
        if len(debit_credit_columns) != 2:
            st.warning("Please select both Debit and Credit columns.")
            debit_credit_columns = None

    if len(selected_columns) >= 3:
        # Allow user to specify custom names for QIF fields
        st.write("### Provide Names for QIF Fields:")
        date_name = st.text_input("Date Field Name", "Date")
        amount_name = st.text_input("Amount Field Name", "Amount")
        payee_name = st.text_input("Payee Field Name", "Payee")
        memo_name = st.text_input("Memo Field Name (optional)", "Memo")

        column_names = [date_name, amount_name, payee_name, memo_name]

        # Convert to QIF and provide download link
        if st.button("Convert to QIF"):
            qif_content = convert_to_qif(df, selected_columns, column_names, debit_credit_columns)
            qif_file_name = "converted.qif"

            # Save QIF to file and provide download button
            with open(qif_file_name, "w") as f:
                f.write(qif_content)

            with open(qif_file_name, "r") as f:
                st.download_button(label="Download QIF File", data=f, file_name=qif_file_name, mime="text/plain")

    else:
        st.warning("Please select at least Date, Amount, and Payee columns.")
