from dotenv import load_dotenv
import os

load_dotenv()

k = os.getenv('OPENAI_KEY')
print(k)



