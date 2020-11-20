data = {
    "User": [
        {
            "id" : 1,
            "email": "carlosjuan1812@gmail.com",
            "password": "123456",
            "is_active" : True,
            "name" : "Juan Carlos",
            "last_name" : "Alcalde",
            "phone" : "605143832",
            "location" : "calle Alberto Conti",
            "biografy" : "Me gustan los perros",
            "image" : None,
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
            "biografy" : "Me gusta los gatos",
            "image" : None,
        },
        {
            "id" : 3,
            'email': 'jancore92@gmail.com',
            "password": '123456789',
            "is_active" : True,
            "name" : "Jan ",
            "last_name" : 'Escobar',
            "phone" : "605146425",
            "location" : "calle escorial",
            "biografy" : "Me gusta los conejos",
            "image" : None,
        },
    ],
     "Animals":[
            {
                "id" : 1,
                "user_id" : 1,
                "name" : "Pluto",
                "image" : None,
                "animal_type" : "perro",
                "age" : 3,
                "personality" : "amigable",
                "sex" : True,
                "weight" : 20.00,
                "size" : 40.00,
                "diseases" : "no lo se",
                "sterilized" : True,
            },
            {
                "id" : 2,
                "user_id" : 2,
                "name" : "Noa",
                "image" : None,
                "animal_type" : "perro",
                "age" : 6,
                "personality" : "amigable",
                "sex" : True,
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
                "sex" : True,
                "weight" : 20.00,
                "size" : 40.00,
                "diseases" : "no lo se",
                "sterilized" : True,
            }
        ],
    "Services":[
        {
            "id" : 1,
            "service" : "Paseador",
            "description" : "blanvjvjsjd",
            "price" : 20.00,
            "image" : None,
            "schedule":"fecha"
        },
        {
            "id" : 2,
            "service" :  "Adiestrador",
            "description" : "blanvjvjsjd",
            "price" : 20.00,
            "image" : None,
            "schedule":"fecha"
        }
    ],
    "Commerce": [
        {
            "id" : 1,
            "user_id" : 1,
            "description" : "grdgdvdvtf",
            "url" : None,
            "image" : None,
            "schedule" : "de 2 a 6",
            "address" : "calle me da igual"
        }
    ],
    "Review":[
        {
            "id" : 1,
            "comerce_id" : 1,
            "review" : 3,   #Cambiar a entro y el nombre
            "comment" : "hola",
            "date" : "20 febrero 2016",
        }
    ]
}

