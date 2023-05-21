from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv('OPENAI_KEY')
print(key)



