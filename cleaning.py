'''
Step 1: Importing Packages and Survey Responses
'''

# Step 1: Import Packages
import pandas as pd
import numpy as np

# Step 2: Import Survey Responses

labs32_HRFAsylumA = pd.read_csv('/content/l32_HRFAsylumA_HASHED.csv')
# NOTE: Labs32 was conducted using slightly different questions; make sure to 
# fill in with 'NaN' where appropriate 

# TPL: Rebecca Duke Wiesenberg
labs33_HRFAsylumAB = pd.read_csv('/content/l33_HRFAsylumAB_HASHED.csv')
labs33_HRFAsylumA = pd.read_csv('/content/l33_HRFAsylumA_HASHED.csv')
labs34_HRFAsylumA = pd.read_csv('/content/l34_HRFAsylumA_HASHED.csv')

# TPL: Paul St. Germain
labs35_HRFAsylumA = pd.read_csv('/content/l35_HRFAsylumA_HASHED.csv')
# TPL: Niki Dossett
labs35_HRFAsylumB = pd.read_csv('/content/l35_HRFAsylumB_HASHED.csv')

# TPL: Christopher Barrett
# NOTE: As of 07/08/2021, survey `l35_HRFBlueWitnessA` still needs to be hashed. 
# Once the student identities have been hashed, the survey will be imported and cleaned.

'''
Step 2: Write Functions for Cleaning Data
'''
# Function to regulate all column names
def rename_feature_name(df, old_cols, new_cols): 
  df = df.rename(columns=dict(zip(old_cols, new_cols)), inplace=True) 
  return df      

# Column names in surveys administered in Labs 33 onwards
old_col_names = [
            "What's your name?", 
            "What track are you in?",
            "What language(s) do you speak? This includes any languages you are currently learning!",
            "What did you do before Lambda? (Previous work)",
            "What's one of your strengths, when it comes to technical skills?",
            "What's one area of improvement for your technical skills?",
            "What's one of your strengths, when it comes to working in a team?",
            "What is one area of improvement for your teamwork skills?",
            "In 10 words or less, what's your goal for Labs?",
            "How confident are you with your writing? (1 == no confidence; 10 == fully confident)",
            "What's one of your strengths, when it comes to writing?",
            "What's something you'd like to improve about your writing?",
            "Do you have any experience in the following things? Check off all that you have experience in. (If you do any of this kind of writing as a hobby, that counts! If you don't have any experience with these types of writing, that's ok!)",
            "When watching a movie, what do you pay the most attention to?"
            ]
# New column names, for brevity and readability
new_col_names =[
         "Learner", 
         "Track", 
         "Languages_spoken", 
         "Previous_work", 
         "Technical_strength",
         "Technical_area_of_improvement",
         "Interpersonal_strength",
         "Interpersonal_area_of_improvement",
         "Labs_goal",
         "Writing_confidence",
         "Writing_strength",
         "Writing_area_of_improvement",
         "Previous_writing_experience", 
         "Movie_predisposition"
         ]

# Function for stripping extra white space, dropping 'Unnamed: 0' and 'Timestamp'
# columns that appear in each survey, and do not offer information about 
# students' academic profile
def clean(df):
  df.columns = df.columns.str.strip()
  df = df.drop(['Unnamed: 0', 'Timestamp'], axis=1)
  return df