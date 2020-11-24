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
            "id_service_type": 1,
            "id_user_offer": 2,
            "description": "Soy buen adiestrador",
            "price_h": 20.00,
        },
        {
            "id": 2,
            "id_service_type": 2,
            "id_user_offer": 1,
            "description": "Soy buen adiestrador",
            "price_h": 20.00,
        }
    ],
    "Review":[
        {
            "id" : 1,
            "id_user_author" : 1,
            "points" : 3.00,   
            "text" : "hola",
        }
    ],
    "Operations":[
        {
            "id": 1,
            "user_id_who_hire": 1,
            "service_id_hired": 2,
            "date": "1992-11-18",
            "price": 20.00
        }
    ],
    "Service_type":[
        {
            "id": 1,
            "service_type": "paseador"
        },
        {
            "id": 2,
            "service_type": "canguro"
        }
    ]
}

