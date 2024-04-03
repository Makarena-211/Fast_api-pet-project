import psycopg2 
from config import Base
from sqlalchemy import Column, Integer, String

class Painting (Base):
    __tablename__ = 'paintings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    photo = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    type = Column(String, nullable=False)























# """
# connection = psycopg2.connect(
#     host = host,
#     user = user,
#     password = password,
#     database = db_name,
#     port = port
# )
# connection.autocommit = True
# # with connection.cursor() as cursor:
# #         cursor.execute(
# #             """CREATE TABLE Paintings(
# #                 id serial PRIMARY KEY,
# #                 name varchar(40) NOT NULL,
# #                 photo varchar(100) NOT NULL,
# #                 author varchar(40) NOT NULL,
# #                 price integer NOT NULL);"""
# #         )
# #         print(f"print db created!")


# with connection.cursor() as cursor:
#     cursor.execute("SELECT * FROM Paintings")
#     print(cursor.fetchall()[0])

"""
[(1, 'The cannon shot', 'https://unsplash.com/photos/brown-and-white-sail-ship-on-sea-painting-TjegK_z-0j8', 'Noname', 10000, 'Classicism'),
  (2, 'Pigment', 'https://unsplash.com/photos/a-painting-of-a-blue-sky-with-red-lines-P6PITLlO7IQ', 'Wesley Tingey', 5000, 'Аbstractionism'),
    (3, 'Creation of Adam', 'https://unsplash.com/photos/a-painting-on-the-ceiling-of-a-building-1rBg5YSi00c', 'Adrianna Geo', 11000, 'Classicism'),
      (4, 'Old pastor', 'https://unsplash.com/photos/man-in-brown-robe-painting-GTghGzaGTJc', 'Noname', 7000, 'Classicism'),
        (5, 'Black&White', 'https://unsplash.com/photos/multicolored-abstract-painting-RzykwoNjoLw', 'Steve Johnson', 3000, 'Abstractionism'),
          (6, 'Hacelblad', 'https://unsplash.com/photos/lake-near-mountain-during-daytime-RRn7VvZCbas', 'Elijah Walton', 10000, 'Landscape'),
            (7, "St Paul's from the River Thames", 'https://unsplash.com/photos/brown-and-white-dome-building-near-body-of-water-painting-qgWUv52K6Fk', 'Henry Dawson', 7000, 'Landscape'),
              (8, 'Sadomy', 'https://unsplash.com/photos/blue-green-and-yellow-abstract-painting-QBGqlIpByog', 'Eduardo Goody', 2000, 'Abstractionism'),
                (9, 'Cyan', 'https://unsplash.com/photos/blue-and-white-abstract-painting-SoB70WFVWGU', 'Pawel Czerwinski', 3000, 'Abstractionism'),
                  (10, "Naples From Sir William Hamilton's Villa", 'https://unsplash.com/photos/island-painting-nbneQlI2M1A', 'John Warwick Smith', 7000, 'Landscape'),
                    (11, 'London', 'https://unsplash.com/photos/a-painting-of-a-city-street-with-a-horse-drawn-carriage-GknO8Wwi7K8', 'James Miller', 12000, 'Landscape')]"""
