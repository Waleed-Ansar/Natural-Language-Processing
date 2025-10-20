from model import API_Response_Model
from fastapi import APIRouter
import service


class API:
    def __init__(self):
        self.router = APIRouter()
        self.register_routes()
    
    def register_routes(self):
        @self.router.post("/create_book", response_model=API_Response_Model, summary='Enter the type of book to write.')
        async def Input(topic: str) -> API_Response_Model:
            response = API_Response_Model()
            
            try:
                result = await service.User_Input(topic)
                
                if result is not None:
                    response.success = True
                    response.message = "Success"
                    response.error = None
                    response.data = result
                
                else:
                    response.success = False
                    response.message = "Enter something first."
                    response.error = "Null input"
            
            except Exception as e:
                response.success = False
                response.message = str(e)
            
            return response
        
        @self.router.get("/get_all_books", response_model=API_Response_Model, summary='Get all books')
        async def get_all():
            response = API_Response_Model()
            
            try:
                result = await service.get_all_books()
                
                if result is not None:
                    response.success = True
                    response.message = "Success"
                    response.error = None
                    response.data = result
                
                else:
                    response.success = False
                    response.message = "No books are available."
            
            except Exception as e:
                response.success = False
                response.message = str(e)
            
            return response

        @self.router.get("/get_by_name/{name}", response_model=API_Response_Model, summary='Get book by name')
        async def get_book_by_name(name: str):
            response = API_Response_Model()

            try:
                result = await service.get_by_name(name)

                if result != []:
                    response.success = True
                    response.message = "Success"
                    response.error = None
                    response.data = result

                else:
                    response.success = False
                    response.message = "Book not present."

            except Exception as e:
                response.success = False
                response.message = str(e)
            
            return response

        @self.router.delete("/delete_book", response_model=API_Response_Model, summary='Select the book to delete.')
        async def delete_the_book(title: str):
            response = API_Response_Model()
            
            try:
                result = await service.delete_book(title)
                
                if result:
                    response.success = True
                    response.message = "Success"
                    response.error = None
                    response.data = result
   
                else:
                    response.success = False
                    response.message = "Book not present."

            except Exception as e:
                response.success = False
                response.message = str(e)
            
            return response