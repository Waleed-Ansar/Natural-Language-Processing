from openai import OpenAI
from connection import collection_name, api_keys


async def User_Input(req: str):
    docs = api_keys.find({})

    keys = []
    async for key in docs:
        if "_id" in key:
            del key['_id']
        keys.append(key['key'])

    client = OpenAI(api_key=keys[0])
    
    topic = req
    prompt = f"{topic}. write comprehensively and specify book name and chapter names and also explain the chapters."
    
    if topic is not None:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",

            messages=[
                {"role": "system", "content": "You are a helpful assistant who is master in writing books on given topic."},
                {"role": "user", "content": f"{prompt}"}
            ],
            temperature=0.5
        )
        
        response = resp.choices[0].message.content
        line = str(response)
        line = line.replace("Book Title:", "").strip()
        
        lines = line.splitlines()
        
        title = lines[0]
        
        data = {"Title": title,
                "Book": line
            }
        
        result = await collection_name.insert_one(data)
        return str(result.inserted_id)
    
    return None

async def get_all_books():
    collection = collection_name.find()
    books = []
    async for book in collection:
        if "_id" in book:
            book["id"] = str(book["_id"])
            del book["_id"]

            books.append(book)

    return books

async def get_by_name(name: str):
    filter = {'Title': f'** "{name.strip()}"**'}
    
    collection = await collection_name.find_one(filter, {"_id": 0})
    docs = collection['Book']
    book = []
    
    book.append(docs)
    
    return book

async def delete_book(title: str):
    filter = {'Title': f'** "{title.strip()}"**'}
    
    result = await collection_name.delete_one(filter)

    if result.deleted_count >0:
        return f'Book: "{title}" is deleted.'
    
    return None
