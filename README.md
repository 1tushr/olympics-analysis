# Olympic Medals Analysis (1976-2008)

## Project Overview
This project analyzes the Summer Olympic medals dataset from 1976 to 2008. The analysis includes exploratory data analysis, visualization of medal distributions, and a predictive model to forecast medal outcomes.

## Dataset
The dataset contains information about all medal winners in the Summer Olympics from 1976 Montreal to 2008 Beijing. Each row represents a medal awarded, with the following columns:
- City: Host city
- Year: Year of the Olympics
- Sport: Sport category
- Discipline: Subcategory of the sport
- Event: Specific event within a discipline
- Athlete: Name of the medal-winning athlete
- Gender: Gender of the athlete
- Country_Code: Country code (abbreviation)
- Country: Full name of the country
- Event_gender: Gender category of the event
- Medal: Type of medal (Gold, Silver, Bronze)

## Analysis Performed

### 1. Data Preparation
- Loaded the dataset with appropriate encoding
- Examined basic dataset information and checked for missing values

### 2. Exploratory Data Analysis (EDA)
- Generated summary statistics for the dataset
- Analyzed medal distribution by type (Gold, Silver, Bronze)
- Identified top countries by medal count
- Tracked medal counts across Olympic years
- Examined gender distribution in medal winners
- Identified top sports by medal count

### 3. Detailed Analysis
- Created a breakdown of medal types for top 10 countries
- Analyzed gender distribution across different sports

### 4. Predictive Analysis
- Built a machine learning model to predict if an athlete will win a Gold medal
- Used features like Country, Sport, and Gender
- Evaluated model performance with accuracy metrics and classification report
- Identified the most important features for predicting gold medal wins

## Results

### Key Findings
- The dataset contains 15,433 medals awarded across 9 Olympic Games
- Medal distribution is relatively even: Bronze (5,258), Gold (5,042), Silver (5,016)
- United States, Soviet Union/Russia, and East Germany/Germany are consistently top performers
- There is significant gender disparity in medal distribution, with men winning approximately 61% of all medals
- Certain countries specialize in specific sports, showing strong performance patterns
- The Random Forest model achieved 72% accuracy in predicting gold medal wins
- Country is the strongest predictor of winning a gold medal, followed by sport

### Visualizations
The comprehensive analysis (olympics_analysis.py) generates several visualizations:
- medal_analysis.png: Overview of medal distribution by country, year, gender, and sport
- top_countries_medals.png: Medal breakdown for top 10 countries
- gender_by_sport.png: Gender distribution in top 10 sports
- feature_importance.png: Important features for predicting gold medal wins

The simplified analysis (simple_olympics_analysis.py) generates these visualizations:
- top_countries.png: Bar chart of top 10 countries by medal count
- medal_types.png: Pie chart showing distribution of medal types
- gender_distribution.png: Pie chart of gender distribution
- medals_by_year.png: Line chart showing medals awarded by Olympic year
- top_sports.png: Horizontal bar chart of top 5 sports
- medal_breakdown.png: Stacked bar chart showing medal types for top countries
- sport_gender.png: Stacked bar chart showing gender distribution in top sports
- feature_importance_simple.png: Bar chart of top features for predicting gold medals

## How to Run the Analysis
1. Ensure you have Python installed with the required libraries:
   - pandas
   - matplotlib
   - numpy
   - seaborn
   - scikit-learn

2. Place the dataset file 'Summer-Olympic-medals-1976-to-2008.csv' in the same directory as the script

3. Run the analysis script:
   ```
   python simple_olympics_analysis.py 
   ```

4. Review the generated visualizations and console output for insights
