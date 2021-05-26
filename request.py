import requests
url = 'http://localhost:5000/results'
r = requests.post(url,json={'Lat':-3.90869,
                            'Area':88.67,
                            'Ofer-Trans':1,
                            'Idade':1,
                            'Data':253,
                            'Cons':6,
                            'Pad':4,
                            'Quartos':2,
                            'WCS':2,
                            'Renda':817.98,
                            'Vagas':1  
                            })
print(r.json())
