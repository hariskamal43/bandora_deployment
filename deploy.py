#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import joblib
import streamlit as st


loaded_model = joblib.load('savemodel.sav', 'r')


# Defining a function

def prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not defaulted'
    else:
        return 'The person is defaulted'


def main():

    # Giving a title
    st.title('Financial Risk Predction')
    # Lets get input from users
    col1, col2, col3 = st.columns(3)
    with col1:
        BidsPortfolioManager = st.number_input(
            'BidsPortfolioManager')
        BidsManual = st.number_input(
            'BidsManual')
        VerificationType = st.selectbox(
            'VerificationType', [1, 2, 3, 4])
        AppliedAmount = st.number_input(
            'AppliedAmount')
        Amount = st.number_input(
            'Amount')
        Interest = st.number_input(
            'Interest')
        LoanDuration = st.number_input('LoanDuration')
        MonthlyPayment = st.number_input(
            'MonthlyPayment')
        IncomeTotal = st.number_input('IncomeTotal')
        LiabilitiesTotal = st.number_input('LiabilitiesTotal')
        DebtToIncome = st.number_input(
            'DebtToIncome')
        FreeCash = st.number_input(
            'FreeCash')
    with col2:
        MonthlyPaymentDay = st.number_input(
            'MonthlyPaymentDay')
        PrincipalPaymentsMade = st.number_input(
            'PrincipalPaymentsMade')
        InterestAndPenaltyPaymentsMade = st.number_input(
            'InterestAndPenaltyPaymentsMade')
        PrincipalBalance = st.number_input(
            'PrincipalBalance')
        InterestAndPenaltyBalance = st.number_input(
            'InterestAndPenaltyBalance')
        AmountOfPreviousLoansBeforeLoan = st.number_input(
            'AmountOfPreviousLoansBeforeLoan')
        PreviousRepaymentsBeforeLoan = st.number_input(
            'PreviousRepaymentsBeforeLoan')
        LanguageCode_1 = st.selectbox(
            'Does the borrower speaks Estonian?', [1, 0])
        LanguageCode_4 = st.selectbox(
            'Does the borrower speaks Finnish?', [1, 0])
        LanguageCode_6 = st.selectbox(
            'Does the borrower speaks Spanish?', [1, 0])
        LanguageCode_9 = st.selectbox(
            'Does the borrower speaks Slovakian?', [1, 0])
        Country_EE = st.selectbox(
            'Does the country is EE?', [1, 0])
    with col3:
        Country_ES = st.selectbox(
            'Does the country is ES?', [1, 0])
        Country_FI = st.selectbox(
            'Does the country is FI?', [1, 0])
        Education_0 = st.selectbox(
            ' Does the borrower is Educated ?', [1, 0])
        UseOfLoan_Not_set = st.selectbox(
            'Does loan consolidated?', [1, 0])
        MaritalStatus_Not_specified = st.selectbox(
            'Does the marrital status is known ?', [1, 0])
        EmploymentStatus_Not_specified = st.selectbox(
            'Does the employment status  is known ?', [1, 0])
        EmploymentDurationCurrentEmployer_MoreThan5Years = st.selectbox(
            'Does the employment duration is more than 5 years ?', [1, 0])
        OccupationArea_Not_specified = st.selectbox(
            'oes the area of Occupation is known ?', [1, 0])
        Rating_HR = st.selectbox(
            'Does the Rating id HR?', [1, 0])
        CreditScoreEsMicroL_M1 = st.selectbox(
            'Does the credit score is M?', [1, 0])
        CreditScoreEsMicroL_M5 = st.selectbox(
            'Does the credit score is M1? ', [1, 0])
        CreditScoreEsMicroL_M10 = st.selectbox(
            'Does the credit score is M5?', [1, 0])
        NewCreditCustomer_True = st.selectbox(
            'Did the customer have prior credit history in Bondora ?', [1, 0])
        Age = st.number_input('Age')
        Gender = st.selectbox('Gender 1:male, 0:female', [0, 1])

    # Code for prediction
    result = ''

    # creating a button for Prediction
    if st.button('Get the result'):
        result = prediction([BidsPortfolioManager, BidsManual, VerificationType, Age, Gender, AppliedAmount, Amount,
                                     Interest, LoanDuration, MonthlyPayment, IncomeTotal, LiabilitiesTotal,
                                     DebtToIncome, FreeCash, MonthlyPaymentDay,  PrincipalPaymentsMade,
                                     InterestAndPenaltyPaymentsMade, PrincipalBalance, InterestAndPenaltyBalance,
                                     AmountOfPreviousLoansBeforeLoan, PreviousRepaymentsBeforeLoan, LanguageCode_1,
                                     LanguageCode_4, LanguageCode_6, LanguageCode_9, Country_EE, Country_ES, Country_FI,
                                     Education_0, UseOfLoan_Not_set, MaritalStatus_Not_specified,
                                     EmploymentStatus_Not_specified, EmploymentDurationCurrentEmployer_MoreThan5Years,
                                     OccupationArea_Not_specified, Rating_HR, CreditScoreEsMicroL_M1,
                                     CreditScoreEsMicroL_M5, CreditScoreEsMicroL_M10, NewCreditCustomer_True])
    st.success(result)


if __name__ == '__main__':
    main()


# In[ ]:




