'''
Author: yizhencode zhangyizhenyizen@gmail.com
Date: 2023-09-21 20:51:43
LastEditors: yizhencode zhangyizhenyizen@gmail.com
LastEditTime: 2023-09-22 16:15:51
FilePath: /ins_fastapi/routers/schemas.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from pydantic import BaseModel
from datetime import datetime
import sqlalchemy
import string
class UserBase(BaseModel):
        username: str 
        email: str
        password: str

class UserDisplay(BaseModel):
        username: str 
        email: str
        class Config():
                orm_mode = True
        
class PostBase(BaseModel):
        image_url: str
        image_url_type: str
        caption: str
        creator_id: int

class UserAuth(BaseModel):
        id: int
        username: str
        email: str

# for PostDisplay
class User(BaseModel):
        username: str
        class Config():
                orm_mode = True
          
class PostDisplay(BaseModel):
        id: int
        image_url: str
        image_url_type: str
        caption: str
        timestamp: datetime
        user: User
        class Config():
                orm_mode = True
        
        