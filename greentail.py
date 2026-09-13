import pandas as pd

# Step 1: Read Excel file
df = pd.read_excel('GreenTrail Store Data.xlsx', sheet_name='Store Data')

# Step 2: Compute percentage lifts
df['Sales_Lift_Pct_During'] = ((df['Weekly Sales During Promotion'] - df['Weekly Sales Before Promotion']) 
                               / df['Weekly Sales Before Promotion']) * 100

df['Sales_Lift_Pct_Post'] = ((df['Weekly Sales After Promotion'] - df['Weekly Sales Before Promotion']) 
                             / df['Weekly Sales Before Promotion']) * 100

df['Visit_Lift_Pct_During'] = ((df['Average Daily Visits During Promotion'] - df['Average Daily Visits Before Promotion']) 
                              / df['Average Daily Visits Before Promotion']) * 100

# Step 3: Segment by Promotion Type
promo_summary = df.groupby('Type of Promotion')[['Sales_Lift_Pct_During', 'Sales_Lift_Pct_Post', 'Visit_Lift_Pct_During']].mean()

# Step 4: Segment by Store Type
store_summary = df.groupby('Store Type')[['Sales_Lift_Pct_During', 'Sales_Lift_Pct_Post']].mean()