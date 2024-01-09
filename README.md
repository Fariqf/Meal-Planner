# Meal-Planner
This project utilizes OpenAI's GPT-3.5-turbo to assist you in meal planning.
You can input a list of ingredients, and the system will generate an example meal along with step-by-step instructions on how to prepare it.

## Getting Started
### Prerequisites
1. Python 3.7 or later
2. Streamlit
3. langchain
4. OpenAI API Key
1. Installation
1. git clone https://github.com/Fariqf/Meal-Planner-repo.git
2. cd Meal-Planner

2. Set up your OpenAI API key by creating a .env file in the root directory:
   OPENAI_API_KEY=your_openai_api_key
3. Run the Streamlit app:
   streamlit run app.py
## How to Use
1. Enter a comma-separated list of ingredients in the provided text input.
2. Click the "Generate" button.
3. The system will utilize OpenAI GPT-3.5-turbo to create a meal plan based on the given ingredients.
4. The generated meal and step-by-step instructions will be displayed.

## Examples
Input:chicken, rice, broccoli, soy sauce
Output:
**Meal:** Chicken Stir-Fry
**Ingredients:**
- Chicken
- Rice
- Broccoli
- Soy Sauce

**Instructions:**
1. Cook rice according to package instructions.
2. Heat a pan, add chicken, and cook until browned.
3. Add broccoli and soy sauce, stir-fry until vegetables are tender.
4. Serve the chicken stir-fry over the cooked rice.

Enjoy your delicious Chicken Stir-Fry!
