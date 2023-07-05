import streamlit as st
import pandas as pd

# Load the recommendation files
df_bert = pd.read_csv("Bert_recommendations.csv")
df_two_tower = pd.read_csv("two_tower_recommendations.csv")
df_svd = pd.read_csv("Svd_recommendations.csv")

# Define the available models
models = {
    "BERT": df_bert,
    "Two Tower": df_two_tower,
    "SVD": df_svd
}

# Set page title and format
st.set_page_config(
    page_title="Movie",
    page_icon="🎥",
    layout="wide"
)

# Create the main function for the Streamlit app
def main():
    st.title("Movie Recommendation Application 🎥 ")
    st.sidebar.title("Select a Model")

    selected_model = st.sidebar.selectbox("Model:", list(models.keys()))

    if selected_model == "BERT":
        movie_name = st.text_input("Enter the movie name:", key="bert_movie_name").lower()
        display_recommendations(df_bert, movie_name, selected_model)
    elif selected_model == "Two Tower":
        user_id = st.text_input("Enter the user ID:", key="two_tower_user_id")
        display_recommendations(df_two_tower, user_id, selected_model)
    elif selected_model == "SVD":
        user_id = st.text_input("Enter the user ID:", key="svd_user_id")
        display_recommendations(df_svd, user_id, selected_model)
    
    # Add empty space at the bottom of the sidebar
    st.sidebar.empty()
    
    # Add your name, title, and project name at the bottom of the sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("SP Jain School of Global Management")
    st.sidebar.markdown("Created by:")
    st.sidebar.markdown("Akash Ramdev | Jinen Mirje | Manglam Jain | Vibhav Bagga")
    st.sidebar.markdown("MAIB")
    st.sidebar.markdown("REMA")
    st.sidebar.markdown("---")

# Function to display recommendations based on the selected model and input
def display_recommendations(df, input_value, model):
    if input_value:
        if model == "BERT":
            recommendations = df.loc[df["Watched Movie"].str.lower() == input_value.lower()][
                df.columns[1:]
            ].values.flatten().tolist()
            st.subheader(f"Top 10 Recommendations for {input_value.capitalize()}:")
            if recommendations:
                for i, recommendation in enumerate(recommendations[:10]):
                    st.write(f"{i+1}. {recommendation}")
            else:
                st.write("No recommendations found for the movie.")
        elif model == "Two Tower":
            if input_value.isdigit():
                recommendations = df.loc[df["User ID"] == int(input_value)].values.tolist()[0][1:]
                st.subheader(f"Top 10 Recommendations for User {input_value}:")
                if recommendations:
                    for i, recommendation in enumerate(recommendations):
                        st.write(f"{i+1}. {recommendation}")
                else:
                    st.write("No recommendations found for the user.")
            else:
                st.write("Invalid input. Please enter a valid User ID.")
        elif model == "SVD":
            if input_value.isdigit():
                recommendations = df.loc[df["userId"] == int(input_value)]["title"].values.tolist()
                st.subheader(f"Top 10 Recommendations for User {input_value}:")
                if recommendations:
                    for i, recommendation in enumerate(recommendations[:10]):
                        st.write(f"{i+1}. {recommendation}")
                else:
                    st.write("No recommendations found for the user.")
            else:
                st.write("Invalid input. Please enter a valid User ID.")
    else:
        st.write("Please provide an input value.")

# Run the app
if __name__ == "__main__":
    main()
