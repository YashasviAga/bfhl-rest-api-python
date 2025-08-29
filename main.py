from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

class DataModel(BaseModel):
    data: List[Union[str, int]]

def build_user_id(full_name: str, dob: str) -> str:
    slug = full_name.strip().lower().replace(" ", "_")
    return f"{slug}_{dob}"

@app.post("/bfhl")
async def process_data(request: DataModel):
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    total_sum = 0
    all_letters = []

    for item in request.data:
        s = str(item)
        if s.lstrip("-").isdigit():
            n = int(s)
            total_sum += n
            if n % 2 == 0:
                even_numbers.append(s)
            else:
                odd_numbers.append(s)
        elif s.isalpha():
            alphabets.append(s.upper())
        elif not s.isalnum():
            special_characters.append(s)

        for ch in s:
            if ch.isalpha():
                all_letters.append(ch)

    all_letters.reverse()
    concat_chars = []
    for i, ch in enumerate(all_letters):
        concat_chars.append(ch.upper() if i % 2 == 0 else ch.lower())
    concat_string = "".join(concat_chars)

    return {
        "is_success": True,
        "user_id": build_user_id("john doe", "17091999"),  # change to your name + dob
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total_sum),
        "concat_string": concat_string
    }
