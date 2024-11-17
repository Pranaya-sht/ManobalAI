# ManobalAI

1. 
   
   i. Create a file called .env.local inside the frontend folder and add these in:
      
   VITE_CLERK_PUBLISHABLE_KEY=pk_test_cm9tYW50aWMtcXVhaWwtMjMuY2xlcmsuYWNjb3VudHMuZGV2JA
   VITE_CLERK_SECRET_KEY=sk_test_0pvdR1t6XJi6C2PawY5uGFrowkJ9lnv2qNDCKv21B4

   ii. Create a file called .env inside the backend folder and add this in:

   GROQ_API_KEY = "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

3. Go to the frontend folder and type this in the terminal:
 npm install
 npm run dev

4. Go to each of the 3 folders in the backend: Emotion, ManobalAI and Quotes and type this in the terminal in each of them: (or do this in a python virtual environment)
   pip install -r requirements.txt

5. Go to the backend folder and type this in the terminal:
   python -m uvicorn main:app (or add a --reload for auto reloading)

 
