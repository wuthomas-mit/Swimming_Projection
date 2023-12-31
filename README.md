# Swimming Career Projection

## Overview

Welcome to the Swimming Career Projection repository! This project aims to develop a predictive model for projecting swimmers' career trajectories, providing valuable insights into the trends of success in competitive swimming. The goal is to create a platform that enables aspiring swimmers to envision their career potential and assists swimming organizations in assessing swimming capabilities. 

## Goals/Outcomes

1. **Predictive Model Development:**
   - Create a robust predictive model that can project swimmers' career trajectories based on relevant factors such as performance metrics, training data, and other relevant variables.

2. **Insights into Success Trends:**
   - Analyze the data to uncover trends and patterns associated with successful swimming careers. This could include identifying key performance indicators, optimal training regimens, and other factors contributing to success.

3. **Platform for Aspiring Swimmers:**
   - Build a user-friendly platform that allows aspiring swimmers to input their data and receive personalized projections for their swimming careers. This can serve as a motivational tool and provide valuable guidance.

4. **Assessment Tool for Organizations:**
   - Provide swimming organizations with a tool to assess the capabilities of swimmers. This could be useful for talent scouting, team building, and making data-driven decisions.

## Steps For Use

1. **Data Collection:**
   - Begin by going to https://www.usaswimming.org/times/popular-resources/event-rank-search, where you find the top ~500 (will only give ~200-300) swimmers using the parameteres that you choose. Download the excel sheet of those entries. Then, in data_retrieval/scrape.py, change the input file and then let run until completion.

2. **Data Preparation:**
   - Use pre_processing/data_congregate.py on the folder of the downloaded excel files from previous step.

3. **Employing Synthetic Control:**
   - Use synth_control.py on the correct combined_output file to run synthetic control.