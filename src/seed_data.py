data = {
    "User": [
        {
            "id": 1,
            "email": "carlosjuan1812@gmail.com",
            "password": "123456",
            "is_active": True,
            "name": "Juan Carlos",
            "last_name": "Alcalde",
            "phone": "605143832",
            "location": "calle Alberto Conti",
            "biografy": "Me gustan los perros",
        },
        {
            "id" : 2,
            "email": "lorella.1892@gmail.com",
            "password": "1234",
            "is_active" : True,
            "name" : "Lorella ",
            "last_name" : 'Mantovani',
            "phone" : "6051",
            "location" : "calle alcorcon",
            "biografy" : "Me gustan los gatos",
            "image" : None,
        },
        {
            "id" : 3,
            'email': 'jancore92@gmail.com',
            "password": '123456789',
            "is_active" : True,
            "name" : "Jan ",
            "last_name" : 'Escobar',
            "phone" : "672226555",
            "location" : "calle escorial",
            "biografy" : "Me gustan los conejos",
        },
    ],
     "Animals":[
            {
                "id": 1,
                "user_id": 1,
                "name": "Pluto",
                "animal_type": "perro",
                "age": 3,
                "personality": "amigable",
                "gender": True,
                "weight": 20.00,
                "size": 40.00,
                "diseases": "no lo se",
                "sterilized": True,
            },
            {
                "id" : 2,
                "user_id" : 2,
                "name" : "Noa",
                "image" : None,
                "animal_type" : "perro",
                "age" : 6,
                "personality" : "amigable",
                "gender" : True,
                "weight" : 20.00,
                "size" : 40.00,
                "diseases" : "no lo se",
                "sterilized" : True,
            },
            {
                "id" : 3,
                "user_id" : 3,
                "name" : "Ankor",
                "image" : None,
                "animal_type" : "perro",
                "age" : 2,
                "personality" : "jugueton",
                "gender" : True,
                "weight" : 20.00,
                "size" : 40.00,
                "diseases" : "no lo se",
                "sterilized" : True,
            }
        ],
    "Services":[
        {
            "id": 1,
            "service": "Paseador",
            "description": "blanvjvjsjd",
            "price": 20.00,
        },
    ],
    "Commerce": [
        {
            "id" : 1,
            "user_id" : 1,
            "description" : "grdgdvdvtf",
            "schedule" : "de 2 a 6",
            "address" : "calle me da igual"
        }
    ],
    "Operations":[
        {
            "id": 1,
            "user_id": 1,
            "service_id": 1,
            "service": "Pasear",
            "date": "18/nov",
            "price": 20.00
        }
    ],
    "User_review": [
        {
            "id": 1,
            "id_user_destination": 1,
            "id_user_author" : 2,
            "points" : 3.00,
            "text" : "hola",
        }
    ],
    "Commerce_review": [
        {
            "id": 2,
            "id_commerce_destination": 1,
            "id_user_author" : 3,
            "points" : 3.00,
            "text" : "hola",
        }
    ]
}

