
# import sys
# sys.path.append("../backend")
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from Emotion.emotion import *
from ManobalAI.main import *
from Quotes.api import *


import uvicorn




app = FastAPI()

origins = [
    "*",  # React frontend URL
]

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins in the list
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
@app.post("/analyze-emotion/")
def analyze_emotion_endpoint(request: EmotionRequest):
    emotion, score = analyze_emotion(request.text)
    save_emotion_for_graph(emotion, score)
    return {"emotion": emotion, "score": score}

@app.get("/generate-graph/")
def generate_graph_endpoint():
    graph_path = "Emotion/"+generate_graph()
    return FileResponse(graph_path, media_type="image/png")
@app.post("/prompt")
async def process_prompt(query_data: QueryRequest) -> Dict[str, Any]:
    """
    Process the incoming prompt and return a response.
    """
    try:
        query = query_data.query.strip()

            
        if not query:
            return {
                "response": "Please ask a question.",
                "status": "success"
            }

        # Regular query processing
        response = chain.invoke({"input": query})
        
        print("Response: ", response)
        
        answer = response.get('answer', '').strip()
            
        if not answer:
            return {
                "response": "I can help you with mental health-related questions. What would you like to know?",
                "status": "success"
            }
        
            
        print("HIIIIIIIIiiii")
            
        return {
            "response": answer,
            "status": "success"
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "response": "I couldn't process that. Could you try asking differently?",
            "status": "success"
        }
        
@app.get("/random-quote")
def random_quote():
    quotes = load_quotes_from_file("mental_health_quotes.txt")  # Load quotes from file
    quote = get_random_quote(quotes)  # Get a random quote
    return {"quote": quote}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)