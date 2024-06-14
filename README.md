# Whatsapp_Chat_Analysis
This is a streamlit webapp and python based whatsapp chat Analyzer its a comprehansive complete whatsapp chat analysis based code you can just export your whatsapp group chat and upload it on streamlit webapp when you run it upload your exported chat and you see different different types of analysis .

#Explaination :
Imports: Import necessary libraries:
streamlit for creating web apps.
preprocessor and helper (custom modules for preprocessing and analysis).
matplotlib.pyplot for plotting.
seaborn for statistical data visualization.
networkx for creating and visualizing complex networks.

Sidebar Title: Adds a title to the sidebar of the Streamlit app.

File Uploader: Provides a file uploader widget in the sidebar for users to upload a file.

File Uploader: Provides a file uploader widget in the sidebar for users to upload a file.

User List Creation:
Extracts a list of unique users from the DataFrame.
Removes 'group_notification' if present.
Sorts the list and adds "Overall" at the beginning for overall analysis

User Selection: Provides a dropdown menu in the sidebar for selecting a user to analyze.

Show Analysis Button: Adds a button in the sidebar to trigger the analysis when clicked.

Fetch Statistics: Calls a helper function to fetch basic statistics (number of messages, words, media messages, and links) for the selected user.

Display Statistics: Creates four columns and displays the fetched statistics in each column with headers and titles.

Monthly Timeline:
Calls a helper function to get monthly timeline data.
Plots the data and displays it in the app.

Daily Timeline: Similar to the monthly timeline, but on a daily basis.

Most Busy Day: Displays a bar chart for the busiest day of the week.

Most Busy Month: Displays a bar chart for the busiest month.
Weekly Activity Map: Displays a heatmap showing user activity throughout the week.
Most Busy Users: If "Overall" is selected, displays a bar chart and data table of the most active users.
Word Cloud: Generates and displays a word cloud of the most frequently used words.
Most Common Words: Displays a horizontal bar chart of the most common words used by the selected user.
Emoji Analysis:
Displays a data table and pie chart of the most used emojis.
Day vs. Night Activity: Displays a bar chart comparing activity during the day vs. night.
Weekly Activity: Displays a line chart showing user activity throughout the week.
User Interaction Network: Visualizes the interaction network between users.
Message Type Analysis: Displays a bar chart of different types of messages (text, media, etc.)

#How to run it 
Python Installation: Ensure Python is installed on your system. You can download it from python.org.

Required Libraries: Make sure you have installed the necessary libraries. You can install them using pip if you haven't already:

install : pip install streamlit matplotlib seaborn networkx
Code Files: Save the provided code snippet into a file, for example, whatsapp_chat_analyzer.py.

Steps to Run the App
Open a Terminal/Command Prompt:

Navigate to the directory where your whatsapp_chat_analyzer.py file is located.
Run Streamlit App:

In the terminal, type the following command and hit Enter:


Copy code:
streamlit run whatsapp_chat_analyzer.py

Wait for Initialization:

Streamlit will start initializing the app and will open it in your default web browser once it's ready.
Use the App:

Once the app opens in your browser, you should see the sidebar with options to upload a WhatsApp chat file and select a user for analysis.
Upload a WhatsApp chat export file (typically a text file).
Select a user from the dropdown list.
Click the "Show Analysis" button to trigger the analysis and display various statistics and visualizations related to the selected user's chat data.
Interact with the App:

Explore the different tabs and visualizations provided in the app interface.
Each visualization or analysis corresponds to a specific function defined in the helper module, processing and displaying insights from the WhatsApp chat data.
Terminate the App:

To stop the app, you can typically press Ctrl + C in the terminal where Streamlit is running.
