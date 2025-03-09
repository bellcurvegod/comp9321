#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Third-party libraries
# NOTE: You may **only** use the following third-party libraries:
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# NOTE: It isn't necessary to use all of these to complete the assignment,
# but you are free to do so, should you choose.

# Standard libraries
# NOTE: You may use **any** of the Python 3.11 or 3.13 standard libraries:
# https://docs.python.org/3.11/library/index.html
# https://docs.python.org/3.13/library/index.html
from pathlib import Path

# ... import your standard libraries here ...


######################################################
# NOTE: DO NOT MODIFY THE LINE BELOW ...
######################################################
studentid = Path(__file__).stem


######################################################
# NOTE: DO NOT MODIFY THE FUNCTION BELOW ...
######################################################
def log(question, output_df=None, other=None):
    print(f"--------------- {question}----------------")

    if other is not None:
        print(question, other)
    if output_df is not None:
        df = output_df.head(5).copy(True)
        for c in df.columns:
            df[c] = df[c].apply(lambda a: a[:20] if isinstance(a, str) else a)

        df.columns = [a[:10] + "..." for a in df.columns]
        print(df.to_string())


######################################################
# NOTE: YOU MAY ADD ANY HELPER FUNCTIONS BELOW ...
######################################################


######################################################
# QUESTIONS TO COMPLETE BELOW ...
######################################################


######################################################
# NOTE: DO NOT MODIFY THE FUNCTION SIGNATURE BELOW ...
######################################################
def question_1(fuel_csv):
    ######################################################
    # TODO: Your code goes here ...
    ######################################################

    ######################################################
    # NOTE: DO NOT MODIFY THE CODE BELOW ...
    ######################################################
    log("QUESTION 1", output_df=df1, other=df1.shape)
    return df1


######################################################
# NOTE: DO NOT MODIFY THE FUNCTION SIGNATURE BELOW ...
######################################################
def question_2(df1):
    ######################################################
    # TODO: Your code goes here ...
    ######################################################

    ######################################################
    # NOTE: DO NOT MODIFY THE CODE BELOW ...
    ######################################################
    log("QUESTION 2", output_df=df2, other=df2.shape)
    return df2


######################################################
# NOTE: DO NOT MODIFY THE FUNCTION SIGNATURE BELOW ...
######################################################
def question_3(postcodes_json):
    ######################################################
    # TODO: Your code goes here ...
    ######################################################

    ######################################################
    # NOTE: DO NOT MODIFY THE CODE BELOW ...
    ######################################################
    log("QUESTION 3", output_df=df3, other=df3.shape)
    return df3


######################################################
# NOTE: DO NOT MODIFY THE FUNCTION SIGNATURE BELOW ...
######################################################
def question_4(df2, df3):
    ######################################################
    # TODO: Your code goes here ...
    ######################################################

    ######################################################
    # NOTE: DO NOT MODIFY THE CODE BELOW ...
    ######################################################
    log("QUESTION 4", output_df=df4, other=df4.shape)
    return df4


######################################################
# NOTE: DO NOT MODIFY THE FUNCTION SIGNATURE BELOW ...
######################################################
def question_5(df4):
    ######################################################
    # TODO: Your code goes here ...
    ######################################################

    ######################################################
    # NOTE: DO NOT MODIFY THE CODE BELOW ...
    ######################################################
    log("QUESTION 5", output_df=df5, other=df5.shape)
    return df5


######################################################
# NOTE: DO NOT MODIFY THE FUNCTION SIGNATURE BELOW ...
######################################################
def question_6(df4, df5):
    ######################################################
    # TODO: Your code goes here ...
    ######################################################

    ######################################################
    # NOTE: DO NOT MODIFY THE CODE BELOW ...
    ######################################################
    log("QUESTION 6", output_df=df6, other=df6.shape)
    return df6


######################################################
# NOTE: DO NOT MODIFY THE FUNCTION SIGNATURE BELOW ...
######################################################
def question_7(df6):
    ######################################################
    # TODO: Your code goes here ...
    ######################################################

    ######################################################
    # NOTE: DO NOT MODIFY THE CODE BELOW ...
    ######################################################
    log("QUESTION 7", output_df=df7, other=df7.shape)
    return df7


######################################################
# NOTE: DO NOT MODIFY THE FUNCTION SIGNATURE BELOW ...
######################################################
def question_8(df7):
    ######################################################
    # TODO: Your code goes here ...
    ######################################################

    ######################################################
    # NOTE: DO NOT MODIFY THE CODE BELOW ...
    ######################################################
    plt.savefig(f"{studentid}-Q8.png")
    log("QUESTION 8", other=answer8)
    return answer8


######################################################
# NOTE: DO NOT MODIFY THE FUNCTION SIGNATURE BELOW ...
######################################################
def question_9(df7):
    ######################################################
    # TODO: Your code goes here ...
    ######################################################

    ######################################################
    # NOTE: DO NOT MODIFY THE CODE BELOW ...
    ######################################################
    plt.savefig(f"{studentid}-Q9.png")
    log("QUESTION 9", other=answer9)
    return answer9


######################################################
# NOTE: DO NOT MODIFY THE MAIN FUNCTION BELOW ...
######################################################
if __name__ == "__main__":
    df1 = question_1("fuel.csv")
    df2 = question_2(df1.copy(True))
    df3 = question_3("postcodes.json")
    df4 = question_4(df2.copy(True), df3.copy(True))
    df5 = question_5(df4.copy(True))
    df6 = question_6(df4.copy(True), df5.copy(True))
    df7 = question_7(df6.copy(True))
    answer8 = question_8(df7.copy(True))
    answer9 = question_9(df7.copy(True))